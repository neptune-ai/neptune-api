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

from ..types import (
    UNSET,
    Unset,
)

T = TypeVar("T", bound="AuditInfo")


@_attrs_define
class AuditInfo:
    """
    Attributes:
        accustomed_experiment_created_at (Union[Unset, datetime.datetime]):
        first_experiment_created_at (Union[Unset, datetime.datetime]):
    """

    accustomed_experiment_created_at: Union[Unset, datetime.datetime] = UNSET
    first_experiment_created_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        accustomed_experiment_created_at: Union[Unset, str] = UNSET
        if not isinstance(self.accustomed_experiment_created_at, Unset):
            accustomed_experiment_created_at = self.accustomed_experiment_created_at.isoformat()

        first_experiment_created_at: Union[Unset, str] = UNSET
        if not isinstance(self.first_experiment_created_at, Unset):
            first_experiment_created_at = self.first_experiment_created_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accustomed_experiment_created_at is not UNSET:
            field_dict["accustomedExperimentCreatedAt"] = accustomed_experiment_created_at
        if first_experiment_created_at is not UNSET:
            field_dict["firstExperimentCreatedAt"] = first_experiment_created_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _accustomed_experiment_created_at = d.pop("accustomedExperimentCreatedAt", UNSET)
        accustomed_experiment_created_at: Union[Unset, datetime.datetime]
        if isinstance(_accustomed_experiment_created_at, Unset):
            accustomed_experiment_created_at = UNSET
        else:
            accustomed_experiment_created_at = isoparse(_accustomed_experiment_created_at)

        _first_experiment_created_at = d.pop("firstExperimentCreatedAt", UNSET)
        first_experiment_created_at: Union[Unset, datetime.datetime]
        if isinstance(_first_experiment_created_at, Unset):
            first_experiment_created_at = UNSET
        else:
            first_experiment_created_at = isoparse(_first_experiment_created_at)

        audit_info = cls(
            accustomed_experiment_created_at=accustomed_experiment_created_at,
            first_experiment_created_at=first_experiment_created_at,
        )

        audit_info.additional_properties = d
        return audit_info

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
