"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

from neptune_retrieval_api.proto import descriptor_pool as _descriptor_pool

_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2

from ...neptune_pb.ingest.v1 import common_pb2 as neptune__pb_dot_ingest_dot_v1_dot_common__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1bneptune_pb/api/fields.proto\x12\x0bneptune.api\x1a\x1fgoogle/protobuf/timestamp.proto\x1a!neptune_pb/ingest/v1/common.proto"\xdf\x02\n\x14AttributeTypeAndPath\x12=\n\x04type\x18\x01 \x01(\x0e2/.neptune.api.AttributeTypeAndPath.AttributeType\x12\x0c\n\x04path\x18\x02 \x01(\t"\xf9\x01\n\rAttributeType\x12\x0f\n\x0bPLACEHOLDER\x10\x00\x12\x0b\n\x07COMPLEX\x10\x01\x12\t\n\x05FLOAT\x10\x02\x12\n\n\x06STRING\x10\x03\x12\x08\n\x04FILE\x10\x04\x12\x0c\n\x08DATETIME\x10\x05\x12\x07\n\x03INT\x10\x06\x12\x08\n\x04BOOL\x10\x07\x12\x10\n\x0cFLOAT_SERIES\x10\x08\x12\x11\n\rSTRING_SERIES\x10\t\x12\x10\n\x0cIMAGE_SERIES\x10\n\x12\x0e\n\nSTRING_SET\x10\x0b\x12\x0c\n\x08FILE_SET\x10\x0c\x12\x0b\n\x07GIT_REF\x10\r\x12\x10\n\x0cNOTEBOOK_REF\x10\x0e\x12\x14\n\x10EXPERIMENT_STATE\x10\x0f"\xf8\x02\n\tFieldData\x12\x19\n\x0ffloat_atom_data\x18\x01 \x01(\x01H\x00\x12\x1a\n\x10string_atom_data\x18\x02 \x01(\tH\x00\x128\n\x12datetime_atom_data\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00\x12\x17\n\rint_atom_data\x18\x04 \x01(\x03H\x00\x12\x18\n\x0ebool_atom_data\x18\x05 \x01(\x08H\x00\x12B\n\x16float_time_series_data\x18\x06 \x01(\x0b2 .neptune.api.FloatTimeSeriesDataH\x00\x12D\n\x17string_time_series_data\x18\x07 \x01(\x0b2!.neptune.api.StringTimeSeriesDataH\x00\x125\n\x0fstring_set_data\x18\x08 \x01(\x0b2\x1a.neptune.api.StringSetDataH\x00B\x06\n\x04data"\x86\x02\n\x13FloatTimeSeriesData\x12\x11\n\tseries_id\x18\x01 \x01(\x0c\x12*\n\tlast_step\x18\x02 \x01(\x0b2\x17.neptune.ingest.v1.Step\x122\n\x0elast_timestamp\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x12\n\nlast_value\x18\x04 \x01(\x01\x12\x1a\n\x12finite_value_count\x18\x05 \x01(\x05\x12\x11\n\tnan_count\x18\x06 \x01(\x05\x12\x0b\n\x03sum\x18\x07 \x01(\x01\x12\x12\n\nsquare_sum\x18\x08 \x01(\x01\x12\x0b\n\x03min\x18\t \x01(\x01\x12\x0b\n\x03max\x18\n \x01(\x01"\xc0\x01\n\x14StringTimeSeriesData\x12\x11\n\tseries_id\x18\x01 \x01(\x0c\x12*\n\tlast_step\x18\x02 \x01(\x0b2\x17.neptune.ingest.v1.Step\x12\r\n\x05index\x18\x03 \x01(\x05\x122\n\x0elast_timestamp\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x12\n\nlast_value\x18\x05 \x01(\t\x12\x12\n\nsum_length\x18\x06 \x01(\x03"\x1f\n\rStringSetData\x12\x0e\n\x06values\x18\x01 \x03(\tB.\n*ml.neptune.leaderboard.api.proto.generatedP\x01b\x06proto3'
)
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "neptune_pb.api.fields_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals["DESCRIPTOR"]._serialized_options = b"\n*ml.neptune.leaderboard.api.proto.generatedP\x01"
    _globals["_ATTRIBUTETYPEANDPATH"]._serialized_start = 113
    _globals["_ATTRIBUTETYPEANDPATH"]._serialized_end = 464
    _globals["_ATTRIBUTETYPEANDPATH_ATTRIBUTETYPE"]._serialized_start = 215
    _globals["_ATTRIBUTETYPEANDPATH_ATTRIBUTETYPE"]._serialized_end = 464
    _globals["_FIELDDATA"]._serialized_start = 467
    _globals["_FIELDDATA"]._serialized_end = 843
    _globals["_FLOATTIMESERIESDATA"]._serialized_start = 846
    _globals["_FLOATTIMESERIESDATA"]._serialized_end = 1108
    _globals["_STRINGTIMESERIESDATA"]._serialized_start = 1111
    _globals["_STRINGTIMESERIESDATA"]._serialized_end = 1303
    _globals["_STRINGSETDATA"]._serialized_start = 1305
    _globals["_STRINGSETDATA"]._serialized_end = 1336
