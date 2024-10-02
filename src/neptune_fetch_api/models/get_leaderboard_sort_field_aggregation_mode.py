from enum import Enum


class GetLeaderboardSortFieldAggregationMode(str, Enum):
    AUTO = "auto"
    AVERAGE = "average"
    LAST = "last"
    MAX = "max"
    MIN = "min"
    VARIANCE = "variance"

    def __str__(self) -> str:
        return str(self.value)
