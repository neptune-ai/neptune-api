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
    from ..models.series_value_object_dto import SeriesValueObjectDTO


T = TypeVar("T", bound="SeriesPointDTO")


@_attrs_define
class SeriesPointDTO:
    """
    Attributes:
        completion_ratio (float):
        is_preview (bool):
        step (float):
        timestamp_millis (int):
        object_ (Union[Unset, SeriesValueObjectDTO]):
        value (Union[Unset, str]):
    """

    completion_ratio: float
    is_preview: bool
    step: float
    timestamp_millis: int
    object_: Union[Unset, "SeriesValueObjectDTO"] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        completion_ratio = self.completion_ratio

        is_preview = self.is_preview

        step = self.step

        timestamp_millis = self.timestamp_millis

        object_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.to_dict()

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "completionRatio": completion_ratio,
                "isPreview": is_preview,
                "step": step,
                "timestampMillis": timestamp_millis,
            }
        )
        if object_ is not UNSET:
            field_dict["object"] = object_
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.series_value_object_dto import SeriesValueObjectDTO

        d = src_dict.copy()
        completion_ratio = d.pop("completionRatio")

        is_preview = d.pop("isPreview")

        step = d.pop("step")

        timestamp_millis = d.pop("timestampMillis")

        _object_ = d.pop("object", UNSET)
        object_: Union[Unset, SeriesValueObjectDTO]
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = SeriesValueObjectDTO.from_dict(_object_)

        value = d.pop("value", UNSET)

        series_point_dto = cls(
            completion_ratio=completion_ratio,
            is_preview=is_preview,
            step=step,
            timestamp_millis=timestamp_millis,
            object_=object_,
            value=value,
        )

        series_point_dto.additional_properties = d
        return series_point_dto

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
