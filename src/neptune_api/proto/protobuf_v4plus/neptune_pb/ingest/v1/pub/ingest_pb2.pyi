"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
from ..... import neptune_pb
import typing
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class RunOperation(google.protobuf.message.Message):
    """RunOperation is a message body for the operation to be performed on the run."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PROJECT_FIELD_NUMBER: builtins.int
    RUN_ID_FIELD_NUMBER: builtins.int
    CREATE_MISSING_PROJECT_FIELD_NUMBER: builtins.int
    CREATE_FIELD_NUMBER: builtins.int
    UPDATE_FIELD_NUMBER: builtins.int
    UPDATE_BATCH_FIELD_NUMBER: builtins.int
    API_KEY_FIELD_NUMBER: builtins.int
    project: builtins.str
    'Qualified name of the context project. This name must include workspace, e.g.: "your-workspace/your-project".'
    run_id: builtins.str
    "Required. Subject run id of the operation. In case of `CreateRun` it's the id of the new run.\n    User must ensure uniqueness of the id within the project.\n    "
    create_missing_project: builtins.bool
    "Optional. Will create project if it doesn't yet exist. This operation is idempotent."
    api_key: builtins.bytes
    'API Key used for authorization of operations.\n    See https://docs.neptune.ai/setup/setting_api_token/ for more information on how to obtain an API Key.\n    '

    @property
    def create(self) -> neptune_pb.ingest.v1.common_pb2.Run:
        """Creates a new run. See `CreateRun` for details."""

    @property
    def update(self) -> neptune_pb.ingest.v1.common_pb2.UpdateRunSnapshot:
        """All included fields will be aligned to the same step. In case the step is not set, it will select the
        successor of the highest last_step value among metrics currently being updated.
        """

    @property
    def update_batch(self) -> neptune_pb.ingest.v1.common_pb2.UpdateRunSnapshots:
        """repeated UpdateRunSnapshot"""

    def __init__(self, *, project: builtins.str=..., run_id: builtins.str=..., create_missing_project: builtins.bool=..., create: neptune_pb.ingest.v1.common_pb2.Run | None=..., update: neptune_pb.ingest.v1.common_pb2.UpdateRunSnapshot | None=..., update_batch: neptune_pb.ingest.v1.common_pb2.UpdateRunSnapshots | None=..., api_key: builtins.bytes=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['create', b'create', 'operation', b'operation', 'update', b'update', 'update_batch', b'update_batch']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['api_key', b'api_key', 'create', b'create', 'create_missing_project', b'create_missing_project', 'operation', b'operation', 'project', b'project', 'run_id', b'run_id', 'update', b'update', 'update_batch', b'update_batch']) -> None:
        ...

    def WhichOneof(self, oneof_group: typing.Literal['operation', b'operation']) -> typing.Literal['create', 'update', 'update_batch'] | None:
        ...
global___RunOperation = RunOperation