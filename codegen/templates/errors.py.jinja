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

"""Contains shared errors types that can be raised from API functions"""

__all__ = [
    "UnexpectedStatus",
    "InvalidApiTokenException",
    "UnableToExchangeApiKeyError",
    "UnableToDeserializeApiKeyError",
    "UnableToRefreshTokenError",
]


class UnexpectedStatus(Exception):
    """Raised by api functions when the response status an undocumented status and Client.raise_on_unexpected_status is True"""

    def __init__(self, status_code: int, content: bytes):
        self.status_code = status_code
        self.content = content

        super().__init__(
            f"Unexpected status code: {status_code}\n\nResponse content:\n{content.decode(errors='ignore')}"
        )


class InvalidApiTokenException(Exception):
    """Raised when the api token is invalid"""

    def __init__(self, reason: str = "") -> None:
        super().__init__(f"Invalid API token. Reason: {reason}")


class UnableToExchangeApiKeyError(Exception):
    """Raised when the API key exchange fails"""

    def __init__(self, reason: str = "Unknown") -> None:
        super().__init__(f"Unable to exchange API key. Reason: {reason}")


class UnableToDeserializeApiKeyError(Exception):
    """Raised when the API key cannot be deserialized"""

    def __init__(self) -> None:
        super().__init__("Unable to deserialize API key")


class UnableToRefreshTokenError(Exception):
    """Raised when the token refresh fails"""

    def __init__(self, reason: str = "Unknown") -> None:
        super().__init__(f"Unable to refresh token. Reason: {reason}")
