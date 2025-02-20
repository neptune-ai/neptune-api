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
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.point_value_dto import PointValueDTO


T = TypeVar("T", bound="LimitedChannelValuesDTO")


@_attrs_define
class LimitedChannelValuesDTO:
    """
    Attributes:
        channel_id (UUID):
        total_item_count (int):
        values (List['PointValueDTO']):
    """

    channel_id: UUID
    total_item_count: int
    values: List["PointValueDTO"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        channel_id = str(self.channel_id)

        total_item_count = self.total_item_count

        values = []
        for values_item_data in self.values:
            values_item = values_item_data.to_dict()
            values.append(values_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channelId": channel_id,
                "totalItemCount": total_item_count,
                "values": values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.point_value_dto import PointValueDTO

        d = src_dict.copy()
        channel_id = UUID(d.pop("channelId"))

        total_item_count = d.pop("totalItemCount")

        values = []
        _values = d.pop("values")
        for values_item_data in _values:
            values_item = PointValueDTO.from_dict(values_item_data)

            values.append(values_item)

        limited_channel_values_dto = cls(
            channel_id=channel_id,
            total_item_count=total_item_count,
            values=values,
        )

        limited_channel_values_dto.additional_properties = d
        return limited_channel_values_dto

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
