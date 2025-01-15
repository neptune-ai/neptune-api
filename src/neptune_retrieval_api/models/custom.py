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

from ..types import (
    UNSET,
    Unset,
)

T = TypeVar("T", bound="Custom")


@_attrs_define
class Custom:
    """
    Attributes:
        attribute (Union[Unset, str]):
        attributes (Union[Unset, List[str]]):
        custom_x_formula (Union[Unset, str]):
    """

    attribute: Union[Unset, str] = UNSET
    attributes: Union[Unset, List[str]] = UNSET
    custom_x_formula: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attribute = self.attribute

        attributes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes

        custom_x_formula = self.custom_x_formula

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attribute is not UNSET:
            field_dict["attribute"] = attribute
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if custom_x_formula is not UNSET:
            field_dict["customXFormula"] = custom_x_formula

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        attribute = d.pop("attribute", UNSET)

        attributes = cast(List[str], d.pop("attributes", UNSET))

        custom_x_formula = d.pop("customXFormula", UNSET)

        custom = cls(
            attribute=attribute,
            attributes=attributes,
            custom_x_formula=custom_x_formula,
        )

        custom.additional_properties = d
        return custom

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
