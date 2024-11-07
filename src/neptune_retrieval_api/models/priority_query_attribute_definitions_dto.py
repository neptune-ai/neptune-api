from typing import (
    Any,
    Dict,
    List,
    Type,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import (
    UNSET,
    Unset,
)

T = TypeVar("T", bound="PriorityQueryAttributeDefinitionsDTO")


@_attrs_define
class PriorityQueryAttributeDefinitionsDTO:
    """
    Attributes:
        experiment_ids (Union[Unset, List[str]]): Prioritize by experiment id, if null no prioritization is applied
    """

    experiment_ids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        experiment_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.experiment_ids, Unset):
            experiment_ids = self.experiment_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if experiment_ids is not UNSET:
            field_dict["experimentIds"] = experiment_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        experiment_ids = cast(List[str], d.pop("experimentIds", UNSET))

        priority_query_attribute_definitions_dto = cls(
            experiment_ids=experiment_ids,
        )

        priority_query_attribute_definitions_dto.additional_properties = d
        return priority_query_attribute_definitions_dto

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
