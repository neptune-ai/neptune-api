from enum import Enum


class FileEntryFileType(str, Enum):
    DIRECTORY = "directory"
    FILE = "file"

    def __str__(self) -> str:
        return str(self.value)
