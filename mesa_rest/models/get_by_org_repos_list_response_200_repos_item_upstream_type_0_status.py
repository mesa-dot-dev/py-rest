from enum import Enum

class GetByOrgReposListResponse200ReposItemUpstreamType0Status(str, Enum):
    ERROR = "error"
    SYNCED = "synced"

    def __str__(self) -> str:
        return str(self.value)
