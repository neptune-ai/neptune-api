__all__ = ["Credentials"]

import base64
import json
from typing import (
    Any,
    Dict,
)

from attr import define

from neptune_api.errors import (
    InvalidApiTokenException,
    UnableToDeserializeApiKeyError,
)


@define
class Credentials:
    api_key: str
    base_url: str

    @classmethod
    def from_api_key(cls, api_key: str) -> "Credentials":
        api_key = api_key.strip()

        try:
            token_data = deserialize(api_key)
        except UnableToDeserializeApiKeyError as e:
            raise InvalidApiTokenException("Unable to deserialize API key") from e

        token_origin_address, api_url = token_data.get("api_address"), token_data.get("api_url")
        if not token_origin_address and not api_url:
            raise InvalidApiTokenException("API key is missing required fields")

        return Credentials(api_key=api_key, base_url=str(api_url) or str(token_origin_address))


def deserialize(api_key: str) -> Dict[str, Any]:
    try:
        data: Dict[str, Any] = json.loads(base64.b64decode(api_key.encode()).decode("utf-8"))
        return data
    except Exception as e:
        raise UnableToDeserializeApiKeyError() from e
