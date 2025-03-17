"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
from ..... import google_rpc
from ..... import neptune_pb
import sys
if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class RequestStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class CodeByCount(google.protobuf.message.Message):
        """in case all operations are successful {"OK": 1}, otherwise errors are reported"""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        CODE_FIELD_NUMBER: builtins.int
        COUNT_FIELD_NUMBER: builtins.int
        DETAIL_FIELD_NUMBER: builtins.int
        code: google_rpc.code_pb2.Code.ValueType
        count: builtins.int
        detail: neptune_pb.ingest.v1.ingest_pb2.IngestCode.ValueType

        def __init__(self, *, code: google_rpc.code_pb2.Code.ValueType=..., count: builtins.int=..., detail: neptune_pb.ingest.v1.ingest_pb2.IngestCode.ValueType=...) -> None:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['code', b'code', 'count', b'count', 'detail', b'detail']) -> None:
            ...
    CODE_BY_COUNT_FIELD_NUMBER: builtins.int

    @property
    def code_by_count(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___RequestStatus.CodeByCount]:
        ...

    def __init__(self, *, code_by_count: collections.abc.Iterable[global___RequestStatus.CodeByCount] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['code_by_count', b'code_by_count']) -> None:
        ...
global___RequestStatus = RequestStatus