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

T = TypeVar("T", bound="WidgetLayoutDTO")


@_attrs_define
class WidgetLayoutDTO:
    """
    Attributes:
        h (int):
        id (str):
        w (int):
        x (int):
        y (int):
        is_static (Union[Unset, bool]):
    """

    h: int
    id: str
    w: int
    x: int
    y: int
    is_static: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        h = self.h

        id = self.id

        w = self.w

        x = self.x

        y = self.y

        is_static = self.is_static

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "h": h,
                "id": id,
                "w": w,
                "x": x,
                "y": y,
            }
        )
        if is_static is not UNSET:
            field_dict["isStatic"] = is_static

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        h = d.pop("h")

        id = d.pop("id")

        w = d.pop("w")

        x = d.pop("x")

        y = d.pop("y")

        is_static = d.pop("isStatic", UNSET)

        widget_layout_dto = cls(
            h=h,
            id=id,
            w=w,
            x=x,
            y=y,
            is_static=is_static,
        )

        widget_layout_dto.additional_properties = d
        return widget_layout_dto

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
