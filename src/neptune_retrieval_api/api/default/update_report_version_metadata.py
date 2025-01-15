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

import datetime
from http import HTTPStatus
from typing import (
    Any,
    Dict,
    Optional,
    Union,
    cast,
)

import httpx

from ... import errors
from ...client import (
    AuthenticatedClient,
    Client,
)
from ...models.dependency_on_inaccessible_projects_error_dto import DependencyOnInaccessibleProjectsErrorDTO
from ...models.report_version_metadata_dto import ReportVersionMetadataDTO
from ...types import (
    UNSET,
    Response,
)


def _get_kwargs(
    report_id: str,
    version_id: str,
    *,
    body: ReportVersionMetadataDTO,
    project_identifier: str,
    publish_if_unmodified_since: datetime.datetime,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    params["projectIdentifier"] = project_identifier

    json_publish_if_unmodified_since = publish_if_unmodified_since.isoformat()
    params["publishIfUnmodifiedSince"] = json_publish_if_unmodified_since

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": f"/api/leaderboard/v1/reports/{report_id}/versions/{version_id}",
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DependencyOnInaccessibleProjectsErrorDTO, ReportVersionMetadataDTO]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ReportVersionMetadataDTO.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = DependencyOnInaccessibleProjectsErrorDTO.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.REQUEST_TIMEOUT:
        response_408 = cast(Any, None)
        return response_408
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = cast(Any, None)
        return response_409
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = cast(Any, None)
        return response_422
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = cast(Any, None)
        return response_429
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, DependencyOnInaccessibleProjectsErrorDTO, ReportVersionMetadataDTO]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    report_id: str,
    version_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ReportVersionMetadataDTO,
    project_identifier: str,
    publish_if_unmodified_since: datetime.datetime,
) -> Response[Union[Any, DependencyOnInaccessibleProjectsErrorDTO, ReportVersionMetadataDTO]]:
    """Update metadata of a report version

    Args:
        report_id (str):
        version_id (str):
        project_identifier (str):
        publish_if_unmodified_since (datetime.datetime):
        body (ReportVersionMetadataDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DependencyOnInaccessibleProjectsErrorDTO, ReportVersionMetadataDTO]]
    """

    kwargs = _get_kwargs(
        report_id=report_id,
        version_id=version_id,
        body=body,
        project_identifier=project_identifier,
        publish_if_unmodified_since=publish_if_unmodified_since,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    report_id: str,
    version_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ReportVersionMetadataDTO,
    project_identifier: str,
    publish_if_unmodified_since: datetime.datetime,
) -> Optional[Union[Any, DependencyOnInaccessibleProjectsErrorDTO, ReportVersionMetadataDTO]]:
    """Update metadata of a report version

    Args:
        report_id (str):
        version_id (str):
        project_identifier (str):
        publish_if_unmodified_since (datetime.datetime):
        body (ReportVersionMetadataDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DependencyOnInaccessibleProjectsErrorDTO, ReportVersionMetadataDTO]
    """

    return sync_detailed(
        report_id=report_id,
        version_id=version_id,
        client=client,
        body=body,
        project_identifier=project_identifier,
        publish_if_unmodified_since=publish_if_unmodified_since,
    ).parsed


async def asyncio_detailed(
    report_id: str,
    version_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ReportVersionMetadataDTO,
    project_identifier: str,
    publish_if_unmodified_since: datetime.datetime,
) -> Response[Union[Any, DependencyOnInaccessibleProjectsErrorDTO, ReportVersionMetadataDTO]]:
    """Update metadata of a report version

    Args:
        report_id (str):
        version_id (str):
        project_identifier (str):
        publish_if_unmodified_since (datetime.datetime):
        body (ReportVersionMetadataDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DependencyOnInaccessibleProjectsErrorDTO, ReportVersionMetadataDTO]]
    """

    kwargs = _get_kwargs(
        report_id=report_id,
        version_id=version_id,
        body=body,
        project_identifier=project_identifier,
        publish_if_unmodified_since=publish_if_unmodified_since,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    report_id: str,
    version_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ReportVersionMetadataDTO,
    project_identifier: str,
    publish_if_unmodified_since: datetime.datetime,
) -> Optional[Union[Any, DependencyOnInaccessibleProjectsErrorDTO, ReportVersionMetadataDTO]]:
    """Update metadata of a report version

    Args:
        report_id (str):
        version_id (str):
        project_identifier (str):
        publish_if_unmodified_since (datetime.datetime):
        body (ReportVersionMetadataDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DependencyOnInaccessibleProjectsErrorDTO, ReportVersionMetadataDTO]
    """

    return (
        await asyncio_detailed(
            report_id=report_id,
            version_id=version_id,
            client=client,
            body=body,
            project_identifier=project_identifier,
            publish_if_unmodified_since=publish_if_unmodified_since,
        )
    ).parsed
