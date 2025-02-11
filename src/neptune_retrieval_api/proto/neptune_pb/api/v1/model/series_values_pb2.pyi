
'\n@generated by mypy-protobuf.  Do not edit manually!\nisort:skip_file\n'
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class ProtoFloatSeriesValuesResponseDTO(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SERIES_FIELD_NUMBER: builtins.int

    @property
    def series(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ProtoFloatSeriesValuesSingleSeriesResponseDTO]:
        ...

    def __init__(self, *, series: (collections.abc.Iterable[global___ProtoFloatSeriesValuesSingleSeriesResponseDTO] | None)=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal[('series', b'series')]) -> None:
        ...
global___ProtoFloatSeriesValuesResponseDTO = ProtoFloatSeriesValuesResponseDTO

@typing.final
class ProtoFloatSeriesValuesSingleSeriesResponseDTO(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    REQUESTID_FIELD_NUMBER: builtins.int
    SERIES_FIELD_NUMBER: builtins.int
    requestId: builtins.str

    @property
    def series(self) -> global___ProtoFloatSeriesValuesDTO:
        ...

    def __init__(self, *, requestId: builtins.str=..., series: (global___ProtoFloatSeriesValuesDTO | None)=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal[('series', b'series')]) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal[('requestId', b'requestId', 'series', b'series')]) -> None:
        ...
global___ProtoFloatSeriesValuesSingleSeriesResponseDTO = ProtoFloatSeriesValuesSingleSeriesResponseDTO

@typing.final
class ProtoFloatSeriesValuesDTO(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TOTAL_ITEM_COUNT_FIELD_NUMBER: builtins.int
    VALUES_FIELD_NUMBER: builtins.int
    total_item_count: builtins.int

    @property
    def values(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ProtoFloatPointValueDTO]:
        ...

    def __init__(self, *, total_item_count: builtins.int=..., values: (collections.abc.Iterable[global___ProtoFloatPointValueDTO] | None)=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal[('total_item_count', b'total_item_count', 'values', b'values')]) -> None:
        ...
global___ProtoFloatSeriesValuesDTO = ProtoFloatSeriesValuesDTO

@typing.final
class ProtoFloatPointValueDTO(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TIMESTAMP_MILLIS_FIELD_NUMBER: builtins.int
    STEP_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    timestamp_millis: builtins.int
    step: builtins.float
    value: builtins.float

    def __init__(self, *, timestamp_millis: builtins.int=..., step: builtins.float=..., value: builtins.float=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal[('step', b'step', 'timestamp_millis', b'timestamp_millis', 'value', b'value')]) -> None:
        ...
global___ProtoFloatPointValueDTO = ProtoFloatPointValueDTO
