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
    from ..models.type_definition_dto import TypeDefinitionDTO


T = TypeVar("T", bound="AssignComplexOperation")


@_attrs_define
class AssignComplexOperation:
    """
    Attributes:
        field_type (TypeDefinitionDTO):
        field_content (str):
    """

    field_type: "TypeDefinitionDTO"
    field_content: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_type = self.field_type.to_dict()

        field_content = self.field_content

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "__type": field_type,
                "__content": field_content,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.type_definition_dto import TypeDefinitionDTO

        d = src_dict.copy()
        field_type = TypeDefinitionDTO.from_dict(d.pop("__type"))

        field_content = d.pop("__content")

        assign_complex_operation = cls(
            field_type=field_type,
            field_content=field_content,
        )

        assign_complex_operation.additional_properties = d
        return assign_complex_operation

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
