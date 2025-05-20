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
    from ..models.report_metadata_dto import ReportMetadataDTO


T = TypeVar("T", bound="ReportMetadataListDTO")


@_attrs_define
class ReportMetadataListDTO:
    """
    Attributes:
        reports_metadata (List['ReportMetadataDTO']):
    """

    reports_metadata: List["ReportMetadataDTO"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reports_metadata = []
        for reports_metadata_item_data in self.reports_metadata:
            reports_metadata_item = reports_metadata_item_data.to_dict()
            reports_metadata.append(reports_metadata_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reportsMetadata": reports_metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.report_metadata_dto import ReportMetadataDTO

        d = src_dict.copy()
        reports_metadata = []
        _reports_metadata = d.pop("reportsMetadata")
        for reports_metadata_item_data in _reports_metadata:
            reports_metadata_item = ReportMetadataDTO.from_dict(reports_metadata_item_data)

            reports_metadata.append(reports_metadata_item)

        report_metadata_list_dto = cls(
            reports_metadata=reports_metadata,
        )

        report_metadata_list_dto.additional_properties = d
        return report_metadata_list_dto

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
