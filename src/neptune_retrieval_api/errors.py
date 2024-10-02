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
