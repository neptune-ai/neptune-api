"""Contains some shared types for properties"""

__all__ = ["File", "Response", "FileJsonType", "Unset", "UNSET", "OAuthToken"]

import time
from http import HTTPStatus
from typing import (
    BinaryIO,
    Generic,
    Literal,
    MutableMapping,
    Optional,
    Tuple,
    TypeVar,
)

import jwt
from attrs import (
    define,
    field,
)

MINIMAL_EXPIRATION_SECONDS = 299
DECODING_OPTIONS = {
    "verify_signature": False,
    "verify_exp": False,
    "verify_nbf": False,
    "verify_iat": False,
    "verify_aud": False,
    "verify_iss": False,
}


class Unset:
    def __bool__(self) -> Literal[False]:
        return False


UNSET: Unset = Unset()

FileJsonType = Tuple[Optional[str], BinaryIO, Optional[str]]


@define
class File:
    """Contains information for file uploads"""

    payload: BinaryIO
    file_name: Optional[str] = None
    mime_type: Optional[str] = None

    def to_tuple(self) -> FileJsonType:
        """Return a tuple representation that httpx will accept for multipart/form-data"""
        return self.file_name, self.payload, self.mime_type


T = TypeVar("T")


@define
class Response(Generic[T]):
    """A response from an endpoint"""

    status_code: HTTPStatus
    content: bytes
    headers: MutableMapping[str, str]
    parsed: Optional[T]


@define
class OAuthToken:
    _expiration_time: float = field(default=0.0, alias="expiration_time", kw_only=True)
    access_token: str
    refresh_token: str

    @classmethod
    def from_tokens(cls, access: str, refresh: str) -> "OAuthToken":
        # Decode the JWT to get expiration time
        try:
            decoded_token = jwt.decode(access, options=DECODING_OPTIONS)
            expiration_time = float(decoded_token["exp"])
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, KeyError):
            # TODO: Better error handling
            expiration_time = 0.0

        return OAuthToken(access_token=access, refresh_token=refresh, expiration_time=expiration_time)

    @property
    def seconds_left(self) -> float:
        print("Seconds left:", self._expiration_time - time.time())
        return self._expiration_time - time.time()

    @property
    def is_expired(self) -> bool:
        return self.seconds_left <= MINIMAL_EXPIRATION_SECONDS
