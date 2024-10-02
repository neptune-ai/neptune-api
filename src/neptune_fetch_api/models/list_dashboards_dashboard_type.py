from enum import Enum


class ListDashboardsDashboardType(str, Enum):
    COMPARE = "compare"
    EXPERIMENT = "experiment"
    REPORT = "report"

    def __str__(self) -> str:
        return str(self.value)
