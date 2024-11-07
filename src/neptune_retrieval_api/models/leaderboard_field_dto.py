from typing import (
    Any,
    Dict,
    List,
    Type,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.attribute_type_dto import AttributeTypeDTO
from ..models.leaderboard_field_dto_aggregation import LeaderboardFieldDTOAggregation

T = TypeVar("T", bound="LeaderboardFieldDTO")


@_attrs_define
class LeaderboardFieldDTO:
    """
    Attributes:
        aggregation (LeaderboardFieldDTOAggregation):
        name (str):
        type (AttributeTypeDTO):
    """

    aggregation: LeaderboardFieldDTOAggregation
    name: str
    type: AttributeTypeDTO
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        aggregation = self.aggregation.value

        name = self.name

        type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "aggregation": aggregation,
                "name": name,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        aggregation = LeaderboardFieldDTOAggregation(d.pop("aggregation"))

        name = d.pop("name")

        type = AttributeTypeDTO(d.pop("type"))

        leaderboard_field_dto = cls(
            aggregation=aggregation,
            name=name,
            type=type,
        )

        leaderboard_field_dto.additional_properties = d
        return leaderboard_field_dto

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
