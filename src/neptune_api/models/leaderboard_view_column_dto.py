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
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.attribute_type_dto import AttributeTypeDTO
from ..models.leaderboard_view_column_dto_aggregation_mode import LeaderboardViewColumnDTOAggregationMode
from ..models.leaderboard_view_column_dto_display_mode import LeaderboardViewColumnDTODisplayMode
from ..types import (
    UNSET,
    Unset,
)

T = TypeVar("T", bound="LeaderboardViewColumnDTO")


@_attrs_define
class LeaderboardViewColumnDTO:
    """
    Attributes:
        column_type (AttributeTypeDTO):
        id (str):
        pinned (bool):
        width (int):
        color (Union[Unset, str]):
        display_name (Union[Unset, str]):
        aggregation_mode (Union[Unset, LeaderboardViewColumnDTOAggregationMode]):
        display_mode (Union[Unset, LeaderboardViewColumnDTODisplayMode]):
    """

    column_type: AttributeTypeDTO
    id: str
    pinned: bool
    width: int
    color: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    aggregation_mode: Union[Unset, LeaderboardViewColumnDTOAggregationMode] = UNSET
    display_mode: Union[Unset, LeaderboardViewColumnDTODisplayMode] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        column_type = self.column_type.value

        id = self.id

        pinned = self.pinned

        width = self.width

        color = self.color

        display_name = self.display_name

        aggregation_mode: Union[Unset, str] = UNSET
        if not isinstance(self.aggregation_mode, Unset):
            aggregation_mode = self.aggregation_mode.value

        display_mode: Union[Unset, str] = UNSET
        if not isinstance(self.display_mode, Unset):
            display_mode = self.display_mode.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "columnType": column_type,
                "id": id,
                "pinned": pinned,
                "width": width,
            }
        )
        if color is not UNSET:
            field_dict["color"] = color
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if aggregation_mode is not UNSET:
            field_dict["aggregationMode"] = aggregation_mode
        if display_mode is not UNSET:
            field_dict["displayMode"] = display_mode

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        column_type = AttributeTypeDTO(d.pop("columnType"))

        id = d.pop("id")

        pinned = d.pop("pinned")

        width = d.pop("width")

        color = d.pop("color", UNSET)

        display_name = d.pop("displayName", UNSET)

        _aggregation_mode = d.pop("aggregationMode", UNSET)
        aggregation_mode: Union[Unset, LeaderboardViewColumnDTOAggregationMode]
        if isinstance(_aggregation_mode, Unset):
            aggregation_mode = UNSET
        else:
            aggregation_mode = LeaderboardViewColumnDTOAggregationMode(_aggregation_mode)

        _display_mode = d.pop("displayMode", UNSET)
        display_mode: Union[Unset, LeaderboardViewColumnDTODisplayMode]
        if isinstance(_display_mode, Unset):
            display_mode = UNSET
        else:
            display_mode = LeaderboardViewColumnDTODisplayMode(_display_mode)

        leaderboard_view_column_dto = cls(
            column_type=column_type,
            id=id,
            pinned=pinned,
            width=width,
            color=color,
            display_name=display_name,
            aggregation_mode=aggregation_mode,
            display_mode=display_mode,
        )

        leaderboard_view_column_dto.additional_properties = d
        return leaderboard_view_column_dto

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
