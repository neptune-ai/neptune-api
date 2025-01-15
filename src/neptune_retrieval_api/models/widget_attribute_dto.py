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

from ..models.widget_attribute_dto_type import WidgetAttributeDTOType
from ..types import (
    UNSET,
    Unset,
)

T = TypeVar("T", bound="WidgetAttributeDTO")


@_attrs_define
class WidgetAttributeDTO:
    """
    Attributes:
        name (str):
        type (WidgetAttributeDTOType):
        subproperty (Union[Unset, str]):
    """

    name: str
    type: WidgetAttributeDTOType
    subproperty: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        type = self.type.value

        subproperty = self.subproperty

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type,
            }
        )
        if subproperty is not UNSET:
            field_dict["subproperty"] = subproperty

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        type = WidgetAttributeDTOType(d.pop("type"))

        subproperty = d.pop("subproperty", UNSET)

        widget_attribute_dto = cls(
            name=name,
            type=type,
            subproperty=subproperty,
        )

        widget_attribute_dto.additional_properties = d
        return widget_attribute_dto

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
