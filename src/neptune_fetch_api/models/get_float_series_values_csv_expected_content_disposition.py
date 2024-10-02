from enum import Enum


class GetFloatSeriesValuesCSVExpectedContentDisposition(str, Enum):
    ATTACHMENT = "attachment"
    INLINE = "inline"

    def __str__(self) -> str:
        return str(self.value)
