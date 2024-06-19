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
    from ..models.client_versions_config_dto import ClientVersionsConfigDTO
    from ..models.security_dto import SecurityDTO


T = TypeVar("T", bound="ClientConfig")


@_attrs_define
class ClientConfig:
    """
    Attributes:
        api_url (str):
        py_lib_versions (ClientVersionsConfigDTO):
        security (SecurityDTO):
    """

    api_url: str
    py_lib_versions: "ClientVersionsConfigDTO"
    security: "SecurityDTO"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        api_url = self.api_url

        py_lib_versions = self.py_lib_versions.to_dict()

        security = self.security.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiUrl": api_url,
                "pyLibVersions": py_lib_versions,
                "security": security,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_versions_config_dto import ClientVersionsConfigDTO
        from ..models.security_dto import SecurityDTO

        d = src_dict.copy()
        api_url = d.pop("apiUrl")

        py_lib_versions = ClientVersionsConfigDTO.from_dict(d.pop("pyLibVersions"))

        security = SecurityDTO.from_dict(d.pop("security"))

        client_config = cls(
            api_url=api_url,
            py_lib_versions=py_lib_versions,
            security=security,
        )

        client_config.additional_properties = d
        return client_config

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
