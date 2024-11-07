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
from ...models.attributes_search_result_dto import AttributesSearchResultDTO
from ...models.search_leaderboard_params_dto import SearchLeaderboardParamsDTO
from ...types import (
    UNSET,
    Response,
    Unset,
)


def _get_kwargs(
    *,
    body: SearchLeaderboardParamsDTO,
    attribute_type: Union[Unset, List[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    project_identifier: str,
    search: Union[Unset, str] = UNSET,
    type: Union[Unset, List[str]] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    json_attribute_type: Union[Unset, List[str]] = UNSET
    if not isinstance(attribute_type, Unset):
        json_attribute_type = attribute_type

    params["attributeType"] = json_attribute_type

    params["limit"] = limit

    params["projectIdentifier"] = project_identifier

    params["search"] = search

    json_type: Union[Unset, List[str]] = UNSET
    if not isinstance(type, Unset):
        json_type = type

    params["type"] = json_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/api/leaderboard/v1/leaderboard/attributes/search",
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, AttributesSearchResultDTO]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AttributesSearchResultDTO.from_dict(response.json())

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
) -> Response[Union[Any, AttributesSearchResultDTO]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SearchLeaderboardParamsDTO,
    attribute_type: Union[Unset, List[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    project_identifier: str,
    search: Union[Unset, str] = UNSET,
    type: Union[Unset, List[str]] = UNSET,
) -> Response[Union[Any, AttributesSearchResultDTO]]:
    """List definitions of all attributes in project

    Args:
        attribute_type (Union[Unset, List[str]]):
        limit (Union[Unset, int]):
        project_identifier (str):
        search (Union[Unset, str]):
        type (Union[Unset, List[str]]):
        body (SearchLeaderboardParamsDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, AttributesSearchResultDTO]]
    """

    kwargs = _get_kwargs(
        body=body,
        attribute_type=attribute_type,
        limit=limit,
        project_identifier=project_identifier,
        search=search,
        type=type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SearchLeaderboardParamsDTO,
    attribute_type: Union[Unset, List[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    project_identifier: str,
    search: Union[Unset, str] = UNSET,
    type: Union[Unset, List[str]] = UNSET,
) -> Optional[Union[Any, AttributesSearchResultDTO]]:
    """List definitions of all attributes in project

    Args:
        attribute_type (Union[Unset, List[str]]):
        limit (Union[Unset, int]):
        project_identifier (str):
        search (Union[Unset, str]):
        type (Union[Unset, List[str]]):
        body (SearchLeaderboardParamsDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, AttributesSearchResultDTO]
    """

    return sync_detailed(
        client=client,
        body=body,
        attribute_type=attribute_type,
        limit=limit,
        project_identifier=project_identifier,
        search=search,
        type=type,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SearchLeaderboardParamsDTO,
    attribute_type: Union[Unset, List[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    project_identifier: str,
    search: Union[Unset, str] = UNSET,
    type: Union[Unset, List[str]] = UNSET,
) -> Response[Union[Any, AttributesSearchResultDTO]]:
    """List definitions of all attributes in project

    Args:
        attribute_type (Union[Unset, List[str]]):
        limit (Union[Unset, int]):
        project_identifier (str):
        search (Union[Unset, str]):
        type (Union[Unset, List[str]]):
        body (SearchLeaderboardParamsDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, AttributesSearchResultDTO]]
    """

    kwargs = _get_kwargs(
        body=body,
        attribute_type=attribute_type,
        limit=limit,
        project_identifier=project_identifier,
        search=search,
        type=type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SearchLeaderboardParamsDTO,
    attribute_type: Union[Unset, List[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    project_identifier: str,
    search: Union[Unset, str] = UNSET,
    type: Union[Unset, List[str]] = UNSET,
) -> Optional[Union[Any, AttributesSearchResultDTO]]:
    """List definitions of all attributes in project

    Args:
        attribute_type (Union[Unset, List[str]]):
        limit (Union[Unset, int]):
        project_identifier (str):
        search (Union[Unset, str]):
        type (Union[Unset, List[str]]):
        body (SearchLeaderboardParamsDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, AttributesSearchResultDTO]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            attribute_type=attribute_type,
            limit=limit,
            project_identifier=project_identifier,
            search=search,
            type=type,
        )
    ).parsed
