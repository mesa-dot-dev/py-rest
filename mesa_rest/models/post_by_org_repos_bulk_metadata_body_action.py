from enum import Enum

class PostByOrgReposBulkMetadataBodyAction(str, Enum):
    REMOVE = "remove"
    SET = "set"

    def __str__(self) -> str:
        return str(self.value)
