from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    Type,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dashboard_dto import DashboardDTO


T = TypeVar("T", bound="DashboardListDTO")


@_attrs_define
class DashboardListDTO:
    """
    Attributes:
        dashboards (List['DashboardDTO']): Dashboard list
    """

    dashboards: List["DashboardDTO"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dashboards = []
        for dashboards_item_data in self.dashboards:
            dashboards_item = dashboards_item_data.to_dict()
            dashboards.append(dashboards_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dashboards": dashboards,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dashboard_dto import DashboardDTO

        d = src_dict.copy()
        dashboards = []
        _dashboards = d.pop("dashboards")
        for dashboards_item_data in _dashboards:
            dashboards_item = DashboardDTO.from_dict(dashboards_item_data)

            dashboards.append(dashboards_item)

        dashboard_list_dto = cls(
            dashboards=dashboards,
        )

        dashboard_list_dto.additional_properties = d
        return dashboard_list_dto

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
