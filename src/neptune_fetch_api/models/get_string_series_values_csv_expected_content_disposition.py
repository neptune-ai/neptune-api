from enum import Enum


class GetStringSeriesValuesCSVExpectedContentDisposition(str, Enum):
    ATTACHMENT = "attachment"
    INLINE = "inline"

    def __str__(self) -> str:
        return str(self.value)
