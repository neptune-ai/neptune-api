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
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.dashboard_version_dto_type import DashboardVersionDTOType
from ..types import (
    UNSET,
    Unset,
)

T = TypeVar("T", bound="DashboardVersionDTO")


@_attrs_define
class DashboardVersionDTO:
    """
    Attributes:
        created_time (datetime.datetime):
        id (str):
        last_updated_time (datetime.datetime):
        name (str):
        type (DashboardVersionDTOType):
        version_branch (str):
        draft (Union[Unset, bool]):
        owner (Union[Unset, str]):
        version_description (Union[Unset, str]):
        version_name (Union[Unset, str]):
    """

    created_time: datetime.datetime
    id: str
    last_updated_time: datetime.datetime
    name: str
    type: DashboardVersionDTOType
    version_branch: str
    draft: Union[Unset, bool] = UNSET
    owner: Union[Unset, str] = UNSET
    version_description: Union[Unset, str] = UNSET
    version_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_time = self.created_time.isoformat()

        id = self.id

        last_updated_time = self.last_updated_time.isoformat()

        name = self.name

        type = self.type.value

        version_branch = self.version_branch

        draft = self.draft

        owner = self.owner

        version_description = self.version_description

        version_name = self.version_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdTime": created_time,
                "id": id,
                "lastUpdatedTime": last_updated_time,
                "name": name,
                "type": type,
                "versionBranch": version_branch,
            }
        )
        if draft is not UNSET:
            field_dict["draft"] = draft
        if owner is not UNSET:
            field_dict["owner"] = owner
        if version_description is not UNSET:
            field_dict["versionDescription"] = version_description
        if version_name is not UNSET:
            field_dict["versionName"] = version_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created_time = isoparse(d.pop("createdTime"))

        id = d.pop("id")

        last_updated_time = isoparse(d.pop("lastUpdatedTime"))

        name = d.pop("name")

        type = DashboardVersionDTOType(d.pop("type"))

        version_branch = d.pop("versionBranch")

        draft = d.pop("draft", UNSET)

        owner = d.pop("owner", UNSET)

        version_description = d.pop("versionDescription", UNSET)

        version_name = d.pop("versionName", UNSET)

        dashboard_version_dto = cls(
            created_time=created_time,
            id=id,
            last_updated_time=last_updated_time,
            name=name,
            type=type,
            version_branch=version_branch,
            draft=draft,
            owner=owner,
            version_description=version_description,
            version_name=version_name,
        )

        dashboard_version_dto.additional_properties = d
        return dashboard_version_dto

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
