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

from ..types import (
    UNSET,
    Unset,
)

T = TypeVar("T", bound="SeriesViewRequestDTO")


@_attrs_define
class SeriesViewRequestDTO:
    """
    Attributes:
        attribute_path (str):
        holder_identifier (str):
        holder_type (str):
        first_point_index (Union[Unset, int]):
        last_point_index (Union[Unset, int]):
    """

    attribute_path: str
    holder_identifier: str
    holder_type: str
    first_point_index: Union[Unset, int] = UNSET
    last_point_index: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attribute_path = self.attribute_path

        holder_identifier = self.holder_identifier

        holder_type = self.holder_type

        first_point_index = self.first_point_index

        last_point_index = self.last_point_index

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attributePath": attribute_path,
                "holderIdentifier": holder_identifier,
                "holderType": holder_type,
            }
        )
        if first_point_index is not UNSET:
            field_dict["firstPointIndex"] = first_point_index
        if last_point_index is not UNSET:
            field_dict["lastPointIndex"] = last_point_index

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        attribute_path = d.pop("attributePath")

        holder_identifier = d.pop("holderIdentifier")

        holder_type = d.pop("holderType")

        first_point_index = d.pop("firstPointIndex", UNSET)

        last_point_index = d.pop("lastPointIndex", UNSET)

        series_view_request_dto = cls(
            attribute_path=attribute_path,
            holder_identifier=holder_identifier,
            holder_type=holder_type,
            first_point_index=first_point_index,
            last_point_index=last_point_index,
        )

        series_view_request_dto.additional_properties = d
        return series_view_request_dto

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
