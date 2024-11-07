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

from ..models.update_dashboard_dto_type import UpdateDashboardDTOType
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


T = TypeVar("T", bound="UpdateDashboardDTO")


@_attrs_define
class UpdateDashboardDTO:
    """
    Attributes:
        layouts (DashboardLayoutsDTO):
        name (str):
        type (UpdateDashboardDTOType):
        widgets (List['WidgetDTO']):
        auto_compare_pool (Union[Unset, int]):
        color (Union[Unset, str]):
        colors_config (Union[Unset, ColorsConfigDTO]):
        config (Union[Unset, DashboardConfigDTO]):
        icon (Union[Unset, str]):
        run_ids (Union[Unset, List[str]]):
        user_experiment_names (Union[Unset, List[str]]):
        view_params (Union[Unset, TableViewParamsDTO]):
    """

    layouts: "DashboardLayoutsDTO"
    name: str
    type: UpdateDashboardDTOType
    widgets: List["WidgetDTO"]
    auto_compare_pool: Union[Unset, int] = UNSET
    color: Union[Unset, str] = UNSET
    colors_config: Union[Unset, "ColorsConfigDTO"] = UNSET
    config: Union[Unset, "DashboardConfigDTO"] = UNSET
    icon: Union[Unset, str] = UNSET
    run_ids: Union[Unset, List[str]] = UNSET
    user_experiment_names: Union[Unset, List[str]] = UNSET
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

        icon = self.icon

        run_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.run_ids, Unset):
            run_ids = self.run_ids

        user_experiment_names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.user_experiment_names, Unset):
            user_experiment_names = self.user_experiment_names

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
        if icon is not UNSET:
            field_dict["icon"] = icon
        if run_ids is not UNSET:
            field_dict["runIds"] = run_ids
        if user_experiment_names is not UNSET:
            field_dict["userExperimentNames"] = user_experiment_names
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

        type = UpdateDashboardDTOType(d.pop("type"))

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

        icon = d.pop("icon", UNSET)

        run_ids = cast(List[str], d.pop("runIds", UNSET))

        user_experiment_names = cast(List[str], d.pop("userExperimentNames", UNSET))

        _view_params = d.pop("viewParams", UNSET)
        view_params: Union[Unset, TableViewParamsDTO]
        if isinstance(_view_params, Unset):
            view_params = UNSET
        else:
            view_params = TableViewParamsDTO.from_dict(_view_params)

        update_dashboard_dto = cls(
            layouts=layouts,
            name=name,
            type=type,
            widgets=widgets,
            auto_compare_pool=auto_compare_pool,
            color=color,
            colors_config=colors_config,
            config=config,
            icon=icon,
            run_ids=run_ids,
            user_experiment_names=user_experiment_names,
            view_params=view_params,
        )

        update_dashboard_dto.additional_properties = d
        return update_dashboard_dto

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
