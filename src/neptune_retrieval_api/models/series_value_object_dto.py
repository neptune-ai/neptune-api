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

from ..types import (
    UNSET,
    Unset,
)

if TYPE_CHECKING:
    from ..models.file_ref_series_value_object_dto import FileRefSeriesValueObjectDTO
    from ..models.histogram_series_value_object_dto import HistogramSeriesValueObjectDTO


T = TypeVar("T", bound="SeriesValueObjectDTO")


@_attrs_define
class SeriesValueObjectDTO:
    """
    Attributes:
        file_ref (Union[Unset, FileRefSeriesValueObjectDTO]):
        histogram (Union[Unset, HistogramSeriesValueObjectDTO]):
        string_value (Union[Unset, str]):
    """

    file_ref: Union[Unset, "FileRefSeriesValueObjectDTO"] = UNSET
    histogram: Union[Unset, "HistogramSeriesValueObjectDTO"] = UNSET
    string_value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        file_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.file_ref, Unset):
            file_ref = self.file_ref.to_dict()

        histogram: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.histogram, Unset):
            histogram = self.histogram.to_dict()

        string_value = self.string_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file_ref is not UNSET:
            field_dict["fileRef"] = file_ref
        if histogram is not UNSET:
            field_dict["histogram"] = histogram
        if string_value is not UNSET:
            field_dict["stringValue"] = string_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.file_ref_series_value_object_dto import FileRefSeriesValueObjectDTO
        from ..models.histogram_series_value_object_dto import HistogramSeriesValueObjectDTO

        d = src_dict.copy()
        _file_ref = d.pop("fileRef", UNSET)
        file_ref: Union[Unset, FileRefSeriesValueObjectDTO]
        if isinstance(_file_ref, Unset):
            file_ref = UNSET
        else:
            file_ref = FileRefSeriesValueObjectDTO.from_dict(_file_ref)

        _histogram = d.pop("histogram", UNSET)
        histogram: Union[Unset, HistogramSeriesValueObjectDTO]
        if isinstance(_histogram, Unset):
            histogram = UNSET
        else:
            histogram = HistogramSeriesValueObjectDTO.from_dict(_histogram)

        string_value = d.pop("stringValue", UNSET)

        series_value_object_dto = cls(
            file_ref=file_ref,
            histogram=histogram,
            string_value=string_value,
        )

        series_value_object_dto.additional_properties = d
        return series_value_object_dto

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
