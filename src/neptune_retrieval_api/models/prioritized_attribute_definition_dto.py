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
    from ..models.attribute_definition_dto import AttributeDefinitionDTO


T = TypeVar("T", bound="PrioritizedAttributeDefinitionDTO")


@_attrs_define
class PrioritizedAttributeDefinitionDTO:
    """
    Attributes:
        attribute_definition_dto (AttributeDefinitionDTO):
        matched_priority_query (Union[Unset, bool]):
    """

    attribute_definition_dto: "AttributeDefinitionDTO"
    matched_priority_query: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attribute_definition_dto = self.attribute_definition_dto.to_dict()

        matched_priority_query = self.matched_priority_query

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attributeDefinitionDTO": attribute_definition_dto,
            }
        )
        if matched_priority_query is not UNSET:
            field_dict["matchedPriorityQuery"] = matched_priority_query

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.attribute_definition_dto import AttributeDefinitionDTO

        d = src_dict.copy()
        attribute_definition_dto = AttributeDefinitionDTO.from_dict(d.pop("attributeDefinitionDTO"))

        matched_priority_query = d.pop("matchedPriorityQuery", UNSET)

        prioritized_attribute_definition_dto = cls(
            attribute_definition_dto=attribute_definition_dto,
            matched_priority_query=matched_priority_query,
        )

        prioritized_attribute_definition_dto.additional_properties = d
        return prioritized_attribute_definition_dto

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
