from enum import Enum


class ListDashboardsDrafts(str, Enum):
    ALL = "all"
    FALSE = "false"
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
