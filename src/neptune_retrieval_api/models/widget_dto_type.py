from enum import Enum


class WidgetDTOType(str, Enum):
    CHART = "chart"
    FILE = "file"
    FILESET = "fileSet"
    GALLERY = "gallery"
    IMAGE = "image"
    IMAGECOMPARISON = "imageComparison"
    INTERACTIVETABLE = "interactiveTable"
    NOTEBOOK = "notebook"
    SCATTERPLOT = "scatterPlot"
    SECTION = "section"
    SINGLEVALUE = "singleValue"
    TABLE = "table"
    TEXTNODE = "textNode"
    VALUELIST = "valueList"

    def __str__(self) -> str:
        return str(self.value)
