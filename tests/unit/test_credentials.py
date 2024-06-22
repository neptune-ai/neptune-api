import pytest

from neptune_api.credentials import Credentials
from neptune_api.errors import InvalidApiTokenException


def test_valid():
    # given
    api_key = "eyJhcGlfYWRkcmVzcyI6Imhvc3QiLCJhcGlfdXJsIjoiaG9zdCIsImFwaV9rZXkiOiI0NDBlZTE0Ni00NDJlLTRkN2MtYThhYy0yNzZiYTk0MGEwNzEifQ=="

    # when
    credentials = Credentials.from_token(token=api_key)

    # then
    assert credentials.base_url == "host"
    assert credentials.token == api_key


def test_invalid_api_key():
    # given
    api_key = "eyJ..."

    # then
    with pytest.raises(InvalidApiTokenException):
        Credentials.from_token(token=api_key)
