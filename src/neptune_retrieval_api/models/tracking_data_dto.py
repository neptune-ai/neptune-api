from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    Type,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import (
    UNSET,
    Unset,
)

if TYPE_CHECKING:
    from ..models.experiments_data_dto import ExperimentsDataDTO
    from ..models.notebooks_data_dto import NotebooksDataDTO


T = TypeVar("T", bound="TrackingDataDTO")


@_attrs_define
class TrackingDataDTO:
    """
    Attributes:
        experiments (Union[Unset, ExperimentsDataDTO]):
        identifier (Union[Unset, str]):
        notebooks (Union[Unset, NotebooksDataDTO]):
    """

    experiments: Union[Unset, "ExperimentsDataDTO"] = UNSET
    identifier: Union[Unset, str] = UNSET
    notebooks: Union[Unset, "NotebooksDataDTO"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        experiments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.experiments, Unset):
            experiments = self.experiments.to_dict()

        identifier = self.identifier

        notebooks: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.notebooks, Unset):
            notebooks = self.notebooks.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if experiments is not UNSET:
            field_dict["experiments"] = experiments
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if notebooks is not UNSET:
            field_dict["notebooks"] = notebooks

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.experiments_data_dto import ExperimentsDataDTO
        from ..models.notebooks_data_dto import NotebooksDataDTO

        d = src_dict.copy()
        _experiments = d.pop("experiments", UNSET)
        experiments: Union[Unset, ExperimentsDataDTO]
        if isinstance(_experiments, Unset):
            experiments = UNSET
        else:
            experiments = ExperimentsDataDTO.from_dict(_experiments)

        identifier = d.pop("identifier", UNSET)

        _notebooks = d.pop("notebooks", UNSET)
        notebooks: Union[Unset, NotebooksDataDTO]
        if isinstance(_notebooks, Unset):
            notebooks = UNSET
        else:
            notebooks = NotebooksDataDTO.from_dict(_notebooks)

        tracking_data_dto = cls(
            experiments=experiments,
            identifier=identifier,
            notebooks=notebooks,
        )

        tracking_data_dto.additional_properties = d
        return tracking_data_dto

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
