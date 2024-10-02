from enum import Enum


class NewDashboardDTOType(str, Enum):
    COMPARE = "compare"
    EXPERIMENT = "experiment"
    REPORT = "report"

    def __str__(self) -> str:
        return str(self.value)
