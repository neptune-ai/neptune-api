from enum import Enum


class ListNotebooksSortBy(str, Enum):
    NAME = "name"
    OWNER = "owner"
    UPDATETIME = "updateTime"

    def __str__(self) -> str:
        return str(self.value)
