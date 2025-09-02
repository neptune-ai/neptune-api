"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&neptune_pb/api/v1/model/requests.proto\x12\x14neptune.api.v1.model"\x93\x01\n ProtoGetTimeseriesBucketsRequest\x12@\n\x0bexpressions\x18\x01 \x03(\x0b2+.neptune.api.v1.model.ProtoCustomExpression\x12-\n\x04view\x18\x02 \x01(\x0b2\x1f.neptune.api.v1.model.ProtoView"\xfa\x01\n\x15ProtoCustomExpression\x12\x11\n\trequestId\x18\x01 \x01(\t\x12@\n\x06holder\x18\x02 \x01(\x0b20.neptune.api.v1.model.AttributesHolderIdentifier\x12\x16\n\x0ecustomYFormula\x18\x03 \x01(\t\x12\x1b\n\x0eincludePreview\x18\x04 \x01(\x08H\x00\x88\x01\x01\x128\n\x07lineage\x18\x05 \x01(\x0e2".neptune.api.v1.model.ProtoLineageH\x01\x88\x01\x01B\x11\n\x0f_includePreviewB\n\n\x08_lineage"\xbd\x02\n\tProtoView\x12\x11\n\x04from\x18\x01 \x01(\x01H\x00\x88\x01\x01\x12\x0f\n\x02to\x18\x02 \x01(\x01H\x01\x88\x01\x01\x12B\n\x0cpointFilters\x18\x03 \x01(\x0b2\'.neptune.api.v1.model.ProtoPointFiltersH\x02\x88\x01\x01\x12\x12\n\nmaxBuckets\x18\x04 \x01(\x05\x120\n\x06xScale\x18\x05 \x01(\x0e2 .neptune.api.v1.model.ProtoScale\x120\n\x06yScale\x18\x06 \x01(\x0e2 .neptune.api.v1.model.ProtoScale\x12/\n\x05xAxis\x18\x07 \x01(\x0b2 .neptune.api.v1.model.ProtoXAxisB\x07\n\x05_fromB\x05\n\x03_toB\x0f\n\r_pointFilters"_\n\x11ProtoPointFilters\x12<\n\tstepRange\x18\x01 \x01(\x0b2$.neptune.api.v1.model.ProtoOpenRangeH\x00\x88\x01\x01B\x0c\n\n_stepRange"D\n\x0eProtoOpenRange\x12\x11\n\x04from\x18\x01 \x01(\x01H\x00\x88\x01\x01\x12\x0f\n\x02to\x18\x02 \x01(\x01H\x01\x88\x01\x01B\x07\n\x05_fromB\x05\n\x03_to"\xed\x01\n\nProtoXAxis\x12-\n\x05steps\x18\x01 \x01(\x0b2\x1c.neptune.api.v1.model.XStepsH\x00\x129\n\x0bepochMillis\x18\x02 \x01(\x0b2".neptune.api.v1.model.XEpochMillisH\x00\x12;\n\x0crelativeTime\x18\x03 \x01(\x0b2#.neptune.api.v1.model.XRelativeTimeH\x00\x12/\n\x06custom\x18\x04 \x01(\x0b2\x1d.neptune.api.v1.model.XCustomH\x00B\x07\n\x05value"\x08\n\x06XSteps"\x0e\n\x0cXEpochMillis"\x0f\n\rXRelativeTime"\x1d\n\x07XCustom\x12\x12\n\nexpression\x18\x01 \x01(\t"m\n\x1aAttributesHolderIdentifier\x12;\n\nentityType\x18\x01 \x01(\x0e2\'.neptune.api.v1.model.LineageEntityType\x12\x12\n\nidentifier\x18\x02 \x01(\t*!\n\nProtoScale\x12\n\n\x06linear\x10\x00\x12\x07\n\x03log\x10\x01*(\n\x0cProtoLineage\x12\x08\n\x04FULL\x10\x00\x12\x0e\n\nONLY_OWNED\x10\x01*,\n\x11LineageEntityType\x12\x0e\n\nEXPERIMENT\x10\x00\x12\x07\n\x03RUN\x10\x01B4\n0ml.neptune.leaderboard.api.model.proto.generatedP\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'neptune_pb.api.v1.model.requests_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n0ml.neptune.leaderboard.api.model.proto.generatedP\x01'
    _globals['_PROTOSCALE']._serialized_start = 1379
    _globals['_PROTOSCALE']._serialized_end = 1412
    _globals['_PROTOLINEAGE']._serialized_start = 1414
    _globals['_PROTOLINEAGE']._serialized_end = 1454
    _globals['_LINEAGEENTITYTYPE']._serialized_start = 1456
    _globals['_LINEAGEENTITYTYPE']._serialized_end = 1500
    _globals['_PROTOGETTIMESERIESBUCKETSREQUEST']._serialized_start = 65
    _globals['_PROTOGETTIMESERIESBUCKETSREQUEST']._serialized_end = 212
    _globals['_PROTOCUSTOMEXPRESSION']._serialized_start = 215
    _globals['_PROTOCUSTOMEXPRESSION']._serialized_end = 465
    _globals['_PROTOVIEW']._serialized_start = 468
    _globals['_PROTOVIEW']._serialized_end = 785
    _globals['_PROTOPOINTFILTERS']._serialized_start = 787
    _globals['_PROTOPOINTFILTERS']._serialized_end = 882
    _globals['_PROTOOPENRANGE']._serialized_start = 884
    _globals['_PROTOOPENRANGE']._serialized_end = 952
    _globals['_PROTOXAXIS']._serialized_start = 955
    _globals['_PROTOXAXIS']._serialized_end = 1192
    _globals['_XSTEPS']._serialized_start = 1194
    _globals['_XSTEPS']._serialized_end = 1202
    _globals['_XEPOCHMILLIS']._serialized_start = 1204
    _globals['_XEPOCHMILLIS']._serialized_end = 1218
    _globals['_XRELATIVETIME']._serialized_start = 1220
    _globals['_XRELATIVETIME']._serialized_end = 1235
    _globals['_XCUSTOM']._serialized_start = 1237
    _globals['_XCUSTOM']._serialized_end = 1266
    _globals['_ATTRIBUTESHOLDERIDENTIFIER']._serialized_start = 1268
    _globals['_ATTRIBUTESHOLDERIDENTIFIER']._serialized_end = 1377