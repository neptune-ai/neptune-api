from enum import Enum


class LeaderboardViewColumnDTODisplayMode(str, Enum):
    AUTO = "auto"
    DECIMAL = "decimal"
    SCIENTIFIC = "scientific"

    def __str__(self) -> str:
        return str(self.value)
