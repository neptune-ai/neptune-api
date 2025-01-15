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

import httpx

from ... import errors
from ...client import (
    AuthenticatedClient,
    Client,
)
from ...models.checkpoint_list_dto import CheckpointListDTO
from ...types import (
    UNSET,
    Response,
    Unset,
)


def _get_kwargs(
    *,
    id: Union[Unset, List[str]] = UNSET,
    limit: Union[Unset, int] = 100,
    max_creation_time: Union[Unset, datetime.datetime] = UNSET,
    min_creation_time: Union[Unset, datetime.datetime] = UNSET,
    notebook_id: str,
    offset: Union[Unset, int] = 0,
    owner: Union[Unset, List[str]] = UNSET,
    search_term: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_id: Union[Unset, List[str]] = UNSET
    if not isinstance(id, Unset):
        json_id = id

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

    params["notebookId"] = notebook_id

    params["offset"] = offset

    json_owner: Union[Unset, List[str]] = UNSET
    if not isinstance(owner, Unset):
        json_owner = owner

    params["owner"] = json_owner

    params["searchTerm"] = search_term

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/leaderboard/v1/notebooks/checkpoints",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CheckpointListDTO]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CheckpointListDTO.from_dict(response.json())

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
) -> Response[Union[Any, CheckpointListDTO]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    id: Union[Unset, List[str]] = UNSET,
    limit: Union[Unset, int] = 100,
    max_creation_time: Union[Unset, datetime.datetime] = UNSET,
    min_creation_time: Union[Unset, datetime.datetime] = UNSET,
    notebook_id: str,
    offset: Union[Unset, int] = 0,
    owner: Union[Unset, List[str]] = UNSET,
    search_term: Union[Unset, str] = UNSET,
) -> Response[Union[Any, CheckpointListDTO]]:
    """Get notebook checkpoints

    Args:
        id (Union[Unset, List[str]]):
        limit (Union[Unset, int]):  Default: 100.
        max_creation_time (Union[Unset, datetime.datetime]):
        min_creation_time (Union[Unset, datetime.datetime]):
        notebook_id (str):
        offset (Union[Unset, int]):  Default: 0.
        owner (Union[Unset, List[str]]):
        search_term (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CheckpointListDTO]]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        max_creation_time=max_creation_time,
        min_creation_time=min_creation_time,
        notebook_id=notebook_id,
        offset=offset,
        owner=owner,
        search_term=search_term,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    id: Union[Unset, List[str]] = UNSET,
    limit: Union[Unset, int] = 100,
    max_creation_time: Union[Unset, datetime.datetime] = UNSET,
    min_creation_time: Union[Unset, datetime.datetime] = UNSET,
    notebook_id: str,
    offset: Union[Unset, int] = 0,
    owner: Union[Unset, List[str]] = UNSET,
    search_term: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, CheckpointListDTO]]:
    """Get notebook checkpoints

    Args:
        id (Union[Unset, List[str]]):
        limit (Union[Unset, int]):  Default: 100.
        max_creation_time (Union[Unset, datetime.datetime]):
        min_creation_time (Union[Unset, datetime.datetime]):
        notebook_id (str):
        offset (Union[Unset, int]):  Default: 0.
        owner (Union[Unset, List[str]]):
        search_term (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CheckpointListDTO]
    """

    return sync_detailed(
        client=client,
        id=id,
        limit=limit,
        max_creation_time=max_creation_time,
        min_creation_time=min_creation_time,
        notebook_id=notebook_id,
        offset=offset,
        owner=owner,
        search_term=search_term,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    id: Union[Unset, List[str]] = UNSET,
    limit: Union[Unset, int] = 100,
    max_creation_time: Union[Unset, datetime.datetime] = UNSET,
    min_creation_time: Union[Unset, datetime.datetime] = UNSET,
    notebook_id: str,
    offset: Union[Unset, int] = 0,
    owner: Union[Unset, List[str]] = UNSET,
    search_term: Union[Unset, str] = UNSET,
) -> Response[Union[Any, CheckpointListDTO]]:
    """Get notebook checkpoints

    Args:
        id (Union[Unset, List[str]]):
        limit (Union[Unset, int]):  Default: 100.
        max_creation_time (Union[Unset, datetime.datetime]):
        min_creation_time (Union[Unset, datetime.datetime]):
        notebook_id (str):
        offset (Union[Unset, int]):  Default: 0.
        owner (Union[Unset, List[str]]):
        search_term (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CheckpointListDTO]]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        max_creation_time=max_creation_time,
        min_creation_time=min_creation_time,
        notebook_id=notebook_id,
        offset=offset,
        owner=owner,
        search_term=search_term,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    id: Union[Unset, List[str]] = UNSET,
    limit: Union[Unset, int] = 100,
    max_creation_time: Union[Unset, datetime.datetime] = UNSET,
    min_creation_time: Union[Unset, datetime.datetime] = UNSET,
    notebook_id: str,
    offset: Union[Unset, int] = 0,
    owner: Union[Unset, List[str]] = UNSET,
    search_term: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, CheckpointListDTO]]:
    """Get notebook checkpoints

    Args:
        id (Union[Unset, List[str]]):
        limit (Union[Unset, int]):  Default: 100.
        max_creation_time (Union[Unset, datetime.datetime]):
        min_creation_time (Union[Unset, datetime.datetime]):
        notebook_id (str):
        offset (Union[Unset, int]):  Default: 0.
        owner (Union[Unset, List[str]]):
        search_term (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CheckpointListDTO]
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            limit=limit,
            max_creation_time=max_creation_time,
            min_creation_time=min_creation_time,
            notebook_id=notebook_id,
            offset=offset,
            owner=owner,
            search_term=search_term,
        )
    ).parsed
