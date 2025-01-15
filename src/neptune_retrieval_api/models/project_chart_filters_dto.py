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

import datetime
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
from dateutil.parser import isoparse

from ..models.project_chart_filters_dto_states_item import ProjectChartFiltersDTOStatesItem
from ..types import (
    UNSET,
    Unset,
)

if TYPE_CHECKING:
    from ..models.time_duration_dto import TimeDurationDTO


T = TypeVar("T", bound="ProjectChartFiltersDTO")


@_attrs_define
class ProjectChartFiltersDTO:
    """
    Attributes:
        owners (List[str]): Filtering owners
        states (List[ProjectChartFiltersDTOStatesItem]): Filtering states
        tags (List[str]): Filtering tags
        from_ (Union[Unset, datetime.datetime]): Filter experiments since
        time_period (Union[Unset, TimeDurationDTO]):
        to (Union[Unset, datetime.datetime]): Filter experiments up to
    """

    owners: List[str]
    states: List[ProjectChartFiltersDTOStatesItem]
    tags: List[str]
    from_: Union[Unset, datetime.datetime] = UNSET
    time_period: Union[Unset, "TimeDurationDTO"] = UNSET
    to: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        owners = self.owners

        states = []
        for states_item_data in self.states:
            states_item = states_item_data.value
            states.append(states_item)

        tags = self.tags

        from_: Union[Unset, str] = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.isoformat()

        time_period: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.time_period, Unset):
            time_period = self.time_period.to_dict()

        to: Union[Unset, str] = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "owners": owners,
                "states": states,
                "tags": tags,
            }
        )
        if from_ is not UNSET:
            field_dict["from"] = from_
        if time_period is not UNSET:
            field_dict["timePeriod"] = time_period
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.time_duration_dto import TimeDurationDTO

        d = src_dict.copy()
        owners = cast(List[str], d.pop("owners"))

        states = []
        _states = d.pop("states")
        for states_item_data in _states:
            states_item = ProjectChartFiltersDTOStatesItem(states_item_data)

            states.append(states_item)

        tags = cast(List[str], d.pop("tags"))

        _from_ = d.pop("from", UNSET)
        from_: Union[Unset, datetime.datetime]
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = isoparse(_from_)

        _time_period = d.pop("timePeriod", UNSET)
        time_period: Union[Unset, TimeDurationDTO]
        if isinstance(_time_period, Unset):
            time_period = UNSET
        else:
            time_period = TimeDurationDTO.from_dict(_time_period)

        _to = d.pop("to", UNSET)
        to: Union[Unset, datetime.datetime]
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = isoparse(_to)

        project_chart_filters_dto = cls(
            owners=owners,
            states=states,
            tags=tags,
            from_=from_,
            time_period=time_period,
            to=to,
        )

        project_chart_filters_dto.additional_properties = d
        return project_chart_filters_dto

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
