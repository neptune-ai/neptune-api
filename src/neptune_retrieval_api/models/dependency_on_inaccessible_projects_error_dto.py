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
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dependency_on_inaccessible_projects_error_dto_error_type import (
    DependencyOnInaccessibleProjectsErrorDTOErrorType,
)

T = TypeVar("T", bound="DependencyOnInaccessibleProjectsErrorDTO")


@_attrs_define
class DependencyOnInaccessibleProjectsErrorDTO:
    """
    Attributes:
        error_type (DependencyOnInaccessibleProjectsErrorDTOErrorType): Error type.
        inaccessible_projects (List[str]): Fully qualified names (`<workspace name>/<project name>`) of the projects
            inaccessible to the user calling the API.
        message (str): Human-readable error message.
    """

    error_type: DependencyOnInaccessibleProjectsErrorDTOErrorType
    inaccessible_projects: List[str]
    message: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error_type = self.error_type.value

        inaccessible_projects = self.inaccessible_projects

        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "errorType": error_type,
                "inaccessibleProjects": inaccessible_projects,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        error_type = DependencyOnInaccessibleProjectsErrorDTOErrorType(d.pop("errorType"))

        inaccessible_projects = cast(List[str], d.pop("inaccessibleProjects"))

        message = d.pop("message")

        dependency_on_inaccessible_projects_error_dto = cls(
            error_type=error_type,
            inaccessible_projects=inaccessible_projects,
            message=message,
        )

        dependency_on_inaccessible_projects_error_dto.additional_properties = d
        return dependency_on_inaccessible_projects_error_dto

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
