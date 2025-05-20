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
from ..models.leaderboard_sort_params_dto_sort_direction_item import LeaderboardSortParamsDTOSortDirectionItem
from ..models.leaderboard_sort_params_dto_sort_field_aggregation_mode_item import (
    LeaderboardSortParamsDTOSortFieldAggregationModeItem,
)
from ..types import (
    UNSET,
    Unset,
)

T = TypeVar("T", bound="LeaderboardSortParamsDTO")


@_attrs_define
class LeaderboardSortParamsDTO:
    """
    Attributes:
        sort_by (Union[Unset, List[str]]):
        sort_field_type (Union[Unset, List[AttributeTypeDTO]]):
        sort_field_aggregation_mode (Union[Unset, List[LeaderboardSortParamsDTOSortFieldAggregationModeItem]]):
        sort_direction (Union[Unset, List[LeaderboardSortParamsDTOSortDirectionItem]]):
    """

    sort_by: Union[Unset, List[str]] = UNSET
    sort_field_type: Union[Unset, List[AttributeTypeDTO]] = UNSET
    sort_field_aggregation_mode: Union[Unset, List[LeaderboardSortParamsDTOSortFieldAggregationModeItem]] = UNSET
    sort_direction: Union[Unset, List[LeaderboardSortParamsDTOSortDirectionItem]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sort_by: Union[Unset, List[str]] = UNSET
        if not isinstance(self.sort_by, Unset):
            sort_by = self.sort_by

        sort_field_type: Union[Unset, List[str]] = UNSET
        if not isinstance(self.sort_field_type, Unset):
            sort_field_type = []
            for sort_field_type_item_data in self.sort_field_type:
                sort_field_type_item = sort_field_type_item_data.value
                sort_field_type.append(sort_field_type_item)

        sort_field_aggregation_mode: Union[Unset, List[str]] = UNSET
        if not isinstance(self.sort_field_aggregation_mode, Unset):
            sort_field_aggregation_mode = []
            for sort_field_aggregation_mode_item_data in self.sort_field_aggregation_mode:
                sort_field_aggregation_mode_item = sort_field_aggregation_mode_item_data.value
                sort_field_aggregation_mode.append(sort_field_aggregation_mode_item)

        sort_direction: Union[Unset, List[str]] = UNSET
        if not isinstance(self.sort_direction, Unset):
            sort_direction = []
            for sort_direction_item_data in self.sort_direction:
                sort_direction_item = sort_direction_item_data.value
                sort_direction.append(sort_direction_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sort_by is not UNSET:
            field_dict["sortBy"] = sort_by
        if sort_field_type is not UNSET:
            field_dict["sortFieldType"] = sort_field_type
        if sort_field_aggregation_mode is not UNSET:
            field_dict["sortFieldAggregationMode"] = sort_field_aggregation_mode
        if sort_direction is not UNSET:
            field_dict["sortDirection"] = sort_direction

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sort_by = cast(List[str], d.pop("sortBy", UNSET))

        sort_field_type: Union[Unset, List[AttributeTypeDTO]] = UNSET
        _sort_field_type = d.pop("sortFieldType", UNSET)
        if not isinstance(_sort_field_type, Unset):
            sort_field_type = []
            for sort_field_type_item_data in _sort_field_type:
                sort_field_type_item = AttributeTypeDTO(sort_field_type_item_data)

                sort_field_type.append(sort_field_type_item)

        sort_field_aggregation_mode: Union[Unset, List[LeaderboardSortParamsDTOSortFieldAggregationModeItem]] = UNSET
        _sort_field_aggregation_mode = d.pop("sortFieldAggregationMode", UNSET)
        if not isinstance(_sort_field_aggregation_mode, Unset):
            sort_field_aggregation_mode = []
            for sort_field_aggregation_mode_item_data in _sort_field_aggregation_mode:
                sort_field_aggregation_mode_item = LeaderboardSortParamsDTOSortFieldAggregationModeItem(
                    sort_field_aggregation_mode_item_data
                )

                sort_field_aggregation_mode.append(sort_field_aggregation_mode_item)

        sort_direction: Union[Unset, List[LeaderboardSortParamsDTOSortDirectionItem]] = UNSET
        _sort_direction = d.pop("sortDirection", UNSET)
        if not isinstance(_sort_direction, Unset):
            sort_direction = []
            for sort_direction_item_data in _sort_direction:
                sort_direction_item = LeaderboardSortParamsDTOSortDirectionItem(sort_direction_item_data)

                sort_direction.append(sort_direction_item)

        leaderboard_sort_params_dto = cls(
            sort_by=sort_by,
            sort_field_type=sort_field_type,
            sort_field_aggregation_mode=sort_field_aggregation_mode,
            sort_direction=sort_direction,
        )

        leaderboard_sort_params_dto.additional_properties = d
        return leaderboard_sort_params_dto

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
