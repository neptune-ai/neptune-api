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

T = TypeVar("T", bound="Point")


@_attrs_define
class Point:
    """
    Attributes:
        interpolation (bool):
        x (float):
        max_y (Union[Unset, float]):
        min_y (Union[Unset, float]):
        y (Union[Unset, float]):
    """

    interpolation: bool
    x: float
    max_y: Union[Unset, float] = UNSET
    min_y: Union[Unset, float] = UNSET
    y: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        interpolation = self.interpolation

        x = self.x

        max_y = self.max_y

        min_y = self.min_y

        y = self.y

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "interpolation": interpolation,
                "x": x,
            }
        )
        if max_y is not UNSET:
            field_dict["maxY"] = max_y
        if min_y is not UNSET:
            field_dict["minY"] = min_y
        if y is not UNSET:
            field_dict["y"] = y

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        interpolation = d.pop("interpolation")

        x = d.pop("x")

        max_y = d.pop("maxY", UNSET)

        min_y = d.pop("minY", UNSET)

        y = d.pop("y", UNSET)

        point = cls(
            interpolation=interpolation,
            x=x,
            max_y=max_y,
            min_y=min_y,
            y=y,
        )

        point.additional_properties = d
        return point

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
