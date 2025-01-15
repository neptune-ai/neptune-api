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
    from ..models.open_range_dto import OpenRangeDTO


T = TypeVar("T", bound="PointFilters")


@_attrs_define
class PointFilters:
    """
    Attributes:
        step_range (Union[Unset, OpenRangeDTO]):
    """

    step_range: Union[Unset, "OpenRangeDTO"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        step_range: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.step_range, Unset):
            step_range = self.step_range.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if step_range is not UNSET:
            field_dict["stepRange"] = step_range

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.open_range_dto import OpenRangeDTO

        d = src_dict.copy()
        _step_range = d.pop("stepRange", UNSET)
        step_range: Union[Unset, OpenRangeDTO]
        if isinstance(_step_range, Unset):
            step_range = UNSET
        else:
            step_range = OpenRangeDTO.from_dict(_step_range)

        point_filters = cls(
            step_range=step_range,
        )

        point_filters.additional_properties = d
        return point_filters

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
