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
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.attribute_type_dto import AttributeTypeDTO
from ..types import (
    UNSET,
    Unset,
)

if TYPE_CHECKING:
    from ..models.float_series_attribute_config_dto import FloatSeriesAttributeConfigDTO


T = TypeVar("T", bound="FloatSeriesAttributeDTO")


@_attrs_define
class FloatSeriesAttributeDTO:
    """
    Attributes:
        attribute_name (str):
        attribute_type (AttributeTypeDTO):
        config (FloatSeriesAttributeConfigDTO):
        has_preview (bool):
        average (Union[Unset, float]):
        last (Union[Unset, float]):
        last_step (Union[Unset, float]):
        max_ (Union[Unset, float]):
        min_ (Union[Unset, float]):
        variance (Union[Unset, float]):
    """

    attribute_name: str
    attribute_type: AttributeTypeDTO
    config: "FloatSeriesAttributeConfigDTO"
    has_preview: bool
    average: Union[Unset, float] = UNSET
    last: Union[Unset, float] = UNSET
    last_step: Union[Unset, float] = UNSET
    max_: Union[Unset, float] = UNSET
    min_: Union[Unset, float] = UNSET
    variance: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attribute_name = self.attribute_name

        attribute_type = self.attribute_type.value

        config = self.config.to_dict()

        has_preview = self.has_preview

        average = self.average

        last = self.last

        last_step = self.last_step

        max_ = self.max_

        min_ = self.min_

        variance = self.variance

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attributeName": attribute_name,
                "attributeType": attribute_type,
                "config": config,
                "hasPreview": has_preview,
            }
        )
        if average is not UNSET:
            field_dict["average"] = average
        if last is not UNSET:
            field_dict["last"] = last
        if last_step is not UNSET:
            field_dict["lastStep"] = last_step
        if max_ is not UNSET:
            field_dict["max"] = max_
        if min_ is not UNSET:
            field_dict["min"] = min_
        if variance is not UNSET:
            field_dict["variance"] = variance

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.float_series_attribute_config_dto import FloatSeriesAttributeConfigDTO

        d = src_dict.copy()
        attribute_name = d.pop("attributeName")

        attribute_type = AttributeTypeDTO(d.pop("attributeType"))

        config = FloatSeriesAttributeConfigDTO.from_dict(d.pop("config"))

        has_preview = d.pop("hasPreview")

        average = d.pop("average", UNSET)

        last = d.pop("last", UNSET)

        last_step = d.pop("lastStep", UNSET)

        max_ = d.pop("max", UNSET)

        min_ = d.pop("min", UNSET)

        variance = d.pop("variance", UNSET)

        float_series_attribute_dto = cls(
            attribute_name=attribute_name,
            attribute_type=attribute_type,
            config=config,
            has_preview=has_preview,
            average=average,
            last=last,
            last_step=last_step,
            max_=max_,
            min_=min_,
            variance=variance,
        )

        float_series_attribute_dto.additional_properties = d
        return float_series_attribute_dto

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
