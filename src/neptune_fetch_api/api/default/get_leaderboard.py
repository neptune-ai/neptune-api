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
from ...models.attribute_type_dto import AttributeTypeDTO
from ...models.experiment_state_dto import ExperimentStateDTO
from ...models.get_leaderboard_group_by_field_aggregation_mode import GetLeaderboardGroupByFieldAggregationMode
from ...models.get_leaderboard_sort_direction import GetLeaderboardSortDirection
from ...models.get_leaderboard_sort_field_aggregation_mode import GetLeaderboardSortFieldAggregationMode
from ...models.get_leaderboard_tags_mode import GetLeaderboardTagsMode
from ...models.get_leaderboard_trashed import GetLeaderboardTrashed
from ...models.leaderboard_dto import LeaderboardDTO
from ...types import (
    UNSET,
    Response,
    Unset,
)


def _get_kwargs(
    *,
    entry_type: Union[Unset, List[str]] = UNSET,
    filter_id: Union[Unset, str] = UNSET,
    flatting_mode: Union[Unset, str] = UNSET,
    group_by: Union[Unset, List[str]] = UNSET,
    group_by_field_aggregation_mode: Union[Unset, GetLeaderboardGroupByFieldAggregationMode] = UNSET,
    group_id: Union[Unset, str] = UNSET,
    group_short_id: Union[Unset, List[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    min_running_time_seconds: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    opened_groups: Union[Unset, List[str]] = UNSET,
    organization_identifier: Union[Unset, str] = UNSET,
    owner: Union[Unset, List[str]] = UNSET,
    project_identifier: Union[Unset, str] = UNSET,
    selected_channels: Union[Unset, List[str]] = UNSET,
    short_id: Union[Unset, List[str]] = UNSET,
    sort_by: Union[Unset, List[str]] = UNSET,
    sort_direction: Union[Unset, GetLeaderboardSortDirection] = UNSET,
    sort_field_aggregation_mode: Union[Unset, GetLeaderboardSortFieldAggregationMode] = UNSET,
    tags: Union[Unset, List[str]] = UNSET,
    tags_mode: Union[Unset, GetLeaderboardTagsMode] = UNSET,
    trashed: Union[Unset, GetLeaderboardTrashed] = UNSET,
    state: Union[Unset, List[ExperimentStateDTO]] = UNSET,
    group_by_field_type: Union[Unset, List[AttributeTypeDTO]] = UNSET,
    sort_field_type: Union[Unset, List[AttributeTypeDTO]] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_entry_type: Union[Unset, List[str]] = UNSET
    if not isinstance(entry_type, Unset):
        json_entry_type = entry_type

    params["entryType"] = json_entry_type

    params["filterId"] = filter_id

    params["flattingMode"] = flatting_mode

    json_group_by: Union[Unset, List[str]] = UNSET
    if not isinstance(group_by, Unset):
        json_group_by = group_by

    params["groupBy"] = json_group_by

    json_group_by_field_aggregation_mode: Union[Unset, str] = UNSET
    if not isinstance(group_by_field_aggregation_mode, Unset):
        json_group_by_field_aggregation_mode = group_by_field_aggregation_mode.value

    params["groupByFieldAggregationMode"] = json_group_by_field_aggregation_mode

    params["groupId"] = group_id

    json_group_short_id: Union[Unset, List[str]] = UNSET
    if not isinstance(group_short_id, Unset):
        json_group_short_id = group_short_id

    params["groupShortId"] = json_group_short_id

    params["limit"] = limit

    params["minRunningTimeSeconds"] = min_running_time_seconds

    params["offset"] = offset

    json_opened_groups: Union[Unset, List[str]] = UNSET
    if not isinstance(opened_groups, Unset):
        json_opened_groups = opened_groups

    params["openedGroups"] = json_opened_groups

    params["organizationIdentifier"] = organization_identifier

    json_owner: Union[Unset, List[str]] = UNSET
    if not isinstance(owner, Unset):
        json_owner = owner

    params["owner"] = json_owner

    params["projectIdentifier"] = project_identifier

    json_selected_channels: Union[Unset, List[str]] = UNSET
    if not isinstance(selected_channels, Unset):
        json_selected_channels = selected_channels

    params["selectedChannels"] = json_selected_channels

    json_short_id: Union[Unset, List[str]] = UNSET
    if not isinstance(short_id, Unset):
        json_short_id = short_id

    params["shortId"] = json_short_id

    json_sort_by: Union[Unset, List[str]] = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by

    params["sortBy"] = json_sort_by

    json_sort_direction: Union[Unset, str] = UNSET
    if not isinstance(sort_direction, Unset):
        json_sort_direction = sort_direction.value

    params["sortDirection"] = json_sort_direction

    json_sort_field_aggregation_mode: Union[Unset, str] = UNSET
    if not isinstance(sort_field_aggregation_mode, Unset):
        json_sort_field_aggregation_mode = sort_field_aggregation_mode.value

    params["sortFieldAggregationMode"] = json_sort_field_aggregation_mode

    json_tags: Union[Unset, List[str]] = UNSET
    if not isinstance(tags, Unset):
        json_tags = tags

    params["tags"] = json_tags

    json_tags_mode: Union[Unset, str] = UNSET
    if not isinstance(tags_mode, Unset):
        json_tags_mode = tags_mode.value

    params["tagsMode"] = json_tags_mode

    json_trashed: Union[Unset, str] = UNSET
    if not isinstance(trashed, Unset):
        json_trashed = trashed.value

    params["trashed"] = json_trashed

    json_state: Union[Unset, List[str]] = UNSET
    if not isinstance(state, Unset):
        json_state = []
        for state_item_data in state:
            state_item = state_item_data.value
            json_state.append(state_item)

    params["state"] = json_state

    json_group_by_field_type: Union[Unset, List[str]] = UNSET
    if not isinstance(group_by_field_type, Unset):
        json_group_by_field_type = []
        for group_by_field_type_item_data in group_by_field_type:
            group_by_field_type_item = group_by_field_type_item_data.value
            json_group_by_field_type.append(group_by_field_type_item)

    params["groupByFieldType"] = json_group_by_field_type

    json_sort_field_type: Union[Unset, List[str]] = UNSET
    if not isinstance(sort_field_type, Unset):
        json_sort_field_type = []
        for sort_field_type_item_data in sort_field_type:
            sort_field_type_item = sort_field_type_item_data.value
            json_sort_field_type.append(sort_field_type_item)

    params["sortFieldType"] = json_sort_field_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/leaderboard/v1/leaderboard",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, LeaderboardDTO]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = LeaderboardDTO.from_dict(response.json())

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
) -> Response[Union[Any, LeaderboardDTO]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    entry_type: Union[Unset, List[str]] = UNSET,
    filter_id: Union[Unset, str] = UNSET,
    flatting_mode: Union[Unset, str] = UNSET,
    group_by: Union[Unset, List[str]] = UNSET,
    group_by_field_aggregation_mode: Union[Unset, GetLeaderboardGroupByFieldAggregationMode] = UNSET,
    group_id: Union[Unset, str] = UNSET,
    group_short_id: Union[Unset, List[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    min_running_time_seconds: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    opened_groups: Union[Unset, List[str]] = UNSET,
    organization_identifier: Union[Unset, str] = UNSET,
    owner: Union[Unset, List[str]] = UNSET,
    project_identifier: Union[Unset, str] = UNSET,
    selected_channels: Union[Unset, List[str]] = UNSET,
    short_id: Union[Unset, List[str]] = UNSET,
    sort_by: Union[Unset, List[str]] = UNSET,
    sort_direction: Union[Unset, GetLeaderboardSortDirection] = UNSET,
    sort_field_aggregation_mode: Union[Unset, GetLeaderboardSortFieldAggregationMode] = UNSET,
    tags: Union[Unset, List[str]] = UNSET,
    tags_mode: Union[Unset, GetLeaderboardTagsMode] = UNSET,
    trashed: Union[Unset, GetLeaderboardTrashed] = UNSET,
    state: Union[Unset, List[ExperimentStateDTO]] = UNSET,
    group_by_field_type: Union[Unset, List[AttributeTypeDTO]] = UNSET,
    sort_field_type: Union[Unset, List[AttributeTypeDTO]] = UNSET,
) -> Response[Union[Any, LeaderboardDTO]]:
    """Get leaderboard

    Args:
        entry_type (Union[Unset, List[str]]):
        filter_id (Union[Unset, str]):
        flatting_mode (Union[Unset, str]):
        group_by (Union[Unset, List[str]]):
        group_by_field_aggregation_mode (Union[Unset, GetLeaderboardGroupByFieldAggregationMode]):
        group_id (Union[Unset, str]):
        group_short_id (Union[Unset, List[str]]):
        limit (Union[Unset, int]):
        min_running_time_seconds (Union[Unset, int]):
        offset (Union[Unset, int]):
        opened_groups (Union[Unset, List[str]]):
        organization_identifier (Union[Unset, str]):
        owner (Union[Unset, List[str]]):
        project_identifier (Union[Unset, str]):
        selected_channels (Union[Unset, List[str]]):
        short_id (Union[Unset, List[str]]):
        sort_by (Union[Unset, List[str]]):
        sort_direction (Union[Unset, GetLeaderboardSortDirection]):
        sort_field_aggregation_mode (Union[Unset, GetLeaderboardSortFieldAggregationMode]):
        tags (Union[Unset, List[str]]):
        tags_mode (Union[Unset, GetLeaderboardTagsMode]):
        trashed (Union[Unset, GetLeaderboardTrashed]):
        state (Union[Unset, List[ExperimentStateDTO]]):
        group_by_field_type (Union[Unset, List[AttributeTypeDTO]]):
        sort_field_type (Union[Unset, List[AttributeTypeDTO]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, LeaderboardDTO]]
    """

    kwargs = _get_kwargs(
        entry_type=entry_type,
        filter_id=filter_id,
        flatting_mode=flatting_mode,
        group_by=group_by,
        group_by_field_aggregation_mode=group_by_field_aggregation_mode,
        group_id=group_id,
        group_short_id=group_short_id,
        limit=limit,
        min_running_time_seconds=min_running_time_seconds,
        offset=offset,
        opened_groups=opened_groups,
        organization_identifier=organization_identifier,
        owner=owner,
        project_identifier=project_identifier,
        selected_channels=selected_channels,
        short_id=short_id,
        sort_by=sort_by,
        sort_direction=sort_direction,
        sort_field_aggregation_mode=sort_field_aggregation_mode,
        tags=tags,
        tags_mode=tags_mode,
        trashed=trashed,
        state=state,
        group_by_field_type=group_by_field_type,
        sort_field_type=sort_field_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    entry_type: Union[Unset, List[str]] = UNSET,
    filter_id: Union[Unset, str] = UNSET,
    flatting_mode: Union[Unset, str] = UNSET,
    group_by: Union[Unset, List[str]] = UNSET,
    group_by_field_aggregation_mode: Union[Unset, GetLeaderboardGroupByFieldAggregationMode] = UNSET,
    group_id: Union[Unset, str] = UNSET,
    group_short_id: Union[Unset, List[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    min_running_time_seconds: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    opened_groups: Union[Unset, List[str]] = UNSET,
    organization_identifier: Union[Unset, str] = UNSET,
    owner: Union[Unset, List[str]] = UNSET,
    project_identifier: Union[Unset, str] = UNSET,
    selected_channels: Union[Unset, List[str]] = UNSET,
    short_id: Union[Unset, List[str]] = UNSET,
    sort_by: Union[Unset, List[str]] = UNSET,
    sort_direction: Union[Unset, GetLeaderboardSortDirection] = UNSET,
    sort_field_aggregation_mode: Union[Unset, GetLeaderboardSortFieldAggregationMode] = UNSET,
    tags: Union[Unset, List[str]] = UNSET,
    tags_mode: Union[Unset, GetLeaderboardTagsMode] = UNSET,
    trashed: Union[Unset, GetLeaderboardTrashed] = UNSET,
    state: Union[Unset, List[ExperimentStateDTO]] = UNSET,
    group_by_field_type: Union[Unset, List[AttributeTypeDTO]] = UNSET,
    sort_field_type: Union[Unset, List[AttributeTypeDTO]] = UNSET,
) -> Optional[Union[Any, LeaderboardDTO]]:
    """Get leaderboard

    Args:
        entry_type (Union[Unset, List[str]]):
        filter_id (Union[Unset, str]):
        flatting_mode (Union[Unset, str]):
        group_by (Union[Unset, List[str]]):
        group_by_field_aggregation_mode (Union[Unset, GetLeaderboardGroupByFieldAggregationMode]):
        group_id (Union[Unset, str]):
        group_short_id (Union[Unset, List[str]]):
        limit (Union[Unset, int]):
        min_running_time_seconds (Union[Unset, int]):
        offset (Union[Unset, int]):
        opened_groups (Union[Unset, List[str]]):
        organization_identifier (Union[Unset, str]):
        owner (Union[Unset, List[str]]):
        project_identifier (Union[Unset, str]):
        selected_channels (Union[Unset, List[str]]):
        short_id (Union[Unset, List[str]]):
        sort_by (Union[Unset, List[str]]):
        sort_direction (Union[Unset, GetLeaderboardSortDirection]):
        sort_field_aggregation_mode (Union[Unset, GetLeaderboardSortFieldAggregationMode]):
        tags (Union[Unset, List[str]]):
        tags_mode (Union[Unset, GetLeaderboardTagsMode]):
        trashed (Union[Unset, GetLeaderboardTrashed]):
        state (Union[Unset, List[ExperimentStateDTO]]):
        group_by_field_type (Union[Unset, List[AttributeTypeDTO]]):
        sort_field_type (Union[Unset, List[AttributeTypeDTO]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, LeaderboardDTO]
    """

    return sync_detailed(
        client=client,
        entry_type=entry_type,
        filter_id=filter_id,
        flatting_mode=flatting_mode,
        group_by=group_by,
        group_by_field_aggregation_mode=group_by_field_aggregation_mode,
        group_id=group_id,
        group_short_id=group_short_id,
        limit=limit,
        min_running_time_seconds=min_running_time_seconds,
        offset=offset,
        opened_groups=opened_groups,
        organization_identifier=organization_identifier,
        owner=owner,
        project_identifier=project_identifier,
        selected_channels=selected_channels,
        short_id=short_id,
        sort_by=sort_by,
        sort_direction=sort_direction,
        sort_field_aggregation_mode=sort_field_aggregation_mode,
        tags=tags,
        tags_mode=tags_mode,
        trashed=trashed,
        state=state,
        group_by_field_type=group_by_field_type,
        sort_field_type=sort_field_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    entry_type: Union[Unset, List[str]] = UNSET,
    filter_id: Union[Unset, str] = UNSET,
    flatting_mode: Union[Unset, str] = UNSET,
    group_by: Union[Unset, List[str]] = UNSET,
    group_by_field_aggregation_mode: Union[Unset, GetLeaderboardGroupByFieldAggregationMode] = UNSET,
    group_id: Union[Unset, str] = UNSET,
    group_short_id: Union[Unset, List[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    min_running_time_seconds: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    opened_groups: Union[Unset, List[str]] = UNSET,
    organization_identifier: Union[Unset, str] = UNSET,
    owner: Union[Unset, List[str]] = UNSET,
    project_identifier: Union[Unset, str] = UNSET,
    selected_channels: Union[Unset, List[str]] = UNSET,
    short_id: Union[Unset, List[str]] = UNSET,
    sort_by: Union[Unset, List[str]] = UNSET,
    sort_direction: Union[Unset, GetLeaderboardSortDirection] = UNSET,
    sort_field_aggregation_mode: Union[Unset, GetLeaderboardSortFieldAggregationMode] = UNSET,
    tags: Union[Unset, List[str]] = UNSET,
    tags_mode: Union[Unset, GetLeaderboardTagsMode] = UNSET,
    trashed: Union[Unset, GetLeaderboardTrashed] = UNSET,
    state: Union[Unset, List[ExperimentStateDTO]] = UNSET,
    group_by_field_type: Union[Unset, List[AttributeTypeDTO]] = UNSET,
    sort_field_type: Union[Unset, List[AttributeTypeDTO]] = UNSET,
) -> Response[Union[Any, LeaderboardDTO]]:
    """Get leaderboard

    Args:
        entry_type (Union[Unset, List[str]]):
        filter_id (Union[Unset, str]):
        flatting_mode (Union[Unset, str]):
        group_by (Union[Unset, List[str]]):
        group_by_field_aggregation_mode (Union[Unset, GetLeaderboardGroupByFieldAggregationMode]):
        group_id (Union[Unset, str]):
        group_short_id (Union[Unset, List[str]]):
        limit (Union[Unset, int]):
        min_running_time_seconds (Union[Unset, int]):
        offset (Union[Unset, int]):
        opened_groups (Union[Unset, List[str]]):
        organization_identifier (Union[Unset, str]):
        owner (Union[Unset, List[str]]):
        project_identifier (Union[Unset, str]):
        selected_channels (Union[Unset, List[str]]):
        short_id (Union[Unset, List[str]]):
        sort_by (Union[Unset, List[str]]):
        sort_direction (Union[Unset, GetLeaderboardSortDirection]):
        sort_field_aggregation_mode (Union[Unset, GetLeaderboardSortFieldAggregationMode]):
        tags (Union[Unset, List[str]]):
        tags_mode (Union[Unset, GetLeaderboardTagsMode]):
        trashed (Union[Unset, GetLeaderboardTrashed]):
        state (Union[Unset, List[ExperimentStateDTO]]):
        group_by_field_type (Union[Unset, List[AttributeTypeDTO]]):
        sort_field_type (Union[Unset, List[AttributeTypeDTO]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, LeaderboardDTO]]
    """

    kwargs = _get_kwargs(
        entry_type=entry_type,
        filter_id=filter_id,
        flatting_mode=flatting_mode,
        group_by=group_by,
        group_by_field_aggregation_mode=group_by_field_aggregation_mode,
        group_id=group_id,
        group_short_id=group_short_id,
        limit=limit,
        min_running_time_seconds=min_running_time_seconds,
        offset=offset,
        opened_groups=opened_groups,
        organization_identifier=organization_identifier,
        owner=owner,
        project_identifier=project_identifier,
        selected_channels=selected_channels,
        short_id=short_id,
        sort_by=sort_by,
        sort_direction=sort_direction,
        sort_field_aggregation_mode=sort_field_aggregation_mode,
        tags=tags,
        tags_mode=tags_mode,
        trashed=trashed,
        state=state,
        group_by_field_type=group_by_field_type,
        sort_field_type=sort_field_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    entry_type: Union[Unset, List[str]] = UNSET,
    filter_id: Union[Unset, str] = UNSET,
    flatting_mode: Union[Unset, str] = UNSET,
    group_by: Union[Unset, List[str]] = UNSET,
    group_by_field_aggregation_mode: Union[Unset, GetLeaderboardGroupByFieldAggregationMode] = UNSET,
    group_id: Union[Unset, str] = UNSET,
    group_short_id: Union[Unset, List[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    min_running_time_seconds: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    opened_groups: Union[Unset, List[str]] = UNSET,
    organization_identifier: Union[Unset, str] = UNSET,
    owner: Union[Unset, List[str]] = UNSET,
    project_identifier: Union[Unset, str] = UNSET,
    selected_channels: Union[Unset, List[str]] = UNSET,
    short_id: Union[Unset, List[str]] = UNSET,
    sort_by: Union[Unset, List[str]] = UNSET,
    sort_direction: Union[Unset, GetLeaderboardSortDirection] = UNSET,
    sort_field_aggregation_mode: Union[Unset, GetLeaderboardSortFieldAggregationMode] = UNSET,
    tags: Union[Unset, List[str]] = UNSET,
    tags_mode: Union[Unset, GetLeaderboardTagsMode] = UNSET,
    trashed: Union[Unset, GetLeaderboardTrashed] = UNSET,
    state: Union[Unset, List[ExperimentStateDTO]] = UNSET,
    group_by_field_type: Union[Unset, List[AttributeTypeDTO]] = UNSET,
    sort_field_type: Union[Unset, List[AttributeTypeDTO]] = UNSET,
) -> Optional[Union[Any, LeaderboardDTO]]:
    """Get leaderboard

    Args:
        entry_type (Union[Unset, List[str]]):
        filter_id (Union[Unset, str]):
        flatting_mode (Union[Unset, str]):
        group_by (Union[Unset, List[str]]):
        group_by_field_aggregation_mode (Union[Unset, GetLeaderboardGroupByFieldAggregationMode]):
        group_id (Union[Unset, str]):
        group_short_id (Union[Unset, List[str]]):
        limit (Union[Unset, int]):
        min_running_time_seconds (Union[Unset, int]):
        offset (Union[Unset, int]):
        opened_groups (Union[Unset, List[str]]):
        organization_identifier (Union[Unset, str]):
        owner (Union[Unset, List[str]]):
        project_identifier (Union[Unset, str]):
        selected_channels (Union[Unset, List[str]]):
        short_id (Union[Unset, List[str]]):
        sort_by (Union[Unset, List[str]]):
        sort_direction (Union[Unset, GetLeaderboardSortDirection]):
        sort_field_aggregation_mode (Union[Unset, GetLeaderboardSortFieldAggregationMode]):
        tags (Union[Unset, List[str]]):
        tags_mode (Union[Unset, GetLeaderboardTagsMode]):
        trashed (Union[Unset, GetLeaderboardTrashed]):
        state (Union[Unset, List[ExperimentStateDTO]]):
        group_by_field_type (Union[Unset, List[AttributeTypeDTO]]):
        sort_field_type (Union[Unset, List[AttributeTypeDTO]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, LeaderboardDTO]
    """

    return (
        await asyncio_detailed(
            client=client,
            entry_type=entry_type,
            filter_id=filter_id,
            flatting_mode=flatting_mode,
            group_by=group_by,
            group_by_field_aggregation_mode=group_by_field_aggregation_mode,
            group_id=group_id,
            group_short_id=group_short_id,
            limit=limit,
            min_running_time_seconds=min_running_time_seconds,
            offset=offset,
            opened_groups=opened_groups,
            organization_identifier=organization_identifier,
            owner=owner,
            project_identifier=project_identifier,
            selected_channels=selected_channels,
            short_id=short_id,
            sort_by=sort_by,
            sort_direction=sort_direction,
            sort_field_aggregation_mode=sort_field_aggregation_mode,
            tags=tags,
            tags_mode=tags_mode,
            trashed=trashed,
            state=state,
            group_by_field_type=group_by_field_type,
            sort_field_type=sort_field_type,
        )
    ).parsed
