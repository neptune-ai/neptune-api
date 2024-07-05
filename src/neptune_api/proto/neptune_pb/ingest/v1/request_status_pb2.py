"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....google_rpc import code_pb2 as google__rpc_dot_code__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)neptune_pb/ingest/v1/request_status.proto\x12\x15neptune.ingest.v1.pub\x1a\x15google_rpc/code.proto"\x96\x01\n\rRequestStatus\x12G\n\rcode_by_count\x18\x01 \x03(\x0b20.neptune.ingest.v1.pub.RequestStatus.CodeByCount\x1a<\n\x0bCodeByCount\x12\x1e\n\x04code\x18\x01 \x01(\x0e2\x10.google_rpc.Code\x12\r\n\x05count\x18\x02 \x01(\x03BQ\n3ml.neptune.leaderboard.api.ingest.v1.request.statusB\x18IngestRequestStatusProtoP\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'neptune_pb.ingest.v1.request_status_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n3ml.neptune.leaderboard.api.ingest.v1.request.statusB\x18IngestRequestStatusProtoP\x01'
    _globals['_REQUESTSTATUS']._serialized_start = 92
    _globals['_REQUESTSTATUS']._serialized_end = 242
    _globals['_REQUESTSTATUS_CODEBYCOUNT']._serialized_start = 182
    _globals['_REQUESTSTATUS_CODEBYCOUNT']._serialized_end = 242