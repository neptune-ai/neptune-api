from enum import Enum


class UpdateTagsParamsAttributePathToBeUpdated(str, Enum):
    SYSGROUP_TAGS = "sys/group_tags"
    SYSTAGS = "sys/tags"

    def __str__(self) -> str:
        return str(self.value)
