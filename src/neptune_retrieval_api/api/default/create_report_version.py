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
from ...models.dependency_on_inaccessible_projects_error_dto import DependencyOnInaccessibleProjectsErrorDTO
from ...models.report_version_dto import ReportVersionDTO
from ...types import (
    UNSET,
    Response,
    Unset,
)


def _get_kwargs(
    *,
    body: ReportVersionDTO,
    project_identifier: str,
    report_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    params["projectIdentifier"] = project_identifier

    params["reportId"] = report_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/api/leaderboard/v1/reports",
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DependencyOnInaccessibleProjectsErrorDTO, ReportVersionDTO]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ReportVersionDTO.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = DependencyOnInaccessibleProjectsErrorDTO.from_dict(response.json())

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
) -> Response[Union[Any, DependencyOnInaccessibleProjectsErrorDTO, ReportVersionDTO]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ReportVersionDTO,
    project_identifier: str,
    report_id: Union[Unset, str] = UNSET,
) -> Response[Union[Any, DependencyOnInaccessibleProjectsErrorDTO, ReportVersionDTO]]:
    """Create a new report version

    Args:
        project_identifier (str):
        report_id (Union[Unset, str]):
        body (ReportVersionDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DependencyOnInaccessibleProjectsErrorDTO, ReportVersionDTO]]
    """

    kwargs = _get_kwargs(
        body=body,
        project_identifier=project_identifier,
        report_id=report_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ReportVersionDTO,
    project_identifier: str,
    report_id: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, DependencyOnInaccessibleProjectsErrorDTO, ReportVersionDTO]]:
    """Create a new report version

    Args:
        project_identifier (str):
        report_id (Union[Unset, str]):
        body (ReportVersionDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DependencyOnInaccessibleProjectsErrorDTO, ReportVersionDTO]
    """

    return sync_detailed(
        client=client,
        body=body,
        project_identifier=project_identifier,
        report_id=report_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ReportVersionDTO,
    project_identifier: str,
    report_id: Union[Unset, str] = UNSET,
) -> Response[Union[Any, DependencyOnInaccessibleProjectsErrorDTO, ReportVersionDTO]]:
    """Create a new report version

    Args:
        project_identifier (str):
        report_id (Union[Unset, str]):
        body (ReportVersionDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DependencyOnInaccessibleProjectsErrorDTO, ReportVersionDTO]]
    """

    kwargs = _get_kwargs(
        body=body,
        project_identifier=project_identifier,
        report_id=report_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ReportVersionDTO,
    project_identifier: str,
    report_id: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, DependencyOnInaccessibleProjectsErrorDTO, ReportVersionDTO]]:
    """Create a new report version

    Args:
        project_identifier (str):
        report_id (Union[Unset, str]):
        body (ReportVersionDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DependencyOnInaccessibleProjectsErrorDTO, ReportVersionDTO]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            project_identifier=project_identifier,
            report_id=report_id,
        )
    ).parsed
