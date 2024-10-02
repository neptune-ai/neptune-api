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
    from ..models.attribute_style_settings_dto import AttributeStyleSettingsDTO


T = TypeVar("T", bound="AttributeStyleSettingsParamsDTO")


@_attrs_define
class AttributeStyleSettingsParamsDTO:
    """
    Attributes:
        project_identifier (str):
        style_settings (AttributeStyleSettingsDTO):
    """

    project_identifier: str
    style_settings: "AttributeStyleSettingsDTO"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        project_identifier = self.project_identifier

        style_settings = self.style_settings.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectIdentifier": project_identifier,
                "styleSettings": style_settings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.attribute_style_settings_dto import AttributeStyleSettingsDTO

        d = src_dict.copy()
        project_identifier = d.pop("projectIdentifier")

        style_settings = AttributeStyleSettingsDTO.from_dict(d.pop("styleSettings"))

        attribute_style_settings_params_dto = cls(
            project_identifier=project_identifier,
            style_settings=style_settings,
        )

        attribute_style_settings_params_dto.additional_properties = d
        return attribute_style_settings_params_dto

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
