#
# Copyright (c) 2024, Neptune Labs Sp. z o.o.
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
#
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


def exchange_to_access_token(credentials: Credentials, client: Client) -> Optional[OAuthToken]:
    token_data: Union[NeptuneOauthToken, None, Error] = exchange_api_token.sync(
        client=client, x_neptune_api_token=credentials.token
    )

    if not token_data or isinstance(token_data, Error):
        return None

    return OAuthToken.from_tokens(access=token_data.access_token, refresh=token_data.refresh_token)
