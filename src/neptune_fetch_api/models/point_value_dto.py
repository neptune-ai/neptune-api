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
    from ..models.y_output import YOutput


T = TypeVar("T", bound="PointValueDTO")


@_attrs_define
class PointValueDTO:
    """
    Attributes:
        timestamp_millis (int):
        y (YOutput):
        x (Union[Unset, float]):
    """

    timestamp_millis: int
    y: "YOutput"
    x: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timestamp_millis = self.timestamp_millis

        y = self.y.to_dict()

        x = self.x

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestampMillis": timestamp_millis,
                "y": y,
            }
        )
        if x is not UNSET:
            field_dict["x"] = x

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.y_output import YOutput

        d = src_dict.copy()
        timestamp_millis = d.pop("timestampMillis")

        y = YOutput.from_dict(d.pop("y"))

        x = d.pop("x", UNSET)

        point_value_dto = cls(
            timestamp_millis=timestamp_millis,
            y=y,
            x=x,
        )

        point_value_dto.additional_properties = d
        return point_value_dto

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
