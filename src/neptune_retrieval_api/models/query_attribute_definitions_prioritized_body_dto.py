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
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import (
    UNSET,
    Unset,
)

if TYPE_CHECKING:
    from ..models.filter_query_attribute_definitions_dto import FilterQueryAttributeDefinitionsDTO
    from ..models.priority_query_attribute_definitions_dto import PriorityQueryAttributeDefinitionsDTO


T = TypeVar("T", bound="QueryAttributeDefinitionsPrioritizedBodyDTO")


@_attrs_define
class QueryAttributeDefinitionsPrioritizedBodyDTO:
    """
    Attributes:
        filter_query_attribute_definitions_dto (FilterQueryAttributeDefinitionsDTO):
        limit (Union[Unset, int]):
        priority_query_attribute_definitions_dto (Union[Unset, PriorityQueryAttributeDefinitionsDTO]):
        project_identifiers (Union[Unset, List[str]]): Project identifiers to filter by
    """

    filter_query_attribute_definitions_dto: "FilterQueryAttributeDefinitionsDTO"
    limit: Union[Unset, int] = UNSET
    priority_query_attribute_definitions_dto: Union[Unset, "PriorityQueryAttributeDefinitionsDTO"] = UNSET
    project_identifiers: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        filter_query_attribute_definitions_dto = self.filter_query_attribute_definitions_dto.to_dict()

        limit = self.limit

        priority_query_attribute_definitions_dto: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.priority_query_attribute_definitions_dto, Unset):
            priority_query_attribute_definitions_dto = self.priority_query_attribute_definitions_dto.to_dict()

        project_identifiers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.project_identifiers, Unset):
            project_identifiers = self.project_identifiers

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filterQueryAttributeDefinitionsDTO": filter_query_attribute_definitions_dto,
            }
        )
        if limit is not UNSET:
            field_dict["limit"] = limit
        if priority_query_attribute_definitions_dto is not UNSET:
            field_dict["priorityQueryAttributeDefinitionsDTO"] = priority_query_attribute_definitions_dto
        if project_identifiers is not UNSET:
            field_dict["projectIdentifiers"] = project_identifiers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.filter_query_attribute_definitions_dto import FilterQueryAttributeDefinitionsDTO
        from ..models.priority_query_attribute_definitions_dto import PriorityQueryAttributeDefinitionsDTO

        d = src_dict.copy()
        filter_query_attribute_definitions_dto = FilterQueryAttributeDefinitionsDTO.from_dict(
            d.pop("filterQueryAttributeDefinitionsDTO")
        )

        limit = d.pop("limit", UNSET)

        _priority_query_attribute_definitions_dto = d.pop("priorityQueryAttributeDefinitionsDTO", UNSET)
        priority_query_attribute_definitions_dto: Union[Unset, PriorityQueryAttributeDefinitionsDTO]
        if isinstance(_priority_query_attribute_definitions_dto, Unset):
            priority_query_attribute_definitions_dto = UNSET
        else:
            priority_query_attribute_definitions_dto = PriorityQueryAttributeDefinitionsDTO.from_dict(
                _priority_query_attribute_definitions_dto
            )

        project_identifiers = cast(List[str], d.pop("projectIdentifiers", UNSET))

        query_attribute_definitions_prioritized_body_dto = cls(
            filter_query_attribute_definitions_dto=filter_query_attribute_definitions_dto,
            limit=limit,
            priority_query_attribute_definitions_dto=priority_query_attribute_definitions_dto,
            project_identifiers=project_identifiers,
        )

        query_attribute_definitions_prioritized_body_dto.additional_properties = d
        return query_attribute_definitions_prioritized_body_dto

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
