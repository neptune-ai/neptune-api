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

T = TypeVar("T", bound="ProjectChartMetricDTO")


@_attrs_define
class ProjectChartMetricDTO:
    """
    Attributes:
        name (Union[Unset, str]):
        use_function (Union[Unset, bool]):
        use_value (Union[Unset, bool]):
    """

    name: Union[Unset, str] = UNSET
    use_function: Union[Unset, bool] = UNSET
    use_value: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        use_function = self.use_function

        use_value = self.use_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if use_function is not UNSET:
            field_dict["useFunction"] = use_function
        if use_value is not UNSET:
            field_dict["useValue"] = use_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        use_function = d.pop("useFunction", UNSET)

        use_value = d.pop("useValue", UNSET)

        project_chart_metric_dto = cls(
            name=name,
            use_function=use_function,
            use_value=use_value,
        )

        project_chart_metric_dto.additional_properties = d
        return project_chart_metric_dto

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
