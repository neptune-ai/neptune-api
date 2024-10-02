from enum import Enum


class BulkOpErrorDTOReason(str, Enum):
    ALREADY_FINISHED = "ALREADY_FINISHED"
    ALREADY_TRASHED = "ALREADY_TRASHED"
    IS_PROJECT = "IS_PROJECT"
    NOT_EXISTS = "NOT_EXISTS"
    NOT_IN_TRASH = "NOT_IN_TRASH"
    TRASHED = "TRASHED"

    def __str__(self) -> str:
        return str(self.value)
