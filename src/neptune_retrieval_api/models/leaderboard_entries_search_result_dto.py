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
    from ..models.attribute_definition_dto import AttributeDefinitionDTO
    from ..models.attributes_dto import AttributesDTO
    from ..models.leaderboard_entry_group_dto import LeaderboardEntryGroupDTO


T = TypeVar("T", bound="LeaderboardEntriesSearchResultDTO")


@_attrs_define
class LeaderboardEntriesSearchResultDTO:
    """
    Attributes:
        entries (List['AttributesDTO']): The entries matching the given criteria.
        matching_item_count (int): The total number of entries matching the given criteria.
        groups (Union[Unset, List['LeaderboardEntryGroupDTO']]): The groups of entities matching given criteria.
        suggestions (Union[Unset, List['AttributeDefinitionDTO']]): The column suggestions to the user, most recommended
            columns first.
        total_group_count (Union[Unset, int]): The total number of group entries.
    """

    entries: List["AttributesDTO"]
    matching_item_count: int
    groups: Union[Unset, List["LeaderboardEntryGroupDTO"]] = UNSET
    suggestions: Union[Unset, List["AttributeDefinitionDTO"]] = UNSET
    total_group_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entries = []
        for entries_item_data in self.entries:
            entries_item = entries_item_data.to_dict()
            entries.append(entries_item)

        matching_item_count = self.matching_item_count

        groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        suggestions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.suggestions, Unset):
            suggestions = []
            for suggestions_item_data in self.suggestions:
                suggestions_item = suggestions_item_data.to_dict()
                suggestions.append(suggestions_item)

        total_group_count = self.total_group_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entries": entries,
                "matchingItemCount": matching_item_count,
            }
        )
        if groups is not UNSET:
            field_dict["groups"] = groups
        if suggestions is not UNSET:
            field_dict["suggestions"] = suggestions
        if total_group_count is not UNSET:
            field_dict["totalGroupCount"] = total_group_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.attribute_definition_dto import AttributeDefinitionDTO
        from ..models.attributes_dto import AttributesDTO
        from ..models.leaderboard_entry_group_dto import LeaderboardEntryGroupDTO

        d = src_dict.copy()
        entries = []
        _entries = d.pop("entries")
        for entries_item_data in _entries:
            entries_item = AttributesDTO.from_dict(entries_item_data)

            entries.append(entries_item)

        matching_item_count = d.pop("matchingItemCount")

        groups: Union[Unset, List[LeaderboardEntryGroupDTO]] = UNSET
        _groups = d.pop("groups", UNSET)
        if not isinstance(_groups, Unset):
            groups = []
            for groups_item_data in _groups:
                groups_item = LeaderboardEntryGroupDTO.from_dict(groups_item_data)

                groups.append(groups_item)

        suggestions: Union[Unset, List[AttributeDefinitionDTO]] = UNSET
        _suggestions = d.pop("suggestions", UNSET)
        if not isinstance(_suggestions, Unset):
            suggestions = []
            for suggestions_item_data in _suggestions:
                suggestions_item = AttributeDefinitionDTO.from_dict(suggestions_item_data)

                suggestions.append(suggestions_item)

        total_group_count = d.pop("totalGroupCount", UNSET)

        leaderboard_entries_search_result_dto = cls(
            entries=entries,
            matching_item_count=matching_item_count,
            groups=groups,
            suggestions=suggestions,
            total_group_count=total_group_count,
        )

        leaderboard_entries_search_result_dto.additional_properties = d
        return leaderboard_entries_search_result_dto

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
