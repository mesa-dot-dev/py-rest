from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_whoami_response_200_org import GetWhoamiResponse200Org





T = TypeVar("T", bound="GetWhoamiResponse200")



@_attrs_define
class GetWhoamiResponse200:
    """ 
        Attributes:
            org (GetWhoamiResponse200Org):
            key_id (None | str):
            key_name (None | str):
            scopes (list[str]):
     """

    org: GetWhoamiResponse200Org
    key_id: None | str
    key_name: None | str
    scopes: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_whoami_response_200_org import GetWhoamiResponse200Org
        org = self.org.to_dict()

        key_id: None | str
        key_id = self.key_id

        key_name: None | str
        key_name = self.key_name

        scopes = self.scopes




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "org": org,
            "key_id": key_id,
            "key_name": key_name,
            "scopes": scopes,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_whoami_response_200_org import GetWhoamiResponse200Org
        d = dict(src_dict)
        org = GetWhoamiResponse200Org.from_dict(d.pop("org"))




        def _parse_key_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        key_id = _parse_key_id(d.pop("key_id"))


        def _parse_key_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        key_name = _parse_key_name(d.pop("key_name"))


        scopes = cast(list[str], d.pop("scopes"))


        get_whoami_response_200 = cls(
            org=org,
            key_id=key_id,
            key_name=key_name,
            scopes=scopes,
        )


        get_whoami_response_200.additional_properties = d
        return get_whoami_response_200

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
