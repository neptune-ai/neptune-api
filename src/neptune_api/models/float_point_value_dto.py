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

T = TypeVar("T", bound="FloatPointValueDTO")


@_attrs_define
class FloatPointValueDTO:
    """
    Attributes:
        completion_ratio (float):
        is_preview (bool):
        step (float):
        timestamp_millis (int):
        value (float):
    """

    completion_ratio: float
    is_preview: bool
    step: float
    timestamp_millis: int
    value: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        completion_ratio = self.completion_ratio

        is_preview = self.is_preview

        step = self.step

        timestamp_millis = self.timestamp_millis

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "completionRatio": completion_ratio,
                "isPreview": is_preview,
                "step": step,
                "timestampMillis": timestamp_millis,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        completion_ratio = d.pop("completionRatio")

        is_preview = d.pop("isPreview")

        step = d.pop("step")

        timestamp_millis = d.pop("timestampMillis")

        value = d.pop("value")

        float_point_value_dto = cls(
            completion_ratio=completion_ratio,
            is_preview=is_preview,
            step=step,
            timestamp_millis=timestamp_millis,
            value=value,
        )

        float_point_value_dto.additional_properties = d
        return float_point_value_dto

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
