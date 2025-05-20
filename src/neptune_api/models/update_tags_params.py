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

from ..models.update_tags_params_attribute_path_to_be_updated import UpdateTagsParamsAttributePathToBeUpdated
from ..types import (
    UNSET,
    Unset,
)

T = TypeVar("T", bound="UpdateTagsParams")


@_attrs_define
class UpdateTagsParams:
    """
    Attributes:
        experiment_identifiers (List[str]):
        tags_to_add (List[str]):
        tags_to_delete (List[str]):
        attribute_path_to_be_updated (Union[Unset, UpdateTagsParamsAttributePathToBeUpdated]):
    """

    experiment_identifiers: List[str]
    tags_to_add: List[str]
    tags_to_delete: List[str]
    attribute_path_to_be_updated: Union[Unset, UpdateTagsParamsAttributePathToBeUpdated] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        experiment_identifiers = self.experiment_identifiers

        tags_to_add = self.tags_to_add

        tags_to_delete = self.tags_to_delete

        attribute_path_to_be_updated: Union[Unset, str] = UNSET
        if not isinstance(self.attribute_path_to_be_updated, Unset):
            attribute_path_to_be_updated = self.attribute_path_to_be_updated.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "experimentIdentifiers": experiment_identifiers,
                "tagsToAdd": tags_to_add,
                "tagsToDelete": tags_to_delete,
            }
        )
        if attribute_path_to_be_updated is not UNSET:
            field_dict["attributePathToBeUpdated"] = attribute_path_to_be_updated

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        experiment_identifiers = cast(List[str], d.pop("experimentIdentifiers"))

        tags_to_add = cast(List[str], d.pop("tagsToAdd"))

        tags_to_delete = cast(List[str], d.pop("tagsToDelete"))

        _attribute_path_to_be_updated = d.pop("attributePathToBeUpdated", UNSET)
        attribute_path_to_be_updated: Union[Unset, UpdateTagsParamsAttributePathToBeUpdated]
        if isinstance(_attribute_path_to_be_updated, Unset):
            attribute_path_to_be_updated = UNSET
        else:
            attribute_path_to_be_updated = UpdateTagsParamsAttributePathToBeUpdated(_attribute_path_to_be_updated)

        update_tags_params = cls(
            experiment_identifiers=experiment_identifiers,
            tags_to_add=tags_to_add,
            tags_to_delete=tags_to_delete,
            attribute_path_to_be_updated=attribute_path_to_be_updated,
        )

        update_tags_params.additional_properties = d
        return update_tags_params

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
