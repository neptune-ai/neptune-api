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
    from ..models.attribute_style_settings_dto import AttributeStyleSettingsDTO


T = TypeVar("T", bound="AttributesStyleSettingsResultDTO")


@_attrs_define
class AttributesStyleSettingsResultDTO:
    """
    Attributes:
        settings (Union[Unset, List['AttributeStyleSettingsDTO']]):
    """

    settings: Union[Unset, List["AttributeStyleSettingsDTO"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        settings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.settings, Unset):
            settings = []
            for settings_item_data in self.settings:
                settings_item = settings_item_data.to_dict()
                settings.append(settings_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if settings is not UNSET:
            field_dict["settings"] = settings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.attribute_style_settings_dto import AttributeStyleSettingsDTO

        d = src_dict.copy()
        settings = []
        _settings = d.pop("settings", UNSET)
        for settings_item_data in _settings or []:
            settings_item = AttributeStyleSettingsDTO.from_dict(settings_item_data)

            settings.append(settings_item)

        attributes_style_settings_result_dto = cls(
            settings=settings,
        )

        attributes_style_settings_result_dto.additional_properties = d
        return attributes_style_settings_result_dto

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
