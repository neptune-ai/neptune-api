from google.protobuf.descriptor_pool import DescriptorPool

_POOL = DescriptorPool()


def Default() -> DescriptorPool:
    return _POOL
