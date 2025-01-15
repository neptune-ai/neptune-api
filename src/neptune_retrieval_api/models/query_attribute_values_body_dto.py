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
from ..types import (
    UNSET,
    Unset,
)

T = TypeVar("T", bound="QueryAttributeValuesBodyDTO")


@_attrs_define
class QueryAttributeValuesBodyDTO:
    """
    Attributes:
        attribute_name (str): Required attribute name
        attribute_type (AttributeTypeDTO):
        limit (Union[Unset, int]): Optional limit of returned values
        regex_value_filter (Union[Unset, str]): Optional regex value filter; used only for `string` attributes
    """

    attribute_name: str
    attribute_type: AttributeTypeDTO
    limit: Union[Unset, int] = UNSET
    regex_value_filter: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attribute_name = self.attribute_name

        attribute_type = self.attribute_type.value

        limit = self.limit

        regex_value_filter = self.regex_value_filter

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attributeName": attribute_name,
                "attributeType": attribute_type,
            }
        )
        if limit is not UNSET:
            field_dict["limit"] = limit
        if regex_value_filter is not UNSET:
            field_dict["regexValueFilter"] = regex_value_filter

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        attribute_name = d.pop("attributeName")

        attribute_type = AttributeTypeDTO(d.pop("attributeType"))

        limit = d.pop("limit", UNSET)

        regex_value_filter = d.pop("regexValueFilter", UNSET)

        query_attribute_values_body_dto = cls(
            attribute_name=attribute_name,
            attribute_type=attribute_type,
            limit=limit,
            regex_value_filter=regex_value_filter,
        )

        query_attribute_values_body_dto.additional_properties = d
        return query_attribute_values_body_dto

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
