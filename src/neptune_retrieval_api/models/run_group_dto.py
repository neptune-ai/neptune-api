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
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import (
    UNSET,
    Unset,
)

if TYPE_CHECKING:
    from ..models.table_view_params_dto import TableViewParamsDTO


T = TypeVar("T", bound="RunGroupDTO")


@_attrs_define
class RunGroupDTO:
    """
    Attributes:
        id (str):
        show_only_selected_runs (bool):
        view_params (TableViewParamsDTO):
        color (Union[Unset, str]):
        experiment_member_keys (Union[Unset, List[str]]):
        first_members_by_query_count (Union[Unset, int]):
        name (Union[Unset, str]):
        project_id (Union[Unset, str]):
        run_member_keys (Union[Unset, List[str]]):
        show_selected_hidden_by_filter (Union[Unset, bool]):
    """

    id: str
    show_only_selected_runs: bool
    view_params: "TableViewParamsDTO"
    color: Union[Unset, str] = UNSET
    experiment_member_keys: Union[Unset, List[str]] = UNSET
    first_members_by_query_count: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    project_id: Union[Unset, str] = UNSET
    run_member_keys: Union[Unset, List[str]] = UNSET
    show_selected_hidden_by_filter: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        show_only_selected_runs = self.show_only_selected_runs

        view_params = self.view_params.to_dict()

        color = self.color

        experiment_member_keys: Union[Unset, List[str]] = UNSET
        if not isinstance(self.experiment_member_keys, Unset):
            experiment_member_keys = self.experiment_member_keys

        first_members_by_query_count = self.first_members_by_query_count

        name = self.name

        project_id = self.project_id

        run_member_keys: Union[Unset, List[str]] = UNSET
        if not isinstance(self.run_member_keys, Unset):
            run_member_keys = self.run_member_keys

        show_selected_hidden_by_filter = self.show_selected_hidden_by_filter

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "showOnlySelectedRuns": show_only_selected_runs,
                "viewParams": view_params,
            }
        )
        if color is not UNSET:
            field_dict["color"] = color
        if experiment_member_keys is not UNSET:
            field_dict["experimentMemberKeys"] = experiment_member_keys
        if first_members_by_query_count is not UNSET:
            field_dict["firstMembersByQueryCount"] = first_members_by_query_count
        if name is not UNSET:
            field_dict["name"] = name
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if run_member_keys is not UNSET:
            field_dict["runMemberKeys"] = run_member_keys
        if show_selected_hidden_by_filter is not UNSET:
            field_dict["showSelectedHiddenByFilter"] = show_selected_hidden_by_filter

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.table_view_params_dto import TableViewParamsDTO

        d = src_dict.copy()
        id = d.pop("id")

        show_only_selected_runs = d.pop("showOnlySelectedRuns")

        view_params = TableViewParamsDTO.from_dict(d.pop("viewParams"))

        color = d.pop("color", UNSET)

        experiment_member_keys = cast(List[str], d.pop("experimentMemberKeys", UNSET))

        first_members_by_query_count = d.pop("firstMembersByQueryCount", UNSET)

        name = d.pop("name", UNSET)

        project_id = d.pop("projectId", UNSET)

        run_member_keys = cast(List[str], d.pop("runMemberKeys", UNSET))

        show_selected_hidden_by_filter = d.pop("showSelectedHiddenByFilter", UNSET)

        run_group_dto = cls(
            id=id,
            show_only_selected_runs=show_only_selected_runs,
            view_params=view_params,
            color=color,
            experiment_member_keys=experiment_member_keys,
            first_members_by_query_count=first_members_by_query_count,
            name=name,
            project_id=project_id,
            run_member_keys=run_member_keys,
            show_selected_hidden_by_filter=show_selected_hidden_by_filter,
        )

        run_group_dto.additional_properties = d
        return run_group_dto

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
