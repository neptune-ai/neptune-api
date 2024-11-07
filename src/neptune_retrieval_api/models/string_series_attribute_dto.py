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

from ..models.attribute_type_dto import AttributeTypeDTO
from ..types import (
    UNSET,
    Unset,
)

T = TypeVar("T", bound="StringSeriesAttributeDTO")


@_attrs_define
class StringSeriesAttributeDTO:
    """
    Attributes:
        attribute_name (str):
        attribute_type (AttributeTypeDTO):
        last (Union[Unset, str]):
        last_step (Union[Unset, float]):
    """

    attribute_name: str
    attribute_type: AttributeTypeDTO
    last: Union[Unset, str] = UNSET
    last_step: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attribute_name = self.attribute_name

        attribute_type = self.attribute_type.value

        last = self.last

        last_step = self.last_step

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attributeName": attribute_name,
                "attributeType": attribute_type,
            }
        )
        if last is not UNSET:
            field_dict["last"] = last
        if last_step is not UNSET:
            field_dict["lastStep"] = last_step

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        attribute_name = d.pop("attributeName")

        attribute_type = AttributeTypeDTO(d.pop("attributeType"))

        last = d.pop("last", UNSET)

        last_step = d.pop("lastStep", UNSET)

        string_series_attribute_dto = cls(
            attribute_name=attribute_name,
            attribute_type=attribute_type,
            last=last,
            last_step=last_step,
        )

        string_series_attribute_dto.additional_properties = d
        return string_series_attribute_dto

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
