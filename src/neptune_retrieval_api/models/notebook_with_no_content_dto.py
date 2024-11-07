import datetime
from typing import (
    Any,
    Dict,
    List,
    Type,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="NotebookWithNoContentDTO")


@_attrs_define
class NotebookWithNoContentDTO:
    """
    Attributes:
        creation_time (datetime.datetime):
        description (str):
        id (str):
        owner (str):
        project_id (str):
    """

    creation_time: datetime.datetime
    description: str
    id: str
    owner: str
    project_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        creation_time = self.creation_time.isoformat()

        description = self.description

        id = self.id

        owner = self.owner

        project_id = self.project_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "creationTime": creation_time,
                "description": description,
                "id": id,
                "owner": owner,
                "projectId": project_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        creation_time = isoparse(d.pop("creationTime"))

        description = d.pop("description")

        id = d.pop("id")

        owner = d.pop("owner")

        project_id = d.pop("projectId")

        notebook_with_no_content_dto = cls(
            creation_time=creation_time,
            description=description,
            id=id,
            owner=owner,
            project_id=project_id,
        )

        notebook_with_no_content_dto.additional_properties = d
        return notebook_with_no_content_dto

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
