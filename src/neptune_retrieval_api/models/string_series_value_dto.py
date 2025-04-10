from typing import (
    Any,
    Dict,
    List,
    Type,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StringSeriesValueDTO")


@_attrs_define
class StringSeriesValueDTO:
    """
    Attributes:
        completion_ratio (float):
        is_preview (bool):
        step (float):
        timestamp_millis (int):
        value (str):
    """

    completion_ratio: float
    is_preview: bool
    step: float
    timestamp_millis: int
    value: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        completion_ratio = self.completion_ratio

        is_preview = self.is_preview

        step = self.step

        timestamp_millis = self.timestamp_millis

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "completionRatio": completion_ratio,
                "isPreview": is_preview,
                "step": step,
                "timestampMillis": timestamp_millis,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        completion_ratio = d.pop("completionRatio")

        is_preview = d.pop("isPreview")

        step = d.pop("step")

        timestamp_millis = d.pop("timestampMillis")

        value = d.pop("value")

        string_series_value_dto = cls(
            completion_ratio=completion_ratio,
            is_preview=is_preview,
            step=step,
            timestamp_millis=timestamp_millis,
            value=value,
        )

        string_series_value_dto.additional_properties = d
        return string_series_value_dto

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
