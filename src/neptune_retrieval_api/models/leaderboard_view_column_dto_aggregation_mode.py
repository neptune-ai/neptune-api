from enum import Enum


class LeaderboardViewColumnDTOAggregationMode(str, Enum):
    AVERAGE = "average"
    LAST = "last"
    MAX = "max"
    MIN = "min"
    VARIANCE = "variance"

    def __str__(self) -> str:
        return str(self.value)
