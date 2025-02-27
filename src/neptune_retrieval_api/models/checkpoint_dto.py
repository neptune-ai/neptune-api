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

T = TypeVar("T", bound="CheckpointDTO")


@_attrs_define
class CheckpointDTO:
    """
    Attributes:
        creation_time (datetime.datetime):
        description (str):
        id (str):
        name (str):
        notebook_id (str):
        owner (str):
        path (str):
        removable (bool):
        size (int):
    """

    creation_time: datetime.datetime
    description: str
    id: str
    name: str
    notebook_id: str
    owner: str
    path: str
    removable: bool
    size: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        creation_time = self.creation_time.isoformat()

        description = self.description

        id = self.id

        name = self.name

        notebook_id = self.notebook_id

        owner = self.owner

        path = self.path

        removable = self.removable

        size = self.size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "creationTime": creation_time,
                "description": description,
                "id": id,
                "name": name,
                "notebookId": notebook_id,
                "owner": owner,
                "path": path,
                "removable": removable,
                "size": size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        creation_time = isoparse(d.pop("creationTime"))

        description = d.pop("description")

        id = d.pop("id")

        name = d.pop("name")

        notebook_id = d.pop("notebookId")

        owner = d.pop("owner")

        path = d.pop("path")

        removable = d.pop("removable")

        size = d.pop("size")

        checkpoint_dto = cls(
            creation_time=creation_time,
            description=description,
            id=id,
            name=name,
            notebook_id=notebook_id,
            owner=owner,
            path=path,
            removable=removable,
            size=size,
        )

        checkpoint_dto.additional_properties = d
        return checkpoint_dto

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
