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
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import (
    UNSET,
    Unset,
)

if TYPE_CHECKING:
    from ..models.attribute_filter_dto import AttributeFilterDTO
    from ..models.attribute_name_filter_dto import AttributeNameFilterDTO


T = TypeVar("T", bound="FilterQueryAttributeDefinitionsDTO")


@_attrs_define
class FilterQueryAttributeDefinitionsDTO:
    """
    Attributes:
        attribute_filter (Union[Unset, List['AttributeFilterDTO']]): Filter by attribute (match any), if null no type or
            property value filtering is applied
        attribute_name_filter (Union[Unset, AttributeNameFilterDTO]):
        attribute_name_regex (Union[Unset, str]): Filter by attribute name with regex, if null no name filtering is
            applied;deprecated, use attributeNameFilter instead; if attributeNameFilter is set, this field is ignored
        project_identifier (Union[Unset, str]): Project identifier; deprecated, use projectIdentifiers instead
    """

    attribute_filter: Union[Unset, List["AttributeFilterDTO"]] = UNSET
    attribute_name_filter: Union[Unset, "AttributeNameFilterDTO"] = UNSET
    attribute_name_regex: Union[Unset, str] = UNSET
    project_identifier: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attribute_filter: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attribute_filter, Unset):
            attribute_filter = []
            for attribute_filter_item_data in self.attribute_filter:
                attribute_filter_item = attribute_filter_item_data.to_dict()
                attribute_filter.append(attribute_filter_item)

        attribute_name_filter: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attribute_name_filter, Unset):
            attribute_name_filter = self.attribute_name_filter.to_dict()

        attribute_name_regex = self.attribute_name_regex

        project_identifier = self.project_identifier

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attribute_filter is not UNSET:
            field_dict["attributeFilter"] = attribute_filter
        if attribute_name_filter is not UNSET:
            field_dict["attributeNameFilter"] = attribute_name_filter
        if attribute_name_regex is not UNSET:
            field_dict["attributeNameRegex"] = attribute_name_regex
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.attribute_filter_dto import AttributeFilterDTO
        from ..models.attribute_name_filter_dto import AttributeNameFilterDTO

        d = src_dict.copy()
        attribute_filter: Union[Unset, List[AttributeFilterDTO]] = UNSET
        _attribute_filter = d.pop("attributeFilter", UNSET)
        if not isinstance(_attribute_filter, Unset):
            attribute_filter = []
            for attribute_filter_item_data in _attribute_filter:
                attribute_filter_item = AttributeFilterDTO.from_dict(attribute_filter_item_data)

                attribute_filter.append(attribute_filter_item)

        _attribute_name_filter = d.pop("attributeNameFilter", UNSET)
        attribute_name_filter: Union[Unset, AttributeNameFilterDTO]
        if isinstance(_attribute_name_filter, Unset):
            attribute_name_filter = UNSET
        else:
            attribute_name_filter = AttributeNameFilterDTO.from_dict(_attribute_name_filter)

        attribute_name_regex = d.pop("attributeNameRegex", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        filter_query_attribute_definitions_dto = cls(
            attribute_filter=attribute_filter,
            attribute_name_filter=attribute_name_filter,
            attribute_name_regex=attribute_name_regex,
            project_identifier=project_identifier,
        )

        filter_query_attribute_definitions_dto.additional_properties = d
        return filter_query_attribute_definitions_dto

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
