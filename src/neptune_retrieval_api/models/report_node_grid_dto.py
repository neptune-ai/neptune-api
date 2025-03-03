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
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import (
    UNSET,
    Unset,
)

if TYPE_CHECKING:
    from ..models.colors_config_dto import ColorsConfigDTO
    from ..models.dashboard_config_dto import DashboardConfigDTO
    from ..models.run_group_dto import RunGroupDTO
    from ..models.widget_dto import WidgetDTO
    from ..models.widget_layout_dto import WidgetLayoutDTO


T = TypeVar("T", bound="ReportNodeGridDTO")


@_attrs_define
class ReportNodeGridDTO:
    """
    Attributes:
        aggregate_by_group (bool):
        charts_config (DashboardConfigDTO):
        colors_config (ColorsConfigDTO):
        inherit_run_color_from_group (bool):
        open_run_groups (List[str]):
        run_groups (List['RunGroupDTO']):
        runs_lineage (bool):
        selected_run_groups (List[str]):
        widget_layouts (List['WidgetLayoutDTO']):
        widgets (List['WidgetDTO']):
        preset_colors (Union[Unset, List[str]]):
    """

    aggregate_by_group: bool
    charts_config: "DashboardConfigDTO"
    colors_config: "ColorsConfigDTO"
    inherit_run_color_from_group: bool
    open_run_groups: List[str]
    run_groups: List["RunGroupDTO"]
    runs_lineage: bool
    selected_run_groups: List[str]
    widget_layouts: List["WidgetLayoutDTO"]
    widgets: List["WidgetDTO"]
    preset_colors: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        aggregate_by_group = self.aggregate_by_group

        charts_config = self.charts_config.to_dict()

        colors_config = self.colors_config.to_dict()

        inherit_run_color_from_group = self.inherit_run_color_from_group

        open_run_groups = self.open_run_groups

        run_groups = []
        for run_groups_item_data in self.run_groups:
            run_groups_item = run_groups_item_data.to_dict()
            run_groups.append(run_groups_item)

        runs_lineage = self.runs_lineage

        selected_run_groups = self.selected_run_groups

        widget_layouts = []
        for widget_layouts_item_data in self.widget_layouts:
            widget_layouts_item = widget_layouts_item_data.to_dict()
            widget_layouts.append(widget_layouts_item)

        widgets = []
        for widgets_item_data in self.widgets:
            widgets_item = widgets_item_data.to_dict()
            widgets.append(widgets_item)

        preset_colors: Union[Unset, List[str]] = UNSET
        if not isinstance(self.preset_colors, Unset):
            preset_colors = self.preset_colors

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "aggregateByGroup": aggregate_by_group,
                "chartsConfig": charts_config,
                "colorsConfig": colors_config,
                "inheritRunColorFromGroup": inherit_run_color_from_group,
                "openRunGroups": open_run_groups,
                "runGroups": run_groups,
                "runsLineage": runs_lineage,
                "selectedRunGroups": selected_run_groups,
                "widgetLayouts": widget_layouts,
                "widgets": widgets,
            }
        )
        if preset_colors is not UNSET:
            field_dict["presetColors"] = preset_colors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.colors_config_dto import ColorsConfigDTO
        from ..models.dashboard_config_dto import DashboardConfigDTO
        from ..models.run_group_dto import RunGroupDTO
        from ..models.widget_dto import WidgetDTO
        from ..models.widget_layout_dto import WidgetLayoutDTO

        d = src_dict.copy()
        aggregate_by_group = d.pop("aggregateByGroup")

        charts_config = DashboardConfigDTO.from_dict(d.pop("chartsConfig"))

        colors_config = ColorsConfigDTO.from_dict(d.pop("colorsConfig"))

        inherit_run_color_from_group = d.pop("inheritRunColorFromGroup")

        open_run_groups = cast(List[str], d.pop("openRunGroups"))

        run_groups = []
        _run_groups = d.pop("runGroups")
        for run_groups_item_data in _run_groups:
            run_groups_item = RunGroupDTO.from_dict(run_groups_item_data)

            run_groups.append(run_groups_item)

        runs_lineage = d.pop("runsLineage")

        selected_run_groups = cast(List[str], d.pop("selectedRunGroups"))

        widget_layouts = []
        _widget_layouts = d.pop("widgetLayouts")
        for widget_layouts_item_data in _widget_layouts:
            widget_layouts_item = WidgetLayoutDTO.from_dict(widget_layouts_item_data)

            widget_layouts.append(widget_layouts_item)

        widgets = []
        _widgets = d.pop("widgets")
        for widgets_item_data in _widgets:
            widgets_item = WidgetDTO.from_dict(widgets_item_data)

            widgets.append(widgets_item)

        preset_colors = cast(List[str], d.pop("presetColors", UNSET))

        report_node_grid_dto = cls(
            aggregate_by_group=aggregate_by_group,
            charts_config=charts_config,
            colors_config=colors_config,
            inherit_run_color_from_group=inherit_run_color_from_group,
            open_run_groups=open_run_groups,
            run_groups=run_groups,
            runs_lineage=runs_lineage,
            selected_run_groups=selected_run_groups,
            widget_layouts=widget_layouts,
            widgets=widgets,
            preset_colors=preset_colors,
        )

        report_node_grid_dto.additional_properties = d
        return report_node_grid_dto

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
