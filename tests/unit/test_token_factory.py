from neptune_api import Client
from neptune_api.credentials import Credentials
from neptune_api.token_factory import exchange_to_access_token


def test_exchange_api_called(mocker):
    # given
    access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ik5FRTFRVVJCT1RNNE16STVSa0ZETlRZeE9UVTFNRGcyT0Rnd1EwVXpNVGsxUWpZeVJrUkZRdyJ9.eyJpc3MiOiJodHRwczovL2Rldi04N2V2eDlydS5hdXRoMC5jb20vIiwic3ViIjoiYVc0Q2NhNzl4UmVMV1V6MGFFMkg2a0QwTzNjWEJWdENAY2xpZW50cyIsImF1ZCI6Imh0dHBzOi8vZXhwZW5zZXMtYXBpIiwiaWF0IjoxNTcyMDA2OTU0LCJleHAiOjE1NzIwMDY5NjQsImF6cCI6ImFXNENjYTc5eFJlTFdVejBhRTJINmtEME8zY1hCVnRDIiwiZ3R5IjoiY2xpZW50LWNyZWRlbnRpYWxzIn0.PUxE7xn52aTCohGiWoSdMBZGiYAHwE5FYie0Y1qUT68IHSTXwXVd6hn02HTah6epvHHVKA2FqcFZ4GGv5VTHEvYpeggiiZMgbxFrmTEY0csL6VNkX1eaJGcuehwQCRBKRLL3zKmA5IKGy5GeUnIbpPHLHDxr-GXvgFzsdsyWlVQvPX2xjeaQ217r2PtxDeqjlf66UYl6oY6AqNS8DH3iryCvIfCcybRZkc_hdy-6ZMoKT6Piijvk_aXdm7-QQqKJFHLuEqrVSOuBqqiNfVrG27QzAPuPOxvfXTVLXL2jek5meH6n-VWgrBdoMFH93QEszEDowDAEhQPHVs0xj7SIzA"
    refresh_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ik5FRTFRVVJCT1RNNE16STVSa0ZETlRZeE9UVTFNRGcyT0Rnd1EwVXpNVGsxUWpZeVJrUkZRdyJ9.eyJpc3MiOiJodHRwczovL2Rldi04N2V2eDlydS5hdXRoMC5jb20vIiwic3ViIjoiYVc0Q2NhNzl4UmVMV1V6MGFFMkg2a0QwTzNjWEJWdENAY2xpZW50cyIsImF1ZCI6Imh0dHBzOi8vZXhwZW5zZXMtYXBpIiwiaWF0IjoxNTcyMDA2OTU0LCJleHAiOjE1NzIwMDY5NjQsImF6cCI6ImFXNENjYTc5eFJlTFdVejBhRTJINmtEME8zY1hCVnRDIiwiZ3R5IjoiY2xpZW50LWNyZWRlbnRpYWxzIn0.PUxE7xn52aTCohGiWoSdMBZGiYAHwE5FYie0Y1qUT68IHSTXwXVd6hn02HTah6epvHHVKA2FqcFZ4GGv5VTHEvYpeggiiZMgbxFrmTEY0csL6VNkX1eaJGcuehwQCRBKRLL3zKmA5IKGy5GeUnIbpPHLHDxr-GXvgFzsdsyWlVQvPX2xjeaQ217r2PtxDeqjlf66UYl6oY6AqNS8DH3iryCvIfCcybRZkc_hdy-6ZMoKT6Piijvk_aXdm7-QQqKJFHLuEqrVSOuBqqiNfVrG27QzAPuPOxvfXTVLXL2jek5meH6n-VWgrBdoMFH93QEszEDowDAEhQPHVs0xj7SIzA"

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

    # and
    api_key = "eyJhcGlfYWRkcmVzcyI6Imhvc3QiLCJhcGlfdXJsIjoiaG9zdCIsImFwaV9rZXkiOiI0NDBlZTE0Ni00NDJlLTRkN2MtYThhYy0yNzZiYTk0MGEwNzEifQ=="
    credentials = Credentials.from_token(token=api_key)

    # when
    token = exchange_to_access_token(client_mock, credentials)

    # then
    assert token.access_token == access_token
    assert token.refresh_token == refresh_token


def test_unauthorized(mocker):
    # given
    client_mock = mocker.MagicMock(spec=Client)
    request_mock = mocker.MagicMock()
    client_mock.get_httpx_client.return_value = request_mock
    request_mock.request.return_value = mocker.MagicMock()
    request_mock.request.return_value.status_code = 401

    # and
    api_key = "eyJhcGlfYWRkcmVzcyI6Imhvc3QiLCJhcGlfdXJsIjoiaG9zdCIsImFwaV9rZXkiOiI0NDBlZTE0Ni00NDJlLTRkN2MtYThhYy0yNzZiYTk0MGEwNzEifQ=="
    credentials = Credentials.from_token(token=api_key)

    # when
    token = exchange_to_access_token(client_mock, credentials)

    # then
    assert token is None
