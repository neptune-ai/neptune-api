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

        metrics = []
        _metrics = d.pop("metrics", UNSET)
        for metrics_item_data in _metrics or []:
            metrics_item = CustomMetric.from_dict(metrics_item_data)

            metrics.append(metrics_item)

        series = []
        _series = d.pop("series", UNSET)
        for series_item_data in _series or []:
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
