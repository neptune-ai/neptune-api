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
    from ..models.point_value_dto import PointValueDTO


T = TypeVar("T", bound="LimitedChannelValuesDTO")


@_attrs_define
class LimitedChannelValuesDTO:
    """
    Attributes:
        channel_id (str):
        total_item_count (int):
        values (List['PointValueDTO']):
    """

    channel_id: str
    total_item_count: int
    values: List["PointValueDTO"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        channel_id = self.channel_id

        total_item_count = self.total_item_count

        values = []
        for values_item_data in self.values:
            values_item = values_item_data.to_dict()
            values.append(values_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channelId": channel_id,
                "totalItemCount": total_item_count,
                "values": values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.point_value_dto import PointValueDTO

        d = src_dict.copy()
        channel_id = d.pop("channelId")

        total_item_count = d.pop("totalItemCount")

        values = []
        _values = d.pop("values")
        for values_item_data in _values:
            values_item = PointValueDTO.from_dict(values_item_data)

            values.append(values_item)

        limited_channel_values_dto = cls(
            channel_id=channel_id,
            total_item_count=total_item_count,
            values=values,
        )

        limited_channel_values_dto.additional_properties = d
        return limited_channel_values_dto

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
