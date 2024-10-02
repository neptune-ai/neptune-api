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
    from ..models.point import Point
    from ..models.time_series import TimeSeries


T = TypeVar("T", bound="SingleTimeSeriesView")


@_attrs_define
class SingleTimeSeriesView:
    """
    Attributes:
        time_series (TimeSeries):
        values (List['Point']):
    """

    time_series: "TimeSeries"
    values: List["Point"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        time_series = self.time_series.to_dict()

        values = []
        for values_item_data in self.values:
            values_item = values_item_data.to_dict()
            values.append(values_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timeSeries": time_series,
                "values": values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.point import Point
        from ..models.time_series import TimeSeries

        d = src_dict.copy()
        time_series = TimeSeries.from_dict(d.pop("timeSeries"))

        values = []
        _values = d.pop("values")
        for values_item_data in _values:
            values_item = Point.from_dict(values_item_data)

            values.append(values_item)

        single_time_series_view = cls(
            time_series=time_series,
            values=values,
        )

        single_time_series_view.additional_properties = d
        return single_time_series_view

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
