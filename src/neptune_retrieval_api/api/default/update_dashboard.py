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
    Optional,
    Union,
    cast,
)
from uuid import UUID

import httpx

from ... import errors
from ...client import (
    AuthenticatedClient,
    Client,
)
from ...models.dashboard_dto import DashboardDTO
from ...models.update_dashboard_dto import UpdateDashboardDTO
from ...types import (
    UNSET,
    Response,
)


def _get_kwargs(
    dashboard_id: UUID,
    *,
    body: UpdateDashboardDTO,
    project_identifier: str,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    params["projectIdentifier"] = project_identifier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/api/leaderboard/v1/dashboards/{dashboard_id}",
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DashboardDTO]]:
    if response.status_code == 200:
        response_200 = DashboardDTO.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 408:
        response_408 = cast(Any, None)
        return response_408
    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409
    if response.status_code == 422:
        response_422 = cast(Any, None)
        return response_422
    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, DashboardDTO]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dashboard_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateDashboardDTO,
    project_identifier: str,
) -> Response[Union[Any, DashboardDTO]]:
    """Update dashboard

    Args:
        dashboard_id (UUID):
        project_identifier (str):
        body (UpdateDashboardDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DashboardDTO]]
    """

    kwargs = _get_kwargs(
        dashboard_id=dashboard_id,
        body=body,
        project_identifier=project_identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dashboard_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateDashboardDTO,
    project_identifier: str,
) -> Optional[Union[Any, DashboardDTO]]:
    """Update dashboard

    Args:
        dashboard_id (UUID):
        project_identifier (str):
        body (UpdateDashboardDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DashboardDTO]
    """

    return sync_detailed(
        dashboard_id=dashboard_id,
        client=client,
        body=body,
        project_identifier=project_identifier,
    ).parsed


async def asyncio_detailed(
    dashboard_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateDashboardDTO,
    project_identifier: str,
) -> Response[Union[Any, DashboardDTO]]:
    """Update dashboard

    Args:
        dashboard_id (UUID):
        project_identifier (str):
        body (UpdateDashboardDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DashboardDTO]]
    """

    kwargs = _get_kwargs(
        dashboard_id=dashboard_id,
        body=body,
        project_identifier=project_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dashboard_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateDashboardDTO,
    project_identifier: str,
) -> Optional[Union[Any, DashboardDTO]]:
    """Update dashboard

    Args:
        dashboard_id (UUID):
        project_identifier (str):
        body (UpdateDashboardDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DashboardDTO]
    """

    return (
        await asyncio_detailed(
            dashboard_id=dashboard_id,
            client=client,
            body=body,
            project_identifier=project_identifier,
        )
    ).parsed
