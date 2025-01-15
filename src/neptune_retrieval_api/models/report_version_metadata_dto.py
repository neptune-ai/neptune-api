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

from ..types import (
    UNSET,
    Unset,
)

if TYPE_CHECKING:
    from ..models.report_version_content_preview_dto import ReportVersionContentPreviewDTO


T = TypeVar("T", bound="ReportVersionMetadataDTO")


@_attrs_define
class ReportVersionMetadataDTO:
    """
    Attributes:
        draft (bool):
        external_projects_dependencies (List[str]): Projects that this report version depends on, other than the project
            that the report is in. In case the user calling the API does not have access to some of them, the version will
            not be returned. The goal is to avoid a round trip to the server querying for access to the projects.
        report_id (str):
        version_author (str):
        version_content_preview (ReportVersionContentPreviewDTO):
        version_creation_time (datetime.datetime):
        version_id (str):
        version_last_modification_time (datetime.datetime):
        version_description (Union[Unset, str]):
        version_name (Union[Unset, str]):
    """

    draft: bool
    external_projects_dependencies: List[str]
    report_id: str
    version_author: str
    version_content_preview: "ReportVersionContentPreviewDTO"
    version_creation_time: datetime.datetime
    version_id: str
    version_last_modification_time: datetime.datetime
    version_description: Union[Unset, str] = UNSET
    version_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        draft = self.draft

        external_projects_dependencies = self.external_projects_dependencies

        report_id = self.report_id

        version_author = self.version_author

        version_content_preview = self.version_content_preview.to_dict()

        version_creation_time = self.version_creation_time.isoformat()

        version_id = self.version_id

        version_last_modification_time = self.version_last_modification_time.isoformat()

        version_description = self.version_description

        version_name = self.version_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "draft": draft,
                "externalProjectsDependencies": external_projects_dependencies,
                "reportId": report_id,
                "versionAuthor": version_author,
                "versionContentPreview": version_content_preview,
                "versionCreationTime": version_creation_time,
                "versionId": version_id,
                "versionLastModificationTime": version_last_modification_time,
            }
        )
        if version_description is not UNSET:
            field_dict["versionDescription"] = version_description
        if version_name is not UNSET:
            field_dict["versionName"] = version_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.report_version_content_preview_dto import ReportVersionContentPreviewDTO

        d = src_dict.copy()
        draft = d.pop("draft")

        external_projects_dependencies = cast(List[str], d.pop("externalProjectsDependencies"))

        report_id = d.pop("reportId")

        version_author = d.pop("versionAuthor")

        version_content_preview = ReportVersionContentPreviewDTO.from_dict(d.pop("versionContentPreview"))

        version_creation_time = isoparse(d.pop("versionCreationTime"))

        version_id = d.pop("versionId")

        version_last_modification_time = isoparse(d.pop("versionLastModificationTime"))

        version_description = d.pop("versionDescription", UNSET)

        version_name = d.pop("versionName", UNSET)

        report_version_metadata_dto = cls(
            draft=draft,
            external_projects_dependencies=external_projects_dependencies,
            report_id=report_id,
            version_author=version_author,
            version_content_preview=version_content_preview,
            version_creation_time=version_creation_time,
            version_id=version_id,
            version_last_modification_time=version_last_modification_time,
            version_description=version_description,
            version_name=version_name,
        )

        report_version_metadata_dto.additional_properties = d
        return report_version_metadata_dto

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
