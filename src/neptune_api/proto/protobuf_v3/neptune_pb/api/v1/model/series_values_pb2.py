"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+neptune_pb/api/v1/model/series_values.proto\x12\x14neptune.api.v1.model"n\n\x1cProtoSeriesValuesResponseDTO\x12N\n\x06series\x18\x01 \x03(\x0b2>.neptune.api.v1.model.ProtoSeriesValuesSingleSeriesResponseDTO"\xb1\x02\n(ProtoSeriesValuesSingleSeriesResponseDTO\x12\x11\n\trequestId\x18\x01 \x01(\t\x12O\n\x0bsearchAfter\x18\x02 \x01(\x0b25.neptune.api.v1.model.ProtoSeriesValuesSearchAfterDTOH\x01\x88\x01\x01\x12C\n\rstring_series\x18\x03 \x01(\x0b2*.neptune.api.v1.model.ProtoSeriesValuesDTOH\x00\x12B\n\x0cseriesValues\x18\x04 \x01(\x0b2*.neptune.api.v1.model.ProtoSeriesValuesDTOH\x00B\x08\n\x06seriesB\x0e\n\x0c_searchAfter"B\n\x1fProtoSeriesValuesSearchAfterDTO\x12\x10\n\x08finished\x18\x01 \x01(\x08\x12\r\n\x05token\x18\x02 \x01(\t"x\n!ProtoFloatSeriesValuesResponseDTO\x12S\n\x06series\x18\x01 \x03(\x0b2C.neptune.api.v1.model.ProtoFloatSeriesValuesSingleSeriesResponseDTO"\x83\x01\n-ProtoFloatSeriesValuesSingleSeriesResponseDTO\x12\x11\n\trequestId\x18\x01 \x01(\t\x12?\n\x06series\x18\x02 \x01(\x0b2/.neptune.api.v1.model.ProtoFloatSeriesValuesDTO"t\n\x19ProtoFloatSeriesValuesDTO\x12\x18\n\x10total_item_count\x18\x01 \x01(\x03\x12=\n\x06values\x18\x02 \x03(\x0b2-.neptune.api.v1.model.ProtoFloatPointValueDTO"~\n\x17ProtoFloatPointValueDTO\x12\x18\n\x10timestamp_millis\x18\x01 \x01(\x03\x12\x0c\n\x04step\x18\x02 \x01(\x01\x12\r\n\x05value\x18\x03 \x01(\x01\x12\x12\n\nis_preview\x18\x04 \x01(\x08\x12\x18\n\x10completion_ratio\x18\x05 \x01(\x02"P\n\x14ProtoSeriesValuesDTO\x128\n\x06values\x18\x01 \x03(\x0b2(.neptune.api.v1.model.ProtoPointValueDTO"\xde\x01\n\x12ProtoPointValueDTO\x12\x18\n\x10timestamp_millis\x18\x01 \x01(\x03\x12\x0c\n\x04step\x18\x02 \x01(\x01\x12\x12\n\x05value\x18\x03 \x01(\tH\x00\x88\x01\x01\x12\x12\n\nis_preview\x18\x04 \x01(\x08\x12\x18\n\x10completion_ratio\x18\x05 \x01(\x02\x12I\n\x06object\x18\x06 \x01(\x0b24.neptune.api.v1.model.ProtoSeriesPointValueObjectDTOH\x01\x88\x01\x01B\x08\n\x06_valueB\t\n\x07_object"\xb2\x01\n\x1eProtoSeriesPointValueObjectDTO\x12\x15\n\x0bstringValue\x18\x01 \x01(\tH\x00\x129\n\thistogram\x18\x02 \x01(\x0b2$.neptune.api.v1.model.ProtoHistogramH\x00\x125\n\x07fileRef\x18\x03 \x01(\x0b2".neptune.api.v1.model.ProtoFileRefH\x00B\x07\n\x05value"=\n\x0eProtoHistogram\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\r\n\x05edges\x18\x02 \x03(\x01\x12\x0e\n\x06values\x18\x03 \x03(\x01"A\n\x0cProtoFileRef\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x11\n\tsizeBytes\x18\x02 \x01(\x03\x12\x10\n\x08mimeType\x18\x03 \x01(\t"U\n\x19ProtoTimeseriesBucketsDTO\x128\n\x07entries\x18\x01 \x03(\x0b2\'.neptune.api.v1.model.TimeseriesBuckets"^\n\x11TimeseriesBuckets\x12\x11\n\trequestId\x18\x01 \x01(\t\x126\n\x06bucket\x18\x02 \x03(\x0b2&.neptune.api.v1.model.TimeseriesBucket"\x89\x03\n\x10TimeseriesBucket\x12\r\n\x05index\x18\x01 \x01(\x03\x12\r\n\x05fromX\x18\x02 \x01(\x01\x12\x0b\n\x03toX\x18\x03 \x01(\x01\x125\n\x05first\x18\x04 \x01(\x0b2!.neptune.api.v1.model.FinitePointH\x00\x88\x01\x01\x124\n\x04last\x18\x05 \x01(\x0b2!.neptune.api.v1.model.FinitePointH\x01\x88\x01\x01\x12\x15\n\x08localMin\x18\x06 \x01(\x01H\x02\x88\x01\x01\x12\x15\n\x08localMax\x18\x07 \x01(\x01H\x03\x88\x01\x01\x12\x18\n\x10finitePointCount\x18\x08 \x01(\x03\x12\x10\n\x08nanCount\x18\t \x01(\x03\x12\x18\n\x10positiveInfCount\x18\n \x01(\x03\x12\x18\n\x10negativeInfCount\x18\x0b \x01(\x03\x12\x15\n\x08localSum\x18\x0c \x01(\x01H\x04\x88\x01\x01B\x08\n\x06_firstB\x07\n\x05_lastB\x0b\n\t_localMinB\x0b\n\t_localMaxB\x0b\n\t_localSum"#\n\x0bFinitePoint\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01B4\n0ml.neptune.leaderboard.api.model.proto.generatedP\x01b\x06proto3')
_PROTOSERIESVALUESRESPONSEDTO = DESCRIPTOR.message_types_by_name['ProtoSeriesValuesResponseDTO']
_PROTOSERIESVALUESSINGLESERIESRESPONSEDTO = DESCRIPTOR.message_types_by_name['ProtoSeriesValuesSingleSeriesResponseDTO']
_PROTOSERIESVALUESSEARCHAFTERDTO = DESCRIPTOR.message_types_by_name['ProtoSeriesValuesSearchAfterDTO']
_PROTOFLOATSERIESVALUESRESPONSEDTO = DESCRIPTOR.message_types_by_name['ProtoFloatSeriesValuesResponseDTO']
_PROTOFLOATSERIESVALUESSINGLESERIESRESPONSEDTO = DESCRIPTOR.message_types_by_name['ProtoFloatSeriesValuesSingleSeriesResponseDTO']
_PROTOFLOATSERIESVALUESDTO = DESCRIPTOR.message_types_by_name['ProtoFloatSeriesValuesDTO']
_PROTOFLOATPOINTVALUEDTO = DESCRIPTOR.message_types_by_name['ProtoFloatPointValueDTO']
_PROTOSERIESVALUESDTO = DESCRIPTOR.message_types_by_name['ProtoSeriesValuesDTO']
_PROTOPOINTVALUEDTO = DESCRIPTOR.message_types_by_name['ProtoPointValueDTO']
_PROTOSERIESPOINTVALUEOBJECTDTO = DESCRIPTOR.message_types_by_name['ProtoSeriesPointValueObjectDTO']
_PROTOHISTOGRAM = DESCRIPTOR.message_types_by_name['ProtoHistogram']
_PROTOFILEREF = DESCRIPTOR.message_types_by_name['ProtoFileRef']
_PROTOTIMESERIESBUCKETSDTO = DESCRIPTOR.message_types_by_name['ProtoTimeseriesBucketsDTO']
_TIMESERIESBUCKETS = DESCRIPTOR.message_types_by_name['TimeseriesBuckets']
_TIMESERIESBUCKET = DESCRIPTOR.message_types_by_name['TimeseriesBucket']
_FINITEPOINT = DESCRIPTOR.message_types_by_name['FinitePoint']
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
ProtoSeriesValuesDTO = _reflection.GeneratedProtocolMessageType('ProtoSeriesValuesDTO', (_message.Message,), {'DESCRIPTOR': _PROTOSERIESVALUESDTO, '__module__': 'neptune_pb.api.v1.model.series_values_pb2'})
_sym_db.RegisterMessage(ProtoSeriesValuesDTO)
ProtoPointValueDTO = _reflection.GeneratedProtocolMessageType('ProtoPointValueDTO', (_message.Message,), {'DESCRIPTOR': _PROTOPOINTVALUEDTO, '__module__': 'neptune_pb.api.v1.model.series_values_pb2'})
_sym_db.RegisterMessage(ProtoPointValueDTO)
ProtoSeriesPointValueObjectDTO = _reflection.GeneratedProtocolMessageType('ProtoSeriesPointValueObjectDTO', (_message.Message,), {'DESCRIPTOR': _PROTOSERIESPOINTVALUEOBJECTDTO, '__module__': 'neptune_pb.api.v1.model.series_values_pb2'})
_sym_db.RegisterMessage(ProtoSeriesPointValueObjectDTO)
ProtoHistogram = _reflection.GeneratedProtocolMessageType('ProtoHistogram', (_message.Message,), {'DESCRIPTOR': _PROTOHISTOGRAM, '__module__': 'neptune_pb.api.v1.model.series_values_pb2'})
_sym_db.RegisterMessage(ProtoHistogram)
ProtoFileRef = _reflection.GeneratedProtocolMessageType('ProtoFileRef', (_message.Message,), {'DESCRIPTOR': _PROTOFILEREF, '__module__': 'neptune_pb.api.v1.model.series_values_pb2'})
_sym_db.RegisterMessage(ProtoFileRef)
ProtoTimeseriesBucketsDTO = _reflection.GeneratedProtocolMessageType('ProtoTimeseriesBucketsDTO', (_message.Message,), {'DESCRIPTOR': _PROTOTIMESERIESBUCKETSDTO, '__module__': 'neptune_pb.api.v1.model.series_values_pb2'})
_sym_db.RegisterMessage(ProtoTimeseriesBucketsDTO)
TimeseriesBuckets = _reflection.GeneratedProtocolMessageType('TimeseriesBuckets', (_message.Message,), {'DESCRIPTOR': _TIMESERIESBUCKETS, '__module__': 'neptune_pb.api.v1.model.series_values_pb2'})
_sym_db.RegisterMessage(TimeseriesBuckets)
TimeseriesBucket = _reflection.GeneratedProtocolMessageType('TimeseriesBucket', (_message.Message,), {'DESCRIPTOR': _TIMESERIESBUCKET, '__module__': 'neptune_pb.api.v1.model.series_values_pb2'})
_sym_db.RegisterMessage(TimeseriesBucket)
FinitePoint = _reflection.GeneratedProtocolMessageType('FinitePoint', (_message.Message,), {'DESCRIPTOR': _FINITEPOINT, '__module__': 'neptune_pb.api.v1.model.series_values_pb2'})
_sym_db.RegisterMessage(FinitePoint)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n0ml.neptune.leaderboard.api.model.proto.generatedP\x01'
    _PROTOSERIESVALUESRESPONSEDTO._serialized_start = 69
    _PROTOSERIESVALUESRESPONSEDTO._serialized_end = 179
    _PROTOSERIESVALUESSINGLESERIESRESPONSEDTO._serialized_start = 182
    _PROTOSERIESVALUESSINGLESERIESRESPONSEDTO._serialized_end = 487
    _PROTOSERIESVALUESSEARCHAFTERDTO._serialized_start = 489
    _PROTOSERIESVALUESSEARCHAFTERDTO._serialized_end = 555
    _PROTOFLOATSERIESVALUESRESPONSEDTO._serialized_start = 557
    _PROTOFLOATSERIESVALUESRESPONSEDTO._serialized_end = 677
    _PROTOFLOATSERIESVALUESSINGLESERIESRESPONSEDTO._serialized_start = 680
    _PROTOFLOATSERIESVALUESSINGLESERIESRESPONSEDTO._serialized_end = 811
    _PROTOFLOATSERIESVALUESDTO._serialized_start = 813
    _PROTOFLOATSERIESVALUESDTO._serialized_end = 929
    _PROTOFLOATPOINTVALUEDTO._serialized_start = 931
    _PROTOFLOATPOINTVALUEDTO._serialized_end = 1057
    _PROTOSERIESVALUESDTO._serialized_start = 1059
    _PROTOSERIESVALUESDTO._serialized_end = 1139
    _PROTOPOINTVALUEDTO._serialized_start = 1142
    _PROTOPOINTVALUEDTO._serialized_end = 1364
    _PROTOSERIESPOINTVALUEOBJECTDTO._serialized_start = 1367
    _PROTOSERIESPOINTVALUEOBJECTDTO._serialized_end = 1545
    _PROTOHISTOGRAM._serialized_start = 1547
    _PROTOHISTOGRAM._serialized_end = 1608
    _PROTOFILEREF._serialized_start = 1610
    _PROTOFILEREF._serialized_end = 1675
    _PROTOTIMESERIESBUCKETSDTO._serialized_start = 1677
    _PROTOTIMESERIESBUCKETSDTO._serialized_end = 1762
    _TIMESERIESBUCKETS._serialized_start = 1764
    _TIMESERIESBUCKETS._serialized_end = 1858
    _TIMESERIESBUCKET._serialized_start = 1861
    _TIMESERIESBUCKET._serialized_end = 2254
    _FINITEPOINT._serialized_start = 2256
    _FINITEPOINT._serialized_end = 2291