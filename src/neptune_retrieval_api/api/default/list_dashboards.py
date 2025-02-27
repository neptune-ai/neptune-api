#
# Copyright (c) 2025, Neptune Labs Sp. z o.o.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
from ...models.dashboard_list_dto import DashboardListDTO
from ...models.list_dashboards_dashboard_type import ListDashboardsDashboardType
from ...models.list_dashboards_drafts import ListDashboardsDrafts
from ...types import (
    UNSET,
    Response,
    Unset,
)


def _get_kwargs(
    *,
    branch_ids: Union[Unset, List[str]] = UNSET,
    dashboard_type: Union[Unset, ListDashboardsDashboardType] = UNSET,
    drafts: Union[Unset, ListDashboardsDrafts] = ListDashboardsDrafts.FALSE,
    owners: Union[Unset, List[str]] = UNSET,
    project_identifier: str,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_branch_ids: Union[Unset, List[str]] = UNSET
    if not isinstance(branch_ids, Unset):
        json_branch_ids = branch_ids

    params["branchIds"] = json_branch_ids

    json_dashboard_type: Union[Unset, str] = UNSET
    if not isinstance(dashboard_type, Unset):
        json_dashboard_type = dashboard_type.value

    params["dashboardType"] = json_dashboard_type

    json_drafts: Union[Unset, str] = UNSET
    if not isinstance(drafts, Unset):
        json_drafts = drafts.value

    params["drafts"] = json_drafts

    json_owners: Union[Unset, List[str]] = UNSET
    if not isinstance(owners, Unset):
        json_owners = owners

    params["owners"] = json_owners

    params["projectIdentifier"] = project_identifier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/leaderboard/v1/dashboards",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DashboardListDTO]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DashboardListDTO.from_dict(response.json())

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
) -> Response[Union[Any, DashboardListDTO]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    branch_ids: Union[Unset, List[str]] = UNSET,
    dashboard_type: Union[Unset, ListDashboardsDashboardType] = UNSET,
    drafts: Union[Unset, ListDashboardsDrafts] = ListDashboardsDrafts.FALSE,
    owners: Union[Unset, List[str]] = UNSET,
    project_identifier: str,
) -> Response[Union[Any, DashboardListDTO]]:
    """List latest versions of dashboard

    Args:
        branch_ids (Union[Unset, List[str]]):
        dashboard_type (Union[Unset, ListDashboardsDashboardType]):
        drafts (Union[Unset, ListDashboardsDrafts]):  Default: ListDashboardsDrafts.FALSE.
        owners (Union[Unset, List[str]]):
        project_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DashboardListDTO]]
    """

    kwargs = _get_kwargs(
        branch_ids=branch_ids,
        dashboard_type=dashboard_type,
        drafts=drafts,
        owners=owners,
        project_identifier=project_identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    branch_ids: Union[Unset, List[str]] = UNSET,
    dashboard_type: Union[Unset, ListDashboardsDashboardType] = UNSET,
    drafts: Union[Unset, ListDashboardsDrafts] = ListDashboardsDrafts.FALSE,
    owners: Union[Unset, List[str]] = UNSET,
    project_identifier: str,
) -> Optional[Union[Any, DashboardListDTO]]:
    """List latest versions of dashboard

    Args:
        branch_ids (Union[Unset, List[str]]):
        dashboard_type (Union[Unset, ListDashboardsDashboardType]):
        drafts (Union[Unset, ListDashboardsDrafts]):  Default: ListDashboardsDrafts.FALSE.
        owners (Union[Unset, List[str]]):
        project_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DashboardListDTO]
    """

    return sync_detailed(
        client=client,
        branch_ids=branch_ids,
        dashboard_type=dashboard_type,
        drafts=drafts,
        owners=owners,
        project_identifier=project_identifier,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    branch_ids: Union[Unset, List[str]] = UNSET,
    dashboard_type: Union[Unset, ListDashboardsDashboardType] = UNSET,
    drafts: Union[Unset, ListDashboardsDrafts] = ListDashboardsDrafts.FALSE,
    owners: Union[Unset, List[str]] = UNSET,
    project_identifier: str,
) -> Response[Union[Any, DashboardListDTO]]:
    """List latest versions of dashboard

    Args:
        branch_ids (Union[Unset, List[str]]):
        dashboard_type (Union[Unset, ListDashboardsDashboardType]):
        drafts (Union[Unset, ListDashboardsDrafts]):  Default: ListDashboardsDrafts.FALSE.
        owners (Union[Unset, List[str]]):
        project_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DashboardListDTO]]
    """

    kwargs = _get_kwargs(
        branch_ids=branch_ids,
        dashboard_type=dashboard_type,
        drafts=drafts,
        owners=owners,
        project_identifier=project_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    branch_ids: Union[Unset, List[str]] = UNSET,
    dashboard_type: Union[Unset, ListDashboardsDashboardType] = UNSET,
    drafts: Union[Unset, ListDashboardsDrafts] = ListDashboardsDrafts.FALSE,
    owners: Union[Unset, List[str]] = UNSET,
    project_identifier: str,
) -> Optional[Union[Any, DashboardListDTO]]:
    """List latest versions of dashboard

    Args:
        branch_ids (Union[Unset, List[str]]):
        dashboard_type (Union[Unset, ListDashboardsDashboardType]):
        drafts (Union[Unset, ListDashboardsDrafts]):  Default: ListDashboardsDrafts.FALSE.
        owners (Union[Unset, List[str]]):
        project_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DashboardListDTO]
    """

    return (
        await asyncio_detailed(
            client=client,
            branch_ids=branch_ids,
            dashboard_type=dashboard_type,
            drafts=drafts,
            owners=owners,
            project_identifier=project_identifier,
        )
    ).parsed
