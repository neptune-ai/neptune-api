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

T = TypeVar("T", bound="FloatSeriesAttributeConfigDTO")


@_attrs_define
class FloatSeriesAttributeConfigDTO:
    """
    Attributes:
        max_ (Union[Unset, float]):
        min_ (Union[Unset, float]):
        unit (Union[Unset, str]):
    """

    max_: Union[Unset, float] = UNSET
    min_: Union[Unset, float] = UNSET
    unit: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        max_ = self.max_

        min_ = self.min_

        unit = self.unit

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_ is not UNSET:
            field_dict["max"] = max_
        if min_ is not UNSET:
            field_dict["min"] = min_
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        max_ = d.pop("max", UNSET)

        min_ = d.pop("min", UNSET)

        unit = d.pop("unit", UNSET)

        float_series_attribute_config_dto = cls(
            max_=max_,
            min_=min_,
            unit=unit,
        )

        float_series_attribute_config_dto.additional_properties = d
        return float_series_attribute_config_dto

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
