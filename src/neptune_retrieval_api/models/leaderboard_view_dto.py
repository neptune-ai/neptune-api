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
    from ..models.leaderboard_group_params_dto import LeaderboardGroupParamsDTO
    from ..models.leaderboard_sort_params_dto import LeaderboardSortParamsDTO
    from ..models.leaderboard_view_column_list_dto import LeaderboardViewColumnListDTO
    from ..models.leaderboard_view_quick_filter_dto import LeaderboardViewQuickFilterDTO


T = TypeVar("T", bound="LeaderboardViewDTO")


@_attrs_define
class LeaderboardViewDTO:
    """
    Attributes:
        column_list (LeaderboardViewColumnListDTO):
        default_view (bool):
        experiments_only (bool):
        id (str):
        name (str):
        runs_lineage (bool):
        sort_options (LeaderboardSortParamsDTO):
        suggestions_enabled (bool):
        group_options (Union[Unset, LeaderboardGroupParamsDTO]):
        query (Union[Unset, str]):
        quick_filters (Union[Unset, LeaderboardViewQuickFilterDTO]):
    """

    column_list: "LeaderboardViewColumnListDTO"
    default_view: bool
    experiments_only: bool
    id: str
    name: str
    runs_lineage: bool
    sort_options: "LeaderboardSortParamsDTO"
    suggestions_enabled: bool
    group_options: Union[Unset, "LeaderboardGroupParamsDTO"] = UNSET
    query: Union[Unset, str] = UNSET
    quick_filters: Union[Unset, "LeaderboardViewQuickFilterDTO"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        column_list = self.column_list.to_dict()

        default_view = self.default_view

        experiments_only = self.experiments_only

        id = self.id

        name = self.name

        runs_lineage = self.runs_lineage

        sort_options = self.sort_options.to_dict()

        suggestions_enabled = self.suggestions_enabled

        group_options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.group_options, Unset):
            group_options = self.group_options.to_dict()

        query = self.query

        quick_filters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.quick_filters, Unset):
            quick_filters = self.quick_filters.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "columnList": column_list,
                "defaultView": default_view,
                "experimentsOnly": experiments_only,
                "id": id,
                "name": name,
                "runsLineage": runs_lineage,
                "sortOptions": sort_options,
                "suggestionsEnabled": suggestions_enabled,
            }
        )
        if group_options is not UNSET:
            field_dict["groupOptions"] = group_options
        if query is not UNSET:
            field_dict["query"] = query
        if quick_filters is not UNSET:
            field_dict["quickFilters"] = quick_filters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.leaderboard_group_params_dto import LeaderboardGroupParamsDTO
        from ..models.leaderboard_sort_params_dto import LeaderboardSortParamsDTO
        from ..models.leaderboard_view_column_list_dto import LeaderboardViewColumnListDTO
        from ..models.leaderboard_view_quick_filter_dto import LeaderboardViewQuickFilterDTO

        d = src_dict.copy()
        column_list = LeaderboardViewColumnListDTO.from_dict(d.pop("columnList"))

        default_view = d.pop("defaultView")

        experiments_only = d.pop("experimentsOnly")

        id = d.pop("id")

        name = d.pop("name")

        runs_lineage = d.pop("runsLineage")

        sort_options = LeaderboardSortParamsDTO.from_dict(d.pop("sortOptions"))

        suggestions_enabled = d.pop("suggestionsEnabled")

        _group_options = d.pop("groupOptions", UNSET)
        group_options: Union[Unset, LeaderboardGroupParamsDTO]
        if isinstance(_group_options, Unset):
            group_options = UNSET
        else:
            group_options = LeaderboardGroupParamsDTO.from_dict(_group_options)

        query = d.pop("query", UNSET)

        _quick_filters = d.pop("quickFilters", UNSET)
        quick_filters: Union[Unset, LeaderboardViewQuickFilterDTO]
        if isinstance(_quick_filters, Unset):
            quick_filters = UNSET
        else:
            quick_filters = LeaderboardViewQuickFilterDTO.from_dict(_quick_filters)

        leaderboard_view_dto = cls(
            column_list=column_list,
            default_view=default_view,
            experiments_only=experiments_only,
            id=id,
            name=name,
            runs_lineage=runs_lineage,
            sort_options=sort_options,
            suggestions_enabled=suggestions_enabled,
            group_options=group_options,
            query=query,
            quick_filters=quick_filters,
        )

        leaderboard_view_dto.additional_properties = d
        return leaderboard_view_dto

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
