__all__ = ["Credentials"]

import base64
import json
from typing import (
    Any,
    Dict,
)

from attr import (
    define,
    field,
)

from neptune_api.errors import NeptuneInvalidApiTokenException


@define
class Credentials:
    _token: str = field(factory=str, kw_only=True, alias="token")
    api_token: str
    base_url: str

    @property
    def token(self) -> str:
        return self._token

    @classmethod
    def from_token(cls, api_token: str) -> "Credentials":
        token = api_token.strip()
        token_dict = deserialize(token)

        token_origin_address = token_dict.get("api_address")
        api_url = token_dict.get("api_url")

        assert token_origin_address is not None
        assert api_url is not None

        return Credentials(api_token=token, base_url=api_url or token_origin_address, token=token)


def deserialize(api_token: str) -> Dict[str, str]:
    try:
        data: Dict[str, Any] = json.loads(base64.b64decode(api_token.encode()).decode("utf-8"))

        if "api_address" not in data:
            raise ValueError("Invalid token: missing 'api_address' field.")

        return data
    except Exception:
        raise NeptuneInvalidApiTokenException()
