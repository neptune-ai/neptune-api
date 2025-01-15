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
    from ..models.assign_bool_operation import AssignBoolOperation
    from ..models.assign_complex_operation import AssignComplexOperation
    from ..models.assign_datetime_operation import AssignDatetimeOperation
    from ..models.assign_float_operation import AssignFloatOperation
    from ..models.assign_int_operation import AssignIntOperation
    from ..models.assign_string_operation import AssignStringOperation
    from ..models.clear_float_series_operation import ClearFloatSeriesOperation
    from ..models.clear_image_series import ClearImageSeries
    from ..models.clear_string_series_operation import ClearStringSeriesOperation
    from ..models.clear_string_set_operation import ClearStringSetOperation
    from ..models.config_float_series import ConfigFloatSeries
    from ..models.delete_files_operation import DeleteFilesOperation
    from ..models.delete_variable_operation import DeleteVariableOperation
    from ..models.insert_strings_operation import InsertStringsOperation
    from ..models.log_floats_operation import LogFloatsOperation
    from ..models.log_images import LogImages
    from ..models.log_strings_operation import LogStringsOperation
    from ..models.remove_strings_operation import RemoveStringsOperation


T = TypeVar("T", bound="Operation")


@_attrs_define
class Operation:
    """
    Attributes:
        path (Union[Unset, str]):
        assign_complex (Union[Unset, AssignComplexOperation]):
        assign_float (Union[Unset, AssignFloatOperation]):
        assign_int (Union[Unset, AssignIntOperation]):
        assign_bool (Union[Unset, AssignBoolOperation]):
        assign_string (Union[Unset, AssignStringOperation]):
        assign_datetime (Union[Unset, AssignDatetimeOperation]):
        log_floats (Union[Unset, LogFloatsOperation]):
        log_strings (Union[Unset, LogStringsOperation]):
        log_images (Union[Unset, LogImages]):
        clear_float_series (Union[Unset, ClearFloatSeriesOperation]):
        clear_string_series (Union[Unset, ClearStringSeriesOperation]):
        clear_image_series (Union[Unset, ClearImageSeries]):
        config_float_series (Union[Unset, ConfigFloatSeries]):
        insert_strings (Union[Unset, InsertStringsOperation]):
        remove_strings (Union[Unset, RemoveStringsOperation]):
        clear_string_set (Union[Unset, ClearStringSetOperation]):
        delete_files (Union[Unset, DeleteFilesOperation]):
        delete_attribute (Union[Unset, DeleteVariableOperation]):
    """

    path: Union[Unset, str] = UNSET
    assign_complex: Union[Unset, "AssignComplexOperation"] = UNSET
    assign_float: Union[Unset, "AssignFloatOperation"] = UNSET
    assign_int: Union[Unset, "AssignIntOperation"] = UNSET
    assign_bool: Union[Unset, "AssignBoolOperation"] = UNSET
    assign_string: Union[Unset, "AssignStringOperation"] = UNSET
    assign_datetime: Union[Unset, "AssignDatetimeOperation"] = UNSET
    log_floats: Union[Unset, "LogFloatsOperation"] = UNSET
    log_strings: Union[Unset, "LogStringsOperation"] = UNSET
    log_images: Union[Unset, "LogImages"] = UNSET
    clear_float_series: Union[Unset, "ClearFloatSeriesOperation"] = UNSET
    clear_string_series: Union[Unset, "ClearStringSeriesOperation"] = UNSET
    clear_image_series: Union[Unset, "ClearImageSeries"] = UNSET
    config_float_series: Union[Unset, "ConfigFloatSeries"] = UNSET
    insert_strings: Union[Unset, "InsertStringsOperation"] = UNSET
    remove_strings: Union[Unset, "RemoveStringsOperation"] = UNSET
    clear_string_set: Union[Unset, "ClearStringSetOperation"] = UNSET
    delete_files: Union[Unset, "DeleteFilesOperation"] = UNSET
    delete_attribute: Union[Unset, "DeleteVariableOperation"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        path = self.path

        assign_complex: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.assign_complex, Unset):
            assign_complex = self.assign_complex.to_dict()

        assign_float: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.assign_float, Unset):
            assign_float = self.assign_float.to_dict()

        assign_int: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.assign_int, Unset):
            assign_int = self.assign_int.to_dict()

        assign_bool: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.assign_bool, Unset):
            assign_bool = self.assign_bool.to_dict()

        assign_string: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.assign_string, Unset):
            assign_string = self.assign_string.to_dict()

        assign_datetime: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.assign_datetime, Unset):
            assign_datetime = self.assign_datetime.to_dict()

        log_floats: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.log_floats, Unset):
            log_floats = self.log_floats.to_dict()

        log_strings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.log_strings, Unset):
            log_strings = self.log_strings.to_dict()

        log_images: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.log_images, Unset):
            log_images = self.log_images.to_dict()

        clear_float_series: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.clear_float_series, Unset):
            clear_float_series = self.clear_float_series.to_dict()

        clear_string_series: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.clear_string_series, Unset):
            clear_string_series = self.clear_string_series.to_dict()

        clear_image_series: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.clear_image_series, Unset):
            clear_image_series = self.clear_image_series.to_dict()

        config_float_series: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.config_float_series, Unset):
            config_float_series = self.config_float_series.to_dict()

        insert_strings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.insert_strings, Unset):
            insert_strings = self.insert_strings.to_dict()

        remove_strings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.remove_strings, Unset):
            remove_strings = self.remove_strings.to_dict()

        clear_string_set: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.clear_string_set, Unset):
            clear_string_set = self.clear_string_set.to_dict()

        delete_files: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.delete_files, Unset):
            delete_files = self.delete_files.to_dict()

        delete_attribute: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.delete_attribute, Unset):
            delete_attribute = self.delete_attribute.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if assign_complex is not UNSET:
            field_dict["assignComplex"] = assign_complex
        if assign_float is not UNSET:
            field_dict["assignFloat"] = assign_float
        if assign_int is not UNSET:
            field_dict["assignInt"] = assign_int
        if assign_bool is not UNSET:
            field_dict["assignBool"] = assign_bool
        if assign_string is not UNSET:
            field_dict["assignString"] = assign_string
        if assign_datetime is not UNSET:
            field_dict["assignDatetime"] = assign_datetime
        if log_floats is not UNSET:
            field_dict["logFloats"] = log_floats
        if log_strings is not UNSET:
            field_dict["logStrings"] = log_strings
        if log_images is not UNSET:
            field_dict["logImages"] = log_images
        if clear_float_series is not UNSET:
            field_dict["clearFloatSeries"] = clear_float_series
        if clear_string_series is not UNSET:
            field_dict["clearStringSeries"] = clear_string_series
        if clear_image_series is not UNSET:
            field_dict["clearImageSeries"] = clear_image_series
        if config_float_series is not UNSET:
            field_dict["configFloatSeries"] = config_float_series
        if insert_strings is not UNSET:
            field_dict["insertStrings"] = insert_strings
        if remove_strings is not UNSET:
            field_dict["removeStrings"] = remove_strings
        if clear_string_set is not UNSET:
            field_dict["clearStringSet"] = clear_string_set
        if delete_files is not UNSET:
            field_dict["deleteFiles"] = delete_files
        if delete_attribute is not UNSET:
            field_dict["deleteAttribute"] = delete_attribute

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.assign_bool_operation import AssignBoolOperation
        from ..models.assign_complex_operation import AssignComplexOperation
        from ..models.assign_datetime_operation import AssignDatetimeOperation
        from ..models.assign_float_operation import AssignFloatOperation
        from ..models.assign_int_operation import AssignIntOperation
        from ..models.assign_string_operation import AssignStringOperation
        from ..models.clear_float_series_operation import ClearFloatSeriesOperation
        from ..models.clear_image_series import ClearImageSeries
        from ..models.clear_string_series_operation import ClearStringSeriesOperation
        from ..models.clear_string_set_operation import ClearStringSetOperation
        from ..models.config_float_series import ConfigFloatSeries
        from ..models.delete_files_operation import DeleteFilesOperation
        from ..models.delete_variable_operation import DeleteVariableOperation
        from ..models.insert_strings_operation import InsertStringsOperation
        from ..models.log_floats_operation import LogFloatsOperation
        from ..models.log_images import LogImages
        from ..models.log_strings_operation import LogStringsOperation
        from ..models.remove_strings_operation import RemoveStringsOperation

        d = src_dict.copy()
        path = d.pop("path", UNSET)

        _assign_complex = d.pop("assignComplex", UNSET)
        assign_complex: Union[Unset, AssignComplexOperation]
        if isinstance(_assign_complex, Unset):
            assign_complex = UNSET
        else:
            assign_complex = AssignComplexOperation.from_dict(_assign_complex)

        _assign_float = d.pop("assignFloat", UNSET)
        assign_float: Union[Unset, AssignFloatOperation]
        if isinstance(_assign_float, Unset):
            assign_float = UNSET
        else:
            assign_float = AssignFloatOperation.from_dict(_assign_float)

        _assign_int = d.pop("assignInt", UNSET)
        assign_int: Union[Unset, AssignIntOperation]
        if isinstance(_assign_int, Unset):
            assign_int = UNSET
        else:
            assign_int = AssignIntOperation.from_dict(_assign_int)

        _assign_bool = d.pop("assignBool", UNSET)
        assign_bool: Union[Unset, AssignBoolOperation]
        if isinstance(_assign_bool, Unset):
            assign_bool = UNSET
        else:
            assign_bool = AssignBoolOperation.from_dict(_assign_bool)

        _assign_string = d.pop("assignString", UNSET)
        assign_string: Union[Unset, AssignStringOperation]
        if isinstance(_assign_string, Unset):
            assign_string = UNSET
        else:
            assign_string = AssignStringOperation.from_dict(_assign_string)

        _assign_datetime = d.pop("assignDatetime", UNSET)
        assign_datetime: Union[Unset, AssignDatetimeOperation]
        if isinstance(_assign_datetime, Unset):
            assign_datetime = UNSET
        else:
            assign_datetime = AssignDatetimeOperation.from_dict(_assign_datetime)

        _log_floats = d.pop("logFloats", UNSET)
        log_floats: Union[Unset, LogFloatsOperation]
        if isinstance(_log_floats, Unset):
            log_floats = UNSET
        else:
            log_floats = LogFloatsOperation.from_dict(_log_floats)

        _log_strings = d.pop("logStrings", UNSET)
        log_strings: Union[Unset, LogStringsOperation]
        if isinstance(_log_strings, Unset):
            log_strings = UNSET
        else:
            log_strings = LogStringsOperation.from_dict(_log_strings)

        _log_images = d.pop("logImages", UNSET)
        log_images: Union[Unset, LogImages]
        if isinstance(_log_images, Unset):
            log_images = UNSET
        else:
            log_images = LogImages.from_dict(_log_images)

        _clear_float_series = d.pop("clearFloatSeries", UNSET)
        clear_float_series: Union[Unset, ClearFloatSeriesOperation]
        if isinstance(_clear_float_series, Unset):
            clear_float_series = UNSET
        else:
            clear_float_series = ClearFloatSeriesOperation.from_dict(_clear_float_series)

        _clear_string_series = d.pop("clearStringSeries", UNSET)
        clear_string_series: Union[Unset, ClearStringSeriesOperation]
        if isinstance(_clear_string_series, Unset):
            clear_string_series = UNSET
        else:
            clear_string_series = ClearStringSeriesOperation.from_dict(_clear_string_series)

        _clear_image_series = d.pop("clearImageSeries", UNSET)
        clear_image_series: Union[Unset, ClearImageSeries]
        if isinstance(_clear_image_series, Unset):
            clear_image_series = UNSET
        else:
            clear_image_series = ClearImageSeries.from_dict(_clear_image_series)

        _config_float_series = d.pop("configFloatSeries", UNSET)
        config_float_series: Union[Unset, ConfigFloatSeries]
        if isinstance(_config_float_series, Unset):
            config_float_series = UNSET
        else:
            config_float_series = ConfigFloatSeries.from_dict(_config_float_series)

        _insert_strings = d.pop("insertStrings", UNSET)
        insert_strings: Union[Unset, InsertStringsOperation]
        if isinstance(_insert_strings, Unset):
            insert_strings = UNSET
        else:
            insert_strings = InsertStringsOperation.from_dict(_insert_strings)

        _remove_strings = d.pop("removeStrings", UNSET)
        remove_strings: Union[Unset, RemoveStringsOperation]
        if isinstance(_remove_strings, Unset):
            remove_strings = UNSET
        else:
            remove_strings = RemoveStringsOperation.from_dict(_remove_strings)

        _clear_string_set = d.pop("clearStringSet", UNSET)
        clear_string_set: Union[Unset, ClearStringSetOperation]
        if isinstance(_clear_string_set, Unset):
            clear_string_set = UNSET
        else:
            clear_string_set = ClearStringSetOperation.from_dict(_clear_string_set)

        _delete_files = d.pop("deleteFiles", UNSET)
        delete_files: Union[Unset, DeleteFilesOperation]
        if isinstance(_delete_files, Unset):
            delete_files = UNSET
        else:
            delete_files = DeleteFilesOperation.from_dict(_delete_files)

        _delete_attribute = d.pop("deleteAttribute", UNSET)
        delete_attribute: Union[Unset, DeleteVariableOperation]
        if isinstance(_delete_attribute, Unset):
            delete_attribute = UNSET
        else:
            delete_attribute = DeleteVariableOperation.from_dict(_delete_attribute)

        operation = cls(
            path=path,
            assign_complex=assign_complex,
            assign_float=assign_float,
            assign_int=assign_int,
            assign_bool=assign_bool,
            assign_string=assign_string,
            assign_datetime=assign_datetime,
            log_floats=log_floats,
            log_strings=log_strings,
            log_images=log_images,
            clear_float_series=clear_float_series,
            clear_string_series=clear_string_series,
            clear_image_series=clear_image_series,
            config_float_series=config_float_series,
            insert_strings=insert_strings,
            remove_strings=remove_strings,
            clear_string_set=clear_string_set,
            delete_files=delete_files,
            delete_attribute=delete_attribute,
        )

        operation.additional_properties = d
        return operation

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
