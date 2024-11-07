from typing import (
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

T = TypeVar("T", bound="LogStringEntry")


@_attrs_define
class LogStringEntry:
    """
    Attributes:
        value (str):
        timestamp_milliseconds (int):
        step (Union[Unset, float]):
    """

    value: str
    timestamp_milliseconds: int
    step: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        value = self.value

        timestamp_milliseconds = self.timestamp_milliseconds

        step = self.step

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
                "timestampMilliseconds": timestamp_milliseconds,
            }
        )
        if step is not UNSET:
            field_dict["step"] = step

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        value = d.pop("value")

        timestamp_milliseconds = d.pop("timestampMilliseconds")

        step = d.pop("step", UNSET)

        log_string_entry = cls(
            value=value,
            timestamp_milliseconds=timestamp_milliseconds,
            step=step,
        )

        log_string_entry.additional_properties = d
        return log_string_entry

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
