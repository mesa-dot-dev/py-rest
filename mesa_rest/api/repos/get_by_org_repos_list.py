from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_by_org_repos_list_response_200 import GetByOrgReposListResponse200
from ...models.get_by_org_repos_list_response_400 import GetByOrgReposListResponse400
from ...models.get_by_org_repos_list_response_401 import GetByOrgReposListResponse401
from ...models.get_by_org_repos_list_response_403 import GetByOrgReposListResponse403
from ...models.get_by_org_repos_list_response_404 import GetByOrgReposListResponse404
from ...models.get_by_org_repos_list_response_406 import GetByOrgReposListResponse406
from ...models.get_by_org_repos_list_response_409 import GetByOrgReposListResponse409
from ...models.get_by_org_repos_list_response_500 import GetByOrgReposListResponse500
from ...models.get_by_org_repos_list_sort_by import GetByOrgReposListSortBy
from ...models.get_by_org_repos_list_sort_order import GetByOrgReposListSortOrder
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    org: str,
    *,
    page: int | Unset = 1,
    page_size: int | Unset = 25,
    sort_by: GetByOrgReposListSortBy | Unset = GetByOrgReposListSortBy.CREATED_AT,
    sort_order: GetByOrgReposListSortOrder | Unset = GetByOrgReposListSortOrder.DESC,
    search: str | Unset = UNSET,
    metadata: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page"] = page

    params["pageSize"] = page_size

    json_sort_by: str | Unset = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value

    params["sortBy"] = json_sort_by

    json_sort_order: str | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sortOrder"] = json_sort_order

    params["search"] = search

    params["metadata"] = metadata


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/{org}/repos/list".format(org=quote(str(org), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetByOrgReposListResponse200 | GetByOrgReposListResponse400 | GetByOrgReposListResponse401 | GetByOrgReposListResponse403 | GetByOrgReposListResponse404 | GetByOrgReposListResponse406 | GetByOrgReposListResponse409 | GetByOrgReposListResponse500 | None:
    if response.status_code == 200:
        response_200 = GetByOrgReposListResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetByOrgReposListResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetByOrgReposListResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetByOrgReposListResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetByOrgReposListResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 406:
        response_406 = GetByOrgReposListResponse406.from_dict(response.json())



        return response_406

    if response.status_code == 409:
        response_409 = GetByOrgReposListResponse409.from_dict(response.json())



        return response_409

    if response.status_code == 500:
        response_500 = GetByOrgReposListResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetByOrgReposListResponse200 | GetByOrgReposListResponse400 | GetByOrgReposListResponse401 | GetByOrgReposListResponse403 | GetByOrgReposListResponse404 | GetByOrgReposListResponse406 | GetByOrgReposListResponse409 | GetByOrgReposListResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    org: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 25,
    sort_by: GetByOrgReposListSortBy | Unset = GetByOrgReposListSortBy.CREATED_AT,
    sort_order: GetByOrgReposListSortOrder | Unset = GetByOrgReposListSortOrder.DESC,
    search: str | Unset = UNSET,
    metadata: str | Unset = UNSET,

) -> Response[GetByOrgReposListResponse200 | GetByOrgReposListResponse400 | GetByOrgReposListResponse401 | GetByOrgReposListResponse403 | GetByOrgReposListResponse404 | GetByOrgReposListResponse406 | GetByOrgReposListResponse409 | GetByOrgReposListResponse500]:
    """ List repositories (paginated)

     List repositories with offset pagination, sorting, search, and metadata filtering

    Args:
        org (str):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 25.
        sort_by (GetByOrgReposListSortBy | Unset):  Default: GetByOrgReposListSortBy.CREATED_AT.
        sort_order (GetByOrgReposListSortOrder | Unset):  Default:
            GetByOrgReposListSortOrder.DESC.
        search (str | Unset):
        metadata (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetByOrgReposListResponse200 | GetByOrgReposListResponse400 | GetByOrgReposListResponse401 | GetByOrgReposListResponse403 | GetByOrgReposListResponse404 | GetByOrgReposListResponse406 | GetByOrgReposListResponse409 | GetByOrgReposListResponse500]
     """


    kwargs = _get_kwargs(
        org=org,
page=page,
page_size=page_size,
sort_by=sort_by,
sort_order=sort_order,
search=search,
metadata=metadata,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    org: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 25,
    sort_by: GetByOrgReposListSortBy | Unset = GetByOrgReposListSortBy.CREATED_AT,
    sort_order: GetByOrgReposListSortOrder | Unset = GetByOrgReposListSortOrder.DESC,
    search: str | Unset = UNSET,
    metadata: str | Unset = UNSET,

) -> GetByOrgReposListResponse200 | GetByOrgReposListResponse400 | GetByOrgReposListResponse401 | GetByOrgReposListResponse403 | GetByOrgReposListResponse404 | GetByOrgReposListResponse406 | GetByOrgReposListResponse409 | GetByOrgReposListResponse500 | None:
    """ List repositories (paginated)

     List repositories with offset pagination, sorting, search, and metadata filtering

    Args:
        org (str):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 25.
        sort_by (GetByOrgReposListSortBy | Unset):  Default: GetByOrgReposListSortBy.CREATED_AT.
        sort_order (GetByOrgReposListSortOrder | Unset):  Default:
            GetByOrgReposListSortOrder.DESC.
        search (str | Unset):
        metadata (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetByOrgReposListResponse200 | GetByOrgReposListResponse400 | GetByOrgReposListResponse401 | GetByOrgReposListResponse403 | GetByOrgReposListResponse404 | GetByOrgReposListResponse406 | GetByOrgReposListResponse409 | GetByOrgReposListResponse500
     """


    return sync_detailed(
        org=org,
client=client,
page=page,
page_size=page_size,
sort_by=sort_by,
sort_order=sort_order,
search=search,
metadata=metadata,

    ).parsed

async def asyncio_detailed(
    org: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 25,
    sort_by: GetByOrgReposListSortBy | Unset = GetByOrgReposListSortBy.CREATED_AT,
    sort_order: GetByOrgReposListSortOrder | Unset = GetByOrgReposListSortOrder.DESC,
    search: str | Unset = UNSET,
    metadata: str | Unset = UNSET,

) -> Response[GetByOrgReposListResponse200 | GetByOrgReposListResponse400 | GetByOrgReposListResponse401 | GetByOrgReposListResponse403 | GetByOrgReposListResponse404 | GetByOrgReposListResponse406 | GetByOrgReposListResponse409 | GetByOrgReposListResponse500]:
    """ List repositories (paginated)

     List repositories with offset pagination, sorting, search, and metadata filtering

    Args:
        org (str):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 25.
        sort_by (GetByOrgReposListSortBy | Unset):  Default: GetByOrgReposListSortBy.CREATED_AT.
        sort_order (GetByOrgReposListSortOrder | Unset):  Default:
            GetByOrgReposListSortOrder.DESC.
        search (str | Unset):
        metadata (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetByOrgReposListResponse200 | GetByOrgReposListResponse400 | GetByOrgReposListResponse401 | GetByOrgReposListResponse403 | GetByOrgReposListResponse404 | GetByOrgReposListResponse406 | GetByOrgReposListResponse409 | GetByOrgReposListResponse500]
     """


    kwargs = _get_kwargs(
        org=org,
page=page,
page_size=page_size,
sort_by=sort_by,
sort_order=sort_order,
search=search,
metadata=metadata,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    org: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 25,
    sort_by: GetByOrgReposListSortBy | Unset = GetByOrgReposListSortBy.CREATED_AT,
    sort_order: GetByOrgReposListSortOrder | Unset = GetByOrgReposListSortOrder.DESC,
    search: str | Unset = UNSET,
    metadata: str | Unset = UNSET,

) -> GetByOrgReposListResponse200 | GetByOrgReposListResponse400 | GetByOrgReposListResponse401 | GetByOrgReposListResponse403 | GetByOrgReposListResponse404 | GetByOrgReposListResponse406 | GetByOrgReposListResponse409 | GetByOrgReposListResponse500 | None:
    """ List repositories (paginated)

     List repositories with offset pagination, sorting, search, and metadata filtering

    Args:
        org (str):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 25.
        sort_by (GetByOrgReposListSortBy | Unset):  Default: GetByOrgReposListSortBy.CREATED_AT.
        sort_order (GetByOrgReposListSortOrder | Unset):  Default:
            GetByOrgReposListSortOrder.DESC.
        search (str | Unset):
        metadata (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetByOrgReposListResponse200 | GetByOrgReposListResponse400 | GetByOrgReposListResponse401 | GetByOrgReposListResponse403 | GetByOrgReposListResponse404 | GetByOrgReposListResponse406 | GetByOrgReposListResponse409 | GetByOrgReposListResponse500
     """


    return (await asyncio_detailed(
        org=org,
client=client,
page=page,
page_size=page_size,
sort_by=sort_by,
sort_order=sort_order,
search=search,
metadata=metadata,

    )).parsed
