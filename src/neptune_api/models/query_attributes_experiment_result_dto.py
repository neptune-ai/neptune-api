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
    from ..models.attribute_dto import AttributeDTO


T = TypeVar("T", bound="QueryAttributesExperimentResultDTO")


@_attrs_define
class QueryAttributesExperimentResultDTO:
    """
    Attributes:
        attributes (List['AttributeDTO']):
        experiment_id (str):
        experiment_short_id (str):
        organization_name (str):
        project_name (str):
    """

    attributes: List["AttributeDTO"]
    experiment_id: str
    experiment_short_id: str
    organization_name: str
    project_name: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attributes = []
        for attributes_item_data in self.attributes:
            attributes_item = attributes_item_data.to_dict()
            attributes.append(attributes_item)

        experiment_id = self.experiment_id

        experiment_short_id = self.experiment_short_id

        organization_name = self.organization_name

        project_name = self.project_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attributes": attributes,
                "experimentId": experiment_id,
                "experimentShortId": experiment_short_id,
                "organizationName": organization_name,
                "projectName": project_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.attribute_dto import AttributeDTO

        d = src_dict.copy()
        attributes = []
        _attributes = d.pop("attributes")
        for attributes_item_data in _attributes:
            attributes_item = AttributeDTO.from_dict(attributes_item_data)

            attributes.append(attributes_item)

        experiment_id = d.pop("experimentId")

        experiment_short_id = d.pop("experimentShortId")

        organization_name = d.pop("organizationName")

        project_name = d.pop("projectName")

        query_attributes_experiment_result_dto = cls(
            attributes=attributes,
            experiment_id=experiment_id,
            experiment_short_id=experiment_short_id,
            organization_name=organization_name,
            project_name=project_name,
        )

        query_attributes_experiment_result_dto.additional_properties = d
        return query_attributes_experiment_result_dto

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
