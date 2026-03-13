from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_by_org_repos_list_response_200_repos_item import GetByOrgReposListResponse200ReposItem





T = TypeVar("T", bound="GetByOrgReposListResponse200")



@_attrs_define
class GetByOrgReposListResponse200:
    """ 
        Attributes:
            total (float):
            page (float):
            page_size (float):
            total_pages (float):
            repos (list[GetByOrgReposListResponse200ReposItem]):
     """

    total: float
    page: float
    page_size: float
    total_pages: float
    repos: list[GetByOrgReposListResponse200ReposItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_by_org_repos_list_response_200_repos_item import GetByOrgReposListResponse200ReposItem
        total = self.total

        page = self.page

        page_size = self.page_size

        total_pages = self.total_pages

        repos = []
        for repos_item_data in self.repos:
            repos_item = repos_item_data.to_dict()
            repos.append(repos_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "total": total,
            "page": page,
            "page_size": page_size,
            "total_pages": total_pages,
            "repos": repos,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_by_org_repos_list_response_200_repos_item import GetByOrgReposListResponse200ReposItem
        d = dict(src_dict)
        total = d.pop("total")

        page = d.pop("page")

        page_size = d.pop("page_size")

        total_pages = d.pop("total_pages")

        repos = []
        _repos = d.pop("repos")
        for repos_item_data in (_repos):
            repos_item = GetByOrgReposListResponse200ReposItem.from_dict(repos_item_data)



            repos.append(repos_item)


        get_by_org_repos_list_response_200 = cls(
            total=total,
            page=page,
            page_size=page_size,
            total_pages=total_pages,
            repos=repos,
        )


        get_by_org_repos_list_response_200.additional_properties = d
        return get_by_org_repos_list_response_200

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
