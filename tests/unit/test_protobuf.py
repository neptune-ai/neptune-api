import inspect

import pytest
from google.protobuf import message

from neptune_api.proto import descriptor_pool as neptune_api_descriptor_pool
from neptune_api.proto.neptune_pb.ingest.v1 import (
    common_pb2,
    ingest_pb2,
)
from neptune_retrieval_api.proto import descriptor_pool as neptune_retrieval_api_descriptor_pool
from neptune_retrieval_api.proto.neptune_pb.api.model import (
    attributes_pb2,
    leaderboard_entries_pb2,
    series_values_pb2,
)


@pytest.mark.parametrize(
    "cls",
    [cls for _, cls in inspect.getmembers(common_pb2, lambda x: inspect.isclass(x) and issubclass(x, message.Message))],
)
def test_protobuf_uses_local_pool__common_pb2(cls):
    # when
    created = cls()
    created_bytes = created.SerializeToString()
    parsed = cls.FromString(created_bytes)

    # then
    assert created.DESCRIPTOR.file.pool == neptune_api_descriptor_pool.Default()
    assert parsed.DESCRIPTOR.file.pool == neptune_api_descriptor_pool.Default()


@pytest.mark.parametrize(
    "cls",
    [cls for _, cls in inspect.getmembers(ingest_pb2, lambda x: inspect.isclass(x) and issubclass(x, message.Message))],
)
def test_protobuf_uses_local_pool__ingest_pb2(cls):
    # when
    created = cls()
    created_bytes = created.SerializeToString()
    parsed = cls.FromString(created_bytes)

    # then
    assert created.DESCRIPTOR.file.pool == neptune_api_descriptor_pool.Default()
    assert parsed.DESCRIPTOR.file.pool == neptune_api_descriptor_pool.Default()


@pytest.mark.parametrize(
    "cls",
    [
        cls
        for _, cls in inspect.getmembers(
            attributes_pb2, lambda x: inspect.isclass(x) and issubclass(x, message.Message)
        )
    ],
)
def test_protobuf_uses_local_pool__attributes_pb2(cls):
    # when
    created = cls()
    created_bytes = created.SerializeToString()
    parsed = cls.FromString(created_bytes)

    # then
    assert created.DESCRIPTOR.file.pool == neptune_retrieval_api_descriptor_pool.Default()
    assert parsed.DESCRIPTOR.file.pool == neptune_retrieval_api_descriptor_pool.Default()


@pytest.mark.parametrize(
    "cls",
    [
        cls
        for _, cls in inspect.getmembers(
            leaderboard_entries_pb2, lambda x: inspect.isclass(x) and issubclass(x, message.Message)
        )
    ],
)
def test_protobuf_uses_local_pool__leaderboard_entries_pb2(cls):
    # when
    created = cls()
    created_bytes = created.SerializeToString()
    parsed = cls.FromString(created_bytes)

    # then
    assert created.DESCRIPTOR.file.pool == neptune_retrieval_api_descriptor_pool.Default()
    assert parsed.DESCRIPTOR.file.pool == neptune_retrieval_api_descriptor_pool.Default()


@pytest.mark.parametrize(
    "cls",
    [
        cls
        for _, cls in inspect.getmembers(
            series_values_pb2, lambda x: inspect.isclass(x) and issubclass(x, message.Message)
        )
    ],
)
def test_protobuf_uses_local_pool__series_values_pb2(cls):
    # when
    created = cls()
    created_bytes = created.SerializeToString()
    parsed = cls.FromString(created_bytes)

    # then
    assert created.DESCRIPTOR.file.pool == neptune_retrieval_api_descriptor_pool.Default()
    assert parsed.DESCRIPTOR.file.pool == neptune_retrieval_api_descriptor_pool.Default()
