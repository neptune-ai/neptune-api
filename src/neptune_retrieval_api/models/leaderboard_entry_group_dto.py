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
    from ..models.leaderboard_field_with_value_dto import LeaderboardFieldWithValueDTO


T = TypeVar("T", bound="LeaderboardEntryGroupDTO")


@_attrs_define
class LeaderboardEntryGroupDTO:
    """
    Attributes:
        children_ids (List[str]):
        id (str): ID of the group
        item_count (int): The number of entries in the group.
        key (List['LeaderboardFieldWithValueDTO']):
        before_token (Union[Unset, str]): Token for searching previous group entries (in case of pagination)
        continuation_token (Union[Unset, str]): Token for searching next group entries (in case of pagination)
    """

    children_ids: List[str]
    id: str
    item_count: int
    key: List["LeaderboardFieldWithValueDTO"]
    before_token: Union[Unset, str] = UNSET
    continuation_token: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        children_ids = self.children_ids

        id = self.id

        item_count = self.item_count

        key = []
        for key_item_data in self.key:
            key_item = key_item_data.to_dict()
            key.append(key_item)

        before_token = self.before_token

        continuation_token = self.continuation_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "childrenIds": children_ids,
                "id": id,
                "itemCount": item_count,
                "key": key,
            }
        )
        if before_token is not UNSET:
            field_dict["beforeToken"] = before_token
        if continuation_token is not UNSET:
            field_dict["continuationToken"] = continuation_token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.leaderboard_field_with_value_dto import LeaderboardFieldWithValueDTO

        d = src_dict.copy()
        children_ids = cast(List[str], d.pop("childrenIds"))

        id = d.pop("id")

        item_count = d.pop("itemCount")

        key = []
        _key = d.pop("key")
        for key_item_data in _key:
            key_item = LeaderboardFieldWithValueDTO.from_dict(key_item_data)

            key.append(key_item)

        before_token = d.pop("beforeToken", UNSET)

        continuation_token = d.pop("continuationToken", UNSET)

        leaderboard_entry_group_dto = cls(
            children_ids=children_ids,
            id=id,
            item_count=item_count,
            key=key,
            before_token=before_token,
            continuation_token=continuation_token,
        )

        leaderboard_entry_group_dto.additional_properties = d
        return leaderboard_entry_group_dto

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
