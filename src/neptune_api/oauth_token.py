__all__ = ["OAuthToken"]

import time

import jwt
from attr import (
    define,
    field,
)

MINIMAL_EXPIRATION_SECONDS = 30
DECODING_OPTIONS = {
    "verify_signature": False,
    "verify_exp": False,
    "verify_nbf": False,
    "verify_iat": False,
    "verify_aud": False,
    "verify_iss": False,
}


@define
class OAuthToken:
    _expiration_time: float = field(default=None, alias="expiration_time", kw_only=True)
    access_token: str
    refresh_token: str

    @classmethod
    def from_tokens(cls, access: str, refresh: str) -> "OAuthToken":
        # Decode the JWT to get expiration time
        try:
            decoded_token = jwt.decode(access, options=DECODING_OPTIONS)
            expiration_time = float(decoded_token["exp"])
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, KeyError):
            expiration_time = 0.0

        return OAuthToken(access_token=access, refresh_token=refresh, expiration_time=expiration_time)

    @property
    def seconds_left(self) -> float:
        return self._expiration_time - time.time()

    @property
    def is_expired(self) -> bool:
        return self.seconds_left <= MINIMAL_EXPIRATION_SECONDS
