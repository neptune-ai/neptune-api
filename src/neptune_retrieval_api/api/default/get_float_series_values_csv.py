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
from ...models.get_float_series_values_csv_expected_content_disposition import (
    GetFloatSeriesValuesCSVExpectedContentDisposition,
)
from ...types import (
    UNSET,
    Response,
    Unset,
)


def _get_kwargs(
    *,
    attribute: str,
    expected_content_disposition: Union[
        Unset, GetFloatSeriesValuesCSVExpectedContentDisposition
    ] = GetFloatSeriesValuesCSVExpectedContentDisposition.ATTACHMENT,
    experiment_id: Union[Unset, str] = UNSET,
    gzipped: Union[Unset, bool] = UNSET,
    holder_identifier: Union[Unset, str] = UNSET,
    holder_type: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["attribute"] = attribute

    json_expected_content_disposition: Union[Unset, str] = UNSET
    if not isinstance(expected_content_disposition, Unset):
        json_expected_content_disposition = expected_content_disposition.value

    params["expectedContentDisposition"] = json_expected_content_disposition

    params["experimentId"] = experiment_id

    params["gzipped"] = gzipped

    params["holderIdentifier"] = holder_identifier

    params["holderType"] = holder_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/leaderboard/v1/attributes/floatSeries/csv",
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
    *,
    client: Union[AuthenticatedClient, Client],
    attribute: str,
    expected_content_disposition: Union[
        Unset, GetFloatSeriesValuesCSVExpectedContentDisposition
    ] = GetFloatSeriesValuesCSVExpectedContentDisposition.ATTACHMENT,
    experiment_id: Union[Unset, str] = UNSET,
    gzipped: Union[Unset, bool] = UNSET,
    holder_identifier: Union[Unset, str] = UNSET,
    holder_type: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Get values of a float series

    Args:
        attribute (str):
        expected_content_disposition (Union[Unset,
            GetFloatSeriesValuesCSVExpectedContentDisposition]):  Default:
            GetFloatSeriesValuesCSVExpectedContentDisposition.ATTACHMENT.
        experiment_id (Union[Unset, str]):
        gzipped (Union[Unset, bool]):
        holder_identifier (Union[Unset, str]):
        holder_type (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        attribute=attribute,
        expected_content_disposition=expected_content_disposition,
        experiment_id=experiment_id,
        gzipped=gzipped,
        holder_identifier=holder_identifier,
        holder_type=holder_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    attribute: str,
    expected_content_disposition: Union[
        Unset, GetFloatSeriesValuesCSVExpectedContentDisposition
    ] = GetFloatSeriesValuesCSVExpectedContentDisposition.ATTACHMENT,
    experiment_id: Union[Unset, str] = UNSET,
    gzipped: Union[Unset, bool] = UNSET,
    holder_identifier: Union[Unset, str] = UNSET,
    holder_type: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Get values of a float series

    Args:
        attribute (str):
        expected_content_disposition (Union[Unset,
            GetFloatSeriesValuesCSVExpectedContentDisposition]):  Default:
            GetFloatSeriesValuesCSVExpectedContentDisposition.ATTACHMENT.
        experiment_id (Union[Unset, str]):
        gzipped (Union[Unset, bool]):
        holder_identifier (Union[Unset, str]):
        holder_type (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        attribute=attribute,
        expected_content_disposition=expected_content_disposition,
        experiment_id=experiment_id,
        gzipped=gzipped,
        holder_identifier=holder_identifier,
        holder_type=holder_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
