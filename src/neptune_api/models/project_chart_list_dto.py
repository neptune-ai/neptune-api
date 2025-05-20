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
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    Type,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.project_chart_dto import ProjectChartDTO


T = TypeVar("T", bound="ProjectChartListDTO")


@_attrs_define
class ProjectChartListDTO:
    """
    Attributes:
        entries (List['ProjectChartDTO']): The entries matching the given criteria.
        matching_item_count (int): The total number of entries matching the given criteria.
        total_item_count (int): The total number of entries.
    """

    entries: List["ProjectChartDTO"]
    matching_item_count: int
    total_item_count: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entries = []
        for entries_item_data in self.entries:
            entries_item = entries_item_data.to_dict()
            entries.append(entries_item)

        matching_item_count = self.matching_item_count

        total_item_count = self.total_item_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entries": entries,
                "matchingItemCount": matching_item_count,
                "totalItemCount": total_item_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.project_chart_dto import ProjectChartDTO

        d = src_dict.copy()
        entries = []
        _entries = d.pop("entries")
        for entries_item_data in _entries:
            entries_item = ProjectChartDTO.from_dict(entries_item_data)

            entries.append(entries_item)

        matching_item_count = d.pop("matchingItemCount")

        total_item_count = d.pop("totalItemCount")

        project_chart_list_dto = cls(
            entries=entries,
            matching_item_count=matching_item_count,
            total_item_count=total_item_count,
        )

        project_chart_list_dto.additional_properties = d
        return project_chart_list_dto

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
