from enum import Enum


class ReportNodeDTOType(str, Enum):
    GRID = "grid"

    def __str__(self) -> str:
        return str(self.value)
