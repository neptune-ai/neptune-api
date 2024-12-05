__all__ = ["Client", "AuthenticatedClient", "NeptuneAuthenticator"]

import datetime
import json
import os
import ssl
import threading
import typing
from datetime import timedelta
from typing import (
    Any,
    Callable,
    Dict,
    Generator,
    Optional,
    Union,
)

import httpx
from attrs import (
    define,
    evolve,
    field,
)

from neptune_api.credentials import Credentials
from neptune_api.errors import UnableToRefreshTokenError
from neptune_api.types import OAuthToken


@define
class Client:
    """A class for keeping track of data related to the API

    The following are accepted as keyword arguments and will be used to construct httpx Clients internally:

        ``base_url``: The base URL for the API, all requests are made to a relative path to this URL

        ``cookies``: A dictionary of cookies to be sent with every request

        ``headers``: A dictionary of headers to be sent with every request

        ``timeout``: The maximum amount of a time a request can take. API functions will raise
        httpx.TimeoutException if this is exceeded.

        ``verify_ssl``: Whether or not to verify the SSL certificate of the API server. This should be True in production,
        but can be set to False for testing purposes.

        ``follow_redirects``: Whether or not to follow redirects. Default value is False.

        ``httpx_args``: A dictionary of additional arguments to be passed to the ``httpx.Client`` and ``httpx.AsyncClient`` constructor.


    Attributes:
        raise_on_unexpected_status: Whether or not to raise an errors.UnexpectedStatus if the API returns a
            status code that was not documented in the source OpenAPI document. Can also be provided as a keyword
            argument to the constructor.
    """

    raise_on_unexpected_status: bool = field(default=False, kw_only=True)
    _base_url: str = field(alias="base_url")
    _cookies: Dict[str, str] = field(factory=dict, kw_only=True, alias="cookies")
    _headers: Dict[str, str] = field(factory=dict, kw_only=True, alias="headers")
    _timeout: Optional[httpx.Timeout] = field(default=None, kw_only=True, alias="timeout")
    _verify_ssl: Union[str, bool, ssl.SSLContext] = field(default=True, kw_only=True, alias="verify_ssl")
    _follow_redirects: bool = field(default=False, kw_only=True, alias="follow_redirects")
    _httpx_args: Dict[str, Any] = field(factory=dict, kw_only=True, alias="httpx_args")
    _client: Optional[httpx.Client] = field(default=None, init=False)
    _async_client: Optional[httpx.AsyncClient] = field(default=None, init=False)

    def with_headers(self, headers: Dict[str, str]) -> "Client":
        """Get a new client matching this one with additional headers"""
        if self._client is not None:
            self._client.headers.update(headers)
        if self._async_client is not None:
            self._async_client.headers.update(headers)
        return evolve(self, headers={**self._headers, **headers})

    def with_cookies(self, cookies: Dict[str, str]) -> "Client":
        """Get a new client matching this one with additional cookies"""
        if self._client is not None:
            self._client.cookies.update(cookies)
        if self._async_client is not None:
            self._async_client.cookies.update(cookies)
        return evolve(self, cookies={**self._cookies, **cookies})

    def with_timeout(self, timeout: httpx.Timeout) -> "Client":
        """Get a new client matching this one with a new timeout (in seconds)"""
        if self._client is not None:
            self._client.timeout = timeout
        if self._async_client is not None:
            self._async_client.timeout = timeout
        return evolve(self, timeout=timeout)

    def set_httpx_client(self, client: httpx.Client) -> "Client":
        """Manually the underlying httpx.Client

        **NOTE**: This will override any other settings on the client, including cookies, headers, and timeout.
        """
        self._client = client
        return self

    def get_httpx_client(self) -> httpx.Client:
        """Get the underlying httpx.Client, constructing a new one if not previously set"""
        if self._client is None:
            self._client = httpx.Client(
                auth=create_proxy_auth(self._base_url),
                base_url=self._base_url,
                cookies=self._cookies,
                headers=self._headers,
                timeout=self._timeout,
                verify=self._verify_ssl,
                follow_redirects=self._follow_redirects,
                **self._httpx_args,
            )
        return self._client

    def __enter__(self) -> "Client":
        """Enter a context manager for self.client—you cannot enter twice (see httpx docs)"""
        self.get_httpx_client().__enter__()
        return self

    def __exit__(self, *args: Any, **kwargs: Any) -> None:
        """Exit a context manager for internal httpx.Client (see httpx docs)"""
        self.get_httpx_client().__exit__(*args, **kwargs)

    def set_async_httpx_client(self, async_client: httpx.AsyncClient) -> "Client":
        """Manually the underlying httpx.AsyncClient

        **NOTE**: This will override any other settings on the client, including cookies, headers, and timeout.
        """
        self._async_client = async_client
        return self

    def get_async_httpx_client(self) -> httpx.AsyncClient:
        """Get the underlying httpx.AsyncClient, constructing a new one if not previously set"""
        if self._async_client is None:
            self._async_client = httpx.AsyncClient(
                base_url=self._base_url,
                cookies=self._cookies,
                headers=self._headers,
                timeout=self._timeout,
                verify=self._verify_ssl,
                follow_redirects=self._follow_redirects,
                **self._httpx_args,
            )
        return self._async_client

    async def __aenter__(self) -> "Client":
        """Enter a context manager for underlying httpx.AsyncClient—you cannot enter twice (see httpx docs)"""
        await self.get_async_httpx_client().__aenter__()
        return self

    async def __aexit__(self, *args: Any, **kwargs: Any) -> None:
        """Exit a context manager for underlying httpx.AsyncClient (see httpx docs)"""
        await self.get_async_httpx_client().__aexit__(*args, **kwargs)


@define
class AuthenticatedClient:
    """A Client which has been authenticated for use on secured endpoints

    The following are accepted as keyword arguments and will be used to construct httpx Clients internally:

        ``base_url``: The base URL for the API, all requests are made to a relative path to this URL

        ``cookies``: A dictionary of cookies to be sent with every request

        ``headers``: A dictionary of headers to be sent with every request

        ``timeout``: The maximum amount of a time a request can take. API functions will raise
        httpx.TimeoutException if this is exceeded.

        ``verify_ssl``: Whether or not to verify the SSL certificate of the API server. This should be True in production,
        but can be set to False for testing purposes.

        ``follow_redirects``: Whether or not to follow redirects. Default value is False.

        ``httpx_args``: A dictionary of additional arguments to be passed to the ``httpx.Client`` and ``httpx.AsyncClient`` constructor.


    Attributes:
        raise_on_unexpected_status: Whether or not to raise an errors.UnexpectedStatus if the API returns a
            status code that was not documented in the source OpenAPI document. Can also be provided as a keyword
            argument to the constructor.
        credentials: User credentials for authentication.
        token_refreshing_endpoint: Token refreshing endpoint url
        client_id: Client identifier for the OAuth application.
        api_key_exchange_callback: The Neptune API Token exchange function
        prefix: The prefix to use for the Authorization header
        auth_header_name: The name of the Authorization header
    """

    raise_on_unexpected_status: bool = field(default=False, kw_only=True)
    _base_url: str = field(alias="base_url")
    _cookies: Dict[str, str] = field(factory=dict, kw_only=True, alias="cookies")
    _headers: Dict[str, str] = field(factory=dict, kw_only=True, alias="headers")
    _timeout: Optional[httpx.Timeout] = field(default=None, kw_only=True, alias="timeout")
    _verify_ssl: Union[str, bool, ssl.SSLContext] = field(default=True, kw_only=True, alias="verify_ssl")
    _follow_redirects: bool = field(default=False, kw_only=True, alias="follow_redirects")
    _httpx_args: Dict[str, Any] = field(factory=dict, kw_only=True, alias="httpx_args")
    _client: Optional[httpx.Client] = field(default=None, init=False)
    _token_refreshing_client: Optional[Client] = field(default=None, init=False)
    _async_client: Optional[httpx.AsyncClient] = field(default=None, init=False)

    credentials: Credentials
    token_refreshing_endpoint: str
    client_id: str
    api_key_exchange_callback: Callable[[Client, Credentials], OAuthToken]
    prefix: str = "Bearer"
    auth_header_name: str = "Authorization"

    def with_headers(self, headers: Dict[str, str]) -> "AuthenticatedClient":
        """Get a new client matching this one with additional headers"""
        if self._client is not None:
            self._client.headers.update(headers)

        if self._async_client is not None:
            self._async_client.headers.update(headers)

        if self._token_refreshing_client is not None:
            self._token_refreshing_client.with_headers(headers)

        return evolve(self, headers={**self._headers, **headers})

    def with_cookies(self, cookies: Dict[str, str]) -> "AuthenticatedClient":
        """Get a new client matching this one with additional cookies"""
        if self._client is not None:
            self._client.cookies.update(cookies)

        if self._async_client is not None:
            self._async_client.cookies.update(cookies)

        if self._token_refreshing_client is not None:
            self._token_refreshing_client.with_cookies(cookies)

        return evolve(self, cookies={**self._cookies, **cookies})

    def with_timeout(self, timeout: httpx.Timeout) -> "AuthenticatedClient":
        """Get a new client matching this one with a new timeout (in seconds)"""
        if self._client is not None:
            self._client.timeout = timeout

        if self._async_client is not None:
            self._async_client.timeout = timeout

        if self._token_refreshing_client is not None:
            self._token_refreshing_client.with_timeout(timeout)

        return evolve(self, timeout=timeout)

    def set_httpx_client(self, client: httpx.Client) -> "AuthenticatedClient":
        """Manually the underlying httpx.Client

        **NOTE**: This will override any other settings on the client, including cookies, headers, and timeout.
        """
        self._client = client
        return self

    def get_token_refreshing_client(self) -> Client:
        """Get the underlying Client, constructing a new one if not previously set"""
        if self._token_refreshing_client is None:
            self._token_refreshing_client = Client(
                base_url=self._base_url,
                cookies=self._cookies,
                headers=self._headers,
                timeout=self._timeout,
                verify_ssl=self._verify_ssl,
                follow_redirects=self._follow_redirects,
                httpx_args=self._httpx_args,
            )
        return self._token_refreshing_client

    def set_token_refreshing_client(self, client: Client) -> "AuthenticatedClient":
        """Manually the underlying Client used for authentication

        **NOTE**: This will override any other settings on the client, including cookies, headers, and timeout.
        """
        self._token_refreshing_client = client
        return self

    def get_httpx_client(self) -> httpx.Client:
        """Get the underlying httpx.Client, constructing a new one if not previously set"""
        if self._client is None:
            self._client = httpx.Client(
                auth=create_auth(
                    credentials=self.credentials,
                    client_id=self.client_id,
                    token_refreshing_endpoint=self.token_refreshing_endpoint,
                    api_key_exchange_factory=self.api_key_exchange_callback,
                    client=self.get_token_refreshing_client(),
                    base_url=self._base_url,
                ),
                base_url=self._base_url,
                cookies=self._cookies,
                headers=self._headers,
                timeout=self._timeout,
                verify=self._verify_ssl,
                follow_redirects=self._follow_redirects,
                **self._httpx_args,
            )
        return self._client

    def __enter__(self) -> "AuthenticatedClient":
        """Enter a context manager for self.client—you cannot enter twice (see httpx docs)"""
        self.get_token_refreshing_client().__enter__()
        self.get_httpx_client().__enter__()
        return self

    def __exit__(self, *args: Any, **kwargs: Any) -> None:
        """Exit a context manager for internal httpx.Client (see httpx docs)"""
        self.get_token_refreshing_client().__exit__(*args, **kwargs)
        self.get_httpx_client().__exit__(*args, **kwargs)

    def set_async_httpx_client(self, async_client: httpx.AsyncClient) -> "AuthenticatedClient":
        """Manually the underlying httpx.AsyncClient

        **NOTE**: This will override any other settings on the client, including cookies, headers, and timeout.
        """
        # TODO: Missing implementation
        raise NotImplementedError

    def get_async_httpx_client(self) -> httpx.AsyncClient:
        """Get the underlying httpx.AsyncClient, constructing a new one if not previously set"""
        # TODO: Missing implementation
        raise NotImplementedError

    async def __aenter__(self) -> "AuthenticatedClient":
        """Enter a context manager for underlying httpx.AsyncClient—you cannot enter twice (see httpx docs)"""
        # TODO: Missing implementation
        raise NotImplementedError

    async def __aexit__(self, *args: Any, **kwargs: Any) -> None:
        """Exit a context manager for underlying httpx.AsyncClient (see httpx docs)"""
        # TODO: Missing implementation
        raise NotImplementedError


class NeptuneAuthenticator(httpx.Auth):
    __LOCK = threading.RLock()

    def __init__(
        self,
        credentials: Credentials,
        client_id: str,
        token_refreshing_endpoint: str,
        api_key_exchange_factory: Callable[[Client, Credentials], OAuthToken],
        client: Client,
    ):
        self._credentials: Credentials = credentials
        self._client_id: str = client_id
        self._token_refreshing_endpoint: str = token_refreshing_endpoint
        self._api_key_exchange_factory: Callable[[Client, Credentials], OAuthToken] = api_key_exchange_factory

        self._client = client
        self._token: Optional[OAuthToken] = None

    def _refresh_existing_token(self) -> None:
        if self._token is None:
            # This should never happen, but just in case
            self._token = self._api_key_exchange_factory(self._client, self._credentials)
            return

        try:
            response = self._client.get_httpx_client().post(
                url=self._token_refreshing_endpoint,
                data={
                    "grant_type": "refresh_token",
                    "refresh_token": self._token.refresh_token,
                    "client_id": self._client_id,
                    "expires_in": self._token.seconds_left,
                },
            )
            data = response.json()
        except Exception as e:
            raise UnableToRefreshTokenError("Unable to refresh token") from e

        self._token = OAuthToken.from_tokens(access=data["access_token"], refresh=data["refresh_token"])

    def _refresh_token(self) -> None:
        with self.__LOCK:
            if self._token is not None:
                self._refresh_existing_token()

            if self._token is None:
                self._token = self._api_key_exchange_factory(self._client, self._credentials)

    def _refresh_token_if_expired(self) -> None:
        if self._token is None or self._token.is_expired:
            self._refresh_token()

    def sync_auth_flow(self, request: httpx.Request) -> Generator[httpx.Request, httpx.Response, None]:
        self._refresh_token_if_expired()

        if self._token is not None:
            request.headers["Authorization"] = f"Bearer {self._token.access_token}"

        yield request

    async def async_auth_flow(self, request: httpx.Request) -> typing.AsyncGenerator[httpx.Request, httpx.Response]:
        # TODO: Missing implementation
        yield request


USE_IAP = os.environ.get("NEPTUNE_GCP_USE_IAP", False) in {"true", "t", "1", "True"}

if USE_IAP:
    from urllib.parse import (
        parse_qs,
        urlparse,
    )

    import google.auth
    import requests
    from google.auth.exceptions import DefaultCredentialsError
    from google.auth.transport.requests import Request
    from google.cloud import iam_credentials_v1
    from google.oauth2 import id_token

    def _find_iap_client_id(url: str) -> Optional[str]:
        try:
            response = requests.get(url, allow_redirects=False)
            if response.status_code == 302:
                location = response.headers.get("location")
                if location:
                    parsed_url = urlparse(location)
                    query_params = parse_qs(parsed_url.query)
                    client_id = query_params.get("client_id", [None])[0]
                    return client_id
            return None
        except Exception as e:
            print(f"Error fetching client_id: {e}")
            return None

    class LocalIdentityAwareProxyAuthenticator(httpx.Auth):
        def __init__(
            self,
            service_account_email: str,
            additional_authenticator: Optional[httpx.Auth] = None,
        ):
            self._additional_authenticator = additional_authenticator
            self._service_account_email = service_account_email
            self._tokens: Dict[str, str] = {}

        def _generate_jwt_payload(self, resource_url: str) -> str:
            iat = datetime.datetime.now(tz=datetime.timezone.utc)
            exp = iat + timedelta(hours=1)
            return json.dumps(
                {
                    "iss": self._service_account_email,
                    "sub": self._service_account_email,
                    "aud": resource_url,
                    "iat": int(iat.timestamp()),
                    "exp": int(exp.timestamp()),
                }
            )

        def _sign_jwt(self, resource_url: str) -> str:
            source_credentials, _ = google.auth.default()
            iam_client = iam_credentials_v1.IAMCredentialsClient(credentials=source_credentials)
            payload = self._generate_jwt_payload(resource_url)
            jwt: str = iam_client.sign_jwt(
                name=iam_client.service_account_path("-", self._service_account_email),
                payload=payload,
            ).signed_jwt
            return jwt

        def sync_auth_flow(self, request: httpx.Request) -> Generator[httpx.Request, httpx.Response, None]:
            url = str(request.url.copy_with(params=None))
            token = self._tokens.get(url)
            if token is None:
                token = self._sign_jwt(url)
                self._tokens[url] = token
            request.headers["Proxy-Authorization"] = f"Bearer {token}"

            if self._additional_authenticator is not None:
                yield from self._additional_authenticator.sync_auth_flow(request)
            else:
                yield request

        async def async_auth_flow(self, request: httpx.Request) -> typing.AsyncGenerator[httpx.Request, httpx.Response]:
            # TODO: Missing implementation
            yield request

    class GKEIdentityAwareProxyAuthenticator(httpx.Auth):
        def __init__(
            self,
            credentials: Any,
            additional_authenticator: Optional[httpx.Auth] = None,
        ):
            self._credentials = credentials
            self._additional_authenticator = additional_authenticator

        def sync_auth_flow(self, request: httpx.Request) -> Generator[httpx.Request, httpx.Response, None]:
            if self._credentials.expired:
                self._credentials.refresh(Request())

            request.headers["Proxy-Authorization"] = f"Bearer {self._credentials.token}"

            if self._additional_authenticator is not None:
                yield from self._additional_authenticator.sync_auth_flow(request)
            else:
                yield request

        async def async_auth_flow(self, request: httpx.Request) -> typing.AsyncGenerator[httpx.Request, httpx.Response]:
            # TODO: Missing implementation
            yield request

    def create_auth(
        credentials: Credentials,
        client_id: str,
        token_refreshing_endpoint: str,
        api_key_exchange_factory: Callable[[Client, Credentials], OAuthToken],
        client: Client,
        base_url: str,
    ) -> httpx.Auth:
        neptune_auth = NeptuneAuthenticator(
            credentials=credentials,
            client_id=client_id,
            token_refreshing_endpoint=token_refreshing_endpoint,
            api_key_exchange_factory=api_key_exchange_factory,
            client=client,
        )
        try:
            iap_client_id = _find_iap_client_id(base_url)
            credentials = id_token.fetch_id_token_credentials(iap_client_id, request=Request())
            # If we can fetch an ID token, we're running on GKE
            return GKEIdentityAwareProxyAuthenticator(credentials=credentials, additional_authenticator=neptune_auth)
        except DefaultCredentialsError:
            # If we can't fetch an ID token, we're running locally
            neptune_iap_service_account: str = os.environ["NEPTUNE_IAP_SERVICE_ACCOUNT"]
            return LocalIdentityAwareProxyAuthenticator(
                service_account_email=neptune_iap_service_account, additional_authenticator=neptune_auth
            )

    def create_proxy_auth(base_url: str) -> Optional[httpx.Auth]:
        try:
            iap_client_id = _find_iap_client_id(base_url)
            credentials = id_token.fetch_id_token_credentials(iap_client_id, request=Request())
            # If we can fetch an ID token, we're running on GKE
            return GKEIdentityAwareProxyAuthenticator(credentials=credentials)
        except DefaultCredentialsError:
            # If we can't fetch an ID token, we're running locally
            neptune_iap_service_account: str = os.environ["NEPTUNE_IAP_SERVICE_ACCOUNT"]
            return LocalIdentityAwareProxyAuthenticator(service_account_email=neptune_iap_service_account)

else:

    def create_auth(
        credentials: Credentials,
        client_id: str,
        token_refreshing_endpoint: str,
        api_key_exchange_factory: Callable[[Client, Credentials], OAuthToken],
        client: Client,
        base_url: str,
    ) -> httpx.Auth:
        return NeptuneAuthenticator(
            credentials=credentials,
            client_id=client_id,
            token_refreshing_endpoint=token_refreshing_endpoint,
            api_key_exchange_factory=api_key_exchange_factory,
            client=client,
        )

    def create_proxy_auth(base_url: str) -> Optional[httpx.Auth]:
        return None
