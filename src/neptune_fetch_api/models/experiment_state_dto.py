from enum import Enum


class ExperimentStateDTO(str, Enum):
    IDLE = "idle"
    RUNNING = "running"

    def __str__(self) -> str:
        return str(self.value)
