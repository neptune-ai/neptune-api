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

from ..models.attribute_type_dto import AttributeTypeDTO
from ..types import (
    UNSET,
    Unset,
)

if TYPE_CHECKING:
    from ..models.git_commit_dto import GitCommitDTO


T = TypeVar("T", bound="GitInfoDTO")


@_attrs_define
class GitInfoDTO:
    """
    Attributes:
        attribute_name (str):
        attribute_type (AttributeTypeDTO):
        commit (GitCommitDTO):
        repository_dirty (bool):
        current_branch (Union[Unset, str]):
        remotes (Union[Unset, List[str]]):
    """

    attribute_name: str
    attribute_type: AttributeTypeDTO
    commit: "GitCommitDTO"
    repository_dirty: bool
    current_branch: Union[Unset, str] = UNSET
    remotes: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attribute_name = self.attribute_name

        attribute_type = self.attribute_type.value

        commit = self.commit.to_dict()

        repository_dirty = self.repository_dirty

        current_branch = self.current_branch

        remotes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.remotes, Unset):
            remotes = self.remotes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attributeName": attribute_name,
                "attributeType": attribute_type,
                "commit": commit,
                "repositoryDirty": repository_dirty,
            }
        )
        if current_branch is not UNSET:
            field_dict["currentBranch"] = current_branch
        if remotes is not UNSET:
            field_dict["remotes"] = remotes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.git_commit_dto import GitCommitDTO

        d = src_dict.copy()
        attribute_name = d.pop("attributeName")

        attribute_type = AttributeTypeDTO(d.pop("attributeType"))

        commit = GitCommitDTO.from_dict(d.pop("commit"))

        repository_dirty = d.pop("repositoryDirty")

        current_branch = d.pop("currentBranch", UNSET)

        remotes = cast(List[str], d.pop("remotes", UNSET))

        git_info_dto = cls(
            attribute_name=attribute_name,
            attribute_type=attribute_type,
            commit=commit,
            repository_dirty=repository_dirty,
            current_branch=current_branch,
            remotes=remotes,
        )

        git_info_dto.additional_properties = d
        return git_info_dto

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
