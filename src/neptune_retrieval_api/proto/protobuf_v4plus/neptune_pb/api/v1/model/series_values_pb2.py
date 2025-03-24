"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+neptune_pb/api/v1/model/series_values.proto\x12\x14neptune.api.v1.model"x\n!ProtoFloatSeriesValuesResponseDTO\x12S\n\x06series\x18\x01 \x03(\x0b2C.neptune.api.v1.model.ProtoFloatSeriesValuesSingleSeriesResponseDTO"\x83\x01\n-ProtoFloatSeriesValuesSingleSeriesResponseDTO\x12\x11\n\trequestId\x18\x01 \x01(\t\x12?\n\x06series\x18\x02 \x01(\x0b2/.neptune.api.v1.model.ProtoFloatSeriesValuesDTO"t\n\x19ProtoFloatSeriesValuesDTO\x12\x18\n\x10total_item_count\x18\x01 \x01(\x03\x12=\n\x06values\x18\x02 \x03(\x0b2-.neptune.api.v1.model.ProtoFloatPointValueDTO"~\n\x17ProtoFloatPointValueDTO\x12\x18\n\x10timestamp_millis\x18\x01 \x01(\x03\x12\x0c\n\x04step\x18\x02 \x01(\x01\x12\r\n\x05value\x18\x03 \x01(\x01\x12\x12\n\nis_preview\x18\x04 \x01(\x08\x12\x18\n\x10completion_ratio\x18\x05 \x01(\x02B4\n0ml.neptune.leaderboard.api.model.proto.generatedP\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'neptune_pb.api.v1.model.series_values_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n0ml.neptune.leaderboard.api.model.proto.generatedP\x01'
    _globals['_PROTOFLOATSERIESVALUESRESPONSEDTO']._serialized_start = 69
    _globals['_PROTOFLOATSERIESVALUESRESPONSEDTO']._serialized_end = 189
    _globals['_PROTOFLOATSERIESVALUESSINGLESERIESRESPONSEDTO']._serialized_start = 192
    _globals['_PROTOFLOATSERIESVALUESSINGLESERIESRESPONSEDTO']._serialized_end = 323
    _globals['_PROTOFLOATSERIESVALUESDTO']._serialized_start = 325
    _globals['_PROTOFLOATSERIESVALUESDTO']._serialized_end = 441
    _globals['_PROTOFLOATPOINTVALUEDTO']._serialized_start = 443
    _globals['_PROTOFLOATPOINTVALUEDTO']._serialized_end = 569