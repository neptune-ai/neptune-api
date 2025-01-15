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

from ..types import (
    UNSET,
    Unset,
)

T = TypeVar("T", bound="UpdateDashboardVersionDTO")


@_attrs_define
class UpdateDashboardVersionDTO:
    """
    Attributes:
        draft (Union[Unset, bool]):
        version_description (Union[Unset, str]):
        version_name (Union[Unset, str]):
    """

    draft: Union[Unset, bool] = UNSET
    version_description: Union[Unset, str] = UNSET
    version_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        draft = self.draft

        version_description = self.version_description

        version_name = self.version_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if draft is not UNSET:
            field_dict["draft"] = draft
        if version_description is not UNSET:
            field_dict["versionDescription"] = version_description
        if version_name is not UNSET:
            field_dict["versionName"] = version_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        draft = d.pop("draft", UNSET)

        version_description = d.pop("versionDescription", UNSET)

        version_name = d.pop("versionName", UNSET)

        update_dashboard_version_dto = cls(
            draft=draft,
            version_description=version_description,
            version_name=version_name,
        )

        update_dashboard_version_dto.additional_properties = d
        return update_dashboard_version_dto

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
