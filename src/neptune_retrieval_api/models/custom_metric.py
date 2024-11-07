from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    Type,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.custom_metric_lineage import CustomMetricLineage
from ..types import (
    UNSET,
    Unset,
)

if TYPE_CHECKING:
    from ..models.attributes_holder_identifier import AttributesHolderIdentifier


T = TypeVar("T", bound="CustomMetric")


@_attrs_define
class CustomMetric:
    """
    Attributes:
        attributes (List[str]):
        custom_id (str):
        holder (AttributesHolderIdentifier):
        custom_y_formula (Union[Unset, str]):
        lineage (Union[Unset, CustomMetricLineage]):
    """

    attributes: List[str]
    custom_id: str
    holder: "AttributesHolderIdentifier"
    custom_y_formula: Union[Unset, str] = UNSET
    lineage: Union[Unset, CustomMetricLineage] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attributes = self.attributes

        custom_id = self.custom_id

        holder = self.holder.to_dict()

        custom_y_formula = self.custom_y_formula

        lineage: Union[Unset, str] = UNSET
        if not isinstance(self.lineage, Unset):
            lineage = self.lineage.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attributes": attributes,
                "customId": custom_id,
                "holder": holder,
            }
        )
        if custom_y_formula is not UNSET:
            field_dict["customYFormula"] = custom_y_formula
        if lineage is not UNSET:
            field_dict["lineage"] = lineage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.attributes_holder_identifier import AttributesHolderIdentifier

        d = src_dict.copy()
        attributes = cast(List[str], d.pop("attributes"))

        custom_id = d.pop("customId")

        holder = AttributesHolderIdentifier.from_dict(d.pop("holder"))

        custom_y_formula = d.pop("customYFormula", UNSET)

        _lineage = d.pop("lineage", UNSET)
        lineage: Union[Unset, CustomMetricLineage]
        if isinstance(_lineage, Unset):
            lineage = UNSET
        else:
            lineage = CustomMetricLineage(_lineage)

        custom_metric = cls(
            attributes=attributes,
            custom_id=custom_id,
            holder=holder,
            custom_y_formula=custom_y_formula,
            lineage=lineage,
        )

        custom_metric.additional_properties = d
        return custom_metric

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
