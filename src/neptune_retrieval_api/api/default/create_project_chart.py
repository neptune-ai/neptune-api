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
from ...models.new_project_chart_dto import NewProjectChartDTO
from ...models.project_chart_dto import ProjectChartDTO
from ...types import Response


def _get_kwargs(
    project_identifier: str,
    *,
    body: NewProjectChartDTO,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/api/leaderboard/v1/projectCharts/{project_identifier}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ProjectChartDTO]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ProjectChartDTO.from_dict(response.json())

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
) -> Response[Union[Any, ProjectChartDTO]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_identifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: NewProjectChartDTO,
) -> Response[Union[Any, ProjectChartDTO]]:
    """Create chart

    Args:
        project_identifier (str):
        body (NewProjectChartDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProjectChartDTO]]
    """

    kwargs = _get_kwargs(
        project_identifier=project_identifier,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_identifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: NewProjectChartDTO,
) -> Optional[Union[Any, ProjectChartDTO]]:
    """Create chart

    Args:
        project_identifier (str):
        body (NewProjectChartDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProjectChartDTO]
    """

    return sync_detailed(
        project_identifier=project_identifier,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_identifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: NewProjectChartDTO,
) -> Response[Union[Any, ProjectChartDTO]]:
    """Create chart

    Args:
        project_identifier (str):
        body (NewProjectChartDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProjectChartDTO]]
    """

    kwargs = _get_kwargs(
        project_identifier=project_identifier,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_identifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: NewProjectChartDTO,
) -> Optional[Union[Any, ProjectChartDTO]]:
    """Create chart

    Args:
        project_identifier (str):
        body (NewProjectChartDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProjectChartDTO]
    """

    return (
        await asyncio_detailed(
            project_identifier=project_identifier,
            client=client,
            body=body,
        )
    ).parsed
