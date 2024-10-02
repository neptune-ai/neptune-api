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

from ..models.time_series_lineage import TimeSeriesLineage
from ..types import (
    UNSET,
    Unset,
)

if TYPE_CHECKING:
    from ..models.attributes_holder_identifier import AttributesHolderIdentifier


T = TypeVar("T", bound="TimeSeries")


@_attrs_define
class TimeSeries:
    """
    Attributes:
        attribute (str):
        holder (AttributesHolderIdentifier):
        lineage (Union[Unset, TimeSeriesLineage]):
    """

    attribute: str
    holder: "AttributesHolderIdentifier"
    lineage: Union[Unset, TimeSeriesLineage] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attribute = self.attribute

        holder = self.holder.to_dict()

        lineage: Union[Unset, str] = UNSET
        if not isinstance(self.lineage, Unset):
            lineage = self.lineage.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attribute": attribute,
                "holder": holder,
            }
        )
        if lineage is not UNSET:
            field_dict["lineage"] = lineage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.attributes_holder_identifier import AttributesHolderIdentifier

        d = src_dict.copy()
        attribute = d.pop("attribute")

        holder = AttributesHolderIdentifier.from_dict(d.pop("holder"))

        _lineage = d.pop("lineage", UNSET)
        lineage: Union[Unset, TimeSeriesLineage]
        if isinstance(_lineage, Unset):
            lineage = UNSET
        else:
            lineage = TimeSeriesLineage(_lineage)

        time_series = cls(
            attribute=attribute,
            holder=holder,
            lineage=lineage,
        )

        time_series.additional_properties = d
        return time_series

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
