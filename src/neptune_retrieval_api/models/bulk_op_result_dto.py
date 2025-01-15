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
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bulk_op_error_dto import BulkOpErrorDTO


T = TypeVar("T", bound="BulkOpResultDTO")


@_attrs_define
class BulkOpResultDTO:
    """
    Attributes:
        errors (List['BulkOpErrorDTO']): Errors.
        updated_experiment_identifiers (List[str]): The entries updated successfully.
    """

    errors: List["BulkOpErrorDTO"]
    updated_experiment_identifiers: List[str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        errors = []
        for errors_item_data in self.errors:
            errors_item = errors_item_data.to_dict()
            errors.append(errors_item)

        updated_experiment_identifiers = self.updated_experiment_identifiers

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "errors": errors,
                "updatedExperimentIdentifiers": updated_experiment_identifiers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bulk_op_error_dto import BulkOpErrorDTO

        d = src_dict.copy()
        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:
            errors_item = BulkOpErrorDTO.from_dict(errors_item_data)

            errors.append(errors_item)

        updated_experiment_identifiers = cast(List[str], d.pop("updatedExperimentIdentifiers"))

        bulk_op_result_dto = cls(
            errors=errors,
            updated_experiment_identifiers=updated_experiment_identifiers,
        )

        bulk_op_result_dto.additional_properties = d
        return bulk_op_result_dto

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
