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
    from ..models.bool_attribute_dto import BoolAttributeDTO
    from ..models.complex_attribute_dto import ComplexAttributeDTO
    from ..models.datetime_attribute_dto import DatetimeAttributeDTO
    from ..models.experiment_state_attribute_dto import ExperimentStateAttributeDTO
    from ..models.file_attribute_dto import FileAttributeDTO
    from ..models.file_set_attribute_dto import FileSetAttributeDTO
    from ..models.float_attribute_dto import FloatAttributeDTO
    from ..models.float_series_attribute_dto import FloatSeriesAttributeDTO
    from ..models.git_info_dto import GitInfoDTO
    from ..models.image_series_attribute_dto import ImageSeriesAttributeDTO
    from ..models.int_attribute_dto import IntAttributeDTO
    from ..models.notebook_ref_attribute_dto import NotebookRefAttributeDTO
    from ..models.string_attribute_dto import StringAttributeDTO
    from ..models.string_series_attribute_dto import StringSeriesAttributeDTO
    from ..models.string_set_attribute_dto import StringSetAttributeDTO


T = TypeVar("T", bound="AttributeDTO")


@_attrs_define
class AttributeDTO:
    """
    Attributes:
        name (str):
        type (AttributeTypeDTO):
        bool_properties (Union[Unset, BoolAttributeDTO]):
        complex_properties (Union[Unset, ComplexAttributeDTO]):
        datetime_properties (Union[Unset, DatetimeAttributeDTO]):
        experiment_state_properties (Union[Unset, ExperimentStateAttributeDTO]):
        file_properties (Union[Unset, FileAttributeDTO]):
        file_set_properties (Union[Unset, FileSetAttributeDTO]):
        float_properties (Union[Unset, FloatAttributeDTO]):
        float_series_properties (Union[Unset, FloatSeriesAttributeDTO]):
        git_ref_properties (Union[Unset, GitInfoDTO]):
        image_series_properties (Union[Unset, ImageSeriesAttributeDTO]):
        int_properties (Union[Unset, IntAttributeDTO]):
        notebook_ref_properties (Union[Unset, NotebookRefAttributeDTO]):
        string_properties (Union[Unset, StringAttributeDTO]):
        string_series_properties (Union[Unset, StringSeriesAttributeDTO]):
        string_set_properties (Union[Unset, StringSetAttributeDTO]):
    """

    name: str
    type: AttributeTypeDTO
    bool_properties: Union[Unset, "BoolAttributeDTO"] = UNSET
    complex_properties: Union[Unset, "ComplexAttributeDTO"] = UNSET
    datetime_properties: Union[Unset, "DatetimeAttributeDTO"] = UNSET
    experiment_state_properties: Union[Unset, "ExperimentStateAttributeDTO"] = UNSET
    file_properties: Union[Unset, "FileAttributeDTO"] = UNSET
    file_set_properties: Union[Unset, "FileSetAttributeDTO"] = UNSET
    float_properties: Union[Unset, "FloatAttributeDTO"] = UNSET
    float_series_properties: Union[Unset, "FloatSeriesAttributeDTO"] = UNSET
    git_ref_properties: Union[Unset, "GitInfoDTO"] = UNSET
    image_series_properties: Union[Unset, "ImageSeriesAttributeDTO"] = UNSET
    int_properties: Union[Unset, "IntAttributeDTO"] = UNSET
    notebook_ref_properties: Union[Unset, "NotebookRefAttributeDTO"] = UNSET
    string_properties: Union[Unset, "StringAttributeDTO"] = UNSET
    string_series_properties: Union[Unset, "StringSeriesAttributeDTO"] = UNSET
    string_set_properties: Union[Unset, "StringSetAttributeDTO"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        type = self.type.value

        bool_properties: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.bool_properties, Unset):
            bool_properties = self.bool_properties.to_dict()

        complex_properties: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.complex_properties, Unset):
            complex_properties = self.complex_properties.to_dict()

        datetime_properties: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.datetime_properties, Unset):
            datetime_properties = self.datetime_properties.to_dict()

        experiment_state_properties: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.experiment_state_properties, Unset):
            experiment_state_properties = self.experiment_state_properties.to_dict()

        file_properties: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.file_properties, Unset):
            file_properties = self.file_properties.to_dict()

        file_set_properties: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.file_set_properties, Unset):
            file_set_properties = self.file_set_properties.to_dict()

        float_properties: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.float_properties, Unset):
            float_properties = self.float_properties.to_dict()

        float_series_properties: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.float_series_properties, Unset):
            float_series_properties = self.float_series_properties.to_dict()

        git_ref_properties: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.git_ref_properties, Unset):
            git_ref_properties = self.git_ref_properties.to_dict()

        image_series_properties: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.image_series_properties, Unset):
            image_series_properties = self.image_series_properties.to_dict()

        int_properties: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.int_properties, Unset):
            int_properties = self.int_properties.to_dict()

        notebook_ref_properties: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.notebook_ref_properties, Unset):
            notebook_ref_properties = self.notebook_ref_properties.to_dict()

        string_properties: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.string_properties, Unset):
            string_properties = self.string_properties.to_dict()

        string_series_properties: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.string_series_properties, Unset):
            string_series_properties = self.string_series_properties.to_dict()

        string_set_properties: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.string_set_properties, Unset):
            string_set_properties = self.string_set_properties.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type,
            }
        )
        if bool_properties is not UNSET:
            field_dict["boolProperties"] = bool_properties
        if complex_properties is not UNSET:
            field_dict["complexProperties"] = complex_properties
        if datetime_properties is not UNSET:
            field_dict["datetimeProperties"] = datetime_properties
        if experiment_state_properties is not UNSET:
            field_dict["experimentStateProperties"] = experiment_state_properties
        if file_properties is not UNSET:
            field_dict["fileProperties"] = file_properties
        if file_set_properties is not UNSET:
            field_dict["fileSetProperties"] = file_set_properties
        if float_properties is not UNSET:
            field_dict["floatProperties"] = float_properties
        if float_series_properties is not UNSET:
            field_dict["floatSeriesProperties"] = float_series_properties
        if git_ref_properties is not UNSET:
            field_dict["gitRefProperties"] = git_ref_properties
        if image_series_properties is not UNSET:
            field_dict["imageSeriesProperties"] = image_series_properties
        if int_properties is not UNSET:
            field_dict["intProperties"] = int_properties
        if notebook_ref_properties is not UNSET:
            field_dict["notebookRefProperties"] = notebook_ref_properties
        if string_properties is not UNSET:
            field_dict["stringProperties"] = string_properties
        if string_series_properties is not UNSET:
            field_dict["stringSeriesProperties"] = string_series_properties
        if string_set_properties is not UNSET:
            field_dict["stringSetProperties"] = string_set_properties

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bool_attribute_dto import BoolAttributeDTO
        from ..models.complex_attribute_dto import ComplexAttributeDTO
        from ..models.datetime_attribute_dto import DatetimeAttributeDTO
        from ..models.experiment_state_attribute_dto import ExperimentStateAttributeDTO
        from ..models.file_attribute_dto import FileAttributeDTO
        from ..models.file_set_attribute_dto import FileSetAttributeDTO
        from ..models.float_attribute_dto import FloatAttributeDTO
        from ..models.float_series_attribute_dto import FloatSeriesAttributeDTO
        from ..models.git_info_dto import GitInfoDTO
        from ..models.image_series_attribute_dto import ImageSeriesAttributeDTO
        from ..models.int_attribute_dto import IntAttributeDTO
        from ..models.notebook_ref_attribute_dto import NotebookRefAttributeDTO
        from ..models.string_attribute_dto import StringAttributeDTO
        from ..models.string_series_attribute_dto import StringSeriesAttributeDTO
        from ..models.string_set_attribute_dto import StringSetAttributeDTO

        d = src_dict.copy()
        name = d.pop("name")

        type = AttributeTypeDTO(d.pop("type"))

        _bool_properties = d.pop("boolProperties", UNSET)
        bool_properties: Union[Unset, BoolAttributeDTO]
        if isinstance(_bool_properties, Unset):
            bool_properties = UNSET
        else:
            bool_properties = BoolAttributeDTO.from_dict(_bool_properties)

        _complex_properties = d.pop("complexProperties", UNSET)
        complex_properties: Union[Unset, ComplexAttributeDTO]
        if isinstance(_complex_properties, Unset):
            complex_properties = UNSET
        else:
            complex_properties = ComplexAttributeDTO.from_dict(_complex_properties)

        _datetime_properties = d.pop("datetimeProperties", UNSET)
        datetime_properties: Union[Unset, DatetimeAttributeDTO]
        if isinstance(_datetime_properties, Unset):
            datetime_properties = UNSET
        else:
            datetime_properties = DatetimeAttributeDTO.from_dict(_datetime_properties)

        _experiment_state_properties = d.pop("experimentStateProperties", UNSET)
        experiment_state_properties: Union[Unset, ExperimentStateAttributeDTO]
        if isinstance(_experiment_state_properties, Unset):
            experiment_state_properties = UNSET
        else:
            experiment_state_properties = ExperimentStateAttributeDTO.from_dict(_experiment_state_properties)

        _file_properties = d.pop("fileProperties", UNSET)
        file_properties: Union[Unset, FileAttributeDTO]
        if isinstance(_file_properties, Unset):
            file_properties = UNSET
        else:
            file_properties = FileAttributeDTO.from_dict(_file_properties)

        _file_set_properties = d.pop("fileSetProperties", UNSET)
        file_set_properties: Union[Unset, FileSetAttributeDTO]
        if isinstance(_file_set_properties, Unset):
            file_set_properties = UNSET
        else:
            file_set_properties = FileSetAttributeDTO.from_dict(_file_set_properties)

        _float_properties = d.pop("floatProperties", UNSET)
        float_properties: Union[Unset, FloatAttributeDTO]
        if isinstance(_float_properties, Unset):
            float_properties = UNSET
        else:
            float_properties = FloatAttributeDTO.from_dict(_float_properties)

        _float_series_properties = d.pop("floatSeriesProperties", UNSET)
        float_series_properties: Union[Unset, FloatSeriesAttributeDTO]
        if isinstance(_float_series_properties, Unset):
            float_series_properties = UNSET
        else:
            float_series_properties = FloatSeriesAttributeDTO.from_dict(_float_series_properties)

        _git_ref_properties = d.pop("gitRefProperties", UNSET)
        git_ref_properties: Union[Unset, GitInfoDTO]
        if isinstance(_git_ref_properties, Unset):
            git_ref_properties = UNSET
        else:
            git_ref_properties = GitInfoDTO.from_dict(_git_ref_properties)

        _image_series_properties = d.pop("imageSeriesProperties", UNSET)
        image_series_properties: Union[Unset, ImageSeriesAttributeDTO]
        if isinstance(_image_series_properties, Unset):
            image_series_properties = UNSET
        else:
            image_series_properties = ImageSeriesAttributeDTO.from_dict(_image_series_properties)

        _int_properties = d.pop("intProperties", UNSET)
        int_properties: Union[Unset, IntAttributeDTO]
        if isinstance(_int_properties, Unset):
            int_properties = UNSET
        else:
            int_properties = IntAttributeDTO.from_dict(_int_properties)

        _notebook_ref_properties = d.pop("notebookRefProperties", UNSET)
        notebook_ref_properties: Union[Unset, NotebookRefAttributeDTO]
        if isinstance(_notebook_ref_properties, Unset):
            notebook_ref_properties = UNSET
        else:
            notebook_ref_properties = NotebookRefAttributeDTO.from_dict(_notebook_ref_properties)

        _string_properties = d.pop("stringProperties", UNSET)
        string_properties: Union[Unset, StringAttributeDTO]
        if isinstance(_string_properties, Unset):
            string_properties = UNSET
        else:
            string_properties = StringAttributeDTO.from_dict(_string_properties)

        _string_series_properties = d.pop("stringSeriesProperties", UNSET)
        string_series_properties: Union[Unset, StringSeriesAttributeDTO]
        if isinstance(_string_series_properties, Unset):
            string_series_properties = UNSET
        else:
            string_series_properties = StringSeriesAttributeDTO.from_dict(_string_series_properties)

        _string_set_properties = d.pop("stringSetProperties", UNSET)
        string_set_properties: Union[Unset, StringSetAttributeDTO]
        if isinstance(_string_set_properties, Unset):
            string_set_properties = UNSET
        else:
            string_set_properties = StringSetAttributeDTO.from_dict(_string_set_properties)

        attribute_dto = cls(
            name=name,
            type=type,
            bool_properties=bool_properties,
            complex_properties=complex_properties,
            datetime_properties=datetime_properties,
            experiment_state_properties=experiment_state_properties,
            file_properties=file_properties,
            file_set_properties=file_set_properties,
            float_properties=float_properties,
            float_series_properties=float_series_properties,
            git_ref_properties=git_ref_properties,
            image_series_properties=image_series_properties,
            int_properties=int_properties,
            notebook_ref_properties=notebook_ref_properties,
            string_properties=string_properties,
            string_series_properties=string_series_properties,
            string_set_properties=string_set_properties,
        )

        attribute_dto.additional_properties = d
        return attribute_dto

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
