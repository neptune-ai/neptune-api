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

T = TypeVar("T", bound="Alias")


@_attrs_define
class Alias:
    """
    Attributes:
        channels (List[str]):
        id (str):
        name (str):
        project_id (str):
    """

    channels: List[str]
    id: str
    name: str
    project_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        channels = self.channels

        id = self.id

        name = self.name

        project_id = self.project_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channels": channels,
                "id": id,
                "name": name,
                "projectId": project_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        channels = cast(List[str], d.pop("channels"))

        id = d.pop("id")

        name = d.pop("name")

        project_id = d.pop("projectId")

        alias = cls(
            channels=channels,
            id=id,
            name=name,
            project_id=project_id,
        )

        alias.additional_properties = d
        return alias

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
