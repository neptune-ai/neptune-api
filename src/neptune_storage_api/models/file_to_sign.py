from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.permission import Permission

T = TypeVar("T", bound="FileToSign")


@_attrs_define
class FileToSign:
    """
    Attributes:
        path (str):
        permission (Permission):
        project_identifier (str):
    """

    path: str
    permission: Permission
    project_identifier: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        permission = self.permission.value

        project_identifier = self.project_identifier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
                "permission": permission,
                "project_identifier": project_identifier,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        path = d.pop("path")

        permission = Permission(d.pop("permission"))

        project_identifier = d.pop("project_identifier")

        file_to_sign = cls(
            path=path,
            permission=permission,
            project_identifier=project_identifier,
        )

        file_to_sign.additional_properties = d
        return file_to_sign

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
