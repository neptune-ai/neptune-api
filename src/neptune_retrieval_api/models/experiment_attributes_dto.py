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
    from ..models.system_attributes_dto import SystemAttributesDTO


T = TypeVar("T", bound="ExperimentAttributesDTO")


@_attrs_define
class ExperimentAttributesDTO:
    """
    Attributes:
        attributes (List['AttributeDTO']):
        id (str):
        organization_id (str):
        organization_name (str):
        project_id (str):
        project_name (str):
        system_attributes (SystemAttributesDTO):
        trashed (bool):
    """

    attributes: List["AttributeDTO"]
    id: str
    organization_id: str
    organization_name: str
    project_id: str
    project_name: str
    system_attributes: "SystemAttributesDTO"
    trashed: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attributes = []
        for attributes_item_data in self.attributes:
            attributes_item = attributes_item_data.to_dict()
            attributes.append(attributes_item)

        id = self.id

        organization_id = self.organization_id

        organization_name = self.organization_name

        project_id = self.project_id

        project_name = self.project_name

        system_attributes = self.system_attributes.to_dict()

        trashed = self.trashed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attributes": attributes,
                "id": id,
                "organizationId": organization_id,
                "organizationName": organization_name,
                "projectId": project_id,
                "projectName": project_name,
                "systemAttributes": system_attributes,
                "trashed": trashed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.attribute_dto import AttributeDTO
        from ..models.system_attributes_dto import SystemAttributesDTO

        d = src_dict.copy()
        attributes = []
        _attributes = d.pop("attributes")
        for attributes_item_data in _attributes:
            attributes_item = AttributeDTO.from_dict(attributes_item_data)

            attributes.append(attributes_item)

        id = d.pop("id")

        organization_id = d.pop("organizationId")

        organization_name = d.pop("organizationName")

        project_id = d.pop("projectId")

        project_name = d.pop("projectName")

        system_attributes = SystemAttributesDTO.from_dict(d.pop("systemAttributes"))

        trashed = d.pop("trashed")

        experiment_attributes_dto = cls(
            attributes=attributes,
            id=id,
            organization_id=organization_id,
            organization_name=organization_name,
            project_id=project_id,
            project_name=project_name,
            system_attributes=system_attributes,
            trashed=trashed,
        )

        experiment_attributes_dto.additional_properties = d
        return experiment_attributes_dto

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
