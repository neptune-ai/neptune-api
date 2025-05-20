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
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.experiment_type_dto import ExperimentTypeDTO
from ..types import (
    UNSET,
    Unset,
)

if TYPE_CHECKING:
    from ..models.git_info_dto import GitInfoDTO


T = TypeVar("T", bound="ExperimentCreationParams")


@_attrs_define
class ExperimentCreationParams:
    """
    Attributes:
        checkpoint_id (Union[Unset, str]):
        custom_id (Union[Unset, str]):
        git_info (Union[Unset, GitInfoDTO]):
        is_head (Union[Unset, bool]):
        key (Union[Unset, str]):
        notebook_id (Union[Unset, str]):
        parent_id (Union[Unset, str]):
        project_id (Union[Unset, str]):
        project_identifier (Union[Unset, str]):
        type (Union[Unset, ExperimentTypeDTO]):
    """

    checkpoint_id: Union[Unset, str] = UNSET
    custom_id: Union[Unset, str] = UNSET
    git_info: Union[Unset, "GitInfoDTO"] = UNSET
    is_head: Union[Unset, bool] = UNSET
    key: Union[Unset, str] = UNSET
    notebook_id: Union[Unset, str] = UNSET
    parent_id: Union[Unset, str] = UNSET
    project_id: Union[Unset, str] = UNSET
    project_identifier: Union[Unset, str] = UNSET
    type: Union[Unset, ExperimentTypeDTO] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        checkpoint_id = self.checkpoint_id

        custom_id = self.custom_id

        git_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.git_info, Unset):
            git_info = self.git_info.to_dict()

        is_head = self.is_head

        key = self.key

        notebook_id = self.notebook_id

        parent_id = self.parent_id

        project_id = self.project_id

        project_identifier = self.project_identifier

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if checkpoint_id is not UNSET:
            field_dict["checkpointId"] = checkpoint_id
        if custom_id is not UNSET:
            field_dict["customId"] = custom_id
        if git_info is not UNSET:
            field_dict["gitInfo"] = git_info
        if is_head is not UNSET:
            field_dict["isHead"] = is_head
        if key is not UNSET:
            field_dict["key"] = key
        if notebook_id is not UNSET:
            field_dict["notebookId"] = notebook_id
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.git_info_dto import GitInfoDTO

        d = src_dict.copy()
        checkpoint_id = d.pop("checkpointId", UNSET)

        custom_id = d.pop("customId", UNSET)

        _git_info = d.pop("gitInfo", UNSET)
        git_info: Union[Unset, GitInfoDTO]
        if isinstance(_git_info, Unset):
            git_info = UNSET
        else:
            git_info = GitInfoDTO.from_dict(_git_info)

        is_head = d.pop("isHead", UNSET)

        key = d.pop("key", UNSET)

        notebook_id = d.pop("notebookId", UNSET)

        parent_id = d.pop("parentId", UNSET)

        project_id = d.pop("projectId", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, ExperimentTypeDTO]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ExperimentTypeDTO(_type)

        experiment_creation_params = cls(
            checkpoint_id=checkpoint_id,
            custom_id=custom_id,
            git_info=git_info,
            is_head=is_head,
            key=key,
            notebook_id=notebook_id,
            parent_id=parent_id,
            project_id=project_id,
            project_identifier=project_identifier,
            type=type,
        )

        experiment_creation_params.additional_properties = d
        return experiment_creation_params

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
