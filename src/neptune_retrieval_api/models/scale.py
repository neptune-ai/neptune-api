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
    from ..models.linear import Linear
    from ..models.log import Log


T = TypeVar("T", bound="Scale")


@_attrs_define
class Scale:
    """
    Attributes:
        linear (Union[Unset, Linear]):
        log (Union[Unset, Log]):
    """

    linear: Union[Unset, "Linear"] = UNSET
    log: Union[Unset, "Log"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        linear: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.linear, Unset):
            linear = self.linear.to_dict()

        log: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.log, Unset):
            log = self.log.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if linear is not UNSET:
            field_dict["linear"] = linear
        if log is not UNSET:
            field_dict["log"] = log

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.linear import Linear
        from ..models.log import Log

        d = src_dict.copy()
        _linear = d.pop("linear", UNSET)
        linear: Union[Unset, Linear]
        if isinstance(_linear, Unset):
            linear = UNSET
        else:
            linear = Linear.from_dict(_linear)

        _log = d.pop("log", UNSET)
        log: Union[Unset, Log]
        if isinstance(_log, Unset):
            log = UNSET
        else:
            log = Log.from_dict(_log)

        scale = cls(
            linear=linear,
            log=log,
        )

        scale.additional_properties = d
        return scale

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
