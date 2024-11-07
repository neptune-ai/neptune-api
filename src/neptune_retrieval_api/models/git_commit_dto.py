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

T = TypeVar("T", bound="GitCommitDTO")


@_attrs_define
class GitCommitDTO:
    """
    Attributes:
        author_email (str):
        author_name (str):
        commit_date (datetime.datetime):
        commit_id (str):
        message (str):
    """

    author_email: str
    author_name: str
    commit_date: datetime.datetime
    commit_id: str
    message: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        author_email = self.author_email

        author_name = self.author_name

        commit_date = self.commit_date.isoformat()

        commit_id = self.commit_id

        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "authorEmail": author_email,
                "authorName": author_name,
                "commitDate": commit_date,
                "commitId": commit_id,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        author_email = d.pop("authorEmail")

        author_name = d.pop("authorName")

        commit_date = isoparse(d.pop("commitDate"))

        commit_id = d.pop("commitId")

        message = d.pop("message")

        git_commit_dto = cls(
            author_email=author_email,
            author_name=author_name,
            commit_date=commit_date,
            commit_id=commit_id,
            message=message,
        )

        git_commit_dto.additional_properties = d
        return git_commit_dto

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
