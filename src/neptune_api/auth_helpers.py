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
