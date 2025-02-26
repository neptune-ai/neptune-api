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
    from ..models.single_time_series_view_bucket import SingleTimeSeriesViewBucket


T = TypeVar("T", bound="Point")


@_attrs_define
class Point:
    """
    Attributes:
        interpolation (bool):
        x (float):
        bucket (Union[Unset, SingleTimeSeriesViewBucket]):
        y (Union[Unset, float]):
    """

    interpolation: bool
    x: float
    bucket: Union[Unset, "SingleTimeSeriesViewBucket"] = UNSET
    y: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        interpolation = self.interpolation

        x = self.x

        bucket: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.bucket, Unset):
            bucket = self.bucket.to_dict()

        y = self.y

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "interpolation": interpolation,
                "x": x,
            }
        )
        if bucket is not UNSET:
            field_dict["bucket"] = bucket
        if y is not UNSET:
            field_dict["y"] = y

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.single_time_series_view_bucket import SingleTimeSeriesViewBucket

        d = src_dict.copy()
        interpolation = d.pop("interpolation")

        x = d.pop("x")

        _bucket = d.pop("bucket", UNSET)
        bucket: Union[Unset, SingleTimeSeriesViewBucket]
        if isinstance(_bucket, Unset):
            bucket = UNSET
        else:
            bucket = SingleTimeSeriesViewBucket.from_dict(_bucket)

        y = d.pop("y", UNSET)

        point = cls(
            interpolation=interpolation,
            x=x,
            bucket=bucket,
            y=y,
        )

        point.additional_properties = d
        return point

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
