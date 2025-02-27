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

from ..models.widget_dto_type import WidgetDTOType
from ..types import (
    UNSET,
    Unset,
)

if TYPE_CHECKING:
    from ..models.widget_attribute_dto import WidgetAttributeDTO
    from ..models.widget_dto_options import WidgetDTOOptions


T = TypeVar("T", bound="WidgetDTO")


@_attrs_define
class WidgetDTO:
    """
    Attributes:
        id (str):
        type (WidgetDTOType):
        attribute_name_must_match_regexes (Union[Unset, List[str]]):
        attribute_name_must_not_match_regexes (Union[Unset, List[str]]):
        attributes (Union[Unset, List['WidgetAttributeDTO']]):
        experiment_short_ids (Union[Unset, List[str]]):
        free_text (Union[Unset, str]):
        name (Union[Unset, str]):
        namespaces (Union[Unset, List[str]]):
        options (Union[Unset, WidgetDTOOptions]):
    """

    id: str
    type: WidgetDTOType
    attribute_name_must_match_regexes: Union[Unset, List[str]] = UNSET
    attribute_name_must_not_match_regexes: Union[Unset, List[str]] = UNSET
    attributes: Union[Unset, List["WidgetAttributeDTO"]] = UNSET
    experiment_short_ids: Union[Unset, List[str]] = UNSET
    free_text: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    namespaces: Union[Unset, List[str]] = UNSET
    options: Union[Unset, "WidgetDTOOptions"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        type = self.type.value

        attribute_name_must_match_regexes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.attribute_name_must_match_regexes, Unset):
            attribute_name_must_match_regexes = self.attribute_name_must_match_regexes

        attribute_name_must_not_match_regexes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.attribute_name_must_not_match_regexes, Unset):
            attribute_name_must_not_match_regexes = self.attribute_name_must_not_match_regexes

        attributes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = []
            for attributes_item_data in self.attributes:
                attributes_item = attributes_item_data.to_dict()
                attributes.append(attributes_item)

        experiment_short_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.experiment_short_ids, Unset):
            experiment_short_ids = self.experiment_short_ids

        free_text = self.free_text

        name = self.name

        namespaces: Union[Unset, List[str]] = UNSET
        if not isinstance(self.namespaces, Unset):
            namespaces = self.namespaces

        options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type,
            }
        )
        if attribute_name_must_match_regexes is not UNSET:
            field_dict["attributeNameMustMatchRegexes"] = attribute_name_must_match_regexes
        if attribute_name_must_not_match_regexes is not UNSET:
            field_dict["attributeNameMustNotMatchRegexes"] = attribute_name_must_not_match_regexes
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if experiment_short_ids is not UNSET:
            field_dict["experimentShortIds"] = experiment_short_ids
        if free_text is not UNSET:
            field_dict["freeText"] = free_text
        if name is not UNSET:
            field_dict["name"] = name
        if namespaces is not UNSET:
            field_dict["namespaces"] = namespaces
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.widget_attribute_dto import WidgetAttributeDTO
        from ..models.widget_dto_options import WidgetDTOOptions

        d = src_dict.copy()
        id = d.pop("id")

        type = WidgetDTOType(d.pop("type"))

        attribute_name_must_match_regexes = cast(List[str], d.pop("attributeNameMustMatchRegexes", UNSET))

        attribute_name_must_not_match_regexes = cast(List[str], d.pop("attributeNameMustNotMatchRegexes", UNSET))

        attributes: Union[Unset, List[WidgetAttributeDTO]] = UNSET
        _attributes = d.pop("attributes", UNSET)
        if not isinstance(_attributes, Unset):
            attributes = []
            for attributes_item_data in _attributes:
                attributes_item = WidgetAttributeDTO.from_dict(attributes_item_data)

                attributes.append(attributes_item)

        experiment_short_ids = cast(List[str], d.pop("experimentShortIds", UNSET))

        free_text = d.pop("freeText", UNSET)

        name = d.pop("name", UNSET)

        namespaces = cast(List[str], d.pop("namespaces", UNSET))

        _options = d.pop("options", UNSET)
        options: Union[Unset, WidgetDTOOptions]
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = WidgetDTOOptions.from_dict(_options)

        widget_dto = cls(
            id=id,
            type=type,
            attribute_name_must_match_regexes=attribute_name_must_match_regexes,
            attribute_name_must_not_match_regexes=attribute_name_must_not_match_regexes,
            attributes=attributes,
            experiment_short_ids=experiment_short_ids,
            free_text=free_text,
            name=name,
            namespaces=namespaces,
            options=options,
        )

        widget_dto.additional_properties = d
        return widget_dto

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
