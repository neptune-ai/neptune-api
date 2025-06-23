from typing import (
    List,
    Tuple,
)

from neptune_api.proto.neptune_pb.ingest.v1.common_pb2 import ForkPoint

from neptune_api.proto import descriptor_pool as neptune_descriptor_pool
from google.protobuf import descriptor_pool as google_descriptor_pool

dto = ForkPoint()

dto_bytes = dto.SerializeToString()

data = ForkPoint.FromString(dto_bytes)

#print(data)
print('Google', google_descriptor_pool.Default())
print('neptune', neptune_descriptor_pool.Default())
print('dto', dto.DESCRIPTOR.file.pool)
print('data', data.DESCRIPTOR.file.pool)

