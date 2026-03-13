from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_by_org_repos_list_response_200_repos_item_metadata import GetByOrgReposListResponse200ReposItemMetadata
  from ..models.get_by_org_repos_list_response_200_repos_item_upstream_type_0 import GetByOrgReposListResponse200ReposItemUpstreamType0





T = TypeVar("T", bound="GetByOrgReposListResponse200ReposItem")



@_attrs_define
class GetByOrgReposListResponse200ReposItem:
    """ 
        Attributes:
            id (str):
            name (str):
            default_branch (str):
            size_bytes (float):
            created_at (str):
            metadata (GetByOrgReposListResponse200ReposItemMetadata):
            upstream (GetByOrgReposListResponse200ReposItemUpstreamType0 | None):
     """

    id: str
    name: str
    default_branch: str
    size_bytes: float
    created_at: str
    metadata: GetByOrgReposListResponse200ReposItemMetadata
    upstream: GetByOrgReposListResponse200ReposItemUpstreamType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_by_org_repos_list_response_200_repos_item_metadata import GetByOrgReposListResponse200ReposItemMetadata
        from ..models.get_by_org_repos_list_response_200_repos_item_upstream_type_0 import GetByOrgReposListResponse200ReposItemUpstreamType0
        id = self.id

        name = self.name

        default_branch = self.default_branch

        size_bytes = self.size_bytes

        created_at = self.created_at

        metadata = self.metadata.to_dict()

        upstream: dict[str, Any] | None
        if isinstance(self.upstream, GetByOrgReposListResponse200ReposItemUpstreamType0):
            upstream = self.upstream.to_dict()
        else:
            upstream = self.upstream


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
            "default_branch": default_branch,
            "size_bytes": size_bytes,
            "created_at": created_at,
            "metadata": metadata,
            "upstream": upstream,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_by_org_repos_list_response_200_repos_item_metadata import GetByOrgReposListResponse200ReposItemMetadata
        from ..models.get_by_org_repos_list_response_200_repos_item_upstream_type_0 import GetByOrgReposListResponse200ReposItemUpstreamType0
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        default_branch = d.pop("default_branch")

        size_bytes = d.pop("size_bytes")

        created_at = d.pop("created_at")

        metadata = GetByOrgReposListResponse200ReposItemMetadata.from_dict(d.pop("metadata"))




        def _parse_upstream(data: object) -> GetByOrgReposListResponse200ReposItemUpstreamType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                upstream_type_0 = GetByOrgReposListResponse200ReposItemUpstreamType0.from_dict(data)



                return upstream_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetByOrgReposListResponse200ReposItemUpstreamType0 | None, data)

        upstream = _parse_upstream(d.pop("upstream"))


        get_by_org_repos_list_response_200_repos_item = cls(
            id=id,
            name=name,
            default_branch=default_branch,
            size_bytes=size_bytes,
            created_at=created_at,
            metadata=metadata,
            upstream=upstream,
        )


        get_by_org_repos_list_response_200_repos_item.additional_properties = d
        return get_by_org_repos_list_response_200_repos_item

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
