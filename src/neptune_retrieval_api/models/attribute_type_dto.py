from enum import Enum


class AttributeTypeDTO(str, Enum):
    BOOL = "bool"
    COMPLEX = "complex"
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
    STRING = "string"
    STRINGSERIES = "stringSeries"
    STRINGSET = "stringSet"

    def __str__(self) -> str:
        return str(self.value)
