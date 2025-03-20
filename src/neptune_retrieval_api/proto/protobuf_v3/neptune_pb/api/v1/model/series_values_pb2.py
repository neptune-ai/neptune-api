"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+neptune_pb/api/v1/model/series_values.proto\x12\x14neptune.api.v1.model"x\n!ProtoFloatSeriesValuesResponseDTO\x12S\n\x06series\x18\x01 \x03(\x0b2C.neptune.api.v1.model.ProtoFloatSeriesValuesSingleSeriesResponseDTO"\x83\x01\n-ProtoFloatSeriesValuesSingleSeriesResponseDTO\x12\x11\n\trequestId\x18\x01 \x01(\t\x12?\n\x06series\x18\x02 \x01(\x0b2/.neptune.api.v1.model.ProtoFloatSeriesValuesDTO"t\n\x19ProtoFloatSeriesValuesDTO\x12\x18\n\x10total_item_count\x18\x01 \x01(\x03\x12=\n\x06values\x18\x02 \x03(\x0b2-.neptune.api.v1.model.ProtoFloatPointValueDTO"~\n\x17ProtoFloatPointValueDTO\x12\x18\n\x10timestamp_millis\x18\x01 \x01(\x03\x12\x0c\n\x04step\x18\x02 \x01(\x01\x12\r\n\x05value\x18\x03 \x01(\x01\x12\x12\n\nis_preview\x18\x04 \x01(\x08\x12\x18\n\x10completion_ratio\x18\x05 \x01(\x02B4\n0ml.neptune.leaderboard.api.model.proto.generatedP\x01b\x06proto3')
_PROTOFLOATSERIESVALUESRESPONSEDTO = DESCRIPTOR.message_types_by_name['ProtoFloatSeriesValuesResponseDTO']
_PROTOFLOATSERIESVALUESSINGLESERIESRESPONSEDTO = DESCRIPTOR.message_types_by_name['ProtoFloatSeriesValuesSingleSeriesResponseDTO']
_PROTOFLOATSERIESVALUESDTO = DESCRIPTOR.message_types_by_name['ProtoFloatSeriesValuesDTO']
_PROTOFLOATPOINTVALUEDTO = DESCRIPTOR.message_types_by_name['ProtoFloatPointValueDTO']
ProtoFloatSeriesValuesResponseDTO = _reflection.GeneratedProtocolMessageType('ProtoFloatSeriesValuesResponseDTO', (_message.Message,), {'DESCRIPTOR': _PROTOFLOATSERIESVALUESRESPONSEDTO, '__module__': 'neptune_pb.api.v1.model.series_values_pb2'})
_sym_db.RegisterMessage(ProtoFloatSeriesValuesResponseDTO)
ProtoFloatSeriesValuesSingleSeriesResponseDTO = _reflection.GeneratedProtocolMessageType('ProtoFloatSeriesValuesSingleSeriesResponseDTO', (_message.Message,), {'DESCRIPTOR': _PROTOFLOATSERIESVALUESSINGLESERIESRESPONSEDTO, '__module__': 'neptune_pb.api.v1.model.series_values_pb2'})
_sym_db.RegisterMessage(ProtoFloatSeriesValuesSingleSeriesResponseDTO)
ProtoFloatSeriesValuesDTO = _reflection.GeneratedProtocolMessageType('ProtoFloatSeriesValuesDTO', (_message.Message,), {'DESCRIPTOR': _PROTOFLOATSERIESVALUESDTO, '__module__': 'neptune_pb.api.v1.model.series_values_pb2'})
_sym_db.RegisterMessage(ProtoFloatSeriesValuesDTO)
ProtoFloatPointValueDTO = _reflection.GeneratedProtocolMessageType('ProtoFloatPointValueDTO', (_message.Message,), {'DESCRIPTOR': _PROTOFLOATPOINTVALUEDTO, '__module__': 'neptune_pb.api.v1.model.series_values_pb2'})
_sym_db.RegisterMessage(ProtoFloatPointValueDTO)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n0ml.neptune.leaderboard.api.model.proto.generatedP\x01'
    _PROTOFLOATSERIESVALUESRESPONSEDTO._serialized_start = 69
    _PROTOFLOATSERIESVALUESRESPONSEDTO._serialized_end = 189
    _PROTOFLOATSERIESVALUESSINGLESERIESRESPONSEDTO._serialized_start = 192
    _PROTOFLOATSERIESVALUESSINGLESERIESRESPONSEDTO._serialized_end = 323
    _PROTOFLOATSERIESVALUESDTO._serialized_start = 325
    _PROTOFLOATSERIESVALUESDTO._serialized_end = 441
    _PROTOFLOATPOINTVALUEDTO._serialized_start = 443
    _PROTOFLOATPOINTVALUEDTO._serialized_end = 569