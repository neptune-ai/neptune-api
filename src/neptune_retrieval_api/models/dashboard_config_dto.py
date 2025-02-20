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

from ..models.dashboard_config_dto_show_metric_by import DashboardConfigDTOShowMetricBy
from ..types import (
    UNSET,
    Unset,
)

if TYPE_CHECKING:
    from ..models.attribute_definition_dto import AttributeDefinitionDTO
    from ..models.open_range_dto import OpenRangeDTO


T = TypeVar("T", bound="DashboardConfigDTO")


@_attrs_define
class DashboardConfigDTO:
    """
    Attributes:
        metrics_steps_range (Union[Unset, OpenRangeDTO]):
        show_metric_by (Union[Unset, DashboardConfigDTOShowMetricBy]):
        smoothing (Union[Unset, int]):
        xaxis_metric (Union[Unset, AttributeDefinitionDTO]):
        xaxis_mode (Union[Unset, str]):
        xaxis_range (Union[Unset, OpenRangeDTO]):
        xaxis_scale (Union[Unset, str]):
        yaxis_scale (Union[Unset, str]):
    """

    metrics_steps_range: Union[Unset, "OpenRangeDTO"] = UNSET
    show_metric_by: Union[Unset, DashboardConfigDTOShowMetricBy] = UNSET
    smoothing: Union[Unset, int] = UNSET
    xaxis_metric: Union[Unset, "AttributeDefinitionDTO"] = UNSET
    xaxis_mode: Union[Unset, str] = UNSET
    xaxis_range: Union[Unset, "OpenRangeDTO"] = UNSET
    xaxis_scale: Union[Unset, str] = UNSET
    yaxis_scale: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        metrics_steps_range: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metrics_steps_range, Unset):
            metrics_steps_range = self.metrics_steps_range.to_dict()

        show_metric_by: Union[Unset, str] = UNSET
        if not isinstance(self.show_metric_by, Unset):
            show_metric_by = self.show_metric_by.value

        smoothing = self.smoothing

        xaxis_metric: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.xaxis_metric, Unset):
            xaxis_metric = self.xaxis_metric.to_dict()

        xaxis_mode = self.xaxis_mode

        xaxis_range: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.xaxis_range, Unset):
            xaxis_range = self.xaxis_range.to_dict()

        xaxis_scale = self.xaxis_scale

        yaxis_scale = self.yaxis_scale

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metrics_steps_range is not UNSET:
            field_dict["metricsStepsRange"] = metrics_steps_range
        if show_metric_by is not UNSET:
            field_dict["showMetricBy"] = show_metric_by
        if smoothing is not UNSET:
            field_dict["smoothing"] = smoothing
        if xaxis_metric is not UNSET:
            field_dict["xaxisMetric"] = xaxis_metric
        if xaxis_mode is not UNSET:
            field_dict["xaxisMode"] = xaxis_mode
        if xaxis_range is not UNSET:
            field_dict["xaxisRange"] = xaxis_range
        if xaxis_scale is not UNSET:
            field_dict["xaxisScale"] = xaxis_scale
        if yaxis_scale is not UNSET:
            field_dict["yaxisScale"] = yaxis_scale

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.attribute_definition_dto import AttributeDefinitionDTO
        from ..models.open_range_dto import OpenRangeDTO

        d = src_dict.copy()
        _metrics_steps_range = d.pop("metricsStepsRange", UNSET)
        metrics_steps_range: Union[Unset, OpenRangeDTO]
        if isinstance(_metrics_steps_range, Unset):
            metrics_steps_range = UNSET
        else:
            metrics_steps_range = OpenRangeDTO.from_dict(_metrics_steps_range)

        _show_metric_by = d.pop("showMetricBy", UNSET)
        show_metric_by: Union[Unset, DashboardConfigDTOShowMetricBy]
        if isinstance(_show_metric_by, Unset):
            show_metric_by = UNSET
        else:
            show_metric_by = DashboardConfigDTOShowMetricBy(_show_metric_by)

        smoothing = d.pop("smoothing", UNSET)

        _xaxis_metric = d.pop("xaxisMetric", UNSET)
        xaxis_metric: Union[Unset, AttributeDefinitionDTO]
        if isinstance(_xaxis_metric, Unset):
            xaxis_metric = UNSET
        else:
            xaxis_metric = AttributeDefinitionDTO.from_dict(_xaxis_metric)

        xaxis_mode = d.pop("xaxisMode", UNSET)

        _xaxis_range = d.pop("xaxisRange", UNSET)
        xaxis_range: Union[Unset, OpenRangeDTO]
        if isinstance(_xaxis_range, Unset):
            xaxis_range = UNSET
        else:
            xaxis_range = OpenRangeDTO.from_dict(_xaxis_range)

        xaxis_scale = d.pop("xaxisScale", UNSET)

        yaxis_scale = d.pop("yaxisScale", UNSET)

        dashboard_config_dto = cls(
            metrics_steps_range=metrics_steps_range,
            show_metric_by=show_metric_by,
            smoothing=smoothing,
            xaxis_metric=xaxis_metric,
            xaxis_mode=xaxis_mode,
            xaxis_range=xaxis_range,
            xaxis_scale=xaxis_scale,
            yaxis_scale=yaxis_scale,
        )

        dashboard_config_dto.additional_properties = d
        return dashboard_config_dto

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
