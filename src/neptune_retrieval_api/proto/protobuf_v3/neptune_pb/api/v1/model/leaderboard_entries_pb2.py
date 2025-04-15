"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1neptune_pb/api/v1/model/leaderboard_entries.proto\x12\x14neptune.api.v1.model"\xb6\x01\n&ProtoLeaderboardEntriesSearchResultDTO\x12\x1b\n\x13matching_item_count\x18\x01 \x01(\x03\x12\x1e\n\x11total_group_count\x18\x02 \x01(\x03H\x00\x88\x01\x01\x129\n\x07entries\x18\x03 \x03(\x0b2(.neptune.api.v1.model.ProtoAttributesDTOB\x14\n\x12_total_group_count"\xd4\x01\n\x12ProtoAttributesDTO\x12\x15\n\rexperiment_id\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x12\n\nproject_id\x18\x03 \x01(\t\x12\x17\n\x0forganization_id\x18\x04 \x01(\t\x12\x14\n\x0cproject_name\x18\x05 \x01(\t\x12\x19\n\x11organization_name\x18\x06 \x01(\t\x12;\n\nattributes\x18\x07 \x03(\x0b2\'.neptune.api.v1.model.ProtoAttributeDTO"\xec\x06\n\x11ProtoAttributeDTO\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12G\n\x0eint_properties\x18\x03 \x01(\x0b2*.neptune.api.v1.model.ProtoIntAttributeDTOH\x00\x88\x01\x01\x12K\n\x10float_properties\x18\x04 \x01(\x0b2,.neptune.api.v1.model.ProtoFloatAttributeDTOH\x01\x88\x01\x01\x12M\n\x11string_properties\x18\x05 \x01(\x0b2-.neptune.api.v1.model.ProtoStringAttributeDTOH\x02\x88\x01\x01\x12I\n\x0fbool_properties\x18\x06 \x01(\x0b2+.neptune.api.v1.model.ProtoBoolAttributeDTOH\x03\x88\x01\x01\x12Q\n\x13datetime_properties\x18\x07 \x01(\x0b2/.neptune.api.v1.model.ProtoDatetimeAttributeDTOH\x04\x88\x01\x01\x12T\n\x15string_set_properties\x18\x08 \x01(\x0b20.neptune.api.v1.model.ProtoStringSetAttributeDTOH\x05\x88\x01\x01\x12X\n\x17float_series_properties\x18\t \x01(\x0b22.neptune.api.v1.model.ProtoFloatSeriesAttributeDTOH\x06\x88\x01\x01\x12P\n\x13file_ref_properties\x18\n \x01(\x0b2..neptune.api.v1.model.ProtoFileRefAttributeDTOH\x07\x88\x01\x01B\x11\n\x0f_int_propertiesB\x13\n\x11_float_propertiesB\x14\n\x12_string_propertiesB\x12\n\x10_bool_propertiesB\x16\n\x14_datetime_propertiesB\x18\n\x16_string_set_propertiesB\x1a\n\x18_float_series_propertiesB\x16\n\x14_file_ref_properties"U\n\x14ProtoIntAttributeDTO\x12\x16\n\x0eattribute_name\x18\x01 \x01(\t\x12\x16\n\x0eattribute_type\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\x03"W\n\x16ProtoFloatAttributeDTO\x12\x16\n\x0eattribute_name\x18\x01 \x01(\t\x12\x16\n\x0eattribute_type\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\x01"X\n\x17ProtoStringAttributeDTO\x12\x16\n\x0eattribute_name\x18\x01 \x01(\t\x12\x16\n\x0eattribute_type\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t"V\n\x15ProtoBoolAttributeDTO\x12\x16\n\x0eattribute_name\x18\x01 \x01(\t\x12\x16\n\x0eattribute_type\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\x08"Z\n\x19ProtoDatetimeAttributeDTO\x12\x16\n\x0eattribute_name\x18\x01 \x01(\t\x12\x16\n\x0eattribute_type\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\x03"[\n\x1aProtoStringSetAttributeDTO\x12\x16\n\x0eattribute_name\x18\x01 \x01(\t\x12\x16\n\x0eattribute_type\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x03(\t"\xe9\x02\n\x1cProtoFloatSeriesAttributeDTO\x12\x16\n\x0eattribute_name\x18\x01 \x01(\t\x12\x16\n\x0eattribute_type\x18\x02 \x01(\t\x12\x16\n\tlast_step\x18\x03 \x01(\x01H\x00\x88\x01\x01\x12\x11\n\x04last\x18\x04 \x01(\x01H\x01\x88\x01\x01\x12\x10\n\x03min\x18\x05 \x01(\x01H\x02\x88\x01\x01\x12\x10\n\x03max\x18\x06 \x01(\x01H\x03\x88\x01\x01\x12\x14\n\x07average\x18\x07 \x01(\x01H\x04\x88\x01\x01\x12\x15\n\x08variance\x18\x08 \x01(\x01H\x05\x88\x01\x01\x12H\n\x06config\x18\t \x01(\x0b28.neptune.api.v1.model.ProtoFloatSeriesAttributeConfigDTO\x12\x13\n\x0bhas_preview\x18\n \x01(\x08B\x0c\n\n_last_stepB\x07\n\x05_lastB\x06\n\x04_minB\x06\n\x04_maxB\n\n\x08_averageB\x0b\n\t_variance"t\n"ProtoFloatSeriesAttributeConfigDTO\x12\x10\n\x03min\x18\x01 \x01(\x01H\x00\x88\x01\x01\x12\x10\n\x03max\x18\x02 \x01(\x01H\x01\x88\x01\x01\x12\x11\n\x04unit\x18\x03 \x01(\tH\x02\x88\x01\x01B\x06\n\x04_minB\x06\n\x04_maxB\x07\n\x05_unit"}\n\x18ProtoFileRefAttributeDTO\x12\x16\n\x0eattribute_name\x18\x01 \x01(\t\x12\x16\n\x0eattribute_type\x18\x02 \x01(\t\x12\x0c\n\x04path\x18\x03 \x01(\t\x12\x11\n\tsizeBytes\x18\x04 \x01(\x03\x12\x10\n\x08mimeType\x18\x05 \x01(\tB4\n0ml.neptune.leaderboard.api.model.proto.generatedP\x01b\x06proto3')
_PROTOLEADERBOARDENTRIESSEARCHRESULTDTO = DESCRIPTOR.message_types_by_name['ProtoLeaderboardEntriesSearchResultDTO']
_PROTOATTRIBUTESDTO = DESCRIPTOR.message_types_by_name['ProtoAttributesDTO']
_PROTOATTRIBUTEDTO = DESCRIPTOR.message_types_by_name['ProtoAttributeDTO']
_PROTOINTATTRIBUTEDTO = DESCRIPTOR.message_types_by_name['ProtoIntAttributeDTO']
_PROTOFLOATATTRIBUTEDTO = DESCRIPTOR.message_types_by_name['ProtoFloatAttributeDTO']
_PROTOSTRINGATTRIBUTEDTO = DESCRIPTOR.message_types_by_name['ProtoStringAttributeDTO']
_PROTOBOOLATTRIBUTEDTO = DESCRIPTOR.message_types_by_name['ProtoBoolAttributeDTO']
_PROTODATETIMEATTRIBUTEDTO = DESCRIPTOR.message_types_by_name['ProtoDatetimeAttributeDTO']
_PROTOSTRINGSETATTRIBUTEDTO = DESCRIPTOR.message_types_by_name['ProtoStringSetAttributeDTO']
_PROTOFLOATSERIESATTRIBUTEDTO = DESCRIPTOR.message_types_by_name['ProtoFloatSeriesAttributeDTO']
_PROTOFLOATSERIESATTRIBUTECONFIGDTO = DESCRIPTOR.message_types_by_name['ProtoFloatSeriesAttributeConfigDTO']
_PROTOFILEREFATTRIBUTEDTO = DESCRIPTOR.message_types_by_name['ProtoFileRefAttributeDTO']
ProtoLeaderboardEntriesSearchResultDTO = _reflection.GeneratedProtocolMessageType('ProtoLeaderboardEntriesSearchResultDTO', (_message.Message,), {'DESCRIPTOR': _PROTOLEADERBOARDENTRIESSEARCHRESULTDTO, '__module__': 'neptune_pb.api.v1.model.leaderboard_entries_pb2'})
_sym_db.RegisterMessage(ProtoLeaderboardEntriesSearchResultDTO)
ProtoAttributesDTO = _reflection.GeneratedProtocolMessageType('ProtoAttributesDTO', (_message.Message,), {'DESCRIPTOR': _PROTOATTRIBUTESDTO, '__module__': 'neptune_pb.api.v1.model.leaderboard_entries_pb2'})
_sym_db.RegisterMessage(ProtoAttributesDTO)
ProtoAttributeDTO = _reflection.GeneratedProtocolMessageType('ProtoAttributeDTO', (_message.Message,), {'DESCRIPTOR': _PROTOATTRIBUTEDTO, '__module__': 'neptune_pb.api.v1.model.leaderboard_entries_pb2'})
_sym_db.RegisterMessage(ProtoAttributeDTO)
ProtoIntAttributeDTO = _reflection.GeneratedProtocolMessageType('ProtoIntAttributeDTO', (_message.Message,), {'DESCRIPTOR': _PROTOINTATTRIBUTEDTO, '__module__': 'neptune_pb.api.v1.model.leaderboard_entries_pb2'})
_sym_db.RegisterMessage(ProtoIntAttributeDTO)
ProtoFloatAttributeDTO = _reflection.GeneratedProtocolMessageType('ProtoFloatAttributeDTO', (_message.Message,), {'DESCRIPTOR': _PROTOFLOATATTRIBUTEDTO, '__module__': 'neptune_pb.api.v1.model.leaderboard_entries_pb2'})
_sym_db.RegisterMessage(ProtoFloatAttributeDTO)
ProtoStringAttributeDTO = _reflection.GeneratedProtocolMessageType('ProtoStringAttributeDTO', (_message.Message,), {'DESCRIPTOR': _PROTOSTRINGATTRIBUTEDTO, '__module__': 'neptune_pb.api.v1.model.leaderboard_entries_pb2'})
_sym_db.RegisterMessage(ProtoStringAttributeDTO)
ProtoBoolAttributeDTO = _reflection.GeneratedProtocolMessageType('ProtoBoolAttributeDTO', (_message.Message,), {'DESCRIPTOR': _PROTOBOOLATTRIBUTEDTO, '__module__': 'neptune_pb.api.v1.model.leaderboard_entries_pb2'})
_sym_db.RegisterMessage(ProtoBoolAttributeDTO)
ProtoDatetimeAttributeDTO = _reflection.GeneratedProtocolMessageType('ProtoDatetimeAttributeDTO', (_message.Message,), {'DESCRIPTOR': _PROTODATETIMEATTRIBUTEDTO, '__module__': 'neptune_pb.api.v1.model.leaderboard_entries_pb2'})
_sym_db.RegisterMessage(ProtoDatetimeAttributeDTO)
ProtoStringSetAttributeDTO = _reflection.GeneratedProtocolMessageType('ProtoStringSetAttributeDTO', (_message.Message,), {'DESCRIPTOR': _PROTOSTRINGSETATTRIBUTEDTO, '__module__': 'neptune_pb.api.v1.model.leaderboard_entries_pb2'})
_sym_db.RegisterMessage(ProtoStringSetAttributeDTO)
ProtoFloatSeriesAttributeDTO = _reflection.GeneratedProtocolMessageType('ProtoFloatSeriesAttributeDTO', (_message.Message,), {'DESCRIPTOR': _PROTOFLOATSERIESATTRIBUTEDTO, '__module__': 'neptune_pb.api.v1.model.leaderboard_entries_pb2'})
_sym_db.RegisterMessage(ProtoFloatSeriesAttributeDTO)
ProtoFloatSeriesAttributeConfigDTO = _reflection.GeneratedProtocolMessageType('ProtoFloatSeriesAttributeConfigDTO', (_message.Message,), {'DESCRIPTOR': _PROTOFLOATSERIESATTRIBUTECONFIGDTO, '__module__': 'neptune_pb.api.v1.model.leaderboard_entries_pb2'})
_sym_db.RegisterMessage(ProtoFloatSeriesAttributeConfigDTO)
ProtoFileRefAttributeDTO = _reflection.GeneratedProtocolMessageType('ProtoFileRefAttributeDTO', (_message.Message,), {'DESCRIPTOR': _PROTOFILEREFATTRIBUTEDTO, '__module__': 'neptune_pb.api.v1.model.leaderboard_entries_pb2'})
_sym_db.RegisterMessage(ProtoFileRefAttributeDTO)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n0ml.neptune.leaderboard.api.model.proto.generatedP\x01'
    _PROTOLEADERBOARDENTRIESSEARCHRESULTDTO._serialized_start = 76
    _PROTOLEADERBOARDENTRIESSEARCHRESULTDTO._serialized_end = 258
    _PROTOATTRIBUTESDTO._serialized_start = 261
    _PROTOATTRIBUTESDTO._serialized_end = 473
    _PROTOATTRIBUTEDTO._serialized_start = 476
    _PROTOATTRIBUTEDTO._serialized_end = 1352
    _PROTOINTATTRIBUTEDTO._serialized_start = 1354
    _PROTOINTATTRIBUTEDTO._serialized_end = 1439
    _PROTOFLOATATTRIBUTEDTO._serialized_start = 1441
    _PROTOFLOATATTRIBUTEDTO._serialized_end = 1528
    _PROTOSTRINGATTRIBUTEDTO._serialized_start = 1530
    _PROTOSTRINGATTRIBUTEDTO._serialized_end = 1618
    _PROTOBOOLATTRIBUTEDTO._serialized_start = 1620
    _PROTOBOOLATTRIBUTEDTO._serialized_end = 1706
    _PROTODATETIMEATTRIBUTEDTO._serialized_start = 1708
    _PROTODATETIMEATTRIBUTEDTO._serialized_end = 1798
    _PROTOSTRINGSETATTRIBUTEDTO._serialized_start = 1800
    _PROTOSTRINGSETATTRIBUTEDTO._serialized_end = 1891
    _PROTOFLOATSERIESATTRIBUTEDTO._serialized_start = 1894
    _PROTOFLOATSERIESATTRIBUTEDTO._serialized_end = 2255
    _PROTOFLOATSERIESATTRIBUTECONFIGDTO._serialized_start = 2257
    _PROTOFLOATSERIESATTRIBUTECONFIGDTO._serialized_end = 2373
    _PROTOFILEREFATTRIBUTEDTO._serialized_start = 2375
    _PROTOFILEREFATTRIBUTEDTO._serialized_end = 2500