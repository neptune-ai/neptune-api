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

from neptune_api.proto.neptune_pb.ingest.v1.pub.client_pb2 import SubmitResponse
from neptune_api.proto.neptune_pb.ingest.v1.pub.ingest_pb2 import RunOperation
from neptune_api.types import Response

from ... import errors
from ...client import (
    AuthenticatedClient,
    Client,
)


def _get_kwargs(
    *,
    body: RunOperation,
    family: str,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/api/client/v1/ingest",
        "params": {
            "family": family,
        },
        "content": body.SerializeToString(),
    }

    headers["Content-Type"] = "application/x-protobuf"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SubmitResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SubmitResponse()
        response_200.ParseFromString(response.content)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SubmitResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RunOperation,
    family: str,
) -> Response[SubmitResponse]:
    """Submits a new operation to be performed asynchronously

    Args:
        body (RunOperation): Operation to submit
        family (str): Partition key

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SubmitResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        family=family,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: RunOperation,
    family: str,
) -> Optional[SubmitResponse]:
    """Submits a new operation to be performed asynchronously

    Args:
        body (RunOperation): Operation to submit
        family (str): Partition key

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SubmitResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        family=family,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RunOperation,
    family: str,
) -> Response[SubmitResponse]:
    """Submits a new operation to be performed asynchronously

    Args:
        body (RunOperation): Operation to submit
        family (str): Partition key

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SubmitResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        family=family,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RunOperation,
    family: str,
) -> Optional[SubmitResponse]:
    """Submits a new operation to be performed asynchronously

    Args:
        body (RunOperation): Operation to submit
        family (str): Partition key

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SubmitResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            family=family,
        )
    ).parsed
