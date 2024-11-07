from http import HTTPStatus
from typing import (
    Any,
    Dict,
    Optional,
    Union,
    cast,
)

import httpx

from ... import errors
from ...client import (
    AuthenticatedClient,
    Client,
)
from ...models.download_prepare_request import DownloadPrepareRequest
from ...models.leaderboard_csv_export_params_dto import LeaderboardCsvExportParamsDTO
from ...types import (
    UNSET,
    Response,
)


def _get_kwargs(
    *,
    body: LeaderboardCsvExportParamsDTO,
    project_identifier: str,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    params["projectIdentifier"] = project_identifier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/api/leaderboard/v1/prepareForDownloadLeaderboardCsv",
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DownloadPrepareRequest]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = DownloadPrepareRequest.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.REQUEST_TIMEOUT:
        response_408 = cast(Any, None)
        return response_408
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = cast(Any, None)
        return response_409
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = cast(Any, None)
        return response_422
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = cast(Any, None)
        return response_429
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, DownloadPrepareRequest]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: LeaderboardCsvExportParamsDTO,
    project_identifier: str,
) -> Response[Union[Any, DownloadPrepareRequest]]:
    """Prepare download leaderboard as CSV

    Args:
        project_identifier (str):
        body (LeaderboardCsvExportParamsDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DownloadPrepareRequest]]
    """

    kwargs = _get_kwargs(
        body=body,
        project_identifier=project_identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: LeaderboardCsvExportParamsDTO,
    project_identifier: str,
) -> Optional[Union[Any, DownloadPrepareRequest]]:
    """Prepare download leaderboard as CSV

    Args:
        project_identifier (str):
        body (LeaderboardCsvExportParamsDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DownloadPrepareRequest]
    """

    return sync_detailed(
        client=client,
        body=body,
        project_identifier=project_identifier,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: LeaderboardCsvExportParamsDTO,
    project_identifier: str,
) -> Response[Union[Any, DownloadPrepareRequest]]:
    """Prepare download leaderboard as CSV

    Args:
        project_identifier (str):
        body (LeaderboardCsvExportParamsDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DownloadPrepareRequest]]
    """

    kwargs = _get_kwargs(
        body=body,
        project_identifier=project_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: LeaderboardCsvExportParamsDTO,
    project_identifier: str,
) -> Optional[Union[Any, DownloadPrepareRequest]]:
    """Prepare download leaderboard as CSV

    Args:
        project_identifier (str):
        body (LeaderboardCsvExportParamsDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DownloadPrepareRequest]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            project_identifier=project_identifier,
        )
    ).parsed
