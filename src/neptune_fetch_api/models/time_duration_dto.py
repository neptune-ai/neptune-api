from typing import (
    Any,
    Dict,
    List,
    Type,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TimeDurationDTO")


@_attrs_define
class TimeDurationDTO:
    """
    Attributes:
        days (int):
        hours (int):
        minutes (int):
        months (int):
        seconds (int):
        weeks (int):
        years (int):
    """

    days: int
    hours: int
    minutes: int
    months: int
    seconds: int
    weeks: int
    years: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        days = self.days

        hours = self.hours

        minutes = self.minutes

        months = self.months

        seconds = self.seconds

        weeks = self.weeks

        years = self.years

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "days": days,
                "hours": hours,
                "minutes": minutes,
                "months": months,
                "seconds": seconds,
                "weeks": weeks,
                "years": years,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        days = d.pop("days")

        hours = d.pop("hours")

        minutes = d.pop("minutes")

        months = d.pop("months")

        seconds = d.pop("seconds")

        weeks = d.pop("weeks")

        years = d.pop("years")

        time_duration_dto = cls(
            days=days,
            hours=hours,
            minutes=minutes,
            months=months,
            seconds=seconds,
            weeks=weeks,
            years=years,
        )

        time_duration_dto.additional_properties = d
        return time_duration_dto

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
