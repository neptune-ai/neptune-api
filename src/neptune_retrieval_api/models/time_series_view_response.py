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
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.single_custom_time_series_view import SingleCustomTimeSeriesView
    from ..models.single_time_series_view import SingleTimeSeriesView


T = TypeVar("T", bound="TimeSeriesViewResponse")


@_attrs_define
class TimeSeriesViewResponse:
    """
    Attributes:
        custom_series (List['SingleCustomTimeSeriesView']):
        elements (List['SingleTimeSeriesView']):
    """

    custom_series: List["SingleCustomTimeSeriesView"]
    elements: List["SingleTimeSeriesView"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        custom_series = []
        for custom_series_item_data in self.custom_series:
            custom_series_item = custom_series_item_data.to_dict()
            custom_series.append(custom_series_item)

        elements = []
        for elements_item_data in self.elements:
            elements_item = elements_item_data.to_dict()
            elements.append(elements_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "customSeries": custom_series,
                "elements": elements,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.single_custom_time_series_view import SingleCustomTimeSeriesView
        from ..models.single_time_series_view import SingleTimeSeriesView

        d = src_dict.copy()
        custom_series = []
        _custom_series = d.pop("customSeries")
        for custom_series_item_data in _custom_series:
            custom_series_item = SingleCustomTimeSeriesView.from_dict(custom_series_item_data)

            custom_series.append(custom_series_item)

        elements = []
        _elements = d.pop("elements")
        for elements_item_data in _elements:
            elements_item = SingleTimeSeriesView.from_dict(elements_item_data)

            elements.append(elements_item)

        time_series_view_response = cls(
            custom_series=custom_series,
            elements=elements,
        )

        time_series_view_response.additional_properties = d
        return time_series_view_response

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
