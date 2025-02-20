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

import datetime
from http import HTTPStatus
from typing import (
    Any,
    Dict,
    List,
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
from ...models.list_notebooks_sort_by import ListNotebooksSortBy
from ...models.list_notebooks_sort_direction import ListNotebooksSortDirection
from ...models.notebook_list_dto import NotebookListDTO
from ...types import (
    UNSET,
    Response,
    Unset,
)


def _get_kwargs(
    *,
    id: Union[Unset, List[UUID]] = UNSET,
    limit: Union[Unset, int] = 100,
    max_creation_time: Union[Unset, datetime.datetime] = UNSET,
    min_creation_time: Union[Unset, datetime.datetime] = UNSET,
    offset: Union[Unset, int] = 0,
    owner: Union[Unset, List[str]] = UNSET,
    project_identifier: str,
    sort_by: Union[Unset, ListNotebooksSortBy] = UNSET,
    sort_direction: Union[Unset, ListNotebooksSortDirection] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_id: Union[Unset, List[str]] = UNSET
    if not isinstance(id, Unset):
        json_id = []
        for id_item_data in id:
            id_item = str(id_item_data)
            json_id.append(id_item)

    params["id"] = json_id

    params["limit"] = limit

    json_max_creation_time: Union[Unset, str] = UNSET
    if not isinstance(max_creation_time, Unset):
        json_max_creation_time = max_creation_time.isoformat()
    params["maxCreationTime"] = json_max_creation_time

    json_min_creation_time: Union[Unset, str] = UNSET
    if not isinstance(min_creation_time, Unset):
        json_min_creation_time = min_creation_time.isoformat()
    params["minCreationTime"] = json_min_creation_time

    params["offset"] = offset

    json_owner: Union[Unset, List[str]] = UNSET
    if not isinstance(owner, Unset):
        json_owner = owner

    params["owner"] = json_owner

    params["projectIdentifier"] = project_identifier

    json_sort_by: Union[Unset, str] = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value

    params["sortBy"] = json_sort_by

    json_sort_direction: Union[Unset, str] = UNSET
    if not isinstance(sort_direction, Unset):
        json_sort_direction = sort_direction.value

    params["sortDirection"] = json_sort_direction

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/leaderboard/v1/notebooks",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, NotebookListDTO]]:
    if response.status_code == 200:
        response_200 = NotebookListDTO.from_dict(response.json())

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
) -> Response[Union[Any, NotebookListDTO]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    id: Union[Unset, List[UUID]] = UNSET,
    limit: Union[Unset, int] = 100,
    max_creation_time: Union[Unset, datetime.datetime] = UNSET,
    min_creation_time: Union[Unset, datetime.datetime] = UNSET,
    offset: Union[Unset, int] = 0,
    owner: Union[Unset, List[str]] = UNSET,
    project_identifier: str,
    sort_by: Union[Unset, ListNotebooksSortBy] = UNSET,
    sort_direction: Union[Unset, ListNotebooksSortDirection] = UNSET,
) -> Response[Union[Any, NotebookListDTO]]:
    """Get notebooks

    Args:
        id (Union[Unset, List[UUID]]):
        limit (Union[Unset, int]):  Default: 100.
        max_creation_time (Union[Unset, datetime.datetime]):
        min_creation_time (Union[Unset, datetime.datetime]):
        offset (Union[Unset, int]):  Default: 0.
        owner (Union[Unset, List[str]]):
        project_identifier (str):
        sort_by (Union[Unset, ListNotebooksSortBy]):
        sort_direction (Union[Unset, ListNotebooksSortDirection]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NotebookListDTO]]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        max_creation_time=max_creation_time,
        min_creation_time=min_creation_time,
        offset=offset,
        owner=owner,
        project_identifier=project_identifier,
        sort_by=sort_by,
        sort_direction=sort_direction,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    id: Union[Unset, List[UUID]] = UNSET,
    limit: Union[Unset, int] = 100,
    max_creation_time: Union[Unset, datetime.datetime] = UNSET,
    min_creation_time: Union[Unset, datetime.datetime] = UNSET,
    offset: Union[Unset, int] = 0,
    owner: Union[Unset, List[str]] = UNSET,
    project_identifier: str,
    sort_by: Union[Unset, ListNotebooksSortBy] = UNSET,
    sort_direction: Union[Unset, ListNotebooksSortDirection] = UNSET,
) -> Optional[Union[Any, NotebookListDTO]]:
    """Get notebooks

    Args:
        id (Union[Unset, List[UUID]]):
        limit (Union[Unset, int]):  Default: 100.
        max_creation_time (Union[Unset, datetime.datetime]):
        min_creation_time (Union[Unset, datetime.datetime]):
        offset (Union[Unset, int]):  Default: 0.
        owner (Union[Unset, List[str]]):
        project_identifier (str):
        sort_by (Union[Unset, ListNotebooksSortBy]):
        sort_direction (Union[Unset, ListNotebooksSortDirection]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, NotebookListDTO]
    """

    return sync_detailed(
        client=client,
        id=id,
        limit=limit,
        max_creation_time=max_creation_time,
        min_creation_time=min_creation_time,
        offset=offset,
        owner=owner,
        project_identifier=project_identifier,
        sort_by=sort_by,
        sort_direction=sort_direction,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    id: Union[Unset, List[UUID]] = UNSET,
    limit: Union[Unset, int] = 100,
    max_creation_time: Union[Unset, datetime.datetime] = UNSET,
    min_creation_time: Union[Unset, datetime.datetime] = UNSET,
    offset: Union[Unset, int] = 0,
    owner: Union[Unset, List[str]] = UNSET,
    project_identifier: str,
    sort_by: Union[Unset, ListNotebooksSortBy] = UNSET,
    sort_direction: Union[Unset, ListNotebooksSortDirection] = UNSET,
) -> Response[Union[Any, NotebookListDTO]]:
    """Get notebooks

    Args:
        id (Union[Unset, List[UUID]]):
        limit (Union[Unset, int]):  Default: 100.
        max_creation_time (Union[Unset, datetime.datetime]):
        min_creation_time (Union[Unset, datetime.datetime]):
        offset (Union[Unset, int]):  Default: 0.
        owner (Union[Unset, List[str]]):
        project_identifier (str):
        sort_by (Union[Unset, ListNotebooksSortBy]):
        sort_direction (Union[Unset, ListNotebooksSortDirection]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NotebookListDTO]]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        max_creation_time=max_creation_time,
        min_creation_time=min_creation_time,
        offset=offset,
        owner=owner,
        project_identifier=project_identifier,
        sort_by=sort_by,
        sort_direction=sort_direction,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    id: Union[Unset, List[UUID]] = UNSET,
    limit: Union[Unset, int] = 100,
    max_creation_time: Union[Unset, datetime.datetime] = UNSET,
    min_creation_time: Union[Unset, datetime.datetime] = UNSET,
    offset: Union[Unset, int] = 0,
    owner: Union[Unset, List[str]] = UNSET,
    project_identifier: str,
    sort_by: Union[Unset, ListNotebooksSortBy] = UNSET,
    sort_direction: Union[Unset, ListNotebooksSortDirection] = UNSET,
) -> Optional[Union[Any, NotebookListDTO]]:
    """Get notebooks

    Args:
        id (Union[Unset, List[UUID]]):
        limit (Union[Unset, int]):  Default: 100.
        max_creation_time (Union[Unset, datetime.datetime]):
        min_creation_time (Union[Unset, datetime.datetime]):
        offset (Union[Unset, int]):  Default: 0.
        owner (Union[Unset, List[str]]):
        project_identifier (str):
        sort_by (Union[Unset, ListNotebooksSortBy]):
        sort_direction (Union[Unset, ListNotebooksSortDirection]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, NotebookListDTO]
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            limit=limit,
            max_creation_time=max_creation_time,
            min_creation_time=min_creation_time,
            offset=offset,
            owner=owner,
            project_identifier=project_identifier,
            sort_by=sort_by,
            sort_direction=sort_direction,
        )
    ).parsed
