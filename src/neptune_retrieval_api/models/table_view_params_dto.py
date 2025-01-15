#
# Copyright (c) 2025, Neptune Labs Sp. z o.o.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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


T = TypeVar("T", bound="TableViewParamsDTO")


@_attrs_define
class TableViewParamsDTO:
    """
    Attributes:
        column_list (LeaderboardViewColumnListDTO):
        sort_options (LeaderboardSortParamsDTO):
        experiments_only (Union[Unset, bool]):
        group_options (Union[Unset, LeaderboardGroupParamsDTO]):
        query (Union[Unset, str]):
        runs_lineage (Union[Unset, bool]):
    """

    column_list: "LeaderboardViewColumnListDTO"
    sort_options: "LeaderboardSortParamsDTO"
    experiments_only: Union[Unset, bool] = UNSET
    group_options: Union[Unset, "LeaderboardGroupParamsDTO"] = UNSET
    query: Union[Unset, str] = UNSET
    runs_lineage: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        column_list = self.column_list.to_dict()

        sort_options = self.sort_options.to_dict()

        experiments_only = self.experiments_only

        group_options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.group_options, Unset):
            group_options = self.group_options.to_dict()

        query = self.query

        runs_lineage = self.runs_lineage

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "columnList": column_list,
                "sortOptions": sort_options,
            }
        )
        if experiments_only is not UNSET:
            field_dict["experimentsOnly"] = experiments_only
        if group_options is not UNSET:
            field_dict["groupOptions"] = group_options
        if query is not UNSET:
            field_dict["query"] = query
        if runs_lineage is not UNSET:
            field_dict["runsLineage"] = runs_lineage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.leaderboard_group_params_dto import LeaderboardGroupParamsDTO
        from ..models.leaderboard_sort_params_dto import LeaderboardSortParamsDTO
        from ..models.leaderboard_view_column_list_dto import LeaderboardViewColumnListDTO

        d = src_dict.copy()
        column_list = LeaderboardViewColumnListDTO.from_dict(d.pop("columnList"))

        sort_options = LeaderboardSortParamsDTO.from_dict(d.pop("sortOptions"))

        experiments_only = d.pop("experimentsOnly", UNSET)

        _group_options = d.pop("groupOptions", UNSET)
        group_options: Union[Unset, LeaderboardGroupParamsDTO]
        if isinstance(_group_options, Unset):
            group_options = UNSET
        else:
            group_options = LeaderboardGroupParamsDTO.from_dict(_group_options)

        query = d.pop("query", UNSET)

        runs_lineage = d.pop("runsLineage", UNSET)

        table_view_params_dto = cls(
            column_list=column_list,
            sort_options=sort_options,
            experiments_only=experiments_only,
            group_options=group_options,
            query=query,
            runs_lineage=runs_lineage,
        )

        table_view_params_dto.additional_properties = d
        return table_view_params_dto

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
