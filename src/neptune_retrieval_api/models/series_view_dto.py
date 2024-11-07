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
    from ..models.series_view_point_dto import SeriesViewPointDTO


T = TypeVar("T", bound="SeriesViewDTO")


@_attrs_define
class SeriesViewDTO:
    """
    Attributes:
        attribute_path (str):
        downsampled (bool):
        first_point_index (int):
        holder_identifier (str):
        holder_type (str):
        last_point_index (int):
        max_y (float):
        min_y (float):
        project_id (str):
        project_name (str):
        values (List['SeriesViewPointDTO']):
    """

    attribute_path: str
    downsampled: bool
    first_point_index: int
    holder_identifier: str
    holder_type: str
    last_point_index: int
    max_y: float
    min_y: float
    project_id: str
    project_name: str
    values: List["SeriesViewPointDTO"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attribute_path = self.attribute_path

        downsampled = self.downsampled

        first_point_index = self.first_point_index

        holder_identifier = self.holder_identifier

        holder_type = self.holder_type

        last_point_index = self.last_point_index

        max_y = self.max_y

        min_y = self.min_y

        project_id = self.project_id

        project_name = self.project_name

        values = []
        for values_item_data in self.values:
            values_item = values_item_data.to_dict()
            values.append(values_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attributePath": attribute_path,
                "downsampled": downsampled,
                "firstPointIndex": first_point_index,
                "holderIdentifier": holder_identifier,
                "holderType": holder_type,
                "lastPointIndex": last_point_index,
                "maxY": max_y,
                "minY": min_y,
                "projectId": project_id,
                "projectName": project_name,
                "values": values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.series_view_point_dto import SeriesViewPointDTO

        d = src_dict.copy()
        attribute_path = d.pop("attributePath")

        downsampled = d.pop("downsampled")

        first_point_index = d.pop("firstPointIndex")

        holder_identifier = d.pop("holderIdentifier")

        holder_type = d.pop("holderType")

        last_point_index = d.pop("lastPointIndex")

        max_y = d.pop("maxY")

        min_y = d.pop("minY")

        project_id = d.pop("projectId")

        project_name = d.pop("projectName")

        values = []
        _values = d.pop("values")
        for values_item_data in _values:
            values_item = SeriesViewPointDTO.from_dict(values_item_data)

            values.append(values_item)

        series_view_dto = cls(
            attribute_path=attribute_path,
            downsampled=downsampled,
            first_point_index=first_point_index,
            holder_identifier=holder_identifier,
            holder_type=holder_type,
            last_point_index=last_point_index,
            max_y=max_y,
            min_y=min_y,
            project_id=project_id,
            project_name=project_name,
            values=values,
        )

        series_view_dto.additional_properties = d
        return series_view_dto

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
