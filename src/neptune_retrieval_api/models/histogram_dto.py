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

from ..models.histogram_dto_type import HistogramDTOType
from ..types import (
    UNSET,
    Unset,
)

T = TypeVar("T", bound="HistogramDTO")


@_attrs_define
class HistogramDTO:
    """
    Attributes:
        edges (Union[Unset, List[float]]):
        type (Union[Unset, HistogramDTOType]):
        values (Union[Unset, List[float]]):
    """

    edges: Union[Unset, List[float]] = UNSET
    type: Union[Unset, HistogramDTOType] = UNSET
    values: Union[Unset, List[float]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        edges: Union[Unset, List[float]] = UNSET
        if not isinstance(self.edges, Unset):
            edges = self.edges

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        values: Union[Unset, List[float]] = UNSET
        if not isinstance(self.values, Unset):
            values = self.values

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if edges is not UNSET:
            field_dict["edges"] = edges
        if type is not UNSET:
            field_dict["type"] = type
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        edges = cast(List[float], d.pop("edges", UNSET))

        _type = d.pop("type", UNSET)
        type: Union[Unset, HistogramDTOType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = HistogramDTOType(_type)

        values = cast(List[float], d.pop("values", UNSET))

        histogram_dto = cls(
            edges=edges,
            type=type,
            values=values,
        )

        histogram_dto.additional_properties = d
        return histogram_dto

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
