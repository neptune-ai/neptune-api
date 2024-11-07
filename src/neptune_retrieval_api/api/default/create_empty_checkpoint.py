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
from ...models.checkpoint_dto import CheckpointDTO
from ...models.new_checkpoint_dto import NewCheckpointDTO
from ...types import Response


def _get_kwargs(
    notebook_id: str,
    *,
    body: NewCheckpointDTO,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/api/leaderboard/v1/notebooks/{notebook_id}/checkpoints2",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CheckpointDTO]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CheckpointDTO.from_dict(response.json())

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
) -> Response[Union[Any, CheckpointDTO]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    notebook_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: NewCheckpointDTO,
) -> Response[Union[Any, CheckpointDTO]]:
    """Create checkpoint

    Args:
        notebook_id (str):
        body (NewCheckpointDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CheckpointDTO]]
    """

    kwargs = _get_kwargs(
        notebook_id=notebook_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    notebook_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: NewCheckpointDTO,
) -> Optional[Union[Any, CheckpointDTO]]:
    """Create checkpoint

    Args:
        notebook_id (str):
        body (NewCheckpointDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CheckpointDTO]
    """

    return sync_detailed(
        notebook_id=notebook_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    notebook_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: NewCheckpointDTO,
) -> Response[Union[Any, CheckpointDTO]]:
    """Create checkpoint

    Args:
        notebook_id (str):
        body (NewCheckpointDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CheckpointDTO]]
    """

    kwargs = _get_kwargs(
        notebook_id=notebook_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    notebook_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: NewCheckpointDTO,
) -> Optional[Union[Any, CheckpointDTO]]:
    """Create checkpoint

    Args:
        notebook_id (str):
        body (NewCheckpointDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CheckpointDTO]
    """

    return (
        await asyncio_detailed(
            notebook_id=notebook_id,
            client=client,
            body=body,
        )
    ).parsed
