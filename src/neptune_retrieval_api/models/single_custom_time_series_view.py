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


T = TypeVar("T", bound="SingleCustomTimeSeriesView")


@_attrs_define
class SingleCustomTimeSeriesView:
    """
    Attributes:
        custom_id (str):
        values (List['Point']):
    """

    custom_id: str
    values: List["Point"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        custom_id = self.custom_id

        values = []
        for values_item_data in self.values:
            values_item = values_item_data.to_dict()
            values.append(values_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "customId": custom_id,
                "values": values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.point import Point

        d = src_dict.copy()
        custom_id = d.pop("customId")

        values = []
        _values = d.pop("values")
        for values_item_data in _values:
            values_item = Point.from_dict(values_item_data)

            values.append(values_item)

        single_custom_time_series_view = cls(
            custom_id=custom_id,
            values=values,
        )

        single_custom_time_series_view.additional_properties = d
        return single_custom_time_series_view

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
