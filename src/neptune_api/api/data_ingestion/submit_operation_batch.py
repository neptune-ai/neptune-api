from http import HTTPStatus
from typing import (
    Any,
    Dict,
    Optional,
    Union,
)

import httpx

from neptune_api.proto.neptune_pb.ingest.v1.pub.client_pb2 import RequestIdList
from neptune_api.proto.neptune_pb.ingest.v1.pub.ingest_pb2 import RunOperationBatch
from neptune_api.types import Response

from ... import errors
from ...client import (
    AuthenticatedClient,
    Client,
)


def _get_kwargs(
    *,
    body: RunOperationBatch,
    family: str,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/api/client/v1/ingest/batch",
        "params": {
            "family": family,
        },
        "content": body.SerializeToString(),
    }

    headers["Content-Type"] = "application/x-protobuf"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[RequestIdList]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RequestIdList()
        response_200.ParseFromString(response.content)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[RequestIdList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RunOperationBatch,
    family: str,
) -> Response[RequestIdList]:
    """Submits multiple new operation to be performed asynchronously

    Args:
        family (str):
        body (RunOperationBatch):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RequestIdList]
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
    body: RunOperationBatch,
    family: str,
) -> Optional[RequestIdList]:
    """Submits multiple new operation to be performed asynchronously

    Args:
        family (str):
        body (RunOperationBatch):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RequestIdList
    """

    return sync_detailed(
        client=client,
        body=body,
        family=family,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RunOperationBatch,
    family: str,
) -> Response[RequestIdList]:
    """Submits multiple new operation to be performed asynchronously

    Args:
        family (str):
        body (RunOperationBatch):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RequestIdList]
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
    body: RunOperationBatch,
    family: str,
) -> Optional[RequestIdList]:
    """Submits multiple new operation to be performed asynchronously

    Args:
        family (str):
        body (RunOperationBatch):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RequestIdList
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            family=family,
        )
    ).parsed