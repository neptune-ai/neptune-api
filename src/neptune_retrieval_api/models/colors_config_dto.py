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
    from ..models.colors_dto import ColorsDTO


T = TypeVar("T", bound="ColorsConfigDTO")


@_attrs_define
class ColorsConfigDTO:
    """
    Attributes:
        colors (Union[Unset, List['ColorsDTO']]):
    """

    colors: Union[Unset, List["ColorsDTO"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        colors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.colors, Unset):
            colors = []
            for colors_item_data in self.colors:
                colors_item = colors_item_data.to_dict()
                colors.append(colors_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if colors is not UNSET:
            field_dict["colors"] = colors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.colors_dto import ColorsDTO

        d = src_dict.copy()
        colors = []
        _colors = d.pop("colors", UNSET)
        for colors_item_data in _colors or []:
            colors_item = ColorsDTO.from_dict(colors_item_data)

            colors.append(colors_item)

        colors_config_dto = cls(
            colors=colors,
        )

        colors_config_dto.additional_properties = d
        return colors_config_dto

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
