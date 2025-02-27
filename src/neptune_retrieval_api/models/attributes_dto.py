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

from ..models.experiment_type_dto import ExperimentTypeDTO

if TYPE_CHECKING:
    from ..models.attribute_dto import AttributeDTO


T = TypeVar("T", bound="AttributesDTO")


@_attrs_define
class AttributesDTO:
    """
    Attributes:
        attributes (List['AttributeDTO']):
        experiment_id (str):
        organization_id (str):
        organization_name (str):
        project_id (str):
        project_name (str):
        type (ExperimentTypeDTO):
    """

    attributes: List["AttributeDTO"]
    experiment_id: str
    organization_id: str
    organization_name: str
    project_id: str
    project_name: str
    type: ExperimentTypeDTO
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attributes = []
        for attributes_item_data in self.attributes:
            attributes_item = attributes_item_data.to_dict()
            attributes.append(attributes_item)

        experiment_id = self.experiment_id

        organization_id = self.organization_id

        organization_name = self.organization_name

        project_id = self.project_id

        project_name = self.project_name

        type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attributes": attributes,
                "experimentId": experiment_id,
                "organizationId": organization_id,
                "organizationName": organization_name,
                "projectId": project_id,
                "projectName": project_name,
                "type": type,
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

        organization_id = d.pop("organizationId")

        organization_name = d.pop("organizationName")

        project_id = d.pop("projectId")

        project_name = d.pop("projectName")

        type = ExperimentTypeDTO(d.pop("type"))

        attributes_dto = cls(
            attributes=attributes,
            experiment_id=experiment_id,
            organization_id=organization_id,
            organization_name=organization_name,
            project_id=project_id,
            project_name=project_name,
            type=type,
        )

        attributes_dto.additional_properties = d
        return attributes_dto

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
