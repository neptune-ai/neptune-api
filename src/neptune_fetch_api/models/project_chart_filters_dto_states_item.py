from enum import Enum


class ProjectChartFiltersDTOStatesItem(str, Enum):
    ABORTED = "aborted"
    FAILED = "failed"
    RUNNING = "running"
    SUCCEEDED = "succeeded"

    def __str__(self) -> str:
        return str(self.value)
