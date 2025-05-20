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
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="SeriesViewPointDTO")


@_attrs_define
class SeriesViewPointDTO:
    """
    Attributes:
        downsampled (bool):
        first_point_index (int):
        last_point_index (int):
        max_y (float):
        min_y (float):
        timestamp (datetime.datetime):
        x (float):
        y (float):
    """

    downsampled: bool
    first_point_index: int
    last_point_index: int
    max_y: float
    min_y: float
    timestamp: datetime.datetime
    x: float
    y: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        downsampled = self.downsampled

        first_point_index = self.first_point_index

        last_point_index = self.last_point_index

        max_y = self.max_y

        min_y = self.min_y

        timestamp = self.timestamp.isoformat()

        x = self.x

        y = self.y

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "downsampled": downsampled,
                "firstPointIndex": first_point_index,
                "lastPointIndex": last_point_index,
                "maxY": max_y,
                "minY": min_y,
                "timestamp": timestamp,
                "x": x,
                "y": y,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        downsampled = d.pop("downsampled")

        first_point_index = d.pop("firstPointIndex")

        last_point_index = d.pop("lastPointIndex")

        max_y = d.pop("maxY")

        min_y = d.pop("minY")

        timestamp = isoparse(d.pop("timestamp"))

        x = d.pop("x")

        y = d.pop("y")

        series_view_point_dto = cls(
            downsampled=downsampled,
            first_point_index=first_point_index,
            last_point_index=last_point_index,
            max_y=max_y,
            min_y=min_y,
            timestamp=timestamp,
            x=x,
            y=y,
        )

        series_view_point_dto.additional_properties = d
        return series_view_point_dto

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
