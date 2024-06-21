__all__ = ["exchange_to_access_token"]

from typing import (
    Optional,
    Union,
)

from neptune_api import Client
from neptune_api.api.backend import exchange_api_token
from neptune_api.client import OAuthToken
from neptune_api.credentials import Credentials
from neptune_api.models import (
    Error,
    NeptuneOauthToken,
)


def exchange_to_access_token(client: Client, credentials: Credentials) -> Optional[OAuthToken]:
    print("Token factory called")
    token_data: Union[NeptuneOauthToken, None, Error] = exchange_api_token.sync(
        client=client, x_neptune_api_token=credentials.token
    )

    if not token_data or isinstance(token_data, Error):
        return None

    return OAuthToken.from_tokens(access=token_data.access_token, refresh=token_data.refresh_token)
