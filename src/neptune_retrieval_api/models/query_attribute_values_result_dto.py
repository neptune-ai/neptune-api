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
    from ..models.attribute_dto import AttributeDTO


T = TypeVar("T", bound="QueryAttributeValuesResultDTO")


@_attrs_define
class QueryAttributeValuesResultDTO:
    """
    Attributes:
        attributes (List['AttributeDTO']): A list of unique attribute values
    """

    attributes: List["AttributeDTO"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attributes = []
        for attributes_item_data in self.attributes:
            attributes_item = attributes_item_data.to_dict()
            attributes.append(attributes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attributes": attributes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.attribute_dto import AttributeDTO

        d = src_dict.copy()
        attributes = []
        _attributes = d.pop("attributes")
        for attributes_item_data in _attributes:
            attributes_item = AttributeDTO.from_dict(attributes_item_data)

            attributes.append(attributes_item)

        query_attribute_values_result_dto = cls(
            attributes=attributes,
        )

        query_attribute_values_result_dto.additional_properties = d
        return query_attribute_values_result_dto

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
