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
    from ..models.plot_mode import PlotMode
    from ..models.point_filters import PointFilters
    from ..models.scale import Scale


T = TypeVar("T", bound="View")


@_attrs_define
class View:
    """
    Attributes:
        max_unique_x (int):
        plot_mode (PlotMode):
        xscale (Scale):
        yscale (Scale):
        from_ (Union[Unset, float]):
        point_filters (Union[Unset, PointFilters]):
        to (Union[Unset, float]):
    """

    max_unique_x: int
    plot_mode: "PlotMode"
    xscale: "Scale"
    yscale: "Scale"
    from_: Union[Unset, float] = UNSET
    point_filters: Union[Unset, "PointFilters"] = UNSET
    to: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        max_unique_x = self.max_unique_x

        plot_mode = self.plot_mode.to_dict()

        xscale = self.xscale.to_dict()

        yscale = self.yscale.to_dict()

        from_ = self.from_

        point_filters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.point_filters, Unset):
            point_filters = self.point_filters.to_dict()

        to = self.to

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "maxUniqueX": max_unique_x,
                "plotMode": plot_mode,
                "xscale": xscale,
                "yscale": yscale,
            }
        )
        if from_ is not UNSET:
            field_dict["from"] = from_
        if point_filters is not UNSET:
            field_dict["pointFilters"] = point_filters
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.plot_mode import PlotMode
        from ..models.point_filters import PointFilters
        from ..models.scale import Scale

        d = src_dict.copy()
        max_unique_x = d.pop("maxUniqueX")

        plot_mode = PlotMode.from_dict(d.pop("plotMode"))

        xscale = Scale.from_dict(d.pop("xscale"))

        yscale = Scale.from_dict(d.pop("yscale"))

        from_ = d.pop("from", UNSET)

        _point_filters = d.pop("pointFilters", UNSET)
        point_filters: Union[Unset, PointFilters]
        if isinstance(_point_filters, Unset):
            point_filters = UNSET
        else:
            point_filters = PointFilters.from_dict(_point_filters)

        to = d.pop("to", UNSET)

        view = cls(
            max_unique_x=max_unique_x,
            plot_mode=plot_mode,
            xscale=xscale,
            yscale=yscale,
            from_=from_,
            point_filters=point_filters,
            to=to,
        )

        view.additional_properties = d
        return view

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
