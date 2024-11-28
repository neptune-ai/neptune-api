from typing import Optional
from google.protobuf import descriptor_pool

_DEFAULT_POOL: descriptor_pool.DescriptorPool = descriptor_pool.Default()
_LOCAL_POOL: Optional[descriptor_pool.DescriptorPool] = None


if _LOCAL_POOL is None:
    import google.protobuf.timestamp_pb2  # loads timestamp.proto

    _LOCAL_POOL = descriptor_pool.DescriptorPool()

    descriptor = _DEFAULT_POOL.FindFileByName('google/protobuf/timestamp.proto')
    _LOCAL_POOL.AddSerializedFile(descriptor.serialized_pb)


def Default() -> descriptor_pool.DescriptorPool:
    assert _LOCAL_POOL is not None
    return _LOCAL_POOL
