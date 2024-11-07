import datetime
from typing import (
    Any,
    Dict,
    List,
    Type,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.attribute_type_dto import AttributeTypeDTO

T = TypeVar("T", bound="DatetimeAttributeDTO")


@_attrs_define
class DatetimeAttributeDTO:
    """
    Attributes:
        attribute_name (str):
        attribute_type (AttributeTypeDTO):
        value (datetime.datetime):
    """

    attribute_name: str
    attribute_type: AttributeTypeDTO
    value: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attribute_name = self.attribute_name

        attribute_type = self.attribute_type.value

        value = self.value.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attributeName": attribute_name,
                "attributeType": attribute_type,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        attribute_name = d.pop("attributeName")

        attribute_type = AttributeTypeDTO(d.pop("attributeType"))

        value = isoparse(d.pop("value"))

        datetime_attribute_dto = cls(
            attribute_name=attribute_name,
            attribute_type=attribute_type,
            value=value,
        )

        datetime_attribute_dto.additional_properties = d
        return datetime_attribute_dto

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
