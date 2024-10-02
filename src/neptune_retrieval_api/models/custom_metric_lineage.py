from enum import Enum


class CustomMetricLineage(str, Enum):
    FULL = "FULL"
    NONE = "NONE"

    def __str__(self) -> str:
        return str(self.value)
