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
from dateutil.parser import isoparse

from ..models.dashboard_dto_type import DashboardDTOType
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


T = TypeVar("T", bound="DashboardDTO")


@_attrs_define
class DashboardDTO:
    """
    Attributes:
        draft (bool):
        id (str):
        layouts (DashboardLayoutsDTO):
        name (str):
        type (DashboardDTOType):
        version_branch (str):
        widgets (List['WidgetDTO']):
        auto_compare_pool (Union[Unset, int]):
        color (Union[Unset, str]):
        colors_config (Union[Unset, ColorsConfigDTO]):
        config (Union[Unset, DashboardConfigDTO]):
        created_time (Union[Unset, datetime.datetime]):
        experiment_short_id (Union[Unset, str]):
        icon (Union[Unset, str]):
        last_updated_time (Union[Unset, datetime.datetime]):
        owner (Union[Unset, str]):
        run_ids (Union[Unset, List[str]]):
        user_experiment_names (Union[Unset, List[str]]):
        version_description (Union[Unset, str]):
        version_name (Union[Unset, str]):
        view_params (Union[Unset, TableViewParamsDTO]):
    """

    draft: bool
    id: str
    layouts: "DashboardLayoutsDTO"
    name: str
    type: DashboardDTOType
    version_branch: str
    widgets: List["WidgetDTO"]
    auto_compare_pool: Union[Unset, int] = UNSET
    color: Union[Unset, str] = UNSET
    colors_config: Union[Unset, "ColorsConfigDTO"] = UNSET
    config: Union[Unset, "DashboardConfigDTO"] = UNSET
    created_time: Union[Unset, datetime.datetime] = UNSET
    experiment_short_id: Union[Unset, str] = UNSET
    icon: Union[Unset, str] = UNSET
    last_updated_time: Union[Unset, datetime.datetime] = UNSET
    owner: Union[Unset, str] = UNSET
    run_ids: Union[Unset, List[str]] = UNSET
    user_experiment_names: Union[Unset, List[str]] = UNSET
    version_description: Union[Unset, str] = UNSET
    version_name: Union[Unset, str] = UNSET
    view_params: Union[Unset, "TableViewParamsDTO"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        draft = self.draft

        id = self.id

        layouts = self.layouts.to_dict()

        name = self.name

        type = self.type.value

        version_branch = self.version_branch

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

        created_time: Union[Unset, str] = UNSET
        if not isinstance(self.created_time, Unset):
            created_time = self.created_time.isoformat()

        experiment_short_id = self.experiment_short_id

        icon = self.icon

        last_updated_time: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated_time, Unset):
            last_updated_time = self.last_updated_time.isoformat()

        owner = self.owner

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
                "draft": draft,
                "id": id,
                "layouts": layouts,
                "name": name,
                "type": type,
                "versionBranch": version_branch,
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
        if created_time is not UNSET:
            field_dict["createdTime"] = created_time
        if experiment_short_id is not UNSET:
            field_dict["experimentShortId"] = experiment_short_id
        if icon is not UNSET:
            field_dict["icon"] = icon
        if last_updated_time is not UNSET:
            field_dict["lastUpdatedTime"] = last_updated_time
        if owner is not UNSET:
            field_dict["owner"] = owner
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
        draft = d.pop("draft")

        id = d.pop("id")

        layouts = DashboardLayoutsDTO.from_dict(d.pop("layouts"))

        name = d.pop("name")

        type = DashboardDTOType(d.pop("type"))

        version_branch = d.pop("versionBranch")

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

        _created_time = d.pop("createdTime", UNSET)
        created_time: Union[Unset, datetime.datetime]
        if isinstance(_created_time, Unset):
            created_time = UNSET
        else:
            created_time = isoparse(_created_time)

        experiment_short_id = d.pop("experimentShortId", UNSET)

        icon = d.pop("icon", UNSET)

        _last_updated_time = d.pop("lastUpdatedTime", UNSET)
        last_updated_time: Union[Unset, datetime.datetime]
        if isinstance(_last_updated_time, Unset):
            last_updated_time = UNSET
        else:
            last_updated_time = isoparse(_last_updated_time)

        owner = d.pop("owner", UNSET)

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

        dashboard_dto = cls(
            draft=draft,
            id=id,
            layouts=layouts,
            name=name,
            type=type,
            version_branch=version_branch,
            widgets=widgets,
            auto_compare_pool=auto_compare_pool,
            color=color,
            colors_config=colors_config,
            config=config,
            created_time=created_time,
            experiment_short_id=experiment_short_id,
            icon=icon,
            last_updated_time=last_updated_time,
            owner=owner,
            run_ids=run_ids,
            user_experiment_names=user_experiment_names,
            version_description=version_description,
            version_name=version_name,
            view_params=view_params,
        )

        dashboard_dto.additional_properties = d
        return dashboard_dto

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
