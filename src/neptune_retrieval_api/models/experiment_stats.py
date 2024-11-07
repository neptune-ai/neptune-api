from typing import (
    Any,
    Dict,
    List,
    Type,
    TypeVar,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ExperimentStats")


@_attrs_define
class ExperimentStats:
    """
    Attributes:
        experiments_created_per_day_count (List[int]):
    """

    experiments_created_per_day_count: List[int]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        experiments_created_per_day_count = self.experiments_created_per_day_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "experimentsCreatedPerDayCount": experiments_created_per_day_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        experiments_created_per_day_count = cast(List[int], d.pop("experimentsCreatedPerDayCount"))

        experiment_stats = cls(
            experiments_created_per_day_count=experiments_created_per_day_count,
        )

        experiment_stats.additional_properties = d
        return experiment_stats

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
