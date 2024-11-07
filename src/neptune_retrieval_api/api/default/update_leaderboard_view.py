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
from ...models.leaderboard_view_dto import LeaderboardViewDTO
from ...models.leaderboard_view_update_dto import LeaderboardViewUpdateDTO
from ...types import (
    UNSET,
    Response,
)


def _get_kwargs(
    view_id: str,
    *,
    body: LeaderboardViewUpdateDTO,
    project_identifier: str,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    params["projectIdentifier"] = project_identifier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/api/leaderboard/v1/views/{view_id}",
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, LeaderboardViewDTO]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = LeaderboardViewDTO.from_dict(response.json())

        return response_200
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
) -> Response[Union[Any, LeaderboardViewDTO]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    view_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: LeaderboardViewUpdateDTO,
    project_identifier: str,
) -> Response[Union[Any, LeaderboardViewDTO]]:
    """Update view

    Args:
        view_id (str):
        project_identifier (str):
        body (LeaderboardViewUpdateDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, LeaderboardViewDTO]]
    """

    kwargs = _get_kwargs(
        view_id=view_id,
        body=body,
        project_identifier=project_identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    view_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: LeaderboardViewUpdateDTO,
    project_identifier: str,
) -> Optional[Union[Any, LeaderboardViewDTO]]:
    """Update view

    Args:
        view_id (str):
        project_identifier (str):
        body (LeaderboardViewUpdateDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, LeaderboardViewDTO]
    """

    return sync_detailed(
        view_id=view_id,
        client=client,
        body=body,
        project_identifier=project_identifier,
    ).parsed


async def asyncio_detailed(
    view_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: LeaderboardViewUpdateDTO,
    project_identifier: str,
) -> Response[Union[Any, LeaderboardViewDTO]]:
    """Update view

    Args:
        view_id (str):
        project_identifier (str):
        body (LeaderboardViewUpdateDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, LeaderboardViewDTO]]
    """

    kwargs = _get_kwargs(
        view_id=view_id,
        body=body,
        project_identifier=project_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    view_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: LeaderboardViewUpdateDTO,
    project_identifier: str,
) -> Optional[Union[Any, LeaderboardViewDTO]]:
    """Update view

    Args:
        view_id (str):
        project_identifier (str):
        body (LeaderboardViewUpdateDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, LeaderboardViewDTO]
    """

    return (
        await asyncio_detailed(
            view_id=view_id,
            client=client,
            body=body,
            project_identifier=project_identifier,
        )
    ).parsed
