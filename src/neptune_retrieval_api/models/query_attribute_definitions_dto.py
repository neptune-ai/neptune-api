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
    from ..models.attribute_name_filter_dto import AttributeNameFilterDTO


T = TypeVar("T", bound="QueryAttributeDefinitionsDTO")


@_attrs_define
class QueryAttributeDefinitionsDTO:
    """
    Attributes:
        attribute_name_filter (Union[Unset, AttributeNameFilterDTO]):
    """

    attribute_name_filter: Union[Unset, "AttributeNameFilterDTO"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attribute_name_filter: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attribute_name_filter, Unset):
            attribute_name_filter = self.attribute_name_filter.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attribute_name_filter is not UNSET:
            field_dict["attributeNameFilter"] = attribute_name_filter

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.attribute_name_filter_dto import AttributeNameFilterDTO

        d = src_dict.copy()
        _attribute_name_filter = d.pop("attributeNameFilter", UNSET)
        attribute_name_filter: Union[Unset, AttributeNameFilterDTO]
        if isinstance(_attribute_name_filter, Unset):
            attribute_name_filter = UNSET
        else:
            attribute_name_filter = AttributeNameFilterDTO.from_dict(_attribute_name_filter)

        query_attribute_definitions_dto = cls(
            attribute_name_filter=attribute_name_filter,
        )

        query_attribute_definitions_dto.additional_properties = d
        return query_attribute_definitions_dto

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
