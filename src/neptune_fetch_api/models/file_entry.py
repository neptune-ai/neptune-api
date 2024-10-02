import datetime
from typing import (
    Any,
    Dict,
    List,
    Type,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.file_entry_file_type import FileEntryFileType
from ..types import (
    UNSET,
    Unset,
)

T = TypeVar("T", bound="FileEntry")


@_attrs_define
class FileEntry:
    """
    Attributes:
        file_type (FileEntryFileType):
        mtime (datetime.datetime):
        name (str):
        size (Union[Unset, int]):
    """

    file_type: FileEntryFileType
    mtime: datetime.datetime
    name: str
    size: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        file_type = self.file_type.value

        mtime = self.mtime.isoformat()

        name = self.name

        size = self.size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fileType": file_type,
                "mtime": mtime,
                "name": name,
            }
        )
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        file_type = FileEntryFileType(d.pop("fileType"))

        mtime = isoparse(d.pop("mtime"))

        name = d.pop("name")

        size = d.pop("size", UNSET)

        file_entry = cls(
            file_type=file_type,
            mtime=mtime,
            name=name,
            size=size,
        )

        file_entry.additional_properties = d
        return file_entry

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
