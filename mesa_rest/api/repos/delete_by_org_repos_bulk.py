from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_by_org_repos_bulk_body import DeleteByOrgReposBulkBody
from ...models.delete_by_org_repos_bulk_response_200 import DeleteByOrgReposBulkResponse200
from ...models.delete_by_org_repos_bulk_response_400 import DeleteByOrgReposBulkResponse400
from ...models.delete_by_org_repos_bulk_response_401 import DeleteByOrgReposBulkResponse401
from ...models.delete_by_org_repos_bulk_response_403 import DeleteByOrgReposBulkResponse403
from ...models.delete_by_org_repos_bulk_response_404 import DeleteByOrgReposBulkResponse404
from ...models.delete_by_org_repos_bulk_response_406 import DeleteByOrgReposBulkResponse406
from ...models.delete_by_org_repos_bulk_response_409 import DeleteByOrgReposBulkResponse409
from ...models.delete_by_org_repos_bulk_response_500 import DeleteByOrgReposBulkResponse500
from typing import cast



def _get_kwargs(
    org: str,
    *,
    body: DeleteByOrgReposBulkBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/{org}/repos/bulk".format(org=quote(str(org), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteByOrgReposBulkResponse200 | DeleteByOrgReposBulkResponse400 | DeleteByOrgReposBulkResponse401 | DeleteByOrgReposBulkResponse403 | DeleteByOrgReposBulkResponse404 | DeleteByOrgReposBulkResponse406 | DeleteByOrgReposBulkResponse409 | DeleteByOrgReposBulkResponse500 | None:
    if response.status_code == 200:
        response_200 = DeleteByOrgReposBulkResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = DeleteByOrgReposBulkResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = DeleteByOrgReposBulkResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DeleteByOrgReposBulkResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DeleteByOrgReposBulkResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 406:
        response_406 = DeleteByOrgReposBulkResponse406.from_dict(response.json())



        return response_406

    if response.status_code == 409:
        response_409 = DeleteByOrgReposBulkResponse409.from_dict(response.json())



        return response_409

    if response.status_code == 500:
        response_500 = DeleteByOrgReposBulkResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteByOrgReposBulkResponse200 | DeleteByOrgReposBulkResponse400 | DeleteByOrgReposBulkResponse401 | DeleteByOrgReposBulkResponse403 | DeleteByOrgReposBulkResponse404 | DeleteByOrgReposBulkResponse406 | DeleteByOrgReposBulkResponse409 | DeleteByOrgReposBulkResponse500]:
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
    body: DeleteByOrgReposBulkBody,

) -> Response[DeleteByOrgReposBulkResponse200 | DeleteByOrgReposBulkResponse400 | DeleteByOrgReposBulkResponse401 | DeleteByOrgReposBulkResponse403 | DeleteByOrgReposBulkResponse404 | DeleteByOrgReposBulkResponse406 | DeleteByOrgReposBulkResponse409 | DeleteByOrgReposBulkResponse500]:
    """ Bulk delete repositories

     Bulk delete repos

    Args:
        org (str):
        body (DeleteByOrgReposBulkBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteByOrgReposBulkResponse200 | DeleteByOrgReposBulkResponse400 | DeleteByOrgReposBulkResponse401 | DeleteByOrgReposBulkResponse403 | DeleteByOrgReposBulkResponse404 | DeleteByOrgReposBulkResponse406 | DeleteByOrgReposBulkResponse409 | DeleteByOrgReposBulkResponse500]
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
    body: DeleteByOrgReposBulkBody,

) -> DeleteByOrgReposBulkResponse200 | DeleteByOrgReposBulkResponse400 | DeleteByOrgReposBulkResponse401 | DeleteByOrgReposBulkResponse403 | DeleteByOrgReposBulkResponse404 | DeleteByOrgReposBulkResponse406 | DeleteByOrgReposBulkResponse409 | DeleteByOrgReposBulkResponse500 | None:
    """ Bulk delete repositories

     Bulk delete repos

    Args:
        org (str):
        body (DeleteByOrgReposBulkBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteByOrgReposBulkResponse200 | DeleteByOrgReposBulkResponse400 | DeleteByOrgReposBulkResponse401 | DeleteByOrgReposBulkResponse403 | DeleteByOrgReposBulkResponse404 | DeleteByOrgReposBulkResponse406 | DeleteByOrgReposBulkResponse409 | DeleteByOrgReposBulkResponse500
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
    body: DeleteByOrgReposBulkBody,

) -> Response[DeleteByOrgReposBulkResponse200 | DeleteByOrgReposBulkResponse400 | DeleteByOrgReposBulkResponse401 | DeleteByOrgReposBulkResponse403 | DeleteByOrgReposBulkResponse404 | DeleteByOrgReposBulkResponse406 | DeleteByOrgReposBulkResponse409 | DeleteByOrgReposBulkResponse500]:
    """ Bulk delete repositories

     Bulk delete repos

    Args:
        org (str):
        body (DeleteByOrgReposBulkBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteByOrgReposBulkResponse200 | DeleteByOrgReposBulkResponse400 | DeleteByOrgReposBulkResponse401 | DeleteByOrgReposBulkResponse403 | DeleteByOrgReposBulkResponse404 | DeleteByOrgReposBulkResponse406 | DeleteByOrgReposBulkResponse409 | DeleteByOrgReposBulkResponse500]
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
    body: DeleteByOrgReposBulkBody,

) -> DeleteByOrgReposBulkResponse200 | DeleteByOrgReposBulkResponse400 | DeleteByOrgReposBulkResponse401 | DeleteByOrgReposBulkResponse403 | DeleteByOrgReposBulkResponse404 | DeleteByOrgReposBulkResponse406 | DeleteByOrgReposBulkResponse409 | DeleteByOrgReposBulkResponse500 | None:
    """ Bulk delete repositories

     Bulk delete repos

    Args:
        org (str):
        body (DeleteByOrgReposBulkBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteByOrgReposBulkResponse200 | DeleteByOrgReposBulkResponse400 | DeleteByOrgReposBulkResponse401 | DeleteByOrgReposBulkResponse403 | DeleteByOrgReposBulkResponse404 | DeleteByOrgReposBulkResponse406 | DeleteByOrgReposBulkResponse409 | DeleteByOrgReposBulkResponse500
     """


    return (await asyncio_detailed(
        org=org,
client=client,
body=body,

    )).parsed
