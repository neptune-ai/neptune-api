from typing import (
    Any,
    Dict,
    List,
    Type,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.operation_error_error_type import OperationErrorErrorType

T = TypeVar("T", bound="OperationError")


@_attrs_define
class OperationError:
    """
    Attributes:
        error_description (str):
        error_type (OperationErrorErrorType):
    """

    error_description: str
    error_type: OperationErrorErrorType
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error_description = self.error_description

        error_type = self.error_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "errorDescription": error_description,
                "errorType": error_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        error_description = d.pop("errorDescription")

        error_type = OperationErrorErrorType(d.pop("errorType"))

        operation_error = cls(
            error_description=error_description,
            error_type=error_type,
        )

        operation_error.additional_properties = d
        return operation_error

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
