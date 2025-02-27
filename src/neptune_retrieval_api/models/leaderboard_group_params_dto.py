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

from ..models.attribute_type_dto import AttributeTypeDTO
from ..models.leaderboard_group_params_dto_group_by_field_aggregation_mode_item import (
    LeaderboardGroupParamsDTOGroupByFieldAggregationModeItem,
)
from ..types import (
    UNSET,
    Unset,
)

T = TypeVar("T", bound="LeaderboardGroupParamsDTO")


@_attrs_define
class LeaderboardGroupParamsDTO:
    """
    Attributes:
        group_by (Union[Unset, List[str]]):
        group_by_field_type (Union[Unset, List[AttributeTypeDTO]]):
        group_by_field_aggregation_mode (Union[Unset, List[LeaderboardGroupParamsDTOGroupByFieldAggregationModeItem]]):
        opened_groups (Union[Unset, List[str]]):
    """

    group_by: Union[Unset, List[str]] = UNSET
    group_by_field_type: Union[Unset, List[AttributeTypeDTO]] = UNSET
    group_by_field_aggregation_mode: Union[Unset, List[LeaderboardGroupParamsDTOGroupByFieldAggregationModeItem]] = (
        UNSET
    )
    opened_groups: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        group_by: Union[Unset, List[str]] = UNSET
        if not isinstance(self.group_by, Unset):
            group_by = self.group_by

        group_by_field_type: Union[Unset, List[str]] = UNSET
        if not isinstance(self.group_by_field_type, Unset):
            group_by_field_type = []
            for group_by_field_type_item_data in self.group_by_field_type:
                group_by_field_type_item = group_by_field_type_item_data.value
                group_by_field_type.append(group_by_field_type_item)

        group_by_field_aggregation_mode: Union[Unset, List[str]] = UNSET
        if not isinstance(self.group_by_field_aggregation_mode, Unset):
            group_by_field_aggregation_mode = []
            for group_by_field_aggregation_mode_item_data in self.group_by_field_aggregation_mode:
                group_by_field_aggregation_mode_item = group_by_field_aggregation_mode_item_data.value
                group_by_field_aggregation_mode.append(group_by_field_aggregation_mode_item)

        opened_groups: Union[Unset, List[str]] = UNSET
        if not isinstance(self.opened_groups, Unset):
            opened_groups = self.opened_groups

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_by is not UNSET:
            field_dict["groupBy"] = group_by
        if group_by_field_type is not UNSET:
            field_dict["groupByFieldType"] = group_by_field_type
        if group_by_field_aggregation_mode is not UNSET:
            field_dict["groupByFieldAggregationMode"] = group_by_field_aggregation_mode
        if opened_groups is not UNSET:
            field_dict["openedGroups"] = opened_groups

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        group_by = cast(List[str], d.pop("groupBy", UNSET))

        group_by_field_type: Union[Unset, List[AttributeTypeDTO]] = UNSET
        _group_by_field_type = d.pop("groupByFieldType", UNSET)
        if not isinstance(_group_by_field_type, Unset):
            group_by_field_type = []
            for group_by_field_type_item_data in _group_by_field_type:
                group_by_field_type_item = AttributeTypeDTO(group_by_field_type_item_data)

                group_by_field_type.append(group_by_field_type_item)

        group_by_field_aggregation_mode: Union[
            Unset, List[LeaderboardGroupParamsDTOGroupByFieldAggregationModeItem]
        ] = UNSET
        _group_by_field_aggregation_mode = d.pop("groupByFieldAggregationMode", UNSET)
        if not isinstance(_group_by_field_aggregation_mode, Unset):
            group_by_field_aggregation_mode = []
            for group_by_field_aggregation_mode_item_data in _group_by_field_aggregation_mode:
                group_by_field_aggregation_mode_item = LeaderboardGroupParamsDTOGroupByFieldAggregationModeItem(
                    group_by_field_aggregation_mode_item_data
                )

                group_by_field_aggregation_mode.append(group_by_field_aggregation_mode_item)

        opened_groups = cast(List[str], d.pop("openedGroups", UNSET))

        leaderboard_group_params_dto = cls(
            group_by=group_by,
            group_by_field_type=group_by_field_type,
            group_by_field_aggregation_mode=group_by_field_aggregation_mode,
            opened_groups=opened_groups,
        )

        leaderboard_group_params_dto.additional_properties = d
        return leaderboard_group_params_dto

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
