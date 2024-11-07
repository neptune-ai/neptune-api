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
    from ..models.attribute_style_identifier_dto import AttributeStyleIdentifierDTO


T = TypeVar("T", bound="SearchAttributesStyleSettingsParamsDTO")


@_attrs_define
class SearchAttributesStyleSettingsParamsDTO:
    """
    Attributes:
        project_identifier (str):
        attributes (Union[Unset, List['AttributeStyleIdentifierDTO']]):
    """

    project_identifier: str
    attributes: Union[Unset, List["AttributeStyleIdentifierDTO"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        project_identifier = self.project_identifier

        attributes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = []
            for attributes_item_data in self.attributes:
                attributes_item = attributes_item_data.to_dict()
                attributes.append(attributes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectIdentifier": project_identifier,
            }
        )
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.attribute_style_identifier_dto import AttributeStyleIdentifierDTO

        d = src_dict.copy()
        project_identifier = d.pop("projectIdentifier")

        attributes = []
        _attributes = d.pop("attributes", UNSET)
        for attributes_item_data in _attributes or []:
            attributes_item = AttributeStyleIdentifierDTO.from_dict(attributes_item_data)

            attributes.append(attributes_item)

        search_attributes_style_settings_params_dto = cls(
            project_identifier=project_identifier,
            attributes=attributes,
        )

        search_attributes_style_settings_params_dto.additional_properties = d
        return search_attributes_style_settings_params_dto

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
