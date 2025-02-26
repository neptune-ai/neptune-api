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
    from ..models.report_version_metadata_dto import ReportVersionMetadataDTO


T = TypeVar("T", bound="ReportVersionListDTO")


@_attrs_define
class ReportVersionListDTO:
    """
    Attributes:
        report_versions_metadata (List['ReportVersionMetadataDTO']):
        total (int):
    """

    report_versions_metadata: List["ReportVersionMetadataDTO"]
    total: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        report_versions_metadata = []
        for report_versions_metadata_item_data in self.report_versions_metadata:
            report_versions_metadata_item = report_versions_metadata_item_data.to_dict()
            report_versions_metadata.append(report_versions_metadata_item)

        total = self.total

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reportVersionsMetadata": report_versions_metadata,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.report_version_metadata_dto import ReportVersionMetadataDTO

        d = src_dict.copy()
        report_versions_metadata = []
        _report_versions_metadata = d.pop("reportVersionsMetadata")
        for report_versions_metadata_item_data in _report_versions_metadata:
            report_versions_metadata_item = ReportVersionMetadataDTO.from_dict(report_versions_metadata_item_data)

            report_versions_metadata.append(report_versions_metadata_item)

        total = d.pop("total")

        report_version_list_dto = cls(
            report_versions_metadata=report_versions_metadata,
            total=total,
        )

        report_version_list_dto.additional_properties = d
        return report_version_list_dto

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
