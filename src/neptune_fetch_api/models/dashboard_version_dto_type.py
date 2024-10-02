from enum import Enum


class DashboardVersionDTOType(str, Enum):
    COMPARE = "compare"
    EXPERIMENT = "experiment"
    REPORT = "report"

    def __str__(self) -> str:
        return str(self.value)
