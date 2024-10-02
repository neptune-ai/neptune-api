from typing import (
    Any,
    Dict,
    List,
    Type,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FloatPointValueDTO")


@_attrs_define
class FloatPointValueDTO:
    """
    Attributes:
        step (float):
        timestamp_millis (int):
        value (float):
    """

    step: float
    timestamp_millis: int
    value: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        step = self.step

        timestamp_millis = self.timestamp_millis

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "step": step,
                "timestampMillis": timestamp_millis,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        step = d.pop("step")

        timestamp_millis = d.pop("timestampMillis")

        value = d.pop("value")

        float_point_value_dto = cls(
            step=step,
            timestamp_millis=timestamp_millis,
            value=value,
        )

        float_point_value_dto.additional_properties = d
        return float_point_value_dto

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
