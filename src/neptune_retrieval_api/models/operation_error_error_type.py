from enum import Enum


class OperationErrorErrorType(str, Enum):
    ASSIGNFLOATVALUEERROR = "assignFloatValueError"
    LOGSERIESVALUEERROR = "logSeriesValueError"
    METADATA_INCONSISTENCY = "metadata_inconsistency"

    def __str__(self) -> str:
        return str(self.value)
