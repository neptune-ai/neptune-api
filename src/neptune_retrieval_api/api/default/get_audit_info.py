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

import httpx

from ... import errors
from ...client import (
    AuthenticatedClient,
    Client,
)
from ...models.audit_info import AuditInfo
from ...types import (
    UNSET,
    Response,
    Unset,
)


def _get_kwargs(
    *,
    organization_identifier: str,
    project_identifier: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["organizationIdentifier"] = organization_identifier

    params["projectIdentifier"] = project_identifier

    params["username"] = username

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/leaderboard/v1/audit",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, AuditInfo]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AuditInfo.from_dict(response.json())

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
) -> Response[Union[Any, AuditInfo]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    organization_identifier: str,
    project_identifier: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Response[Union[Any, AuditInfo]]:
    """Get organization audit data

    Args:
        organization_identifier (str):
        project_identifier (Union[Unset, str]):
        username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, AuditInfo]]
    """

    kwargs = _get_kwargs(
        organization_identifier=organization_identifier,
        project_identifier=project_identifier,
        username=username,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    organization_identifier: str,
    project_identifier: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, AuditInfo]]:
    """Get organization audit data

    Args:
        organization_identifier (str):
        project_identifier (Union[Unset, str]):
        username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, AuditInfo]
    """

    return sync_detailed(
        client=client,
        organization_identifier=organization_identifier,
        project_identifier=project_identifier,
        username=username,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    organization_identifier: str,
    project_identifier: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Response[Union[Any, AuditInfo]]:
    """Get organization audit data

    Args:
        organization_identifier (str):
        project_identifier (Union[Unset, str]):
        username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, AuditInfo]]
    """

    kwargs = _get_kwargs(
        organization_identifier=organization_identifier,
        project_identifier=project_identifier,
        username=username,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    organization_identifier: str,
    project_identifier: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, AuditInfo]]:
    """Get organization audit data

    Args:
        organization_identifier (str):
        project_identifier (Union[Unset, str]):
        username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, AuditInfo]
    """

    return (
        await asyncio_detailed(
            client=client,
            organization_identifier=organization_identifier,
            project_identifier=project_identifier,
            username=username,
        )
    ).parsed
