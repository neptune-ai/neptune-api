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
    from ..models.project_chart_filters_dto import ProjectChartFiltersDTO
    from ..models.project_chart_metric_dto import ProjectChartMetricDTO


T = TypeVar("T", bound="ProjectChartDTO")


@_attrs_define
class ProjectChartDTO:
    """
    Attributes:
        filters (ProjectChartFiltersDTO):
        id (str): Chart id
        metrics (List['ProjectChartMetricDTO']): Chart metrics
        name (str): Chart name
    """

    filters: "ProjectChartFiltersDTO"
    id: str
    metrics: List["ProjectChartMetricDTO"]
    name: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        filters = self.filters.to_dict()

        id = self.id

        metrics = []
        for metrics_item_data in self.metrics:
            metrics_item = metrics_item_data.to_dict()
            metrics.append(metrics_item)

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filters": filters,
                "id": id,
                "metrics": metrics,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.project_chart_filters_dto import ProjectChartFiltersDTO
        from ..models.project_chart_metric_dto import ProjectChartMetricDTO

        d = src_dict.copy()
        filters = ProjectChartFiltersDTO.from_dict(d.pop("filters"))

        id = d.pop("id")

        metrics = []
        _metrics = d.pop("metrics")
        for metrics_item_data in _metrics:
            metrics_item = ProjectChartMetricDTO.from_dict(metrics_item_data)

            metrics.append(metrics_item)

        name = d.pop("name")

        project_chart_dto = cls(
            filters=filters,
            id=id,
            metrics=metrics,
            name=name,
        )

        project_chart_dto.additional_properties = d
        return project_chart_dto

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
