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
from io import BytesIO
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
from ...models.get_float_series_values_proto_lineage import GetFloatSeriesValuesProtoLineage
from ...types import (
    UNSET,
    File,
    Response,
    Unset,
)


def _get_kwargs(
    *,
    attribute: str,
    experiment_id: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10000,
    lineage: Union[Unset, GetFloatSeriesValuesProtoLineage] = UNSET,
    skip_to_step: Union[Unset, float] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["attribute"] = attribute

    params["experimentId"] = experiment_id

    params["limit"] = limit

    json_lineage: Union[Unset, str] = UNSET
    if not isinstance(lineage, Unset):
        json_lineage = lineage.value

    params["lineage"] = json_lineage

    params["skipToStep"] = skip_to_step

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/leaderboard/v1/proto/attributes/series/float",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, File]]:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.content))

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
) -> Response[Union[Any, File]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    attribute: str,
    experiment_id: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10000,
    lineage: Union[Unset, GetFloatSeriesValuesProtoLineage] = UNSET,
    skip_to_step: Union[Unset, float] = UNSET,
) -> Response[Union[Any, File]]:
    """Get float series values

    Args:
        attribute (str):
        experiment_id (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 10000.
        lineage (Union[Unset, GetFloatSeriesValuesProtoLineage]):
        skip_to_step (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, File]]
    """

    kwargs = _get_kwargs(
        attribute=attribute,
        experiment_id=experiment_id,
        limit=limit,
        lineage=lineage,
        skip_to_step=skip_to_step,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    attribute: str,
    experiment_id: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10000,
    lineage: Union[Unset, GetFloatSeriesValuesProtoLineage] = UNSET,
    skip_to_step: Union[Unset, float] = UNSET,
) -> Optional[Union[Any, File]]:
    """Get float series values

    Args:
        attribute (str):
        experiment_id (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 10000.
        lineage (Union[Unset, GetFloatSeriesValuesProtoLineage]):
        skip_to_step (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, File]
    """

    return sync_detailed(
        client=client,
        attribute=attribute,
        experiment_id=experiment_id,
        limit=limit,
        lineage=lineage,
        skip_to_step=skip_to_step,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    attribute: str,
    experiment_id: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10000,
    lineage: Union[Unset, GetFloatSeriesValuesProtoLineage] = UNSET,
    skip_to_step: Union[Unset, float] = UNSET,
) -> Response[Union[Any, File]]:
    """Get float series values

    Args:
        attribute (str):
        experiment_id (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 10000.
        lineage (Union[Unset, GetFloatSeriesValuesProtoLineage]):
        skip_to_step (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, File]]
    """

    kwargs = _get_kwargs(
        attribute=attribute,
        experiment_id=experiment_id,
        limit=limit,
        lineage=lineage,
        skip_to_step=skip_to_step,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    attribute: str,
    experiment_id: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10000,
    lineage: Union[Unset, GetFloatSeriesValuesProtoLineage] = UNSET,
    skip_to_step: Union[Unset, float] = UNSET,
) -> Optional[Union[Any, File]]:
    """Get float series values

    Args:
        attribute (str):
        experiment_id (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 10000.
        lineage (Union[Unset, GetFloatSeriesValuesProtoLineage]):
        skip_to_step (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, File]
    """

    return (
        await asyncio_detailed(
            client=client,
            attribute=attribute,
            experiment_id=experiment_id,
            limit=limit,
            lineage=lineage,
            skip_to_step=skip_to_step,
        )
    ).parsed
