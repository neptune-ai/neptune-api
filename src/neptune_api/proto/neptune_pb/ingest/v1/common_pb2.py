"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!neptune_pb/ingest/v1/common.proto\x12\x11neptune.ingest.v1\x1a\x1fgoogle/protobuf/timestamp.proto"$\n\x04Step\x12\r\n\x05whole\x18\x01 \x01(\x04\x12\r\n\x05micro\x18\x02 \x01(\x04"\x9b\x01\n\tForkPoint\x12\x16\n\x0eparent_project\x18\x01 \x01(\t\x12\x15\n\rparent_run_id\x18\x02 \x01(\t\x12%\n\x04step\x18\x04 \x01(\x0b2\x17.neptune.ingest.v1.Step\x12 \n\x13requested_parent_id\x18\x0f \x01(\tH\x00\x88\x01\x01B\x16\n\x14_requested_parent_id"\x1b\n\tStringSet\x12\x0e\n\x06values\x18\x01 \x03(\t"\xbb\x01\n\x05Value\x12\x11\n\x07float64\x18\x01 \x01(\x01H\x00\x12\x0f\n\x05int64\x18\x03 \x01(\x03H\x00\x12\x0e\n\x04bool\x18\x05 \x01(\x08H\x00\x12\x10\n\x06string\x18\x06 \x01(\tH\x00\x12/\n\ttimestamp\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00\x122\n\nstring_set\x18\x0c \x01(\x0b2\x1c.neptune.ingest.v1.StringSetH\x00B\x07\n\x05value"\xa2\x01\n\x0fModifyStringSet\x12>\n\x06values\x18\x01 \x03(\x0b2..neptune.ingest.v1.ModifyStringSet.ValuesEntry\x1aO\n\x0bValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12/\n\x05value\x18\x02 \x01(\x0e2 .neptune.ingest.v1.SET_OPERATION:\x028\x01"I\n\tModifySet\x124\n\x06string\x18\x01 \x01(\x0b2".neptune.ingest.v1.ModifyStringSetH\x00B\x06\n\x04type"F\n\x05Owner\x12\x11\n\x07user_id\x18\x01 \x01(\tH\x00\x12\x1c\n\x12service_account_id\x18\x02 \x01(\tH\x00B\x0c\n\nowner_type"\xa9\x03\n\x03Run\x12\x13\n\x06run_id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1a\n\rexperiment_id\x18\x05 \x01(\tH\x01\x88\x01\x01\x120\n\nfork_point\x18\x02 \x01(\x0b2\x1c.neptune.ingest.v1.ForkPoint\x12\x13\n\x06family\x18\x04 \x01(\tH\x02\x88\x01\x01\x126\n\rcreation_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampH\x03\x88\x01\x01\x12,\n\x05owner\x18\x06 \x01(\x0b2\x18.neptune.ingest.v1.OwnerH\x04\x88\x01\x01\x12\x17\n\nrequest_id\x18\x07 \x01(\tH\x05\x88\x01\x01\x12>\n\x15start_processing_time\x18\x0b \x01(\x0b2\x1a.google.protobuf.TimestampH\x06\x88\x01\x01B\t\n\x07_run_idB\x10\n\x0e_experiment_idB\t\n\x07_familyB\x10\n\x0e_creation_timeB\x08\n\x06_ownerB\r\n\x0b_request_idB\x18\n\x16_start_processing_time"7\n\x07Preview\x12\x12\n\nis_preview\x18\x01 \x01(\x08\x12\x18\n\x10completion_ratio\x18\x02 \x01(\x02"\xdb\x05\n\x11UpdateRunSnapshot\x12%\n\x04step\x18\x01 \x01(\x0b2\x17.neptune.ingest.v1.Step\x12-\n\ttimestamp\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x120\n\x07preview\x18\n \x01(\x0b2\x1a.neptune.ingest.v1.PreviewH\x00\x88\x01\x01\x12@\n\x06assign\x18\x04 \x03(\x0b20.neptune.ingest.v1.UpdateRunSnapshot.AssignEntry\x12I\n\x0bmodify_sets\x18\x05 \x03(\x0b24.neptune.ingest.v1.UpdateRunSnapshot.ModifySetsEntry\x12@\n\x06append\x18\x08 \x03(\x0b20.neptune.ingest.v1.UpdateRunSnapshot.AppendEntry\x12\x17\n\nrequest_id\x18\t \x01(\tH\x01\x88\x01\x01\x12>\n\x15start_processing_time\x18\x0b \x01(\x0b2\x1a.google.protobuf.TimestampH\x02\x88\x01\x01\x1aG\n\x0bAssignEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\'\n\x05value\x18\x02 \x01(\x0b2\x18.neptune.ingest.v1.Value:\x028\x01\x1aO\n\x0fModifySetsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12+\n\x05value\x18\x02 \x01(\x0b2\x1c.neptune.ingest.v1.ModifySet:\x028\x01\x1aG\n\x0bAppendEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\'\n\x05value\x18\x02 \x01(\x0b2\x18.neptune.ingest.v1.Value:\x028\x01B\n\n\x08_previewB\r\n\x0b_request_idB\x18\n\x16_start_processing_time"M\n\x12UpdateRunSnapshots\x127\n\tsnapshots\x18\x01 \x03(\x0b2$.neptune.ingest.v1.UpdateRunSnapshot*.\n\rSET_OPERATION\x12\x08\n\x04NOOP\x10\x00\x12\x07\n\x03ADD\x10\x01\x12\n\n\x06REMOVE\x10\x02B5\n$ml.neptune.leaderboard.api.ingest.v1B\x0bCommonProtoP\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'neptune_pb.ingest.v1.common_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$ml.neptune.leaderboard.api.ingest.v1B\x0bCommonProtoP\x01'
    _globals['_MODIFYSTRINGSET_VALUESENTRY']._options = None
    _globals['_MODIFYSTRINGSET_VALUESENTRY']._serialized_options = b'8\x01'
    _globals['_UPDATERUNSNAPSHOT_ASSIGNENTRY']._options = None
    _globals['_UPDATERUNSNAPSHOT_ASSIGNENTRY']._serialized_options = b'8\x01'
    _globals['_UPDATERUNSNAPSHOT_MODIFYSETSENTRY']._options = None
    _globals['_UPDATERUNSNAPSHOT_MODIFYSETSENTRY']._serialized_options = b'8\x01'
    _globals['_UPDATERUNSNAPSHOT_APPENDENTRY']._options = None
    _globals['_UPDATERUNSNAPSHOT_APPENDENTRY']._serialized_options = b'8\x01'
    _globals['_SET_OPERATION']._serialized_start = 2114
    _globals['_SET_OPERATION']._serialized_end = 2160
    _globals['_STEP']._serialized_start = 89
    _globals['_STEP']._serialized_end = 125
    _globals['_FORKPOINT']._serialized_start = 128
    _globals['_FORKPOINT']._serialized_end = 283
    _globals['_STRINGSET']._serialized_start = 285
    _globals['_STRINGSET']._serialized_end = 312
    _globals['_VALUE']._serialized_start = 315
    _globals['_VALUE']._serialized_end = 502
    _globals['_MODIFYSTRINGSET']._serialized_start = 505
    _globals['_MODIFYSTRINGSET']._serialized_end = 667
    _globals['_MODIFYSTRINGSET_VALUESENTRY']._serialized_start = 588
    _globals['_MODIFYSTRINGSET_VALUESENTRY']._serialized_end = 667
    _globals['_MODIFYSET']._serialized_start = 669
    _globals['_MODIFYSET']._serialized_end = 742
    _globals['_OWNER']._serialized_start = 744
    _globals['_OWNER']._serialized_end = 814
    _globals['_RUN']._serialized_start = 817
    _globals['_RUN']._serialized_end = 1242
    _globals['_PREVIEW']._serialized_start = 1244
    _globals['_PREVIEW']._serialized_end = 1299
    _globals['_UPDATERUNSNAPSHOT']._serialized_start = 1302
    _globals['_UPDATERUNSNAPSHOT']._serialized_end = 2033
    _globals['_UPDATERUNSNAPSHOT_ASSIGNENTRY']._serialized_start = 1755
    _globals['_UPDATERUNSNAPSHOT_ASSIGNENTRY']._serialized_end = 1826
    _globals['_UPDATERUNSNAPSHOT_MODIFYSETSENTRY']._serialized_start = 1828
    _globals['_UPDATERUNSNAPSHOT_MODIFYSETSENTRY']._serialized_end = 1907
    _globals['_UPDATERUNSNAPSHOT_APPENDENTRY']._serialized_start = 1909
    _globals['_UPDATERUNSNAPSHOT_APPENDENTRY']._serialized_end = 1980
    _globals['_UPDATERUNSNAPSHOTS']._serialized_start = 2035
    _globals['_UPDATERUNSNAPSHOTS']._serialized_end = 2112