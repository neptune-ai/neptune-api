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

from ..types import (
    UNSET,
    Unset,
)

if TYPE_CHECKING:
    from ..models.bool_attribute_dto import BoolAttributeDTO
    from ..models.datetime_attribute_dto import DatetimeAttributeDTO
    from ..models.experiment_state_attribute_dto import ExperimentStateAttributeDTO
    from ..models.float_attribute_dto import FloatAttributeDTO
    from ..models.git_info_dto import GitInfoDTO
    from ..models.int_attribute_dto import IntAttributeDTO
    from ..models.notebook_ref_attribute_dto import NotebookRefAttributeDTO
    from ..models.string_attribute_dto import StringAttributeDTO
    from ..models.string_set_attribute_dto import StringSetAttributeDTO


T = TypeVar("T", bound="SystemAttributesDTO")


@_attrs_define
class SystemAttributesDTO:
    """
    Attributes:
        creation_time (DatetimeAttributeDTO):
        custom_id (StringAttributeDTO):
        description (StringAttributeDTO):
        failed (BoolAttributeDTO):
        family (StringAttributeDTO):
        modification_time (DatetimeAttributeDTO):
        monitoring_time (IntAttributeDTO):
        name (StringAttributeDTO):
        ping_time (DatetimeAttributeDTO):
        running_time (FloatAttributeDTO):
        short_id (StringAttributeDTO):
        size (FloatAttributeDTO):
        state (ExperimentStateAttributeDTO):
        tags (StringSetAttributeDTO):
        trashed (BoolAttributeDTO):
        git_ref (Union[Unset, GitInfoDTO]):
        hostname (Union[Unset, StringAttributeDTO]):
        notebook_ref (Union[Unset, NotebookRefAttributeDTO]):
        owner (Union[Unset, StringAttributeDTO]):
    """

    creation_time: "DatetimeAttributeDTO"
    custom_id: "StringAttributeDTO"
    description: "StringAttributeDTO"
    failed: "BoolAttributeDTO"
    family: "StringAttributeDTO"
    modification_time: "DatetimeAttributeDTO"
    monitoring_time: "IntAttributeDTO"
    name: "StringAttributeDTO"
    ping_time: "DatetimeAttributeDTO"
    running_time: "FloatAttributeDTO"
    short_id: "StringAttributeDTO"
    size: "FloatAttributeDTO"
    state: "ExperimentStateAttributeDTO"
    tags: "StringSetAttributeDTO"
    trashed: "BoolAttributeDTO"
    git_ref: Union[Unset, "GitInfoDTO"] = UNSET
    hostname: Union[Unset, "StringAttributeDTO"] = UNSET
    notebook_ref: Union[Unset, "NotebookRefAttributeDTO"] = UNSET
    owner: Union[Unset, "StringAttributeDTO"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        creation_time = self.creation_time.to_dict()

        custom_id = self.custom_id.to_dict()

        description = self.description.to_dict()

        failed = self.failed.to_dict()

        family = self.family.to_dict()

        modification_time = self.modification_time.to_dict()

        monitoring_time = self.monitoring_time.to_dict()

        name = self.name.to_dict()

        ping_time = self.ping_time.to_dict()

        running_time = self.running_time.to_dict()

        short_id = self.short_id.to_dict()

        size = self.size.to_dict()

        state = self.state.to_dict()

        tags = self.tags.to_dict()

        trashed = self.trashed.to_dict()

        git_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.git_ref, Unset):
            git_ref = self.git_ref.to_dict()

        hostname: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.hostname, Unset):
            hostname = self.hostname.to_dict()

        notebook_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.notebook_ref, Unset):
            notebook_ref = self.notebook_ref.to_dict()

        owner: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "creationTime": creation_time,
                "customId": custom_id,
                "description": description,
                "failed": failed,
                "family": family,
                "modificationTime": modification_time,
                "monitoringTime": monitoring_time,
                "name": name,
                "pingTime": ping_time,
                "runningTime": running_time,
                "shortId": short_id,
                "size": size,
                "state": state,
                "tags": tags,
                "trashed": trashed,
            }
        )
        if git_ref is not UNSET:
            field_dict["gitRef"] = git_ref
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if notebook_ref is not UNSET:
            field_dict["notebookRef"] = notebook_ref
        if owner is not UNSET:
            field_dict["owner"] = owner

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bool_attribute_dto import BoolAttributeDTO
        from ..models.datetime_attribute_dto import DatetimeAttributeDTO
        from ..models.experiment_state_attribute_dto import ExperimentStateAttributeDTO
        from ..models.float_attribute_dto import FloatAttributeDTO
        from ..models.git_info_dto import GitInfoDTO
        from ..models.int_attribute_dto import IntAttributeDTO
        from ..models.notebook_ref_attribute_dto import NotebookRefAttributeDTO
        from ..models.string_attribute_dto import StringAttributeDTO
        from ..models.string_set_attribute_dto import StringSetAttributeDTO

        d = src_dict.copy()
        creation_time = DatetimeAttributeDTO.from_dict(d.pop("creationTime"))

        custom_id = StringAttributeDTO.from_dict(d.pop("customId"))

        description = StringAttributeDTO.from_dict(d.pop("description"))

        failed = BoolAttributeDTO.from_dict(d.pop("failed"))

        family = StringAttributeDTO.from_dict(d.pop("family"))

        modification_time = DatetimeAttributeDTO.from_dict(d.pop("modificationTime"))

        monitoring_time = IntAttributeDTO.from_dict(d.pop("monitoringTime"))

        name = StringAttributeDTO.from_dict(d.pop("name"))

        ping_time = DatetimeAttributeDTO.from_dict(d.pop("pingTime"))

        running_time = FloatAttributeDTO.from_dict(d.pop("runningTime"))

        short_id = StringAttributeDTO.from_dict(d.pop("shortId"))

        size = FloatAttributeDTO.from_dict(d.pop("size"))

        state = ExperimentStateAttributeDTO.from_dict(d.pop("state"))

        tags = StringSetAttributeDTO.from_dict(d.pop("tags"))

        trashed = BoolAttributeDTO.from_dict(d.pop("trashed"))

        _git_ref = d.pop("gitRef", UNSET)
        git_ref: Union[Unset, GitInfoDTO]
        if isinstance(_git_ref, Unset):
            git_ref = UNSET
        else:
            git_ref = GitInfoDTO.from_dict(_git_ref)

        _hostname = d.pop("hostname", UNSET)
        hostname: Union[Unset, StringAttributeDTO]
        if isinstance(_hostname, Unset):
            hostname = UNSET
        else:
            hostname = StringAttributeDTO.from_dict(_hostname)

        _notebook_ref = d.pop("notebookRef", UNSET)
        notebook_ref: Union[Unset, NotebookRefAttributeDTO]
        if isinstance(_notebook_ref, Unset):
            notebook_ref = UNSET
        else:
            notebook_ref = NotebookRefAttributeDTO.from_dict(_notebook_ref)

        _owner = d.pop("owner", UNSET)
        owner: Union[Unset, StringAttributeDTO]
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = StringAttributeDTO.from_dict(_owner)

        system_attributes_dto = cls(
            creation_time=creation_time,
            custom_id=custom_id,
            description=description,
            failed=failed,
            family=family,
            modification_time=modification_time,
            monitoring_time=monitoring_time,
            name=name,
            ping_time=ping_time,
            running_time=running_time,
            short_id=short_id,
            size=size,
            state=state,
            tags=tags,
            trashed=trashed,
            git_ref=git_ref,
            hostname=hostname,
            notebook_ref=notebook_ref,
            owner=owner,
        )

        system_attributes_dto.additional_properties = d
        return system_attributes_dto

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
