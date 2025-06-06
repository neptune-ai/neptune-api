"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
from ..... import neptune_pb
import typing
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class ProtoLeaderboardEntriesSearchResultDTO(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MATCHING_ITEM_COUNT_FIELD_NUMBER: builtins.int
    TOTAL_GROUP_COUNT_FIELD_NUMBER: builtins.int
    ENTRIES_FIELD_NUMBER: builtins.int
    matching_item_count: builtins.int
    total_group_count: builtins.int

    @property
    def entries(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ProtoAttributesDTO]:
        ...

    def __init__(self, *, matching_item_count: builtins.int=..., total_group_count: builtins.int | None=..., entries: collections.abc.Iterable[global___ProtoAttributesDTO] | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['_total_group_count', b'_total_group_count', 'total_group_count', b'total_group_count']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['_total_group_count', b'_total_group_count', 'entries', b'entries', 'matching_item_count', b'matching_item_count', 'total_group_count', b'total_group_count']) -> None:
        ...

    def WhichOneof(self, oneof_group: typing.Literal['_total_group_count', b'_total_group_count']) -> typing.Literal['total_group_count'] | None:
        ...
global___ProtoLeaderboardEntriesSearchResultDTO = ProtoLeaderboardEntriesSearchResultDTO

@typing.final
class ProtoAttributesDTO(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    EXPERIMENT_ID_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    PROJECT_ID_FIELD_NUMBER: builtins.int
    ORGANIZATION_ID_FIELD_NUMBER: builtins.int
    PROJECT_NAME_FIELD_NUMBER: builtins.int
    ORGANIZATION_NAME_FIELD_NUMBER: builtins.int
    ATTRIBUTES_FIELD_NUMBER: builtins.int
    experiment_id: builtins.str
    type: builtins.str
    project_id: builtins.str
    organization_id: builtins.str
    project_name: builtins.str
    organization_name: builtins.str

    @property
    def attributes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ProtoAttributeDTO]:
        ...

    def __init__(self, *, experiment_id: builtins.str=..., type: builtins.str=..., project_id: builtins.str=..., organization_id: builtins.str=..., project_name: builtins.str=..., organization_name: builtins.str=..., attributes: collections.abc.Iterable[global___ProtoAttributeDTO] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['attributes', b'attributes', 'experiment_id', b'experiment_id', 'organization_id', b'organization_id', 'organization_name', b'organization_name', 'project_id', b'project_id', 'project_name', b'project_name', 'type', b'type']) -> None:
        ...
global___ProtoAttributesDTO = ProtoAttributesDTO

@typing.final
class ProtoAttributeDTO(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    INT_PROPERTIES_FIELD_NUMBER: builtins.int
    FLOAT_PROPERTIES_FIELD_NUMBER: builtins.int
    STRING_PROPERTIES_FIELD_NUMBER: builtins.int
    BOOL_PROPERTIES_FIELD_NUMBER: builtins.int
    DATETIME_PROPERTIES_FIELD_NUMBER: builtins.int
    STRING_SET_PROPERTIES_FIELD_NUMBER: builtins.int
    FLOAT_SERIES_PROPERTIES_FIELD_NUMBER: builtins.int
    FILE_REF_PROPERTIES_FIELD_NUMBER: builtins.int
    STRING_SERIES_PROPERTIES_FIELD_NUMBER: builtins.int
    FILE_REF_SERIES_PROPERTIES_FIELD_NUMBER: builtins.int
    HISTOGRAM_SERIES_PROPERTIES_FIELD_NUMBER: builtins.int
    name: builtins.str
    type: builtins.str

    @property
    def int_properties(self) -> global___ProtoIntAttributeDTO:
        ...

    @property
    def float_properties(self) -> global___ProtoFloatAttributeDTO:
        ...

    @property
    def string_properties(self) -> global___ProtoStringAttributeDTO:
        ...

    @property
    def bool_properties(self) -> global___ProtoBoolAttributeDTO:
        ...

    @property
    def datetime_properties(self) -> global___ProtoDatetimeAttributeDTO:
        ...

    @property
    def string_set_properties(self) -> global___ProtoStringSetAttributeDTO:
        ...

    @property
    def float_series_properties(self) -> global___ProtoFloatSeriesAttributeDTO:
        ...

    @property
    def file_ref_properties(self) -> global___ProtoFileRefAttributeDTO:
        ...

    @property
    def string_series_properties(self) -> global___ProtoStringSeriesAttributeDTO:
        ...

    @property
    def file_ref_series_properties(self) -> global___ProtoFileRefSeriesAttributeDTO:
        ...

    @property
    def histogram_series_properties(self) -> global___ProtoHistogramSeriesAttributeDTO:
        ...

    def __init__(self, *, name: builtins.str=..., type: builtins.str=..., int_properties: global___ProtoIntAttributeDTO | None=..., float_properties: global___ProtoFloatAttributeDTO | None=..., string_properties: global___ProtoStringAttributeDTO | None=..., bool_properties: global___ProtoBoolAttributeDTO | None=..., datetime_properties: global___ProtoDatetimeAttributeDTO | None=..., string_set_properties: global___ProtoStringSetAttributeDTO | None=..., float_series_properties: global___ProtoFloatSeriesAttributeDTO | None=..., file_ref_properties: global___ProtoFileRefAttributeDTO | None=..., string_series_properties: global___ProtoStringSeriesAttributeDTO | None=..., file_ref_series_properties: global___ProtoFileRefSeriesAttributeDTO | None=..., histogram_series_properties: global___ProtoHistogramSeriesAttributeDTO | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['_bool_properties', b'_bool_properties', '_datetime_properties', b'_datetime_properties', '_file_ref_properties', b'_file_ref_properties', '_file_ref_series_properties', b'_file_ref_series_properties', '_float_properties', b'_float_properties', '_float_series_properties', b'_float_series_properties', '_histogram_series_properties', b'_histogram_series_properties', '_int_properties', b'_int_properties', '_string_properties', b'_string_properties', '_string_series_properties', b'_string_series_properties', '_string_set_properties', b'_string_set_properties', 'bool_properties', b'bool_properties', 'datetime_properties', b'datetime_properties', 'file_ref_properties', b'file_ref_properties', 'file_ref_series_properties', b'file_ref_series_properties', 'float_properties', b'float_properties', 'float_series_properties', b'float_series_properties', 'histogram_series_properties', b'histogram_series_properties', 'int_properties', b'int_properties', 'string_properties', b'string_properties', 'string_series_properties', b'string_series_properties', 'string_set_properties', b'string_set_properties']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['_bool_properties', b'_bool_properties', '_datetime_properties', b'_datetime_properties', '_file_ref_properties', b'_file_ref_properties', '_file_ref_series_properties', b'_file_ref_series_properties', '_float_properties', b'_float_properties', '_float_series_properties', b'_float_series_properties', '_histogram_series_properties', b'_histogram_series_properties', '_int_properties', b'_int_properties', '_string_properties', b'_string_properties', '_string_series_properties', b'_string_series_properties', '_string_set_properties', b'_string_set_properties', 'bool_properties', b'bool_properties', 'datetime_properties', b'datetime_properties', 'file_ref_properties', b'file_ref_properties', 'file_ref_series_properties', b'file_ref_series_properties', 'float_properties', b'float_properties', 'float_series_properties', b'float_series_properties', 'histogram_series_properties', b'histogram_series_properties', 'int_properties', b'int_properties', 'name', b'name', 'string_properties', b'string_properties', 'string_series_properties', b'string_series_properties', 'string_set_properties', b'string_set_properties', 'type', b'type']) -> None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_bool_properties', b'_bool_properties']) -> typing.Literal['bool_properties'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_datetime_properties', b'_datetime_properties']) -> typing.Literal['datetime_properties'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_file_ref_properties', b'_file_ref_properties']) -> typing.Literal['file_ref_properties'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_file_ref_series_properties', b'_file_ref_series_properties']) -> typing.Literal['file_ref_series_properties'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_float_properties', b'_float_properties']) -> typing.Literal['float_properties'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_float_series_properties', b'_float_series_properties']) -> typing.Literal['float_series_properties'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_histogram_series_properties', b'_histogram_series_properties']) -> typing.Literal['histogram_series_properties'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_int_properties', b'_int_properties']) -> typing.Literal['int_properties'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_string_properties', b'_string_properties']) -> typing.Literal['string_properties'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_string_series_properties', b'_string_series_properties']) -> typing.Literal['string_series_properties'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_string_set_properties', b'_string_set_properties']) -> typing.Literal['string_set_properties'] | None:
        ...
global___ProtoAttributeDTO = ProtoAttributeDTO

@typing.final
class ProtoIntAttributeDTO(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ATTRIBUTE_NAME_FIELD_NUMBER: builtins.int
    ATTRIBUTE_TYPE_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    attribute_name: builtins.str
    attribute_type: builtins.str
    value: builtins.int

    def __init__(self, *, attribute_name: builtins.str=..., attribute_type: builtins.str=..., value: builtins.int=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['attribute_name', b'attribute_name', 'attribute_type', b'attribute_type', 'value', b'value']) -> None:
        ...
global___ProtoIntAttributeDTO = ProtoIntAttributeDTO

@typing.final
class ProtoFloatAttributeDTO(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ATTRIBUTE_NAME_FIELD_NUMBER: builtins.int
    ATTRIBUTE_TYPE_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    attribute_name: builtins.str
    attribute_type: builtins.str
    value: builtins.float

    def __init__(self, *, attribute_name: builtins.str=..., attribute_type: builtins.str=..., value: builtins.float=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['attribute_name', b'attribute_name', 'attribute_type', b'attribute_type', 'value', b'value']) -> None:
        ...
global___ProtoFloatAttributeDTO = ProtoFloatAttributeDTO

@typing.final
class ProtoStringAttributeDTO(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ATTRIBUTE_NAME_FIELD_NUMBER: builtins.int
    ATTRIBUTE_TYPE_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    attribute_name: builtins.str
    attribute_type: builtins.str
    value: builtins.str

    def __init__(self, *, attribute_name: builtins.str=..., attribute_type: builtins.str=..., value: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['attribute_name', b'attribute_name', 'attribute_type', b'attribute_type', 'value', b'value']) -> None:
        ...
global___ProtoStringAttributeDTO = ProtoStringAttributeDTO

@typing.final
class ProtoBoolAttributeDTO(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ATTRIBUTE_NAME_FIELD_NUMBER: builtins.int
    ATTRIBUTE_TYPE_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    attribute_name: builtins.str
    attribute_type: builtins.str
    value: builtins.bool

    def __init__(self, *, attribute_name: builtins.str=..., attribute_type: builtins.str=..., value: builtins.bool=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['attribute_name', b'attribute_name', 'attribute_type', b'attribute_type', 'value', b'value']) -> None:
        ...
global___ProtoBoolAttributeDTO = ProtoBoolAttributeDTO

@typing.final
class ProtoDatetimeAttributeDTO(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ATTRIBUTE_NAME_FIELD_NUMBER: builtins.int
    ATTRIBUTE_TYPE_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    attribute_name: builtins.str
    attribute_type: builtins.str
    value: builtins.int

    def __init__(self, *, attribute_name: builtins.str=..., attribute_type: builtins.str=..., value: builtins.int=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['attribute_name', b'attribute_name', 'attribute_type', b'attribute_type', 'value', b'value']) -> None:
        ...
global___ProtoDatetimeAttributeDTO = ProtoDatetimeAttributeDTO

@typing.final
class ProtoStringSetAttributeDTO(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ATTRIBUTE_NAME_FIELD_NUMBER: builtins.int
    ATTRIBUTE_TYPE_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    attribute_name: builtins.str
    attribute_type: builtins.str

    @property
    def value(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        ...

    def __init__(self, *, attribute_name: builtins.str=..., attribute_type: builtins.str=..., value: collections.abc.Iterable[builtins.str] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['attribute_name', b'attribute_name', 'attribute_type', b'attribute_type', 'value', b'value']) -> None:
        ...
global___ProtoStringSetAttributeDTO = ProtoStringSetAttributeDTO

@typing.final
class ProtoFloatSeriesAttributeDTO(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ATTRIBUTE_NAME_FIELD_NUMBER: builtins.int
    ATTRIBUTE_TYPE_FIELD_NUMBER: builtins.int
    LAST_STEP_FIELD_NUMBER: builtins.int
    LAST_FIELD_NUMBER: builtins.int
    MIN_FIELD_NUMBER: builtins.int
    MAX_FIELD_NUMBER: builtins.int
    AVERAGE_FIELD_NUMBER: builtins.int
    VARIANCE_FIELD_NUMBER: builtins.int
    CONFIG_FIELD_NUMBER: builtins.int
    HAS_PREVIEW_FIELD_NUMBER: builtins.int
    attribute_name: builtins.str
    attribute_type: builtins.str
    last_step: builtins.float
    last: builtins.float
    min: builtins.float
    max: builtins.float
    average: builtins.float
    variance: builtins.float
    has_preview: builtins.bool

    @property
    def config(self) -> global___ProtoFloatSeriesAttributeConfigDTO:
        ...

    def __init__(self, *, attribute_name: builtins.str=..., attribute_type: builtins.str=..., last_step: builtins.float | None=..., last: builtins.float | None=..., min: builtins.float | None=..., max: builtins.float | None=..., average: builtins.float | None=..., variance: builtins.float | None=..., config: global___ProtoFloatSeriesAttributeConfigDTO | None=..., has_preview: builtins.bool=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['_average', b'_average', '_last', b'_last', '_last_step', b'_last_step', '_max', b'_max', '_min', b'_min', '_variance', b'_variance', 'average', b'average', 'config', b'config', 'last', b'last', 'last_step', b'last_step', 'max', b'max', 'min', b'min', 'variance', b'variance']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['_average', b'_average', '_last', b'_last', '_last_step', b'_last_step', '_max', b'_max', '_min', b'_min', '_variance', b'_variance', 'attribute_name', b'attribute_name', 'attribute_type', b'attribute_type', 'average', b'average', 'config', b'config', 'has_preview', b'has_preview', 'last', b'last', 'last_step', b'last_step', 'max', b'max', 'min', b'min', 'variance', b'variance']) -> None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_average', b'_average']) -> typing.Literal['average'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_last', b'_last']) -> typing.Literal['last'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_last_step', b'_last_step']) -> typing.Literal['last_step'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_max', b'_max']) -> typing.Literal['max'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_min', b'_min']) -> typing.Literal['min'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_variance', b'_variance']) -> typing.Literal['variance'] | None:
        ...
global___ProtoFloatSeriesAttributeDTO = ProtoFloatSeriesAttributeDTO

@typing.final
class ProtoFloatSeriesAttributeConfigDTO(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MIN_FIELD_NUMBER: builtins.int
    MAX_FIELD_NUMBER: builtins.int
    UNIT_FIELD_NUMBER: builtins.int
    min: builtins.float
    max: builtins.float
    unit: builtins.str

    def __init__(self, *, min: builtins.float | None=..., max: builtins.float | None=..., unit: builtins.str | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['_max', b'_max', '_min', b'_min', '_unit', b'_unit', 'max', b'max', 'min', b'min', 'unit', b'unit']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['_max', b'_max', '_min', b'_min', '_unit', b'_unit', 'max', b'max', 'min', b'min', 'unit', b'unit']) -> None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_max', b'_max']) -> typing.Literal['max'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_min', b'_min']) -> typing.Literal['min'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_unit', b'_unit']) -> typing.Literal['unit'] | None:
        ...
global___ProtoFloatSeriesAttributeConfigDTO = ProtoFloatSeriesAttributeConfigDTO

@typing.final
class ProtoFileRefAttributeDTO(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ATTRIBUTE_NAME_FIELD_NUMBER: builtins.int
    ATTRIBUTE_TYPE_FIELD_NUMBER: builtins.int
    PATH_FIELD_NUMBER: builtins.int
    SIZEBYTES_FIELD_NUMBER: builtins.int
    MIMETYPE_FIELD_NUMBER: builtins.int
    attribute_name: builtins.str
    attribute_type: builtins.str
    path: builtins.str
    sizeBytes: builtins.int
    mimeType: builtins.str

    def __init__(self, *, attribute_name: builtins.str=..., attribute_type: builtins.str=..., path: builtins.str=..., sizeBytes: builtins.int=..., mimeType: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['attribute_name', b'attribute_name', 'attribute_type', b'attribute_type', 'mimeType', b'mimeType', 'path', b'path', 'sizeBytes', b'sizeBytes']) -> None:
        ...
global___ProtoFileRefAttributeDTO = ProtoFileRefAttributeDTO

@typing.final
class ProtoStringSeriesAttributeDTO(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ATTRIBUTE_NAME_FIELD_NUMBER: builtins.int
    ATTRIBUTE_TYPE_FIELD_NUMBER: builtins.int
    LAST_STEP_FIELD_NUMBER: builtins.int
    LAST_FIELD_NUMBER: builtins.int
    attribute_name: builtins.str
    attribute_type: builtins.str
    last_step: builtins.float
    last: builtins.str

    def __init__(self, *, attribute_name: builtins.str=..., attribute_type: builtins.str=..., last_step: builtins.float | None=..., last: builtins.str | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['_last', b'_last', '_last_step', b'_last_step', 'last', b'last', 'last_step', b'last_step']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['_last', b'_last', '_last_step', b'_last_step', 'attribute_name', b'attribute_name', 'attribute_type', b'attribute_type', 'last', b'last', 'last_step', b'last_step']) -> None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_last', b'_last']) -> typing.Literal['last'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_last_step', b'_last_step']) -> typing.Literal['last_step'] | None:
        ...
global___ProtoStringSeriesAttributeDTO = ProtoStringSeriesAttributeDTO

@typing.final
class ProtoFileRefSeriesAttributeDTO(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ATTRIBUTE_NAME_FIELD_NUMBER: builtins.int
    ATTRIBUTE_TYPE_FIELD_NUMBER: builtins.int
    LAST_STEP_FIELD_NUMBER: builtins.int
    LAST_FIELD_NUMBER: builtins.int
    attribute_name: builtins.str
    attribute_type: builtins.str
    last_step: builtins.float

    @property
    def last(self) -> neptune_pb.api.v1.model.series_values_pb2.ProtoFileRef:
        ...

    def __init__(self, *, attribute_name: builtins.str=..., attribute_type: builtins.str=..., last_step: builtins.float | None=..., last: neptune_pb.api.v1.model.series_values_pb2.ProtoFileRef | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['_last', b'_last', '_last_step', b'_last_step', 'last', b'last', 'last_step', b'last_step']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['_last', b'_last', '_last_step', b'_last_step', 'attribute_name', b'attribute_name', 'attribute_type', b'attribute_type', 'last', b'last', 'last_step', b'last_step']) -> None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_last', b'_last']) -> typing.Literal['last'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_last_step', b'_last_step']) -> typing.Literal['last_step'] | None:
        ...
global___ProtoFileRefSeriesAttributeDTO = ProtoFileRefSeriesAttributeDTO

@typing.final
class ProtoHistogramSeriesAttributeDTO(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ATTRIBUTE_NAME_FIELD_NUMBER: builtins.int
    ATTRIBUTE_TYPE_FIELD_NUMBER: builtins.int
    LAST_STEP_FIELD_NUMBER: builtins.int
    LAST_FIELD_NUMBER: builtins.int
    attribute_name: builtins.str
    attribute_type: builtins.str
    last_step: builtins.float

    @property
    def last(self) -> neptune_pb.api.v1.model.series_values_pb2.ProtoHistogram:
        ...

    def __init__(self, *, attribute_name: builtins.str=..., attribute_type: builtins.str=..., last_step: builtins.float | None=..., last: neptune_pb.api.v1.model.series_values_pb2.ProtoHistogram | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['_last', b'_last', '_last_step', b'_last_step', 'last', b'last', 'last_step', b'last_step']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['_last', b'_last', '_last_step', b'_last_step', 'attribute_name', b'attribute_name', 'attribute_type', b'attribute_type', 'last', b'last', 'last_step', b'last_step']) -> None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_last', b'_last']) -> typing.Literal['last'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_last_step', b'_last_step']) -> typing.Literal['last_step'] | None:
        ...
global___ProtoHistogramSeriesAttributeDTO = ProtoHistogramSeriesAttributeDTO