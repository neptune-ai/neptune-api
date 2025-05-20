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

from ..models.attribute_type_dto import AttributeTypeDTO
from ..models.leaderboard_csv_export_params_dto_export_field_aggregations_item import (
    LeaderboardCsvExportParamsDTOExportFieldAggregationsItem,
)
from ..types import (
    UNSET,
    Unset,
)

if TYPE_CHECKING:
    from ..models.leaderboard_sort_params_dto import LeaderboardSortParamsDTO


T = TypeVar("T", bound="LeaderboardCsvExportParamsDTO")


@_attrs_define
class LeaderboardCsvExportParamsDTO:
    """
    Attributes:
        export_field_aggregations (List[LeaderboardCsvExportParamsDTOExportFieldAggregationsItem]):
        export_field_names (List[str]):
        export_field_types (List[AttributeTypeDTO]):
        export_fields (List[str]):
        zone_offset (int):
        query (Union[Unset, str]):
        sorting (Union[Unset, LeaderboardSortParamsDTO]):
        zone_region (Union[Unset, str]):
    """

    export_field_aggregations: List[LeaderboardCsvExportParamsDTOExportFieldAggregationsItem]
    export_field_names: List[str]
    export_field_types: List[AttributeTypeDTO]
    export_fields: List[str]
    zone_offset: int
    query: Union[Unset, str] = UNSET
    sorting: Union[Unset, "LeaderboardSortParamsDTO"] = UNSET
    zone_region: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        export_field_aggregations = []
        for export_field_aggregations_item_data in self.export_field_aggregations:
            export_field_aggregations_item = export_field_aggregations_item_data.value
            export_field_aggregations.append(export_field_aggregations_item)

        export_field_names = self.export_field_names

        export_field_types = []
        for export_field_types_item_data in self.export_field_types:
            export_field_types_item = export_field_types_item_data.value
            export_field_types.append(export_field_types_item)

        export_fields = self.export_fields

        zone_offset = self.zone_offset

        query = self.query

        sorting: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sorting, Unset):
            sorting = self.sorting.to_dict()

        zone_region = self.zone_region

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "exportFieldAggregations": export_field_aggregations,
                "exportFieldNames": export_field_names,
                "exportFieldTypes": export_field_types,
                "exportFields": export_fields,
                "zoneOffset": zone_offset,
            }
        )
        if query is not UNSET:
            field_dict["query"] = query
        if sorting is not UNSET:
            field_dict["sorting"] = sorting
        if zone_region is not UNSET:
            field_dict["zoneRegion"] = zone_region

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.leaderboard_sort_params_dto import LeaderboardSortParamsDTO

        d = src_dict.copy()
        export_field_aggregations = []
        _export_field_aggregations = d.pop("exportFieldAggregations")
        for export_field_aggregations_item_data in _export_field_aggregations:
            export_field_aggregations_item = LeaderboardCsvExportParamsDTOExportFieldAggregationsItem(
                export_field_aggregations_item_data
            )

            export_field_aggregations.append(export_field_aggregations_item)

        export_field_names = cast(List[str], d.pop("exportFieldNames"))

        export_field_types = []
        _export_field_types = d.pop("exportFieldTypes")
        for export_field_types_item_data in _export_field_types:
            export_field_types_item = AttributeTypeDTO(export_field_types_item_data)

            export_field_types.append(export_field_types_item)

        export_fields = cast(List[str], d.pop("exportFields"))

        zone_offset = d.pop("zoneOffset")

        query = d.pop("query", UNSET)

        _sorting = d.pop("sorting", UNSET)
        sorting: Union[Unset, LeaderboardSortParamsDTO]
        if isinstance(_sorting, Unset):
            sorting = UNSET
        else:
            sorting = LeaderboardSortParamsDTO.from_dict(_sorting)

        zone_region = d.pop("zoneRegion", UNSET)

        leaderboard_csv_export_params_dto = cls(
            export_field_aggregations=export_field_aggregations,
            export_field_names=export_field_names,
            export_field_types=export_field_types,
            export_fields=export_fields,
            zone_offset=zone_offset,
            query=query,
            sorting=sorting,
            zone_region=zone_region,
        )

        leaderboard_csv_export_params_dto.additional_properties = d
        return leaderboard_csv_export_params_dto

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
