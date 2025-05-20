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

import datetime
from typing import (
    Any,
    Dict,
    List,
    Type,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.experiment_state_dto import ExperimentStateDTO
from ..models.leaderboard_view_quick_filter_dto_relative_time import LeaderboardViewQuickFilterDTORelativeTime
from ..types import (
    UNSET,
    Unset,
)

T = TypeVar("T", bound="LeaderboardViewQuickFilterDTO")


@_attrs_define
class LeaderboardViewQuickFilterDTO:
    """
    Attributes:
        creation_date_range_end (Union[Unset, datetime.datetime]):
        creation_date_range_start (Union[Unset, datetime.datetime]):
        owner (Union[Unset, List[str]]):
        relative_time (Union[Unset, LeaderboardViewQuickFilterDTORelativeTime]):
        search_term (Union[Unset, str]):
        status (Union[Unset, List[ExperimentStateDTO]]):
        tags (Union[Unset, List[str]]):
    """

    creation_date_range_end: Union[Unset, datetime.datetime] = UNSET
    creation_date_range_start: Union[Unset, datetime.datetime] = UNSET
    owner: Union[Unset, List[str]] = UNSET
    relative_time: Union[Unset, LeaderboardViewQuickFilterDTORelativeTime] = UNSET
    search_term: Union[Unset, str] = UNSET
    status: Union[Unset, List[ExperimentStateDTO]] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        creation_date_range_end: Union[Unset, str] = UNSET
        if not isinstance(self.creation_date_range_end, Unset):
            creation_date_range_end = self.creation_date_range_end.isoformat()

        creation_date_range_start: Union[Unset, str] = UNSET
        if not isinstance(self.creation_date_range_start, Unset):
            creation_date_range_start = self.creation_date_range_start.isoformat()

        owner: Union[Unset, List[str]] = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner

        relative_time: Union[Unset, str] = UNSET
        if not isinstance(self.relative_time, Unset):
            relative_time = self.relative_time.value

        search_term = self.search_term

        status: Union[Unset, List[str]] = UNSET
        if not isinstance(self.status, Unset):
            status = []
            for status_item_data in self.status:
                status_item = status_item_data.value
                status.append(status_item)

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if creation_date_range_end is not UNSET:
            field_dict["creationDateRangeEnd"] = creation_date_range_end
        if creation_date_range_start is not UNSET:
            field_dict["creationDateRangeStart"] = creation_date_range_start
        if owner is not UNSET:
            field_dict["owner"] = owner
        if relative_time is not UNSET:
            field_dict["relativeTime"] = relative_time
        if search_term is not UNSET:
            field_dict["searchTerm"] = search_term
        if status is not UNSET:
            field_dict["status"] = status
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _creation_date_range_end = d.pop("creationDateRangeEnd", UNSET)
        creation_date_range_end: Union[Unset, datetime.datetime]
        if isinstance(_creation_date_range_end, Unset):
            creation_date_range_end = UNSET
        else:
            creation_date_range_end = isoparse(_creation_date_range_end)

        _creation_date_range_start = d.pop("creationDateRangeStart", UNSET)
        creation_date_range_start: Union[Unset, datetime.datetime]
        if isinstance(_creation_date_range_start, Unset):
            creation_date_range_start = UNSET
        else:
            creation_date_range_start = isoparse(_creation_date_range_start)

        owner = cast(List[str], d.pop("owner", UNSET))

        _relative_time = d.pop("relativeTime", UNSET)
        relative_time: Union[Unset, LeaderboardViewQuickFilterDTORelativeTime]
        if isinstance(_relative_time, Unset):
            relative_time = UNSET
        else:
            relative_time = LeaderboardViewQuickFilterDTORelativeTime(_relative_time)

        search_term = d.pop("searchTerm", UNSET)

        status: Union[Unset, List[ExperimentStateDTO]] = UNSET
        _status = d.pop("status", UNSET)
        if not isinstance(_status, Unset):
            status = []
            for status_item_data in _status:
                status_item = ExperimentStateDTO(status_item_data)

                status.append(status_item)

        tags = cast(List[str], d.pop("tags", UNSET))

        leaderboard_view_quick_filter_dto = cls(
            creation_date_range_end=creation_date_range_end,
            creation_date_range_start=creation_date_range_start,
            owner=owner,
            relative_time=relative_time,
            search_term=search_term,
            status=status,
            tags=tags,
        )

        leaderboard_view_quick_filter_dto.additional_properties = d
        return leaderboard_view_quick_filter_dto

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
