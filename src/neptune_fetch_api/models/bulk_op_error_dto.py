from typing import (
    Any,
    Dict,
    List,
    Type,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bulk_op_error_dto_reason import BulkOpErrorDTOReason

T = TypeVar("T", bound="BulkOpErrorDTO")


@_attrs_define
class BulkOpErrorDTO:
    """
    Attributes:
        experiment_identifier (str): Same format as sent in request.
        message (str): Error message.
        reason (BulkOpErrorDTOReason): Error reason.
    """

    experiment_identifier: str
    message: str
    reason: BulkOpErrorDTOReason
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        experiment_identifier = self.experiment_identifier

        message = self.message

        reason = self.reason.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "experimentIdentifier": experiment_identifier,
                "message": message,
                "reason": reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        experiment_identifier = d.pop("experimentIdentifier")

        message = d.pop("message")

        reason = BulkOpErrorDTOReason(d.pop("reason"))

        bulk_op_error_dto = cls(
            experiment_identifier=experiment_identifier,
            message=message,
            reason=reason,
        )

        bulk_op_error_dto.additional_properties = d
        return bulk_op_error_dto

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
