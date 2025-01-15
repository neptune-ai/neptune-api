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

import datetime
from typing import (
    Any,
    Dict,
    List,
    Type,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="NotebookDTO")


@_attrs_define
class NotebookDTO:
    """
    Attributes:
        creation_time (datetime.datetime):
        description (str):
        id (str):
        last_checkpoint_id (str):
        last_checkpoint_time (datetime.datetime):
        name (str):
        organization_id (str):
        organization_name (str):
        owner (str):
        path (str):
        project_id (str):
        project_name (str):
        removable (bool):
        size (int):
        total_storage_size (int):
    """

    creation_time: datetime.datetime
    description: str
    id: str
    last_checkpoint_id: str
    last_checkpoint_time: datetime.datetime
    name: str
    organization_id: str
    organization_name: str
    owner: str
    path: str
    project_id: str
    project_name: str
    removable: bool
    size: int
    total_storage_size: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        creation_time = self.creation_time.isoformat()

        description = self.description

        id = self.id

        last_checkpoint_id = self.last_checkpoint_id

        last_checkpoint_time = self.last_checkpoint_time.isoformat()

        name = self.name

        organization_id = self.organization_id

        organization_name = self.organization_name

        owner = self.owner

        path = self.path

        project_id = self.project_id

        project_name = self.project_name

        removable = self.removable

        size = self.size

        total_storage_size = self.total_storage_size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "creationTime": creation_time,
                "description": description,
                "id": id,
                "lastCheckpointId": last_checkpoint_id,
                "lastCheckpointTime": last_checkpoint_time,
                "name": name,
                "organizationId": organization_id,
                "organizationName": organization_name,
                "owner": owner,
                "path": path,
                "projectId": project_id,
                "projectName": project_name,
                "removable": removable,
                "size": size,
                "totalStorageSize": total_storage_size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        creation_time = isoparse(d.pop("creationTime"))

        description = d.pop("description")

        id = d.pop("id")

        last_checkpoint_id = d.pop("lastCheckpointId")

        last_checkpoint_time = isoparse(d.pop("lastCheckpointTime"))

        name = d.pop("name")

        organization_id = d.pop("organizationId")

        organization_name = d.pop("organizationName")

        owner = d.pop("owner")

        path = d.pop("path")

        project_id = d.pop("projectId")

        project_name = d.pop("projectName")

        removable = d.pop("removable")

        size = d.pop("size")

        total_storage_size = d.pop("totalStorageSize")

        notebook_dto = cls(
            creation_time=creation_time,
            description=description,
            id=id,
            last_checkpoint_id=last_checkpoint_id,
            last_checkpoint_time=last_checkpoint_time,
            name=name,
            organization_id=organization_id,
            organization_name=organization_name,
            owner=owner,
            path=path,
            project_id=project_id,
            project_name=project_name,
            removable=removable,
            size=size,
            total_storage_size=total_storage_size,
        )

        notebook_dto.additional_properties = d
        return notebook_dto

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
