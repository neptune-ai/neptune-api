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
    from ..models.custom_metric import CustomMetric
    from ..models.time_series import TimeSeries
    from ..models.view import View
    from ..models.x_axis import XAxis


T = TypeVar("T", bound="TimeSeriesViewRequest")


@_attrs_define
class TimeSeriesViewRequest:
    """
    Attributes:
        view (View):
        xaxis (XAxis):
        metrics (Union[Unset, List['CustomMetric']]):
        series (Union[Unset, List['TimeSeries']]): Deprecated, use metrics instead.
    """

    view: "View"
    xaxis: "XAxis"
    metrics: Union[Unset, List["CustomMetric"]] = UNSET
    series: Union[Unset, List["TimeSeries"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        view = self.view.to_dict()

        xaxis = self.xaxis.to_dict()

        metrics: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = []
            for metrics_item_data in self.metrics:
                metrics_item = metrics_item_data.to_dict()
                metrics.append(metrics_item)

        series: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.series, Unset):
            series = []
            for series_item_data in self.series:
                series_item = series_item_data.to_dict()
                series.append(series_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "view": view,
                "xaxis": xaxis,
            }
        )
        if metrics is not UNSET:
            field_dict["metrics"] = metrics
        if series is not UNSET:
            field_dict["series"] = series

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.custom_metric import CustomMetric
        from ..models.time_series import TimeSeries
        from ..models.view import View
        from ..models.x_axis import XAxis

        d = src_dict.copy()
        view = View.from_dict(d.pop("view"))

        xaxis = XAxis.from_dict(d.pop("xaxis"))

        metrics: Union[Unset, List[CustomMetric]] = UNSET
        _metrics = d.pop("metrics", UNSET)
        if not isinstance(_metrics, Unset):
            metrics = []
            for metrics_item_data in _metrics:
                metrics_item = CustomMetric.from_dict(metrics_item_data)

                metrics.append(metrics_item)

        series: Union[Unset, List[TimeSeries]] = UNSET
        _series = d.pop("series", UNSET)
        if not isinstance(_series, Unset):
            series = []
            for series_item_data in _series:
                series_item = TimeSeries.from_dict(series_item_data)

                series.append(series_item)

        time_series_view_request = cls(
            view=view,
            xaxis=xaxis,
            metrics=metrics,
            series=series,
        )

        time_series_view_request.additional_properties = d
        return time_series_view_request

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
