from enum import Enum


class WidgetAttributeDTOType(str, Enum):
    BOOL = "bool"
    DATETIME = "datetime"
    EXPERIMENTSTATE = "experimentState"
    FILE = "file"
    FILESET = "fileSet"
    FLOAT = "float"
    FLOATSERIES = "floatSeries"
    GITREF = "gitRef"
    IMAGESERIES = "imageSeries"
    INT = "int"
    NOTEBOOKREF = "notebookRef"
    NOTSUPPORTED = "notSupported"
    STRING = "string"
    STRINGSERIES = "stringSeries"
    STRINGSET = "stringSet"

    def __str__(self) -> str:
        return str(self.value)
