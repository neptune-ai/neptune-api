from enum import Enum


class LeaderboardViewQuickFilterDTORelativeTime(str, Enum):
    LASTDAY = "lastDay"
    LASTMONTH = "lastMonth"
    LASTQUARTER = "lastQuarter"
    LASTWEEK = "lastWeek"

    def __str__(self) -> str:
        return str(self.value)
