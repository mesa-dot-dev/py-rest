from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_by_org_repos_facets_response_200_facets import GetByOrgReposFacetsResponse200Facets





T = TypeVar("T", bound="GetByOrgReposFacetsResponse200")



@_attrs_define
class GetByOrgReposFacetsResponse200:
    """ 
        Attributes:
            facets (GetByOrgReposFacetsResponse200Facets):
     """

    facets: GetByOrgReposFacetsResponse200Facets
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_by_org_repos_facets_response_200_facets import GetByOrgReposFacetsResponse200Facets
        facets = self.facets.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "facets": facets,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_by_org_repos_facets_response_200_facets import GetByOrgReposFacetsResponse200Facets
        d = dict(src_dict)
        facets = GetByOrgReposFacetsResponse200Facets.from_dict(d.pop("facets"))




        get_by_org_repos_facets_response_200 = cls(
            facets=facets,
        )


        get_by_org_repos_facets_response_200.additional_properties = d
        return get_by_org_repos_facets_response_200

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
