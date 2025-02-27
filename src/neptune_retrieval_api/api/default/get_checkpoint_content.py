#
# Copyright (c) 2025, Neptune Labs Sp. z o.o.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from http import HTTPStatus
from typing import (
    Any,
    Dict,
    Optional,
    Union,
)

import httpx

from ... import errors
from ...client import (
    AuthenticatedClient,
    Client,
)
from ...models.get_checkpoint_content_expected_content_disposition import GetCheckpointContentExpectedContentDisposition
from ...types import (
    UNSET,
    Response,
    Unset,
)


def _get_kwargs(
    id: str,
    *,
    expected_content_disposition: Union[
        Unset, GetCheckpointContentExpectedContentDisposition
    ] = GetCheckpointContentExpectedContentDisposition.ATTACHMENT,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_expected_content_disposition: Union[Unset, str] = UNSET
    if not isinstance(expected_content_disposition, Unset):
        json_expected_content_disposition = expected_content_disposition.value

    params["expectedContentDisposition"] = json_expected_content_disposition

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/leaderboard/v1/notebooks/checkpoints/{id}/content",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.BAD_REQUEST:
        return None
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        return None
    if response.status_code == HTTPStatus.FORBIDDEN:
        return None
    if response.status_code == HTTPStatus.NOT_FOUND:
        return None
    if response.status_code == HTTPStatus.REQUEST_TIMEOUT:
        return None
    if response.status_code == HTTPStatus.CONFLICT:
        return None
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        return None
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    expected_content_disposition: Union[
        Unset, GetCheckpointContentExpectedContentDisposition
    ] = GetCheckpointContentExpectedContentDisposition.ATTACHMENT,
) -> Response[Any]:
    """Get notebook checkpoint content

    Args:
        id (str):
        expected_content_disposition (Union[Unset,
            GetCheckpointContentExpectedContentDisposition]):  Default:
            GetCheckpointContentExpectedContentDisposition.ATTACHMENT.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        expected_content_disposition=expected_content_disposition,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    expected_content_disposition: Union[
        Unset, GetCheckpointContentExpectedContentDisposition
    ] = GetCheckpointContentExpectedContentDisposition.ATTACHMENT,
) -> Response[Any]:
    """Get notebook checkpoint content

    Args:
        id (str):
        expected_content_disposition (Union[Unset,
            GetCheckpointContentExpectedContentDisposition]):  Default:
            GetCheckpointContentExpectedContentDisposition.ATTACHMENT.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        expected_content_disposition=expected_content_disposition,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
