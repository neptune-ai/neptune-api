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
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bulk_op_error_dto_reason import BulkOpErrorDTOReason

T = TypeVar("T", bound="BulkOpErrorDTO")


@_attrs_define
class BulkOpErrorDTO:
    """
    Attributes:
        experiment_identifier (str): Same format as sent in request.
        message (str): Error message.
        reason (BulkOpErrorDTOReason): Error reason.
    """

    experiment_identifier: str
    message: str
    reason: BulkOpErrorDTOReason
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        experiment_identifier = self.experiment_identifier

        message = self.message

        reason = self.reason.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "experimentIdentifier": experiment_identifier,
                "message": message,
                "reason": reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        experiment_identifier = d.pop("experimentIdentifier")

        message = d.pop("message")

        reason = BulkOpErrorDTOReason(d.pop("reason"))

        bulk_op_error_dto = cls(
            experiment_identifier=experiment_identifier,
            message=message,
            reason=reason,
        )

        bulk_op_error_dto.additional_properties = d
        return bulk_op_error_dto

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
