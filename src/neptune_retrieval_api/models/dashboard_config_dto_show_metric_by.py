from enum import Enum


class DashboardConfigDTOShowMetricBy(str, Enum):
    COLOR = "color"
    LINESTYLE = "lineStyle"

    def __str__(self) -> str:
        return str(self.value)
