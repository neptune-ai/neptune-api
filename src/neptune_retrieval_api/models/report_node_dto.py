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

from ..models.report_node_dto_type import ReportNodeDTOType
from ..types import (
    UNSET,
    Unset,
)

if TYPE_CHECKING:
    from ..models.report_node_grid_dto import ReportNodeGridDTO


T = TypeVar("T", bound="ReportNodeDTO")


@_attrs_define
class ReportNodeDTO:
    """
    Attributes:
        id (str):
        type (ReportNodeDTOType):
        grid_properties (Union[Unset, ReportNodeGridDTO]):
        name (Union[Unset, str]):
    """

    id: str
    type: ReportNodeDTOType
    grid_properties: Union[Unset, "ReportNodeGridDTO"] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        type = self.type.value

        grid_properties: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.grid_properties, Unset):
            grid_properties = self.grid_properties.to_dict()

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type,
            }
        )
        if grid_properties is not UNSET:
            field_dict["gridProperties"] = grid_properties
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.report_node_grid_dto import ReportNodeGridDTO

        d = src_dict.copy()
        id = d.pop("id")

        type = ReportNodeDTOType(d.pop("type"))

        _grid_properties = d.pop("gridProperties", UNSET)
        grid_properties: Union[Unset, ReportNodeGridDTO]
        if isinstance(_grid_properties, Unset):
            grid_properties = UNSET
        else:
            grid_properties = ReportNodeGridDTO.from_dict(_grid_properties)

        name = d.pop("name", UNSET)

        report_node_dto = cls(
            id=id,
            type=type,
            grid_properties=grid_properties,
            name=name,
        )

        report_node_dto.additional_properties = d
        return report_node_dto

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
