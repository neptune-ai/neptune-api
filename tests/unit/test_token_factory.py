from neptune_api import Client
from neptune_api.token_factory import exchange_api_key


def test_exchange_api_called(mocker, credentials, oauth_token):
    # given
    access_token, refresh_token = oauth_token.access_token, oauth_token.refresh_token

    client_mock = mocker.MagicMock(spec=Client)
    request_mock = mocker.MagicMock()
    client_mock.get_httpx_client.return_value = request_mock
    request_mock.request.return_value = mocker.MagicMock()
    request_mock.request.return_value.status_code = 200
    request_mock.request.return_value.json.return_value = {
        "accessToken": access_token,
        "refreshToken": refresh_token,
        "username": "henry",
    }

    # when
    token = exchange_api_key(client_mock, credentials)

    # then
    assert token.access_token == access_token
    assert token.refresh_token == refresh_token


def test_unauthorized(mocker, credentials):
    # given
    client_mock = mocker.MagicMock(spec=Client)
    request_mock = mocker.MagicMock()
    client_mock.get_httpx_client.return_value = request_mock
    request_mock.request.return_value = mocker.MagicMock()
    request_mock.request.return_value.status_code = 401

    # when
    token = exchange_api_key(client_mock, credentials)

    # then
    assert token is None
