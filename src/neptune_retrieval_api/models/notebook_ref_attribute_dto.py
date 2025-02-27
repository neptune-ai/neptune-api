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

from ..models.attribute_type_dto import AttributeTypeDTO
from ..types import (
    UNSET,
    Unset,
)

T = TypeVar("T", bound="NotebookRefAttributeDTO")


@_attrs_define
class NotebookRefAttributeDTO:
    """
    Attributes:
        attribute_name (str):
        attribute_type (AttributeTypeDTO):
        notebook_deleted (bool):
        notebook_id (str):
        checkpoint_created (Union[Unset, datetime.datetime]):
        checkpoint_deleted (Union[Unset, bool]):
        checkpoint_id (Union[Unset, str]):
        checkpoint_name (Union[Unset, str]):
        notebook_name (Union[Unset, str]):
    """

    attribute_name: str
    attribute_type: AttributeTypeDTO
    notebook_deleted: bool
    notebook_id: str
    checkpoint_created: Union[Unset, datetime.datetime] = UNSET
    checkpoint_deleted: Union[Unset, bool] = UNSET
    checkpoint_id: Union[Unset, str] = UNSET
    checkpoint_name: Union[Unset, str] = UNSET
    notebook_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attribute_name = self.attribute_name

        attribute_type = self.attribute_type.value

        notebook_deleted = self.notebook_deleted

        notebook_id = self.notebook_id

        checkpoint_created: Union[Unset, str] = UNSET
        if not isinstance(self.checkpoint_created, Unset):
            checkpoint_created = self.checkpoint_created.isoformat()

        checkpoint_deleted = self.checkpoint_deleted

        checkpoint_id = self.checkpoint_id

        checkpoint_name = self.checkpoint_name

        notebook_name = self.notebook_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attributeName": attribute_name,
                "attributeType": attribute_type,
                "notebookDeleted": notebook_deleted,
                "notebookId": notebook_id,
            }
        )
        if checkpoint_created is not UNSET:
            field_dict["checkpointCreated"] = checkpoint_created
        if checkpoint_deleted is not UNSET:
            field_dict["checkpointDeleted"] = checkpoint_deleted
        if checkpoint_id is not UNSET:
            field_dict["checkpointId"] = checkpoint_id
        if checkpoint_name is not UNSET:
            field_dict["checkpointName"] = checkpoint_name
        if notebook_name is not UNSET:
            field_dict["notebookName"] = notebook_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        attribute_name = d.pop("attributeName")

        attribute_type = AttributeTypeDTO(d.pop("attributeType"))

        notebook_deleted = d.pop("notebookDeleted")

        notebook_id = d.pop("notebookId")

        _checkpoint_created = d.pop("checkpointCreated", UNSET)
        checkpoint_created: Union[Unset, datetime.datetime]
        if isinstance(_checkpoint_created, Unset):
            checkpoint_created = UNSET
        else:
            checkpoint_created = isoparse(_checkpoint_created)

        checkpoint_deleted = d.pop("checkpointDeleted", UNSET)

        checkpoint_id = d.pop("checkpointId", UNSET)

        checkpoint_name = d.pop("checkpointName", UNSET)

        notebook_name = d.pop("notebookName", UNSET)

        notebook_ref_attribute_dto = cls(
            attribute_name=attribute_name,
            attribute_type=attribute_type,
            notebook_deleted=notebook_deleted,
            notebook_id=notebook_id,
            checkpoint_created=checkpoint_created,
            checkpoint_deleted=checkpoint_deleted,
            checkpoint_id=checkpoint_id,
            checkpoint_name=checkpoint_name,
            notebook_name=notebook_name,
        )

        notebook_ref_attribute_dto.additional_properties = d
        return notebook_ref_attribute_dto

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
