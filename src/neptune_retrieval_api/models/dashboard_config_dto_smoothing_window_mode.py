from enum import Enum


class DashboardConfigDTOSmoothingWindowMode(str, Enum):
    CAUSAL = "causal"
    CENTERED = "centered"

    def __str__(self) -> str:
        return str(self.value)
