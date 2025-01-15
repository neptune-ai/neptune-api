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

from ..models.experiment_type_dto import ExperimentTypeDTO
from ..types import (
    UNSET,
    Unset,
)

T = TypeVar("T", bound="Experiment")


@_attrs_define
class Experiment:
    """
    Attributes:
        id (str):
        organization_id (str):
        organization_name (str):
        parent_id (str):
        project_id (str):
        project_name (str):
        short_id (str):
        trashed (bool):
        type (ExperimentTypeDTO):
        custom_id (Union[Unset, str]):
    """

    id: str
    organization_id: str
    organization_name: str
    parent_id: str
    project_id: str
    project_name: str
    short_id: str
    trashed: bool
    type: ExperimentTypeDTO
    custom_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        organization_id = self.organization_id

        organization_name = self.organization_name

        parent_id = self.parent_id

        project_id = self.project_id

        project_name = self.project_name

        short_id = self.short_id

        trashed = self.trashed

        type = self.type.value

        custom_id = self.custom_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "organizationId": organization_id,
                "organizationName": organization_name,
                "parentId": parent_id,
                "projectId": project_id,
                "projectName": project_name,
                "shortId": short_id,
                "trashed": trashed,
                "type": type,
            }
        )
        if custom_id is not UNSET:
            field_dict["customId"] = custom_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        organization_id = d.pop("organizationId")

        organization_name = d.pop("organizationName")

        parent_id = d.pop("parentId")

        project_id = d.pop("projectId")

        project_name = d.pop("projectName")

        short_id = d.pop("shortId")

        trashed = d.pop("trashed")

        type = ExperimentTypeDTO(d.pop("type"))

        custom_id = d.pop("customId", UNSET)

        experiment = cls(
            id=id,
            organization_id=organization_id,
            organization_name=organization_name,
            parent_id=parent_id,
            project_id=project_id,
            project_name=project_name,
            short_id=short_id,
            trashed=trashed,
            type=type,
            custom_id=custom_id,
        )

        experiment.additional_properties = d
        return experiment

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
