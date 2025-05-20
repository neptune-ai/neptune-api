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

from ..models.attribute_type_dto import AttributeTypeDTO
from ..types import (
    UNSET,
    Unset,
)

if TYPE_CHECKING:
    from ..models.file_ref_dto import FileRefDTO


T = TypeVar("T", bound="FileRefSeriesAttributeDTO")


@_attrs_define
class FileRefSeriesAttributeDTO:
    """
    Attributes:
        attribute_name (str):
        attribute_type (AttributeTypeDTO):
        last (Union[Unset, FileRefDTO]):
        last_step (Union[Unset, float]):
    """

    attribute_name: str
    attribute_type: AttributeTypeDTO
    last: Union[Unset, "FileRefDTO"] = UNSET
    last_step: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attribute_name = self.attribute_name

        attribute_type = self.attribute_type.value

        last: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.last, Unset):
            last = self.last.to_dict()

        last_step = self.last_step

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attributeName": attribute_name,
                "attributeType": attribute_type,
            }
        )
        if last is not UNSET:
            field_dict["last"] = last
        if last_step is not UNSET:
            field_dict["lastStep"] = last_step

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.file_ref_dto import FileRefDTO

        d = src_dict.copy()
        attribute_name = d.pop("attributeName")

        attribute_type = AttributeTypeDTO(d.pop("attributeType"))

        _last = d.pop("last", UNSET)
        last: Union[Unset, FileRefDTO]
        if isinstance(_last, Unset):
            last = UNSET
        else:
            last = FileRefDTO.from_dict(_last)

        last_step = d.pop("lastStep", UNSET)

        file_ref_series_attribute_dto = cls(
            attribute_name=attribute_name,
            attribute_type=attribute_type,
            last=last,
            last_step=last_step,
        )

        file_ref_series_attribute_dto.additional_properties = d
        return file_ref_series_attribute_dto

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
