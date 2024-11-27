"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

from neptune_retrieval_api.proto import descriptor_pool as _descriptor_pool

_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n.neptune_pb/api/model/leaderboard_entries.proto\x12\x11neptune.api.model"\xb3\x01\n&ProtoLeaderboardEntriesSearchResultDTO\x12\x1b\n\x13matching_item_count\x18\x01 \x01(\x03\x12\x1e\n\x11total_group_count\x18\x02 \x01(\x03H\x00\x88\x01\x01\x126\n\x07entries\x18\x03 \x03(\x0b2%.neptune.api.model.ProtoAttributesDTOB\x14\n\x12_total_group_count"\xd1\x01\n\x12ProtoAttributesDTO\x12\x15\n\rexperiment_id\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x12\n\nproject_id\x18\x03 \x01(\t\x12\x17\n\x0forganization_id\x18\x04 \x01(\t\x12\x14\n\x0cproject_name\x18\x05 \x01(\t\x12\x19\n\x11organization_name\x18\x06 \x01(\t\x128\n\nattributes\x18\x07 \x03(\x0b2$.neptune.api.model.ProtoAttributeDTO"\xed\x05\n\x11ProtoAttributeDTO\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12D\n\x0eint_properties\x18\x03 \x01(\x0b2\'.neptune.api.model.ProtoIntAttributeDTOH\x00\x88\x01\x01\x12H\n\x10float_properties\x18\x04 \x01(\x0b2).neptune.api.model.ProtoFloatAttributeDTOH\x01\x88\x01\x01\x12J\n\x11string_properties\x18\x05 \x01(\x0b2*.neptune.api.model.ProtoStringAttributeDTOH\x02\x88\x01\x01\x12F\n\x0fbool_properties\x18\x06 \x01(\x0b2(.neptune.api.model.ProtoBoolAttributeDTOH\x03\x88\x01\x01\x12N\n\x13datetime_properties\x18\x07 \x01(\x0b2,.neptune.api.model.ProtoDatetimeAttributeDTOH\x04\x88\x01\x01\x12Q\n\x15string_set_properties\x18\x08 \x01(\x0b2-.neptune.api.model.ProtoStringSetAttributeDTOH\x05\x88\x01\x01\x12U\n\x17float_series_properties\x18\t \x01(\x0b2/.neptune.api.model.ProtoFloatSeriesAttributeDTOH\x06\x88\x01\x01B\x11\n\x0f_int_propertiesB\x13\n\x11_float_propertiesB\x14\n\x12_string_propertiesB\x12\n\x10_bool_propertiesB\x16\n\x14_datetime_propertiesB\x18\n\x16_string_set_propertiesB\x1a\n\x18_float_series_properties"U\n\x14ProtoIntAttributeDTO\x12\x16\n\x0eattribute_name\x18\x01 \x01(\t\x12\x16\n\x0eattribute_type\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\x03"W\n\x16ProtoFloatAttributeDTO\x12\x16\n\x0eattribute_name\x18\x01 \x01(\t\x12\x16\n\x0eattribute_type\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\x01"X\n\x17ProtoStringAttributeDTO\x12\x16\n\x0eattribute_name\x18\x01 \x01(\t\x12\x16\n\x0eattribute_type\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t"V\n\x15ProtoBoolAttributeDTO\x12\x16\n\x0eattribute_name\x18\x01 \x01(\t\x12\x16\n\x0eattribute_type\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\x08"Z\n\x19ProtoDatetimeAttributeDTO\x12\x16\n\x0eattribute_name\x18\x01 \x01(\t\x12\x16\n\x0eattribute_type\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\x03"[\n\x1aProtoStringSetAttributeDTO\x12\x16\n\x0eattribute_name\x18\x01 \x01(\t\x12\x16\n\x0eattribute_type\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x03(\t"\xd1\x02\n\x1cProtoFloatSeriesAttributeDTO\x12\x16\n\x0eattribute_name\x18\x01 \x01(\t\x12\x16\n\x0eattribute_type\x18\x02 \x01(\t\x12\x16\n\tlast_step\x18\x03 \x01(\x01H\x00\x88\x01\x01\x12\x11\n\x04last\x18\x04 \x01(\x01H\x01\x88\x01\x01\x12\x10\n\x03min\x18\x05 \x01(\x01H\x02\x88\x01\x01\x12\x10\n\x03max\x18\x06 \x01(\x01H\x03\x88\x01\x01\x12\x14\n\x07average\x18\x07 \x01(\x01H\x04\x88\x01\x01\x12\x15\n\x08variance\x18\x08 \x01(\x01H\x05\x88\x01\x01\x12E\n\x06config\x18\t \x01(\x0b25.neptune.api.model.ProtoFloatSeriesAttributeConfigDTOB\x0c\n\n_last_stepB\x07\n\x05_lastB\x06\n\x04_minB\x06\n\x04_maxB\n\n\x08_averageB\x0b\n\t_variance"t\n"ProtoFloatSeriesAttributeConfigDTO\x12\x10\n\x03min\x18\x01 \x01(\x01H\x00\x88\x01\x01\x12\x10\n\x03max\x18\x02 \x01(\x01H\x01\x88\x01\x01\x12\x11\n\x04unit\x18\x03 \x01(\tH\x02\x88\x01\x01B\x06\n\x04_minB\x06\n\x04_maxB\x07\n\x05_unitB4\n0ml.neptune.leaderboard.api.model.proto.generatedP\x01b\x06proto3'
)
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "neptune_pb.api.model.leaderboard_entries_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals["DESCRIPTOR"]._serialized_options = b"\n0ml.neptune.leaderboard.api.model.proto.generatedP\x01"
    _globals["_PROTOLEADERBOARDENTRIESSEARCHRESULTDTO"]._serialized_start = 70
    _globals["_PROTOLEADERBOARDENTRIESSEARCHRESULTDTO"]._serialized_end = 249
    _globals["_PROTOATTRIBUTESDTO"]._serialized_start = 252
    _globals["_PROTOATTRIBUTESDTO"]._serialized_end = 461
    _globals["_PROTOATTRIBUTEDTO"]._serialized_start = 464
    _globals["_PROTOATTRIBUTEDTO"]._serialized_end = 1213
    _globals["_PROTOINTATTRIBUTEDTO"]._serialized_start = 1215
    _globals["_PROTOINTATTRIBUTEDTO"]._serialized_end = 1300
    _globals["_PROTOFLOATATTRIBUTEDTO"]._serialized_start = 1302
    _globals["_PROTOFLOATATTRIBUTEDTO"]._serialized_end = 1389
    _globals["_PROTOSTRINGATTRIBUTEDTO"]._serialized_start = 1391
    _globals["_PROTOSTRINGATTRIBUTEDTO"]._serialized_end = 1479
    _globals["_PROTOBOOLATTRIBUTEDTO"]._serialized_start = 1481
    _globals["_PROTOBOOLATTRIBUTEDTO"]._serialized_end = 1567
    _globals["_PROTODATETIMEATTRIBUTEDTO"]._serialized_start = 1569
    _globals["_PROTODATETIMEATTRIBUTEDTO"]._serialized_end = 1659
    _globals["_PROTOSTRINGSETATTRIBUTEDTO"]._serialized_start = 1661
    _globals["_PROTOSTRINGSETATTRIBUTEDTO"]._serialized_end = 1752
    _globals["_PROTOFLOATSERIESATTRIBUTEDTO"]._serialized_start = 1755
    _globals["_PROTOFLOATSERIESATTRIBUTEDTO"]._serialized_end = 2092
    _globals["_PROTOFLOATSERIESATTRIBUTECONFIGDTO"]._serialized_start = 2094
    _globals["_PROTOFLOATSERIESATTRIBUTECONFIGDTO"]._serialized_end = 2210
