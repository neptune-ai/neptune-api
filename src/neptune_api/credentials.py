__all__ = ["Credentials"]

import base64
import json
from typing import (
    Any,
    Dict,
)

from attr import define

from neptune_api.errors import UnableToDeserializeApiKeyError


@define
class Credentials:
    token: str
    base_url: str

    @classmethod
    def from_token(cls, token: str) -> "Credentials":
        clean_token = token.strip()

        token_data = deserialize(clean_token)
        token_origin_address = token_data.get("api_address")
        api_url = token_data.get("api_url")

        # TODO: Better validation or mypy suggestions
        assert token_origin_address is not None
        assert api_url is not None

        return Credentials(token=clean_token, base_url=api_url or token_origin_address)


def deserialize(api_key: str) -> Dict[str, Any]:
    try:
        data: Dict[str, Any] = json.loads(base64.b64decode(api_key.encode()).decode("utf-8"))
        return data
    except Exception:
        raise UnableToDeserializeApiKeyError()
