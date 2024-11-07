from http import HTTPStatus
from typing import (
    Any,
    Dict,
    List,
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
from ...models.series_view_list_dto import SeriesViewListDTO
from ...models.series_view_request_dto import SeriesViewRequestDTO
from ...types import (
    UNSET,
    Response,
    Unset,
)


def _get_kwargs(
    *,
    body: List["SeriesViewRequestDTO"],
    point_count: Union[Unset, int] = 1000,
    project_identifier: str,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    params["pointCount"] = point_count

    params["projectIdentifier"] = project_identifier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/api/leaderboard/v1/channels/view",
        "params": params,
    }

    _body = []
    for body_item_data in body:
        body_item = body_item_data.to_dict()
        _body.append(body_item)

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, SeriesViewListDTO]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SeriesViewListDTO.from_dict(response.json())

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
) -> Response[Union[Any, SeriesViewListDTO]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: List["SeriesViewRequestDTO"],
    point_count: Union[Unset, int] = 1000,
    project_identifier: str,
) -> Response[Union[Any, SeriesViewListDTO]]:
    """Get series view by channel UUIDs

    Args:
        point_count (Union[Unset, int]):  Default: 1000.
        project_identifier (str):
        body (List['SeriesViewRequestDTO']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SeriesViewListDTO]]
    """

    kwargs = _get_kwargs(
        body=body,
        point_count=point_count,
        project_identifier=project_identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: List["SeriesViewRequestDTO"],
    point_count: Union[Unset, int] = 1000,
    project_identifier: str,
) -> Optional[Union[Any, SeriesViewListDTO]]:
    """Get series view by channel UUIDs

    Args:
        point_count (Union[Unset, int]):  Default: 1000.
        project_identifier (str):
        body (List['SeriesViewRequestDTO']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SeriesViewListDTO]
    """

    return sync_detailed(
        client=client,
        body=body,
        point_count=point_count,
        project_identifier=project_identifier,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: List["SeriesViewRequestDTO"],
    point_count: Union[Unset, int] = 1000,
    project_identifier: str,
) -> Response[Union[Any, SeriesViewListDTO]]:
    """Get series view by channel UUIDs

    Args:
        point_count (Union[Unset, int]):  Default: 1000.
        project_identifier (str):
        body (List['SeriesViewRequestDTO']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SeriesViewListDTO]]
    """

    kwargs = _get_kwargs(
        body=body,
        point_count=point_count,
        project_identifier=project_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: List["SeriesViewRequestDTO"],
    point_count: Union[Unset, int] = 1000,
    project_identifier: str,
) -> Optional[Union[Any, SeriesViewListDTO]]:
    """Get series view by channel UUIDs

    Args:
        point_count (Union[Unset, int]):  Default: 1000.
        project_identifier (str):
        body (List['SeriesViewRequestDTO']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SeriesViewListDTO]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            point_count=point_count,
            project_identifier=project_identifier,
        )
    ).parsed
