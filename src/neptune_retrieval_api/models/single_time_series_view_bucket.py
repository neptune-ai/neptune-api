from typing import (
    Any,
    Dict,
    List,
    Type,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SingleTimeSeriesViewBucket")


@_attrs_define
class SingleTimeSeriesViewBucket:
    """
    Attributes:
        bucket_no (int):
        count (int):
        max_y (float):
        min_y (float):
        sum_ (float):
    """

    bucket_no: int
    count: int
    max_y: float
    min_y: float
    sum_: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bucket_no = self.bucket_no

        count = self.count

        max_y = self.max_y

        min_y = self.min_y

        sum_ = self.sum_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bucketNo": bucket_no,
                "count": count,
                "maxY": max_y,
                "minY": min_y,
                "sum": sum_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        bucket_no = d.pop("bucketNo")

        count = d.pop("count")

        max_y = d.pop("maxY")

        min_y = d.pop("minY")

        sum_ = d.pop("sum")

        single_time_series_view_bucket = cls(
            bucket_no=bucket_no,
            count=count,
            max_y=max_y,
            min_y=min_y,
            sum_=sum_,
        )

        single_time_series_view_bucket.additional_properties = d
        return single_time_series_view_bucket

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
