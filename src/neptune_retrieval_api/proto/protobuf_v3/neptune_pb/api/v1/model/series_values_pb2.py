"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+neptune_pb/api/v1/model/series_values.proto\x12\x14neptune.api.v1.model"n\n\x1cProtoSeriesValuesResponseDTO\x12N\n\x06series\x18\x01 \x03(\x0b2>.neptune.api.v1.model.ProtoSeriesValuesSingleSeriesResponseDTO"\xf3\x01\n(ProtoSeriesValuesSingleSeriesResponseDTO\x12\x11\n\trequestId\x18\x01 \x01(\t\x12O\n\x0bsearchAfter\x18\x02 \x01(\x0b25.neptune.api.v1.model.ProtoSeriesValuesSearchAfterDTOH\x01\x88\x01\x01\x12I\n\rstring_series\x18\x03 \x01(\x0b20.neptune.api.v1.model.ProtoStringSeriesValuesDTOH\x00B\x08\n\x06seriesB\x0e\n\x0c_searchAfter"B\n\x1fProtoSeriesValuesSearchAfterDTO\x12\x10\n\x08finished\x18\x01 \x01(\x08\x12\r\n\x05token\x18\x02 \x01(\t"x\n!ProtoFloatSeriesValuesResponseDTO\x12S\n\x06series\x18\x01 \x03(\x0b2C.neptune.api.v1.model.ProtoFloatSeriesValuesSingleSeriesResponseDTO"\x83\x01\n-ProtoFloatSeriesValuesSingleSeriesResponseDTO\x12\x11\n\trequestId\x18\x01 \x01(\t\x12?\n\x06series\x18\x02 \x01(\x0b2/.neptune.api.v1.model.ProtoFloatSeriesValuesDTO"t\n\x19ProtoFloatSeriesValuesDTO\x12\x18\n\x10total_item_count\x18\x01 \x01(\x03\x12=\n\x06values\x18\x02 \x03(\x0b2-.neptune.api.v1.model.ProtoFloatPointValueDTO"~\n\x17ProtoFloatPointValueDTO\x12\x18\n\x10timestamp_millis\x18\x01 \x01(\x03\x12\x0c\n\x04step\x18\x02 \x01(\x01\x12\r\n\x05value\x18\x03 \x01(\x01\x12\x12\n\nis_preview\x18\x04 \x01(\x08\x12\x18\n\x10completion_ratio\x18\x05 \x01(\x02"\\\n\x1aProtoStringSeriesValuesDTO\x12>\n\x06values\x18\x01 \x03(\x0b2..neptune.api.v1.model.ProtoStringPointValueDTO"\x7f\n\x18ProtoStringPointValueDTO\x12\x18\n\x10timestamp_millis\x18\x01 \x01(\x03\x12\x0c\n\x04step\x18\x02 \x01(\x01\x12\r\n\x05value\x18\x03 \x01(\t\x12\x12\n\nis_preview\x18\x04 \x01(\x08\x12\x18\n\x10completion_ratio\x18\x05 \x01(\x02B4\n0ml.neptune.leaderboard.api.model.proto.generatedP\x01b\x06proto3')
_PROTOSERIESVALUESRESPONSEDTO = DESCRIPTOR.message_types_by_name['ProtoSeriesValuesResponseDTO']
_PROTOSERIESVALUESSINGLESERIESRESPONSEDTO = DESCRIPTOR.message_types_by_name['ProtoSeriesValuesSingleSeriesResponseDTO']
_PROTOSERIESVALUESSEARCHAFTERDTO = DESCRIPTOR.message_types_by_name['ProtoSeriesValuesSearchAfterDTO']
_PROTOFLOATSERIESVALUESRESPONSEDTO = DESCRIPTOR.message_types_by_name['ProtoFloatSeriesValuesResponseDTO']
_PROTOFLOATSERIESVALUESSINGLESERIESRESPONSEDTO = DESCRIPTOR.message_types_by_name['ProtoFloatSeriesValuesSingleSeriesResponseDTO']
_PROTOFLOATSERIESVALUESDTO = DESCRIPTOR.message_types_by_name['ProtoFloatSeriesValuesDTO']
_PROTOFLOATPOINTVALUEDTO = DESCRIPTOR.message_types_by_name['ProtoFloatPointValueDTO']
_PROTOSTRINGSERIESVALUESDTO = DESCRIPTOR.message_types_by_name['ProtoStringSeriesValuesDTO']
_PROTOSTRINGPOINTVALUEDTO = DESCRIPTOR.message_types_by_name['ProtoStringPointValueDTO']
ProtoSeriesValuesResponseDTO = _reflection.GeneratedProtocolMessageType('ProtoSeriesValuesResponseDTO', (_message.Message,), {'DESCRIPTOR': _PROTOSERIESVALUESRESPONSEDTO, '__module__': 'neptune_pb.api.v1.model.series_values_pb2'})
_sym_db.RegisterMessage(ProtoSeriesValuesResponseDTO)
ProtoSeriesValuesSingleSeriesResponseDTO = _reflection.GeneratedProtocolMessageType('ProtoSeriesValuesSingleSeriesResponseDTO', (_message.Message,), {'DESCRIPTOR': _PROTOSERIESVALUESSINGLESERIESRESPONSEDTO, '__module__': 'neptune_pb.api.v1.model.series_values_pb2'})
_sym_db.RegisterMessage(ProtoSeriesValuesSingleSeriesResponseDTO)
ProtoSeriesValuesSearchAfterDTO = _reflection.GeneratedProtocolMessageType('ProtoSeriesValuesSearchAfterDTO', (_message.Message,), {'DESCRIPTOR': _PROTOSERIESVALUESSEARCHAFTERDTO, '__module__': 'neptune_pb.api.v1.model.series_values_pb2'})
_sym_db.RegisterMessage(ProtoSeriesValuesSearchAfterDTO)
ProtoFloatSeriesValuesResponseDTO = _reflection.GeneratedProtocolMessageType('ProtoFloatSeriesValuesResponseDTO', (_message.Message,), {'DESCRIPTOR': _PROTOFLOATSERIESVALUESRESPONSEDTO, '__module__': 'neptune_pb.api.v1.model.series_values_pb2'})
_sym_db.RegisterMessage(ProtoFloatSeriesValuesResponseDTO)
ProtoFloatSeriesValuesSingleSeriesResponseDTO = _reflection.GeneratedProtocolMessageType('ProtoFloatSeriesValuesSingleSeriesResponseDTO', (_message.Message,), {'DESCRIPTOR': _PROTOFLOATSERIESVALUESSINGLESERIESRESPONSEDTO, '__module__': 'neptune_pb.api.v1.model.series_values_pb2'})
_sym_db.RegisterMessage(ProtoFloatSeriesValuesSingleSeriesResponseDTO)
ProtoFloatSeriesValuesDTO = _reflection.GeneratedProtocolMessageType('ProtoFloatSeriesValuesDTO', (_message.Message,), {'DESCRIPTOR': _PROTOFLOATSERIESVALUESDTO, '__module__': 'neptune_pb.api.v1.model.series_values_pb2'})
_sym_db.RegisterMessage(ProtoFloatSeriesValuesDTO)
ProtoFloatPointValueDTO = _reflection.GeneratedProtocolMessageType('ProtoFloatPointValueDTO', (_message.Message,), {'DESCRIPTOR': _PROTOFLOATPOINTVALUEDTO, '__module__': 'neptune_pb.api.v1.model.series_values_pb2'})
_sym_db.RegisterMessage(ProtoFloatPointValueDTO)
ProtoStringSeriesValuesDTO = _reflection.GeneratedProtocolMessageType('ProtoStringSeriesValuesDTO', (_message.Message,), {'DESCRIPTOR': _PROTOSTRINGSERIESVALUESDTO, '__module__': 'neptune_pb.api.v1.model.series_values_pb2'})
_sym_db.RegisterMessage(ProtoStringSeriesValuesDTO)
ProtoStringPointValueDTO = _reflection.GeneratedProtocolMessageType('ProtoStringPointValueDTO', (_message.Message,), {'DESCRIPTOR': _PROTOSTRINGPOINTVALUEDTO, '__module__': 'neptune_pb.api.v1.model.series_values_pb2'})
_sym_db.RegisterMessage(ProtoStringPointValueDTO)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n0ml.neptune.leaderboard.api.model.proto.generatedP\x01'
    _PROTOSERIESVALUESRESPONSEDTO._serialized_start = 69
    _PROTOSERIESVALUESRESPONSEDTO._serialized_end = 179
    _PROTOSERIESVALUESSINGLESERIESRESPONSEDTO._serialized_start = 182
    _PROTOSERIESVALUESSINGLESERIESRESPONSEDTO._serialized_end = 425
    _PROTOSERIESVALUESSEARCHAFTERDTO._serialized_start = 427
    _PROTOSERIESVALUESSEARCHAFTERDTO._serialized_end = 493
    _PROTOFLOATSERIESVALUESRESPONSEDTO._serialized_start = 495
    _PROTOFLOATSERIESVALUESRESPONSEDTO._serialized_end = 615
    _PROTOFLOATSERIESVALUESSINGLESERIESRESPONSEDTO._serialized_start = 618
    _PROTOFLOATSERIESVALUESSINGLESERIESRESPONSEDTO._serialized_end = 749
    _PROTOFLOATSERIESVALUESDTO._serialized_start = 751
    _PROTOFLOATSERIESVALUESDTO._serialized_end = 867
    _PROTOFLOATPOINTVALUEDTO._serialized_start = 869
    _PROTOFLOATPOINTVALUEDTO._serialized_end = 995
    _PROTOSTRINGSERIESVALUESDTO._serialized_start = 997
    _PROTOSTRINGSERIESVALUESDTO._serialized_end = 1089
    _PROTOSTRINGPOINTVALUEDTO._serialized_start = 1091
    _PROTOSTRINGPOINTVALUEDTO._serialized_end = 1218