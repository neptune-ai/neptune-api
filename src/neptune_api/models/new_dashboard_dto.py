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

from ..models.new_dashboard_dto_type import NewDashboardDTOType
from ..types import (
    UNSET,
    Unset,
)

if TYPE_CHECKING:
    from ..models.colors_config_dto import ColorsConfigDTO
    from ..models.dashboard_config_dto import DashboardConfigDTO
    from ..models.dashboard_layouts_dto import DashboardLayoutsDTO
    from ..models.table_view_params_dto import TableViewParamsDTO
    from ..models.widget_dto import WidgetDTO


T = TypeVar("T", bound="NewDashboardDTO")


@_attrs_define
class NewDashboardDTO:
    """
    Attributes:
        layouts (DashboardLayoutsDTO):
        name (str):
        type (NewDashboardDTOType):
        widgets (List['WidgetDTO']):
        auto_compare_pool (Union[Unset, int]):
        color (Union[Unset, str]):
        colors_config (Union[Unset, ColorsConfigDTO]):
        config (Union[Unset, DashboardConfigDTO]):
        experiment_short_id (Union[Unset, str]):
        icon (Union[Unset, str]):
        is_draft (Union[Unset, bool]):
        run_ids (Union[Unset, List[str]]):
        user_experiment_names (Union[Unset, List[str]]):
        version_description (Union[Unset, str]):
        version_name (Union[Unset, str]):
        view_params (Union[Unset, TableViewParamsDTO]):
    """

    layouts: "DashboardLayoutsDTO"
    name: str
    type: NewDashboardDTOType
    widgets: List["WidgetDTO"]
    auto_compare_pool: Union[Unset, int] = UNSET
    color: Union[Unset, str] = UNSET
    colors_config: Union[Unset, "ColorsConfigDTO"] = UNSET
    config: Union[Unset, "DashboardConfigDTO"] = UNSET
    experiment_short_id: Union[Unset, str] = UNSET
    icon: Union[Unset, str] = UNSET
    is_draft: Union[Unset, bool] = UNSET
    run_ids: Union[Unset, List[str]] = UNSET
    user_experiment_names: Union[Unset, List[str]] = UNSET
    version_description: Union[Unset, str] = UNSET
    version_name: Union[Unset, str] = UNSET
    view_params: Union[Unset, "TableViewParamsDTO"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        layouts = self.layouts.to_dict()

        name = self.name

        type = self.type.value

        widgets = []
        for widgets_item_data in self.widgets:
            widgets_item = widgets_item_data.to_dict()
            widgets.append(widgets_item)

        auto_compare_pool = self.auto_compare_pool

        color = self.color

        colors_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.colors_config, Unset):
            colors_config = self.colors_config.to_dict()

        config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        experiment_short_id = self.experiment_short_id

        icon = self.icon

        is_draft = self.is_draft

        run_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.run_ids, Unset):
            run_ids = self.run_ids

        user_experiment_names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.user_experiment_names, Unset):
            user_experiment_names = self.user_experiment_names

        version_description = self.version_description

        version_name = self.version_name

        view_params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.view_params, Unset):
            view_params = self.view_params.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "layouts": layouts,
                "name": name,
                "type": type,
                "widgets": widgets,
            }
        )
        if auto_compare_pool is not UNSET:
            field_dict["autoComparePool"] = auto_compare_pool
        if color is not UNSET:
            field_dict["color"] = color
        if colors_config is not UNSET:
            field_dict["colorsConfig"] = colors_config
        if config is not UNSET:
            field_dict["config"] = config
        if experiment_short_id is not UNSET:
            field_dict["experimentShortId"] = experiment_short_id
        if icon is not UNSET:
            field_dict["icon"] = icon
        if is_draft is not UNSET:
            field_dict["isDraft"] = is_draft
        if run_ids is not UNSET:
            field_dict["runIds"] = run_ids
        if user_experiment_names is not UNSET:
            field_dict["userExperimentNames"] = user_experiment_names
        if version_description is not UNSET:
            field_dict["versionDescription"] = version_description
        if version_name is not UNSET:
            field_dict["versionName"] = version_name
        if view_params is not UNSET:
            field_dict["viewParams"] = view_params

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.colors_config_dto import ColorsConfigDTO
        from ..models.dashboard_config_dto import DashboardConfigDTO
        from ..models.dashboard_layouts_dto import DashboardLayoutsDTO
        from ..models.table_view_params_dto import TableViewParamsDTO
        from ..models.widget_dto import WidgetDTO

        d = src_dict.copy()
        layouts = DashboardLayoutsDTO.from_dict(d.pop("layouts"))

        name = d.pop("name")

        type = NewDashboardDTOType(d.pop("type"))

        widgets = []
        _widgets = d.pop("widgets")
        for widgets_item_data in _widgets:
            widgets_item = WidgetDTO.from_dict(widgets_item_data)

            widgets.append(widgets_item)

        auto_compare_pool = d.pop("autoComparePool", UNSET)

        color = d.pop("color", UNSET)

        _colors_config = d.pop("colorsConfig", UNSET)
        colors_config: Union[Unset, ColorsConfigDTO]
        if isinstance(_colors_config, Unset):
            colors_config = UNSET
        else:
            colors_config = ColorsConfigDTO.from_dict(_colors_config)

        _config = d.pop("config", UNSET)
        config: Union[Unset, DashboardConfigDTO]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = DashboardConfigDTO.from_dict(_config)

        experiment_short_id = d.pop("experimentShortId", UNSET)

        icon = d.pop("icon", UNSET)

        is_draft = d.pop("isDraft", UNSET)

        run_ids = cast(List[str], d.pop("runIds", UNSET))

        user_experiment_names = cast(List[str], d.pop("userExperimentNames", UNSET))

        version_description = d.pop("versionDescription", UNSET)

        version_name = d.pop("versionName", UNSET)

        _view_params = d.pop("viewParams", UNSET)
        view_params: Union[Unset, TableViewParamsDTO]
        if isinstance(_view_params, Unset):
            view_params = UNSET
        else:
            view_params = TableViewParamsDTO.from_dict(_view_params)

        new_dashboard_dto = cls(
            layouts=layouts,
            name=name,
            type=type,
            widgets=widgets,
            auto_compare_pool=auto_compare_pool,
            color=color,
            colors_config=colors_config,
            config=config,
            experiment_short_id=experiment_short_id,
            icon=icon,
            is_draft=is_draft,
            run_ids=run_ids,
            user_experiment_names=user_experiment_names,
            version_description=version_description,
            version_name=version_name,
            view_params=view_params,
        )

        new_dashboard_dto.additional_properties = d
        return new_dashboard_dto

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
