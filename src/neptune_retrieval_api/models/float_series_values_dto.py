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
    from ..models.float_point_value_dto import FloatPointValueDTO


T = TypeVar("T", bound="FloatSeriesValuesDTO")


@_attrs_define
class FloatSeriesValuesDTO:
    """
    Attributes:
        total_item_count (int):
        values (List['FloatPointValueDTO']):
    """

    total_item_count: int
    values: List["FloatPointValueDTO"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_item_count = self.total_item_count

        values = []
        for values_item_data in self.values:
            values_item = values_item_data.to_dict()
            values.append(values_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalItemCount": total_item_count,
                "values": values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.float_point_value_dto import FloatPointValueDTO

        d = src_dict.copy()
        total_item_count = d.pop("totalItemCount")

        values = []
        _values = d.pop("values")
        for values_item_data in _values:
            values_item = FloatPointValueDTO.from_dict(values_item_data)

            values.append(values_item)

        float_series_values_dto = cls(
            total_item_count=total_item_count,
            values=values,
        )

        float_series_values_dto.additional_properties = d
        return float_series_values_dto

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
