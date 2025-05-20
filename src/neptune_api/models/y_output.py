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
    from ..models.output_image_dto import OutputImageDTO


T = TypeVar("T", bound="YOutput")


@_attrs_define
class YOutput:
    """
    Attributes:
        image_value (Union[Unset, OutputImageDTO]):
        numeric_value (Union[Unset, float]):
        text_value (Union[Unset, str]):
    """

    image_value: Union[Unset, "OutputImageDTO"] = UNSET
    numeric_value: Union[Unset, float] = UNSET
    text_value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        image_value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.image_value, Unset):
            image_value = self.image_value.to_dict()

        numeric_value = self.numeric_value

        text_value = self.text_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if image_value is not UNSET:
            field_dict["imageValue"] = image_value
        if numeric_value is not UNSET:
            field_dict["numericValue"] = numeric_value
        if text_value is not UNSET:
            field_dict["textValue"] = text_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.output_image_dto import OutputImageDTO

        d = src_dict.copy()
        _image_value = d.pop("imageValue", UNSET)
        image_value: Union[Unset, OutputImageDTO]
        if isinstance(_image_value, Unset):
            image_value = UNSET
        else:
            image_value = OutputImageDTO.from_dict(_image_value)

        numeric_value = d.pop("numericValue", UNSET)

        text_value = d.pop("textValue", UNSET)

        y_output = cls(
            image_value=image_value,
            numeric_value=numeric_value,
            text_value=text_value,
        )

        y_output.additional_properties = d
        return y_output

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
