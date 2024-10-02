from enum import Enum


class ExperimentTypeDTO(str, Enum):
    MODEL = "model"
    MODELVERSION = "modelVersion"
    PROJECT = "project"
    REPORT = "report"
    RUN = "run"

    def __str__(self) -> str:
        return str(self.value)
