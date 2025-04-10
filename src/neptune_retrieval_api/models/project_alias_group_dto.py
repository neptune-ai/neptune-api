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
    from ..models.name_alias_dto import NameAliasDTO


T = TypeVar("T", bound="ProjectAliasGroupDTO")


@_attrs_define
class ProjectAliasGroupDTO:
    """
    Attributes:
        aliases (List['NameAliasDTO']): List of aliases in this project
        project_id (str): Project ID
    """

    aliases: List["NameAliasDTO"]
    project_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        aliases = []
        for aliases_item_data in self.aliases:
            aliases_item = aliases_item_data.to_dict()
            aliases.append(aliases_item)

        project_id = self.project_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "aliases": aliases,
                "projectId": project_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.name_alias_dto import NameAliasDTO

        d = src_dict.copy()
        aliases = []
        _aliases = d.pop("aliases")
        for aliases_item_data in _aliases:
            aliases_item = NameAliasDTO.from_dict(aliases_item_data)

            aliases.append(aliases_item)

        project_id = d.pop("projectId")

        project_alias_group_dto = cls(
            aliases=aliases,
            project_id=project_id,
        )

        project_alias_group_dto.additional_properties = d
        return project_alias_group_dto

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
