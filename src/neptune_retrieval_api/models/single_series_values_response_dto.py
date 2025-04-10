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
    from ..models.series_values_request_search_after import SeriesValuesRequestSearchAfter
    from ..models.string_series_values_response_dto import StringSeriesValuesResponseDTO


T = TypeVar("T", bound="SingleSeriesValuesResponseDTO")


@_attrs_define
class SingleSeriesValuesResponseDTO:
    """
    Attributes:
        request_id (str):
        search_after (Union[Unset, SeriesValuesRequestSearchAfter]):
        string_series (Union[Unset, StringSeriesValuesResponseDTO]):
    """

    request_id: str
    search_after: Union[Unset, "SeriesValuesRequestSearchAfter"] = UNSET
    string_series: Union[Unset, "StringSeriesValuesResponseDTO"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        request_id = self.request_id

        search_after: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.search_after, Unset):
            search_after = self.search_after.to_dict()

        string_series: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.string_series, Unset):
            string_series = self.string_series.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "requestId": request_id,
            }
        )
        if search_after is not UNSET:
            field_dict["searchAfter"] = search_after
        if string_series is not UNSET:
            field_dict["stringSeries"] = string_series

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.series_values_request_search_after import SeriesValuesRequestSearchAfter
        from ..models.string_series_values_response_dto import StringSeriesValuesResponseDTO

        d = src_dict.copy()
        request_id = d.pop("requestId")

        _search_after = d.pop("searchAfter", UNSET)
        search_after: Union[Unset, SeriesValuesRequestSearchAfter]
        if isinstance(_search_after, Unset):
            search_after = UNSET
        else:
            search_after = SeriesValuesRequestSearchAfter.from_dict(_search_after)

        _string_series = d.pop("stringSeries", UNSET)
        string_series: Union[Unset, StringSeriesValuesResponseDTO]
        if isinstance(_string_series, Unset):
            string_series = UNSET
        else:
            string_series = StringSeriesValuesResponseDTO.from_dict(_string_series)

        single_series_values_response_dto = cls(
            request_id=request_id,
            search_after=search_after,
            string_series=string_series,
        )

        single_series_values_response_dto.additional_properties = d
        return single_series_values_response_dto

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
