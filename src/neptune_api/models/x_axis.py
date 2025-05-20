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
    from ..models.custom import Custom
    from ..models.epoch_millis import EpochMillis
    from ..models.relative_timestamp import RelativeTimestamp
    from ..models.steps import Steps


T = TypeVar("T", bound="XAxis")


@_attrs_define
class XAxis:
    """
    Attributes:
        custom (Union[Unset, Custom]):
        epoch_millis (Union[Unset, EpochMillis]):
        relative_millis (Union[Unset, RelativeTimestamp]):
        steps (Union[Unset, Steps]):
    """

    custom: Union[Unset, "Custom"] = UNSET
    epoch_millis: Union[Unset, "EpochMillis"] = UNSET
    relative_millis: Union[Unset, "RelativeTimestamp"] = UNSET
    steps: Union[Unset, "Steps"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        custom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

        epoch_millis: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.epoch_millis, Unset):
            epoch_millis = self.epoch_millis.to_dict()

        relative_millis: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.relative_millis, Unset):
            relative_millis = self.relative_millis.to_dict()

        steps: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.steps, Unset):
            steps = self.steps.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if custom is not UNSET:
            field_dict["custom"] = custom
        if epoch_millis is not UNSET:
            field_dict["epochMillis"] = epoch_millis
        if relative_millis is not UNSET:
            field_dict["relativeMillis"] = relative_millis
        if steps is not UNSET:
            field_dict["steps"] = steps

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.custom import Custom
        from ..models.epoch_millis import EpochMillis
        from ..models.relative_timestamp import RelativeTimestamp
        from ..models.steps import Steps

        d = src_dict.copy()
        _custom = d.pop("custom", UNSET)
        custom: Union[Unset, Custom]
        if isinstance(_custom, Unset):
            custom = UNSET
        else:
            custom = Custom.from_dict(_custom)

        _epoch_millis = d.pop("epochMillis", UNSET)
        epoch_millis: Union[Unset, EpochMillis]
        if isinstance(_epoch_millis, Unset):
            epoch_millis = UNSET
        else:
            epoch_millis = EpochMillis.from_dict(_epoch_millis)

        _relative_millis = d.pop("relativeMillis", UNSET)
        relative_millis: Union[Unset, RelativeTimestamp]
        if isinstance(_relative_millis, Unset):
            relative_millis = UNSET
        else:
            relative_millis = RelativeTimestamp.from_dict(_relative_millis)

        _steps = d.pop("steps", UNSET)
        steps: Union[Unset, Steps]
        if isinstance(_steps, Unset):
            steps = UNSET
        else:
            steps = Steps.from_dict(_steps)

        x_axis = cls(
            custom=custom,
            epoch_millis=epoch_millis,
            relative_millis=relative_millis,
            steps=steps,
        )

        x_axis.additional_properties = d
        return x_axis

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
