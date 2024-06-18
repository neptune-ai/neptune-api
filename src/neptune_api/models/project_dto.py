from typing import (
    Any,
    Dict,
    List,
    Type,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ProjectDTO")


@_attrs_define
class ProjectDTO:
    """
    Attributes:
        name (str):
        organization_name (str):
        version (int):
        id (str):
        project_key (str):
        organization_id (str):
    """

    name: str
    organization_name: str
    version: int
    id: str
    project_key: str
    organization_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        organization_name = self.organization_name

        version = self.version

        id = self.id

        project_key = self.project_key

        organization_id = self.organization_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "organizationName": organization_name,
                "version": version,
                "id": id,
                "projectKey": project_key,
                "organizationId": organization_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        organization_name = d.pop("organizationName")

        version = d.pop("version")

        id = d.pop("id")

        project_key = d.pop("projectKey")

        organization_id = d.pop("organizationId")

        project_dto = cls(
            name=name,
            organization_name=organization_name,
            version=version,
            id=id,
            project_key=project_key,
            organization_id=organization_id,
        )

        project_dto.additional_properties = d
        return project_dto

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
