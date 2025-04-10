from enum import Enum


class LeaderboardViewUpdateDTONameSearchMode(str, Enum):
    REGEXP = "regexp"
    SUBSTRING = "substring"

    def __str__(self) -> str:
        return str(self.value)
