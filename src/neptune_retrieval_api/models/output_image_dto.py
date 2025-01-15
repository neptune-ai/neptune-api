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
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import (
    UNSET,
    Unset,
)

T = TypeVar("T", bound="OutputImageDTO")


@_attrs_define
class OutputImageDTO:
    """
    Attributes:
        description (Union[Unset, str]):
        image_url (Union[Unset, str]):
        name (Union[Unset, str]):
        thumbnail_url (Union[Unset, str]):
    """

    description: Union[Unset, str] = UNSET
    image_url: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    thumbnail_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        image_url = self.image_url

        name = self.name

        thumbnail_url = self.thumbnail_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if image_url is not UNSET:
            field_dict["imageUrl"] = image_url
        if name is not UNSET:
            field_dict["name"] = name
        if thumbnail_url is not UNSET:
            field_dict["thumbnailUrl"] = thumbnail_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        image_url = d.pop("imageUrl", UNSET)

        name = d.pop("name", UNSET)

        thumbnail_url = d.pop("thumbnailUrl", UNSET)

        output_image_dto = cls(
            description=description,
            image_url=image_url,
            name=name,
            thumbnail_url=thumbnail_url,
        )

        output_image_dto.additional_properties = d
        return output_image_dto

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
