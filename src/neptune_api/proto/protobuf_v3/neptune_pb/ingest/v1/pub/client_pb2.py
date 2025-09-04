"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....neptune_pb.ingest.v1.pub import request_status_pb2 as neptune__pb_dot_ingest_dot_v1_dot_pub_dot_request__status__pb2
from .....neptune_pb.ingest.v1 import ingest_pb2 as neptune__pb_dot_ingest_dot_v1_dot_ingest__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%neptune_pb/ingest/v1/pub/client.proto\x12\x15neptune.ingest.v1.pub\x1a-neptune_pb/ingest/v1/pub/request_status.proto\x1a!neptune_pb/ingest/v1/ingest.proto"\x1a\n\tRequestId\x12\r\n\x05value\x18\x01 \x01(\t">\n\rRequestIdList\x12-\n\x03ids\x18\x01 \x03(\x0b2 .neptune.ingest.v1.pub.RequestId"K\n\x11BulkRequestStatus\x126\n\x08statuses\x18\x01 \x03(\x0b2$.neptune.ingest.v1.pub.RequestStatus"9\n\x0eSubmitResponse\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x13\n\x0brequest_ids\x18\x02 \x03(\t"T\n\x0bStatusCheck\x12\x0f\n\x07project\x18\x01 \x01(\t\x124\n\nrequest_id\x18\x02 \x01(\x0b2 .neptune.ingest.v1.pub.RequestId"Q\n\x0fBulkStatusCheck\x12\x0f\n\x07project\x18\x02 \x01(\t\x12-\n\x03ids\x18\x01 \x03(\x0b2 .neptune.ingest.v1.pub.RequestId"\x99\x01\n\x0fBulkCheckDetail\x12\x0f\n\x07project\x18\x01 \x01(\t\x12-\n\x03ids\x18\x02 \x03(\x0b2 .neptune.ingest.v1.pub.RequestId\x12\x18\n\x0bnext_cursor\x18\x03 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05limit\x18\x04 \x01(\x05H\x01\x88\x01\x01B\x0e\n\x0c_next_cursorB\x08\n\x06_limit"\xa2\x01\n\x12IngestResultDetail\x124\n\nrequest_id\x18\x01 \x01(\x0b2 .neptune.ingest.v1.pub.RequestId\x12\x0c\n\x04path\x18\x02 \x01(\t\x122\n\x0bingest_code\x18\x03 \x01(\x0e2\x1d.neptune.ingest.v1.IngestCode\x12\x14\n\x0cerror_detail\x18\x04 \x01(\t"i\n\x16BulkIngestResultDetail\x12:\n\x07details\x18\x01 \x03(\x0b2).neptune.ingest.v1.pub.IngestResultDetail\x12\x13\n\x0bnext_cursor\x18\x02 \x01(\tB3\n\x1cml.neptune.client.api.modelsB\x11ClientIngestProtoP\x01b\x06proto3')
_REQUESTID = DESCRIPTOR.message_types_by_name['RequestId']
_REQUESTIDLIST = DESCRIPTOR.message_types_by_name['RequestIdList']
_BULKREQUESTSTATUS = DESCRIPTOR.message_types_by_name['BulkRequestStatus']
_SUBMITRESPONSE = DESCRIPTOR.message_types_by_name['SubmitResponse']
_STATUSCHECK = DESCRIPTOR.message_types_by_name['StatusCheck']
_BULKSTATUSCHECK = DESCRIPTOR.message_types_by_name['BulkStatusCheck']
_BULKCHECKDETAIL = DESCRIPTOR.message_types_by_name['BulkCheckDetail']
_INGESTRESULTDETAIL = DESCRIPTOR.message_types_by_name['IngestResultDetail']
_BULKINGESTRESULTDETAIL = DESCRIPTOR.message_types_by_name['BulkIngestResultDetail']
RequestId = _reflection.GeneratedProtocolMessageType('RequestId', (_message.Message,), {'DESCRIPTOR': _REQUESTID, '__module__': 'neptune_pb.ingest.v1.pub.client_pb2'})
_sym_db.RegisterMessage(RequestId)
RequestIdList = _reflection.GeneratedProtocolMessageType('RequestIdList', (_message.Message,), {'DESCRIPTOR': _REQUESTIDLIST, '__module__': 'neptune_pb.ingest.v1.pub.client_pb2'})
_sym_db.RegisterMessage(RequestIdList)
BulkRequestStatus = _reflection.GeneratedProtocolMessageType('BulkRequestStatus', (_message.Message,), {'DESCRIPTOR': _BULKREQUESTSTATUS, '__module__': 'neptune_pb.ingest.v1.pub.client_pb2'})
_sym_db.RegisterMessage(BulkRequestStatus)
SubmitResponse = _reflection.GeneratedProtocolMessageType('SubmitResponse', (_message.Message,), {'DESCRIPTOR': _SUBMITRESPONSE, '__module__': 'neptune_pb.ingest.v1.pub.client_pb2'})
_sym_db.RegisterMessage(SubmitResponse)
StatusCheck = _reflection.GeneratedProtocolMessageType('StatusCheck', (_message.Message,), {'DESCRIPTOR': _STATUSCHECK, '__module__': 'neptune_pb.ingest.v1.pub.client_pb2'})
_sym_db.RegisterMessage(StatusCheck)
BulkStatusCheck = _reflection.GeneratedProtocolMessageType('BulkStatusCheck', (_message.Message,), {'DESCRIPTOR': _BULKSTATUSCHECK, '__module__': 'neptune_pb.ingest.v1.pub.client_pb2'})
_sym_db.RegisterMessage(BulkStatusCheck)
BulkCheckDetail = _reflection.GeneratedProtocolMessageType('BulkCheckDetail', (_message.Message,), {'DESCRIPTOR': _BULKCHECKDETAIL, '__module__': 'neptune_pb.ingest.v1.pub.client_pb2'})
_sym_db.RegisterMessage(BulkCheckDetail)
IngestResultDetail = _reflection.GeneratedProtocolMessageType('IngestResultDetail', (_message.Message,), {'DESCRIPTOR': _INGESTRESULTDETAIL, '__module__': 'neptune_pb.ingest.v1.pub.client_pb2'})
_sym_db.RegisterMessage(IngestResultDetail)
BulkIngestResultDetail = _reflection.GeneratedProtocolMessageType('BulkIngestResultDetail', (_message.Message,), {'DESCRIPTOR': _BULKINGESTRESULTDETAIL, '__module__': 'neptune_pb.ingest.v1.pub.client_pb2'})
_sym_db.RegisterMessage(BulkIngestResultDetail)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x1cml.neptune.client.api.modelsB\x11ClientIngestProtoP\x01'
    _REQUESTID._serialized_start = 146
    _REQUESTID._serialized_end = 172
    _REQUESTIDLIST._serialized_start = 174
    _REQUESTIDLIST._serialized_end = 236
    _BULKREQUESTSTATUS._serialized_start = 238
    _BULKREQUESTSTATUS._serialized_end = 313
    _SUBMITRESPONSE._serialized_start = 315
    _SUBMITRESPONSE._serialized_end = 372
    _STATUSCHECK._serialized_start = 374
    _STATUSCHECK._serialized_end = 458
    _BULKSTATUSCHECK._serialized_start = 460
    _BULKSTATUSCHECK._serialized_end = 541
    _BULKCHECKDETAIL._serialized_start = 544
    _BULKCHECKDETAIL._serialized_end = 697
    _INGESTRESULTDETAIL._serialized_start = 700
    _INGESTRESULTDETAIL._serialized_end = 862
    _BULKINGESTRESULTDETAIL._serialized_start = 864
    _BULKINGESTRESULTDETAIL._serialized_end = 969