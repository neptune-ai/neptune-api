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
    from ..models.leaderboard_field_dto import LeaderboardFieldDTO
    from ..models.leaderboard_field_with_value_dto_value import LeaderboardFieldWithValueDTOValue


T = TypeVar("T", bound="LeaderboardFieldWithValueDTO")


@_attrs_define
class LeaderboardFieldWithValueDTO:
    """
    Attributes:
        field (LeaderboardFieldDTO):
        value (Union[Unset, LeaderboardFieldWithValueDTOValue]):
    """

    field: "LeaderboardFieldDTO"
    value: Union[Unset, "LeaderboardFieldWithValueDTOValue"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field = self.field.to_dict()

        value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field": field,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.leaderboard_field_dto import LeaderboardFieldDTO
        from ..models.leaderboard_field_with_value_dto_value import LeaderboardFieldWithValueDTOValue

        d = src_dict.copy()
        field = LeaderboardFieldDTO.from_dict(d.pop("field"))

        _value = d.pop("value", UNSET)
        value: Union[Unset, LeaderboardFieldWithValueDTOValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = LeaderboardFieldWithValueDTOValue.from_dict(_value)

        leaderboard_field_with_value_dto = cls(
            field=field,
            value=value,
        )

        leaderboard_field_with_value_dto.additional_properties = d
        return leaderboard_field_with_value_dto

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
