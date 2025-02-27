#
# Copyright (c) 2025, Neptune Labs Sp. z o.o.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
        include_preview (Union[Unset, bool]):
        lineage (Union[Unset, CustomMetricLineage]):
    """

    attributes: List[str]
    custom_id: str
    holder: "AttributesHolderIdentifier"
    custom_y_formula: Union[Unset, str] = UNSET
    include_preview: Union[Unset, bool] = UNSET
    lineage: Union[Unset, CustomMetricLineage] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attributes = self.attributes

        custom_id = self.custom_id

        holder = self.holder.to_dict()

        custom_y_formula = self.custom_y_formula

        include_preview = self.include_preview

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
        if include_preview is not UNSET:
            field_dict["includePreview"] = include_preview
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

        include_preview = d.pop("includePreview", UNSET)

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
            include_preview=include_preview,
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
