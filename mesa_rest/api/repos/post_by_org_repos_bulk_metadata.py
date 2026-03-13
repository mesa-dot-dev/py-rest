from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_by_org_repos_bulk_metadata_body import PostByOrgReposBulkMetadataBody
from ...models.post_by_org_repos_bulk_metadata_response_200 import PostByOrgReposBulkMetadataResponse200
from ...models.post_by_org_repos_bulk_metadata_response_400 import PostByOrgReposBulkMetadataResponse400
from ...models.post_by_org_repos_bulk_metadata_response_401 import PostByOrgReposBulkMetadataResponse401
from ...models.post_by_org_repos_bulk_metadata_response_403 import PostByOrgReposBulkMetadataResponse403
from ...models.post_by_org_repos_bulk_metadata_response_404 import PostByOrgReposBulkMetadataResponse404
from ...models.post_by_org_repos_bulk_metadata_response_406 import PostByOrgReposBulkMetadataResponse406
from ...models.post_by_org_repos_bulk_metadata_response_409 import PostByOrgReposBulkMetadataResponse409
from ...models.post_by_org_repos_bulk_metadata_response_500 import PostByOrgReposBulkMetadataResponse500
from typing import cast



def _get_kwargs(
    org: str,
    *,
    body: PostByOrgReposBulkMetadataBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/{org}/repos/bulk/metadata".format(org=quote(str(org), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostByOrgReposBulkMetadataResponse200 | PostByOrgReposBulkMetadataResponse400 | PostByOrgReposBulkMetadataResponse401 | PostByOrgReposBulkMetadataResponse403 | PostByOrgReposBulkMetadataResponse404 | PostByOrgReposBulkMetadataResponse406 | PostByOrgReposBulkMetadataResponse409 | PostByOrgReposBulkMetadataResponse500 | None:
    if response.status_code == 200:
        response_200 = PostByOrgReposBulkMetadataResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PostByOrgReposBulkMetadataResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostByOrgReposBulkMetadataResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostByOrgReposBulkMetadataResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PostByOrgReposBulkMetadataResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 406:
        response_406 = PostByOrgReposBulkMetadataResponse406.from_dict(response.json())



        return response_406

    if response.status_code == 409:
        response_409 = PostByOrgReposBulkMetadataResponse409.from_dict(response.json())



        return response_409

    if response.status_code == 500:
        response_500 = PostByOrgReposBulkMetadataResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostByOrgReposBulkMetadataResponse200 | PostByOrgReposBulkMetadataResponse400 | PostByOrgReposBulkMetadataResponse401 | PostByOrgReposBulkMetadataResponse403 | PostByOrgReposBulkMetadataResponse404 | PostByOrgReposBulkMetadataResponse406 | PostByOrgReposBulkMetadataResponse409 | PostByOrgReposBulkMetadataResponse500]:
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
    body: PostByOrgReposBulkMetadataBody,

) -> Response[PostByOrgReposBulkMetadataResponse200 | PostByOrgReposBulkMetadataResponse400 | PostByOrgReposBulkMetadataResponse401 | PostByOrgReposBulkMetadataResponse403 | PostByOrgReposBulkMetadataResponse404 | PostByOrgReposBulkMetadataResponse406 | PostByOrgReposBulkMetadataResponse409 | PostByOrgReposBulkMetadataResponse500]:
    """ Bulk set or remove metadata

     Bulk set or remove metadata

    Args:
        org (str):
        body (PostByOrgReposBulkMetadataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostByOrgReposBulkMetadataResponse200 | PostByOrgReposBulkMetadataResponse400 | PostByOrgReposBulkMetadataResponse401 | PostByOrgReposBulkMetadataResponse403 | PostByOrgReposBulkMetadataResponse404 | PostByOrgReposBulkMetadataResponse406 | PostByOrgReposBulkMetadataResponse409 | PostByOrgReposBulkMetadataResponse500]
     """


    kwargs = _get_kwargs(
        org=org,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    org: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostByOrgReposBulkMetadataBody,

) -> PostByOrgReposBulkMetadataResponse200 | PostByOrgReposBulkMetadataResponse400 | PostByOrgReposBulkMetadataResponse401 | PostByOrgReposBulkMetadataResponse403 | PostByOrgReposBulkMetadataResponse404 | PostByOrgReposBulkMetadataResponse406 | PostByOrgReposBulkMetadataResponse409 | PostByOrgReposBulkMetadataResponse500 | None:
    """ Bulk set or remove metadata

     Bulk set or remove metadata

    Args:
        org (str):
        body (PostByOrgReposBulkMetadataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostByOrgReposBulkMetadataResponse200 | PostByOrgReposBulkMetadataResponse400 | PostByOrgReposBulkMetadataResponse401 | PostByOrgReposBulkMetadataResponse403 | PostByOrgReposBulkMetadataResponse404 | PostByOrgReposBulkMetadataResponse406 | PostByOrgReposBulkMetadataResponse409 | PostByOrgReposBulkMetadataResponse500
     """


    return sync_detailed(
        org=org,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    org: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostByOrgReposBulkMetadataBody,

) -> Response[PostByOrgReposBulkMetadataResponse200 | PostByOrgReposBulkMetadataResponse400 | PostByOrgReposBulkMetadataResponse401 | PostByOrgReposBulkMetadataResponse403 | PostByOrgReposBulkMetadataResponse404 | PostByOrgReposBulkMetadataResponse406 | PostByOrgReposBulkMetadataResponse409 | PostByOrgReposBulkMetadataResponse500]:
    """ Bulk set or remove metadata

     Bulk set or remove metadata

    Args:
        org (str):
        body (PostByOrgReposBulkMetadataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostByOrgReposBulkMetadataResponse200 | PostByOrgReposBulkMetadataResponse400 | PostByOrgReposBulkMetadataResponse401 | PostByOrgReposBulkMetadataResponse403 | PostByOrgReposBulkMetadataResponse404 | PostByOrgReposBulkMetadataResponse406 | PostByOrgReposBulkMetadataResponse409 | PostByOrgReposBulkMetadataResponse500]
     """


    kwargs = _get_kwargs(
        org=org,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    org: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostByOrgReposBulkMetadataBody,

) -> PostByOrgReposBulkMetadataResponse200 | PostByOrgReposBulkMetadataResponse400 | PostByOrgReposBulkMetadataResponse401 | PostByOrgReposBulkMetadataResponse403 | PostByOrgReposBulkMetadataResponse404 | PostByOrgReposBulkMetadataResponse406 | PostByOrgReposBulkMetadataResponse409 | PostByOrgReposBulkMetadataResponse500 | None:
    """ Bulk set or remove metadata

     Bulk set or remove metadata

    Args:
        org (str):
        body (PostByOrgReposBulkMetadataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostByOrgReposBulkMetadataResponse200 | PostByOrgReposBulkMetadataResponse400 | PostByOrgReposBulkMetadataResponse401 | PostByOrgReposBulkMetadataResponse403 | PostByOrgReposBulkMetadataResponse404 | PostByOrgReposBulkMetadataResponse406 | PostByOrgReposBulkMetadataResponse409 | PostByOrgReposBulkMetadataResponse500
     """


    return (await asyncio_detailed(
        org=org,
client=client,
body=body,

    )).parsed
