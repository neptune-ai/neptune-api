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
)

import httpx

from ... import errors
from ...client import (
    AuthenticatedClient,
    Client,
)
from ...models.get_string_series_values_csv_expected_content_disposition import (
    GetStringSeriesValuesCSVExpectedContentDisposition,
)
from ...types import (
    UNSET,
    Response,
    Unset,
)


def _get_kwargs(
    *,
    attribute: str,
    expected_content_disposition: Union[
        Unset, GetStringSeriesValuesCSVExpectedContentDisposition
    ] = GetStringSeriesValuesCSVExpectedContentDisposition.ATTACHMENT,
    experiment_id: Union[Unset, str] = UNSET,
    gzipped: Union[Unset, bool] = UNSET,
    holder_identifier: Union[Unset, str] = UNSET,
    holder_type: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["attribute"] = attribute

    json_expected_content_disposition: Union[Unset, str] = UNSET
    if not isinstance(expected_content_disposition, Unset):
        json_expected_content_disposition = expected_content_disposition.value

    params["expectedContentDisposition"] = json_expected_content_disposition

    params["experimentId"] = experiment_id

    params["gzipped"] = gzipped

    params["holderIdentifier"] = holder_identifier

    params["holderType"] = holder_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/leaderboard/v1/attributes/stringSeries/csv",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 400:
        return None
    if response.status_code == 401:
        return None
    if response.status_code == 403:
        return None
    if response.status_code == 404:
        return None
    if response.status_code == 408:
        return None
    if response.status_code == 409:
        return None
    if response.status_code == 422:
        return None
    if response.status_code == 429:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
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
    expected_content_disposition: Union[
        Unset, GetStringSeriesValuesCSVExpectedContentDisposition
    ] = GetStringSeriesValuesCSVExpectedContentDisposition.ATTACHMENT,
    experiment_id: Union[Unset, str] = UNSET,
    gzipped: Union[Unset, bool] = UNSET,
    holder_identifier: Union[Unset, str] = UNSET,
    holder_type: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Get values of a string series

    Args:
        attribute (str):
        expected_content_disposition (Union[Unset,
            GetStringSeriesValuesCSVExpectedContentDisposition]):  Default:
            GetStringSeriesValuesCSVExpectedContentDisposition.ATTACHMENT.
        experiment_id (Union[Unset, str]):
        gzipped (Union[Unset, bool]):
        holder_identifier (Union[Unset, str]):
        holder_type (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        attribute=attribute,
        expected_content_disposition=expected_content_disposition,
        experiment_id=experiment_id,
        gzipped=gzipped,
        holder_identifier=holder_identifier,
        holder_type=holder_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    attribute: str,
    expected_content_disposition: Union[
        Unset, GetStringSeriesValuesCSVExpectedContentDisposition
    ] = GetStringSeriesValuesCSVExpectedContentDisposition.ATTACHMENT,
    experiment_id: Union[Unset, str] = UNSET,
    gzipped: Union[Unset, bool] = UNSET,
    holder_identifier: Union[Unset, str] = UNSET,
    holder_type: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Get values of a string series

    Args:
        attribute (str):
        expected_content_disposition (Union[Unset,
            GetStringSeriesValuesCSVExpectedContentDisposition]):  Default:
            GetStringSeriesValuesCSVExpectedContentDisposition.ATTACHMENT.
        experiment_id (Union[Unset, str]):
        gzipped (Union[Unset, bool]):
        holder_identifier (Union[Unset, str]):
        holder_type (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        attribute=attribute,
        expected_content_disposition=expected_content_disposition,
        experiment_id=experiment_id,
        gzipped=gzipped,
        holder_identifier=holder_identifier,
        holder_type=holder_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
