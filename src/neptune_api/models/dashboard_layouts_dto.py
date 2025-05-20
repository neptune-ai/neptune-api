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
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.widget_layout_dto import WidgetLayoutDTO


T = TypeVar("T", bound="DashboardLayoutsDTO")


@_attrs_define
class DashboardLayoutsDTO:
    """
    Attributes:
        lg (List['WidgetLayoutDTO']):
        md (List['WidgetLayoutDTO']):
        sm (List['WidgetLayoutDTO']):
        xl (List['WidgetLayoutDTO']):
        xs (List['WidgetLayoutDTO']):
    """

    lg: List["WidgetLayoutDTO"]
    md: List["WidgetLayoutDTO"]
    sm: List["WidgetLayoutDTO"]
    xl: List["WidgetLayoutDTO"]
    xs: List["WidgetLayoutDTO"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        lg = []
        for lg_item_data in self.lg:
            lg_item = lg_item_data.to_dict()
            lg.append(lg_item)

        md = []
        for md_item_data in self.md:
            md_item = md_item_data.to_dict()
            md.append(md_item)

        sm = []
        for sm_item_data in self.sm:
            sm_item = sm_item_data.to_dict()
            sm.append(sm_item)

        xl = []
        for xl_item_data in self.xl:
            xl_item = xl_item_data.to_dict()
            xl.append(xl_item)

        xs = []
        for xs_item_data in self.xs:
            xs_item = xs_item_data.to_dict()
            xs.append(xs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lg": lg,
                "md": md,
                "sm": sm,
                "xl": xl,
                "xs": xs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.widget_layout_dto import WidgetLayoutDTO

        d = src_dict.copy()
        lg = []
        _lg = d.pop("lg")
        for lg_item_data in _lg:
            lg_item = WidgetLayoutDTO.from_dict(lg_item_data)

            lg.append(lg_item)

        md = []
        _md = d.pop("md")
        for md_item_data in _md:
            md_item = WidgetLayoutDTO.from_dict(md_item_data)

            md.append(md_item)

        sm = []
        _sm = d.pop("sm")
        for sm_item_data in _sm:
            sm_item = WidgetLayoutDTO.from_dict(sm_item_data)

            sm.append(sm_item)

        xl = []
        _xl = d.pop("xl")
        for xl_item_data in _xl:
            xl_item = WidgetLayoutDTO.from_dict(xl_item_data)

            xl.append(xl_item)

        xs = []
        _xs = d.pop("xs")
        for xs_item_data in _xs:
            xs_item = WidgetLayoutDTO.from_dict(xs_item_data)

            xs.append(xs_item)

        dashboard_layouts_dto = cls(
            lg=lg,
            md=md,
            sm=sm,
            xl=xl,
            xs=xs,
        )

        dashboard_layouts_dto.additional_properties = d
        return dashboard_layouts_dto

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
