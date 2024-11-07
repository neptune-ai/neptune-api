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
    from ..models.leaderboard_view_dto import LeaderboardViewDTO


T = TypeVar("T", bound="LeaderboardViewListDTO")


@_attrs_define
class LeaderboardViewListDTO:
    """
    Attributes:
        views (List['LeaderboardViewDTO']): Leaderpoard views list
    """

    views: List["LeaderboardViewDTO"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        views = []
        for views_item_data in self.views:
            views_item = views_item_data.to_dict()
            views.append(views_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "views": views,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.leaderboard_view_dto import LeaderboardViewDTO

        d = src_dict.copy()
        views = []
        _views = d.pop("views")
        for views_item_data in _views:
            views_item = LeaderboardViewDTO.from_dict(views_item_data)

            views.append(views_item)

        leaderboard_view_list_dto = cls(
            views=views,
        )

        leaderboard_view_list_dto.additional_properties = d
        return leaderboard_view_list_dto

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
