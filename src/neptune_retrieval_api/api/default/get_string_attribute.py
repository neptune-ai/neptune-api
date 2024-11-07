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
from ...models.string_attribute_dto import StringAttributeDTO
from ...types import (
    UNSET,
    Response,
    Unset,
)


def _get_kwargs(
    *,
    attribute: str,
    experiment_id: Union[Unset, str] = UNSET,
    holder_identifier: Union[Unset, str] = UNSET,
    holder_type: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["attribute"] = attribute

    params["experimentId"] = experiment_id

    params["holderIdentifier"] = holder_identifier

    params["holderType"] = holder_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/leaderboard/v1/attributes/strings",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, StringAttributeDTO]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = StringAttributeDTO.from_dict(response.json())

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
) -> Response[Union[Any, StringAttributeDTO]]:
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
    holder_identifier: Union[Unset, str] = UNSET,
    holder_type: Union[Unset, str] = UNSET,
) -> Response[Union[Any, StringAttributeDTO]]:
    """Get string attribute

    Args:
        attribute (str):
        experiment_id (Union[Unset, str]):
        holder_identifier (Union[Unset, str]):
        holder_type (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StringAttributeDTO]]
    """

    kwargs = _get_kwargs(
        attribute=attribute,
        experiment_id=experiment_id,
        holder_identifier=holder_identifier,
        holder_type=holder_type,
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
    holder_identifier: Union[Unset, str] = UNSET,
    holder_type: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, StringAttributeDTO]]:
    """Get string attribute

    Args:
        attribute (str):
        experiment_id (Union[Unset, str]):
        holder_identifier (Union[Unset, str]):
        holder_type (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, StringAttributeDTO]
    """

    return sync_detailed(
        client=client,
        attribute=attribute,
        experiment_id=experiment_id,
        holder_identifier=holder_identifier,
        holder_type=holder_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    attribute: str,
    experiment_id: Union[Unset, str] = UNSET,
    holder_identifier: Union[Unset, str] = UNSET,
    holder_type: Union[Unset, str] = UNSET,
) -> Response[Union[Any, StringAttributeDTO]]:
    """Get string attribute

    Args:
        attribute (str):
        experiment_id (Union[Unset, str]):
        holder_identifier (Union[Unset, str]):
        holder_type (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StringAttributeDTO]]
    """

    kwargs = _get_kwargs(
        attribute=attribute,
        experiment_id=experiment_id,
        holder_identifier=holder_identifier,
        holder_type=holder_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    attribute: str,
    experiment_id: Union[Unset, str] = UNSET,
    holder_identifier: Union[Unset, str] = UNSET,
    holder_type: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, StringAttributeDTO]]:
    """Get string attribute

    Args:
        attribute (str):
        experiment_id (Union[Unset, str]):
        holder_identifier (Union[Unset, str]):
        holder_type (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, StringAttributeDTO]
    """

    return (
        await asyncio_detailed(
            client=client,
            attribute=attribute,
            experiment_id=experiment_id,
            holder_identifier=holder_identifier,
            holder_type=holder_type,
        )
    ).parsed
