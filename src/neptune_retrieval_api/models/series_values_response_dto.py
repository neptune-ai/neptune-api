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
    from ..models.single_series_values_response_dto import SingleSeriesValuesResponseDTO


T = TypeVar("T", bound="SeriesValuesResponseDTO")


@_attrs_define
class SeriesValuesResponseDTO:
    """
    Attributes:
        series (List['SingleSeriesValuesResponseDTO']):
    """

    series: List["SingleSeriesValuesResponseDTO"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        series = []
        for series_item_data in self.series:
            series_item = series_item_data.to_dict()
            series.append(series_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "series": series,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.single_series_values_response_dto import SingleSeriesValuesResponseDTO

        d = src_dict.copy()
        series = []
        _series = d.pop("series")
        for series_item_data in _series:
            series_item = SingleSeriesValuesResponseDTO.from_dict(series_item_data)

            series.append(series_item)

        series_values_response_dto = cls(
            series=series,
        )

        series_values_response_dto.additional_properties = d
        return series_values_response_dto

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
