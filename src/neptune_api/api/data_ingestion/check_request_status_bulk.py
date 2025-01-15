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

from neptune_api import errors
from neptune_api.client import (
    AuthenticatedClient,
    Client,
)
from neptune_api.proto.neptune_pb.ingest.v1.pub.client_pb2 import (
    BulkRequestStatus,
    RequestIdList,
)
from neptune_api.types import Response


def _get_kwargs(
    *,
    body: RequestIdList,
    project_identifier: str,
) -> Dict[str, Any]:
    return {
        "method": "post",
        "url": "/api/client/v1/ingest/check",
        "params": {
            "projectIdentifier": project_identifier,
        },
        "content": body.SerializeToString(),
        "headers": {
            "Content-Type": "application/x-protobuf",
        },
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[BulkRequestStatus]:
    if response.status_code == HTTPStatus.OK:
        response_200 = BulkRequestStatus()
        response_200.ParseFromString(response.content)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[BulkRequestStatus]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RequestIdList,
    project_identifier: str,
) -> Response[BulkRequestStatus]:
    """Checks the processing status of multiple operations

    Args:
        project_identifier (str):
        body (RequestIdList):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkRequestStatus]
    """

    kwargs = _get_kwargs(
        body=body,
        project_identifier=project_identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: RequestIdList,
    project_identifier: str,
) -> Optional[BulkRequestStatus]:
    """Checks the processing status of multiple operations

    Args:
        project_identifier (str):
        body (RequestIdList):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkRequestStatus
    """

    return sync_detailed(
        client=client,
        body=body,
        project_identifier=project_identifier,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RequestIdList,
    project_identifier: str,
) -> Response[BulkRequestStatus]:
    """Checks the processing status of multiple operations

    Args:
        project_identifier (str):
        body (RequestIdList):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkRequestStatus]
    """

    kwargs = _get_kwargs(
        body=body,
        project_identifier=project_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RequestIdList,
    project_identifier: str,
) -> Optional[BulkRequestStatus]:
    """Checks the processing status of multiple operations

    Args:
        project_identifier (str):
        body (RequestIdList):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkRequestStatus
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            project_identifier=project_identifier,
        )
    ).parsed
