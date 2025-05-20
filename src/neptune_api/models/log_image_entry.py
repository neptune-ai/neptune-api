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
    from ..models.image import Image


T = TypeVar("T", bound="LogImageEntry")


@_attrs_define
class LogImageEntry:
    """
    Attributes:
        timestamp_milliseconds (int):
        value (Union[Unset, Image]):
        step (Union[Unset, float]):
    """

    timestamp_milliseconds: int
    value: Union[Unset, "Image"] = UNSET
    step: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timestamp_milliseconds = self.timestamp_milliseconds

        value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        step = self.step

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestampMilliseconds": timestamp_milliseconds,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value
        if step is not UNSET:
            field_dict["step"] = step

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.image import Image

        d = src_dict.copy()
        timestamp_milliseconds = d.pop("timestampMilliseconds")

        _value = d.pop("value", UNSET)
        value: Union[Unset, Image]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = Image.from_dict(_value)

        step = d.pop("step", UNSET)

        log_image_entry = cls(
            timestamp_milliseconds=timestamp_milliseconds,
            value=value,
            step=step,
        )

        log_image_entry.additional_properties = d
        return log_image_entry

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
