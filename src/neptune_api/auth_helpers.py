__all__ = ["exchange_api_key"]

from typing import Union

from neptune_api import Client
from neptune_api.api.backend import exchange_api_token
from neptune_api.credentials import Credentials
from neptune_api.errors import UnableToExchangeApiKeyError
from neptune_api.models import (
    Error,
    NeptuneOauthToken,
)
from neptune_api.types import OAuthToken


def exchange_api_key(client: Client, credentials: Credentials) -> OAuthToken:
    token_data: Union[NeptuneOauthToken, None, Error] = exchange_api_token.sync(
        client=client, x_neptune_api_token=credentials.api_key
    )

    if isinstance(token_data, Error):
        raise UnableToExchangeApiKeyError(reason=str(token_data.message))
    if not token_data:
        raise UnableToExchangeApiKeyError()

    return OAuthToken.from_tokens(access=token_data.access_token, refresh=token_data.refresh_token)
