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
from ...models.ingest_response import IngestResponse
from ...types import (
    UNSET,
    Response,
)


def _get_kwargs(
    *,
    project_identifier: str,
    request_id: str,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["projectIdentifier"] = project_identifier

    params["requestId"] = request_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/client/v1/ingest/check",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[IngestResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = IngestResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[IngestResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    project_identifier: str,
    request_id: str,
) -> Response[IngestResponse]:
    """Checks operation processing status

    Args:
        project_identifier (str):
        request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IngestResponse]
    """

    kwargs = _get_kwargs(
        project_identifier=project_identifier,
        request_id=request_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    project_identifier: str,
    request_id: str,
) -> Optional[IngestResponse]:
    """Checks operation processing status

    Args:
        project_identifier (str):
        request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IngestResponse
    """

    return sync_detailed(
        client=client,
        project_identifier=project_identifier,
        request_id=request_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    project_identifier: str,
    request_id: str,
) -> Response[IngestResponse]:
    """Checks operation processing status

    Args:
        project_identifier (str):
        request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IngestResponse]
    """

    kwargs = _get_kwargs(
        project_identifier=project_identifier,
        request_id=request_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    project_identifier: str,
    request_id: str,
) -> Optional[IngestResponse]:
    """Checks operation processing status

    Args:
        project_identifier (str):
        request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IngestResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            project_identifier=project_identifier,
            request_id=request_id,
        )
    ).parsed
