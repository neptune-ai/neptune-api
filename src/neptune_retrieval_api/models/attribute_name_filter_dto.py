from typing import (
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

from ..types import (
    UNSET,
    Unset,
)

T = TypeVar("T", bound="AttributeNameFilterDTO")


@_attrs_define
class AttributeNameFilterDTO:
    """
    Attributes:
        must_match_regexes (Union[Unset, List[str]]): An attribute must match all of the regexes from the list to be
            returned
        must_not_match_regexes (Union[Unset, List[str]]): An attribute must match none of the regexes from the list to
            be returned
    """

    must_match_regexes: Union[Unset, List[str]] = UNSET
    must_not_match_regexes: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        must_match_regexes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.must_match_regexes, Unset):
            must_match_regexes = self.must_match_regexes

        must_not_match_regexes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.must_not_match_regexes, Unset):
            must_not_match_regexes = self.must_not_match_regexes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if must_match_regexes is not UNSET:
            field_dict["mustMatchRegexes"] = must_match_regexes
        if must_not_match_regexes is not UNSET:
            field_dict["mustNotMatchRegexes"] = must_not_match_regexes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        must_match_regexes = cast(List[str], d.pop("mustMatchRegexes", UNSET))

        must_not_match_regexes = cast(List[str], d.pop("mustNotMatchRegexes", UNSET))

        attribute_name_filter_dto = cls(
            must_match_regexes=must_match_regexes,
            must_not_match_regexes=must_not_match_regexes,
        )

        attribute_name_filter_dto.additional_properties = d
        return attribute_name_filter_dto

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
