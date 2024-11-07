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
    from ..models.nql_query_params_dto import NqlQueryParamsDTO


T = TypeVar("T", bound="SearchLeaderboardParamsDTO")


@_attrs_define
class SearchLeaderboardParamsDTO:
    """
    Attributes:
        query (Union[Unset, NqlQueryParamsDTO]):
    """

    query: Union[Unset, "NqlQueryParamsDTO"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        query: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.query, Unset):
            query = self.query.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if query is not UNSET:
            field_dict["query"] = query

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nql_query_params_dto import NqlQueryParamsDTO

        d = src_dict.copy()
        _query = d.pop("query", UNSET)
        query: Union[Unset, NqlQueryParamsDTO]
        if isinstance(_query, Unset):
            query = UNSET
        else:
            query = NqlQueryParamsDTO.from_dict(_query)

        search_leaderboard_params_dto = cls(
            query=query,
        )

        search_leaderboard_params_dto.additional_properties = d
        return search_leaderboard_params_dto

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
