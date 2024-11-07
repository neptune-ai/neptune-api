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

from ..types import (
    UNSET,
    Unset,
)

T = TypeVar("T", bound="LeaderboardViewSetDefaultDTO")


@_attrs_define
class LeaderboardViewSetDefaultDTO:
    """
    Attributes:
        project_identifier (str):
        view_id (Union[Unset, str]):
    """

    project_identifier: str
    view_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        project_identifier = self.project_identifier

        view_id = self.view_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectIdentifier": project_identifier,
            }
        )
        if view_id is not UNSET:
            field_dict["viewId"] = view_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        project_identifier = d.pop("projectIdentifier")

        view_id = d.pop("viewId", UNSET)

        leaderboard_view_set_default_dto = cls(
            project_identifier=project_identifier,
            view_id=view_id,
        )

        leaderboard_view_set_default_dto.additional_properties = d
        return leaderboard_view_set_default_dto

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
