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
    from ..models.line import Line
    from ..models.scatter import Scatter


T = TypeVar("T", bound="PlotMode")


@_attrs_define
class PlotMode:
    """
    Attributes:
        line (Union[Unset, Line]):
        scatter (Union[Unset, Scatter]):
    """

    line: Union[Unset, "Line"] = UNSET
    scatter: Union[Unset, "Scatter"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        line: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.line, Unset):
            line = self.line.to_dict()

        scatter: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.scatter, Unset):
            scatter = self.scatter.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if line is not UNSET:
            field_dict["line"] = line
        if scatter is not UNSET:
            field_dict["scatter"] = scatter

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.line import Line
        from ..models.scatter import Scatter

        d = src_dict.copy()
        _line = d.pop("line", UNSET)
        line: Union[Unset, Line]
        if isinstance(_line, Unset):
            line = UNSET
        else:
            line = Line.from_dict(_line)

        _scatter = d.pop("scatter", UNSET)
        scatter: Union[Unset, Scatter]
        if isinstance(_scatter, Unset):
            scatter = UNSET
        else:
            scatter = Scatter.from_dict(_scatter)

        plot_mode = cls(
            line=line,
            scatter=scatter,
        )

        plot_mode.additional_properties = d
        return plot_mode

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
