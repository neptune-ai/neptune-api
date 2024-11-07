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
    from ..models.attribute_definition_dto import AttributeDefinitionDTO
    from ..models.open_range_dto import OpenRangeDTO


T = TypeVar("T", bound="DashboardConfigDTO")


@_attrs_define
class DashboardConfigDTO:
    """
    Attributes:
        metrics_steps_range (Union[Unset, OpenRangeDTO]):
        smoothing (Union[Unset, int]):
        xaxis_metric (Union[Unset, AttributeDefinitionDTO]):
        xaxis_mode (Union[Unset, str]):
        xaxis_scale (Union[Unset, str]):
        yaxis_scale (Union[Unset, str]):
    """

    metrics_steps_range: Union[Unset, "OpenRangeDTO"] = UNSET
    smoothing: Union[Unset, int] = UNSET
    xaxis_metric: Union[Unset, "AttributeDefinitionDTO"] = UNSET
    xaxis_mode: Union[Unset, str] = UNSET
    xaxis_scale: Union[Unset, str] = UNSET
    yaxis_scale: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        metrics_steps_range: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metrics_steps_range, Unset):
            metrics_steps_range = self.metrics_steps_range.to_dict()

        smoothing = self.smoothing

        xaxis_metric: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.xaxis_metric, Unset):
            xaxis_metric = self.xaxis_metric.to_dict()

        xaxis_mode = self.xaxis_mode

        xaxis_scale = self.xaxis_scale

        yaxis_scale = self.yaxis_scale

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metrics_steps_range is not UNSET:
            field_dict["metricsStepsRange"] = metrics_steps_range
        if smoothing is not UNSET:
            field_dict["smoothing"] = smoothing
        if xaxis_metric is not UNSET:
            field_dict["xaxisMetric"] = xaxis_metric
        if xaxis_mode is not UNSET:
            field_dict["xaxisMode"] = xaxis_mode
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

        smoothing = d.pop("smoothing", UNSET)

        _xaxis_metric = d.pop("xaxisMetric", UNSET)
        xaxis_metric: Union[Unset, AttributeDefinitionDTO]
        if isinstance(_xaxis_metric, Unset):
            xaxis_metric = UNSET
        else:
            xaxis_metric = AttributeDefinitionDTO.from_dict(_xaxis_metric)

        xaxis_mode = d.pop("xaxisMode", UNSET)

        xaxis_scale = d.pop("xaxisScale", UNSET)

        yaxis_scale = d.pop("yaxisScale", UNSET)

        dashboard_config_dto = cls(
            metrics_steps_range=metrics_steps_range,
            smoothing=smoothing,
            xaxis_metric=xaxis_metric,
            xaxis_mode=xaxis_mode,
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
