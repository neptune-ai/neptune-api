from enum import Enum


class FloatTimeSeriesValuesRequestOrder(str, Enum):
    ASCENDING = "ascending"
    DESCENDING = "descending"

    def __str__(self) -> str:
        return str(self.value)
