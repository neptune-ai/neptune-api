#
# Copyright (c) 2025, Neptune Labs Sp. z o.o.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__all__ = ["exchange_api_key"]

from neptune_api import Client
from neptune_api.api.backend import exchange_api_token
from neptune_api.credentials import Credentials
from neptune_api.errors import (
    ApiKeyRejectedError,
    UnableToExchangeApiKeyError,
)
from neptune_api.models import Error
from neptune_api.types import OAuthToken


def exchange_api_key(client: Client, credentials: Credentials) -> OAuthToken:
    response = exchange_api_token.sync_detailed(client=client, x_neptune_api_token=credentials.api_key)

    # HTTP 401 is an indicator that the API token is rejected by the server
    if response.status_code == 401:
        raise ApiKeyRejectedError()

    token_data = response.parsed
    if isinstance(token_data, Error):
        raise UnableToExchangeApiKeyError(
            reason=f"Unexpected response from Neptune API: HTTP {response.status_code} ({token_data.message})"
        )

    if response.status_code != 200 or not token_data:
        raise UnableToExchangeApiKeyError(reason=f"Unexpected response from Neptune API: HTTP {response.status_code}")

    return OAuthToken.from_tokens(access=token_data.access_token, refresh=token_data.refresh_token)
