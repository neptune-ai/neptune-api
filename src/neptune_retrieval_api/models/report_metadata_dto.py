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
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.report_version_metadata_dto import ReportVersionMetadataDTO


T = TypeVar("T", bound="ReportMetadataDTO")


@_attrs_define
class ReportMetadataDTO:
    """
    Attributes:
        creation_time (datetime.datetime):
        initial_author (str):
        latest_publish_time (datetime.datetime):
        latest_version_metadata (ReportVersionMetadataDTO):
        report_id (str):
    """

    creation_time: datetime.datetime
    initial_author: str
    latest_publish_time: datetime.datetime
    latest_version_metadata: "ReportVersionMetadataDTO"
    report_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        creation_time = self.creation_time.isoformat()

        initial_author = self.initial_author

        latest_publish_time = self.latest_publish_time.isoformat()

        latest_version_metadata = self.latest_version_metadata.to_dict()

        report_id = self.report_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "creationTime": creation_time,
                "initialAuthor": initial_author,
                "latestPublishTime": latest_publish_time,
                "latestVersionMetadata": latest_version_metadata,
                "reportId": report_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.report_version_metadata_dto import ReportVersionMetadataDTO

        d = src_dict.copy()
        creation_time = isoparse(d.pop("creationTime"))

        initial_author = d.pop("initialAuthor")

        latest_publish_time = isoparse(d.pop("latestPublishTime"))

        latest_version_metadata = ReportVersionMetadataDTO.from_dict(d.pop("latestVersionMetadata"))

        report_id = d.pop("reportId")

        report_metadata_dto = cls(
            creation_time=creation_time,
            initial_author=initial_author,
            latest_publish_time=latest_publish_time,
            latest_version_metadata=latest_version_metadata,
            report_id=report_id,
        )

        report_metadata_dto.additional_properties = d
        return report_metadata_dto

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
