from typing import (
    List,
    Tuple,
)

from neptune_retrieval_api.proto.neptune_pb.api.model.series_values_pb2 import (
    ProtoFloatPointValueDTO,
    ProtoFloatSeriesValuesDTO,
    ProtoFloatSeriesValuesResponseDTO,
    ProtoFloatSeriesValuesSingleSeriesResponseDTO,
)

from neptune_retrieval_api.proto import descriptor_pool as neptune_descriptor_pool
from google.protobuf import descriptor_pool as google_descriptor_pool


def values_dto(steps_values: List[Tuple[float, float]]) -> [ProtoFloatPointValueDTO]:
    return [
        ProtoFloatPointValueDTO(
            timestamp_millis=i,
            step=step,
            value=value,
        )
        for i, (step, value) in enumerate(steps_values)
    ]

def single_series_dto(
    steps_values: List[Tuple[float, float]], request_id: str = "0"
) -> ProtoFloatSeriesValuesSingleSeriesResponseDTO:
    return ProtoFloatSeriesValuesSingleSeriesResponseDTO(
        requestId=request_id,
        series=ProtoFloatSeriesValuesDTO(
            total_item_count=len(steps_values),
            values=values_dto(steps_values),
        ),
    )


dto = single_series_dto([(step, step * 2) for step in range(10)])

dto_bytes = dto.SerializeToString()

data = ProtoFloatSeriesValuesSingleSeriesResponseDTO.FromString(dto_bytes)

#print(data)
print('google', google_descriptor_pool.Default())
print('neptune', neptune_descriptor_pool.Default())
print('dto', dto.DESCRIPTOR.file.pool)
print('data', data.DESCRIPTOR.file.pool)

import inspect

print('google', type(google_descriptor_pool.Default()))
print('neptune', type(neptune_descriptor_pool.Default()))
print('google', inspect.getfile(type(google_descriptor_pool.Default())))
print('neptune', inspect.getfile(type(neptune_descriptor_pool.Default())))
