"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
from .... import google_rpc
from .... import neptune_pb
import sys
import typing
if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _IngestCode:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _IngestCodeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_IngestCode.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    OK: _IngestCode.ValueType
    'OK is returned on successful operations.'
    BATCH_CONTAINS_DEPENDENT_RUNS: _IngestCode.ValueType
    'Run create requests are not topologically sorted across batches. A single batch must not contain dependent runs.'
    PROJECT_NOT_FOUND: _IngestCode.ValueType
    'Project not found. May happen when the project is not created yet and `create_missing_project` is not set.'
    PROJECT_INVALID_NAME: _IngestCode.ValueType
    'Project name is either empty or too long.'
    RUN_NOT_FOUND: _IngestCode.ValueType
    'Run not found. May happen when the run is not yet created.'
    RUN_DUPLICATE: _IngestCode.ValueType
    'Idempotency Warning: Identical run already exists.'
    RUN_CONFLICTING: _IngestCode.ValueType
    'Run with specified `run_id` already exists, but has different creation parameters (`run_family` or `fork_point`).'
    RUN_FORK_PARENT_NOT_FOUND: _IngestCode.ValueType
    'Warning: Missing fork parent run.'
    RUN_INVALID_CREATION_PARAMETERS: _IngestCode.ValueType
    'Invalid run creation parameters. For example, experiment id is too large, etc'
    FIELD_PATH_EXCEEDS_SIZE_LIMIT: _IngestCode.ValueType
    'Field Path is too long. Maximum length is 1024 bytes (not characters)'
    FIELD_PATH_EMPTY: _IngestCode.ValueType
    'Field Path is empty.'
    FIELD_PATH_INVALID: _IngestCode.ValueType
    'Field Path is invalid for other reasons, like invalid UTF-8 encoding.'
    FIELD_PATH_NON_WRITABLE: _IngestCode.ValueType
    'Field Path is non-writable. Some special sys/ fields are read-only.'
    FIELD_TYPE_UNSUPPORTED: _IngestCode.ValueType
    'Field Type is not supported by the system.'
    FIELD_TYPE_CONFLICTING: _IngestCode.ValueType
    'Field type is different from the one that was previously logged for this series.\n    Once a field type is set, it cannot be changed.\n    '
    SERIES_POINT_DUPLICATE: _IngestCode.ValueType
    'Idempotency Warning: The exact same data point was already logged for this series.'
    SERIES_STEP_TOO_LARGE: _IngestCode.ValueType
    'Step value must be smaller than: `1_000_000_000_000`.'
    SERIES_STEP_INVALID: _IngestCode.ValueType
    'Invalid step value. Step `micro` part must be smaller than `1_000_000`.'
    SERIES_PREVIEW_STEP_NOT_AFTER_LAST_COMMITTED_STEP: _IngestCode.ValueType
    'Series preview step not after last committed step.'
    SERIES_STEP_NON_INCREASING: _IngestCode.ValueType
    "The step of a series value is lesser than the most recently logged step for this series or the step is exactly the\n    same, but the value is different (DUPLICATE_DATA_POINT doesn't apply).\n    "
    SERIES_STEP_NOT_AFTER_FORK_POINT: _IngestCode.ValueType
    'The series value must be greater than the step specified in the run Fork Point.'
    SERIES_TIMESTAMP_DECREASING: _IngestCode.ValueType
    'The timestamp of a series value is lesser than the most recently logged value. Identical timestamps are allowed.'
    FLOAT_VALUE_NAN_INF_UNSUPPORTED: _IngestCode.ValueType
    'Unsupported value type for float64 field or float64 series. Applies to Inf and NaN values.'
    STRING_VALUE_EXCEEDS_SIZE_LIMIT: _IngestCode.ValueType
    'String value is too long. Maximum length is 1MiB.'
    STRING_SET_EXCEEDS_SIZE_LIMIT: _IngestCode.ValueType
    'String Set value is too long. Maximum length is 1MiB.'
    FILE_REF_EXCEEDS_SIZE_LIMIT: _IngestCode.ValueType
    'File Ref value is too long. Maximum length is 4KiB.'
    INGEST_SUSPENDED: _IngestCode.ValueType
    'Ingest is currently suspended'
    INTERNAL: _IngestCode.ValueType
    'Internal failure'

class IngestCode(_IngestCode, metaclass=_IngestCodeEnumTypeWrapper):
    """Error codes for the operations"""
OK: IngestCode.ValueType
'OK is returned on successful operations.'
BATCH_CONTAINS_DEPENDENT_RUNS: IngestCode.ValueType
'Run create requests are not topologically sorted across batches. A single batch must not contain dependent runs.'
PROJECT_NOT_FOUND: IngestCode.ValueType
'Project not found. May happen when the project is not created yet and `create_missing_project` is not set.'
PROJECT_INVALID_NAME: IngestCode.ValueType
'Project name is either empty or too long.'
RUN_NOT_FOUND: IngestCode.ValueType
'Run not found. May happen when the run is not yet created.'
RUN_DUPLICATE: IngestCode.ValueType
'Idempotency Warning: Identical run already exists.'
RUN_CONFLICTING: IngestCode.ValueType
'Run with specified `run_id` already exists, but has different creation parameters (`run_family` or `fork_point`).'
RUN_FORK_PARENT_NOT_FOUND: IngestCode.ValueType
'Warning: Missing fork parent run.'
RUN_INVALID_CREATION_PARAMETERS: IngestCode.ValueType
'Invalid run creation parameters. For example, experiment id is too large, etc'
FIELD_PATH_EXCEEDS_SIZE_LIMIT: IngestCode.ValueType
'Field Path is too long. Maximum length is 1024 bytes (not characters)'
FIELD_PATH_EMPTY: IngestCode.ValueType
'Field Path is empty.'
FIELD_PATH_INVALID: IngestCode.ValueType
'Field Path is invalid for other reasons, like invalid UTF-8 encoding.'
FIELD_PATH_NON_WRITABLE: IngestCode.ValueType
'Field Path is non-writable. Some special sys/ fields are read-only.'
FIELD_TYPE_UNSUPPORTED: IngestCode.ValueType
'Field Type is not supported by the system.'
FIELD_TYPE_CONFLICTING: IngestCode.ValueType
'Field type is different from the one that was previously logged for this series.\nOnce a field type is set, it cannot be changed.\n'
SERIES_POINT_DUPLICATE: IngestCode.ValueType
'Idempotency Warning: The exact same data point was already logged for this series.'
SERIES_STEP_TOO_LARGE: IngestCode.ValueType
'Step value must be smaller than: `1_000_000_000_000`.'
SERIES_STEP_INVALID: IngestCode.ValueType
'Invalid step value. Step `micro` part must be smaller than `1_000_000`.'
SERIES_PREVIEW_STEP_NOT_AFTER_LAST_COMMITTED_STEP: IngestCode.ValueType
'Series preview step not after last committed step.'
SERIES_STEP_NON_INCREASING: IngestCode.ValueType
"The step of a series value is lesser than the most recently logged step for this series or the step is exactly the\nsame, but the value is different (DUPLICATE_DATA_POINT doesn't apply).\n"
SERIES_STEP_NOT_AFTER_FORK_POINT: IngestCode.ValueType
'The series value must be greater than the step specified in the run Fork Point.'
SERIES_TIMESTAMP_DECREASING: IngestCode.ValueType
'The timestamp of a series value is lesser than the most recently logged value. Identical timestamps are allowed.'
FLOAT_VALUE_NAN_INF_UNSUPPORTED: IngestCode.ValueType
'Unsupported value type for float64 field or float64 series. Applies to Inf and NaN values.'
STRING_VALUE_EXCEEDS_SIZE_LIMIT: IngestCode.ValueType
'String value is too long. Maximum length is 1MiB.'
STRING_SET_EXCEEDS_SIZE_LIMIT: IngestCode.ValueType
'String Set value is too long. Maximum length is 1MiB.'
FILE_REF_EXCEEDS_SIZE_LIMIT: IngestCode.ValueType
'File Ref value is too long. Maximum length is 4KiB.'
INGEST_SUSPENDED: IngestCode.ValueType
'Ingest is currently suspended'
INTERNAL: IngestCode.ValueType
'Internal failure'
global___IngestCode = IngestCode

class BatchContext(google.protobuf.message.Message):
    """BatchContext"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PROJECT_FIELD_NUMBER: builtins.int
    API_KEY_FIELD_NUMBER: builtins.int
    project: builtins.str
    'Project qualified name, e.g. "your-workspace/your-project".'
    api_key: builtins.bytes
    'API Key required used to authorize all operations withing batch.'

    def __init__(self, *, project: builtins.str=..., api_key: builtins.bytes=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['api_key', b'api_key', 'project', b'project']) -> None:
        ...
global___BatchContext = BatchContext

class UpdateRun(google.protobuf.message.Message):
    """Mode of update run. We currently support only Update Snapshots."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    UPDATE_SNAPSHOTS_FIELD_NUMBER: builtins.int

    @property
    def update_snapshots(self) -> neptune_pb.ingest.v1.common_pb2.UpdateRunSnapshots:
        """All included fields will be aligned to the same step. In case the step is not set, it will select the
        successor of the run step, which is the highest step across individual metric leaders for this run.
        """

    def __init__(self, *, update_snapshots: neptune_pb.ingest.v1.common_pb2.UpdateRunSnapshots | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['mode', b'mode', 'update_snapshots', b'update_snapshots']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['mode', b'mode', 'update_snapshots', b'update_snapshots']) -> None:
        ...

    def WhichOneof(self, oneof_group: typing_extensions.Literal['mode', b'mode']) -> typing_extensions.Literal['update_snapshots'] | None:
        ...
global___UpdateRun = UpdateRun

class BatchProjectOperations(google.protobuf.message.Message):
    """BatchProjectOperations will execute operations within provided `context`. It will execute `create_runs` first and
    then `update_run_fields`. All operations within each group are unordered and may be executed simultaneously.

    Currently, Ingest API does not perform any topological sort within a single batch. Customer of this API must ensure
    that all required dependencies are met before this Batch is executed.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class UpdateRunsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str

        @property
        def value(self) -> global___UpdateRun:
            ...

        def __init__(self, *, key: builtins.str=..., value: global___UpdateRun | None=...) -> None:
            ...

        def HasField(self, field_name: typing_extensions.Literal['value', b'value']) -> builtins.bool:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['key', b'key', 'value', b'value']) -> None:
            ...
    CONTEXT_FIELD_NUMBER: builtins.int
    CREATE_MISSING_PROJECT_FIELD_NUMBER: builtins.int
    CREATE_RUNS_FIELD_NUMBER: builtins.int
    UPDATE_RUNS_FIELD_NUMBER: builtins.int

    @property
    def context(self) -> global___BatchContext:
        """Required. Context of the operation: workspace, project and api key used for authorization"""
    create_missing_project: builtins.bool
    "Optional. This option will instrument the server to create project if it doesn't yet exist.\n    This operation is idempotent.\n    "

    @property
    def create_runs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[neptune_pb.ingest.v1.common_pb2.Run]:
        """Optional. Creates a new Run or Forks an existing Run from the specified `parent_run` and `step`."""

    @property
    def update_runs(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___UpdateRun]:
        """Optional. Update fields for selected runs. Map key is an id of the run to be updated.
        Allows users to provide shared StepInfo, which is useful for large updates happening for the same step.
        """

    def __init__(self, *, context: global___BatchContext | None=..., create_missing_project: builtins.bool=..., create_runs: collections.abc.Iterable[neptune_pb.ingest.v1.common_pb2.Run] | None=..., update_runs: collections.abc.Mapping[builtins.str, global___UpdateRun] | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['context', b'context']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['context', b'context', 'create_missing_project', b'create_missing_project', 'create_runs', b'create_runs', 'update_runs', b'update_runs']) -> None:
        ...
global___BatchProjectOperations = BatchProjectOperations

class CreateRunError(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    GRPC_CODE_FIELD_NUMBER: builtins.int
    INGEST_CODE_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    grpc_code: google_rpc.code_pb2.Code.ValueType
    'grpc response code of the operation.'
    ingest_code: global___IngestCode.ValueType
    'error code of the operation.'
    message: builtins.str
    'error message related to the operation.'

    def __init__(self, *, grpc_code: google_rpc.code_pb2.Code.ValueType=..., ingest_code: global___IngestCode.ValueType=..., message: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['grpc_code', b'grpc_code', 'ingest_code', b'ingest_code', 'message', b'message']) -> None:
        ...
global___CreateRunError = CreateRunError

class CreateRunResult(google.protobuf.message.Message):
    """Run create results"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RUN_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int

    @property
    def run(self) -> neptune_pb.ingest.v1.common_pb2.Run:
        """Run successfully created by the server."""

    @property
    def error(self) -> global___CreateRunError:
        """error details."""

    def __init__(self, *, run: neptune_pb.ingest.v1.common_pb2.Run | None=..., error: global___CreateRunError | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['error', b'error', 'run', b'run', 'type', b'type']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['error', b'error', 'run', b'run', 'type', b'type']) -> None:
        ...

    def WhichOneof(self, oneof_group: typing_extensions.Literal['type', b'type']) -> typing_extensions.Literal['run', 'error'] | None:
        ...
global___CreateRunResult = CreateRunResult

class ResultSummary(google.protobuf.message.Message):
    """counters for the operations performed in the request, batch or run update"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class FailedByGRPCCodeCounters(google.protobuf.message.Message):
        """Mapping of failed operations counts by error code."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        GRPC_CODE_FIELD_NUMBER: builtins.int
        COUNT_FIELD_NUMBER: builtins.int
        grpc_code: google_rpc.code_pb2.Code.ValueType
        count: builtins.int

        def __init__(self, *, grpc_code: google_rpc.code_pb2.Code.ValueType=..., count: builtins.int=...) -> None:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['count', b'count', 'grpc_code', b'grpc_code']) -> None:
            ...

    class IngestCodeCounters(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        INGEST_CODE_FIELD_NUMBER: builtins.int
        COUNT_FIELD_NUMBER: builtins.int
        ingest_code: global___IngestCode.ValueType
        count: builtins.int

        def __init__(self, *, ingest_code: global___IngestCode.ValueType=..., count: builtins.int=...) -> None:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['count', b'count', 'ingest_code', b'ingest_code']) -> None:
            ...
    TOTAL_OPERATIONS_COUNT_FIELD_NUMBER: builtins.int
    SUCCESSFUL_COUNT_FIELD_NUMBER: builtins.int
    FAILED_COUNT_FIELD_NUMBER: builtins.int
    FAILED_BY_GRPC_CODE_FIELD_NUMBER: builtins.int
    FAILED_BY_INGEST_CODE_FIELD_NUMBER: builtins.int
    total_operations_count: builtins.int
    'failed_count + successful_count = total_operations_count'
    successful_count: builtins.int
    failed_count: builtins.int

    @property
    def failed_by_grpc_code(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ResultSummary.FailedByGRPCCodeCounters]:
        """Failed summary details"""

    @property
    def failed_by_ingest_code(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ResultSummary.IngestCodeCounters]:
        ...

    def __init__(self, *, total_operations_count: builtins.int=..., successful_count: builtins.int=..., failed_count: builtins.int=..., failed_by_grpc_code: collections.abc.Iterable[global___ResultSummary.FailedByGRPCCodeCounters] | None=..., failed_by_ingest_code: collections.abc.Iterable[global___ResultSummary.IngestCodeCounters] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['failed_by_grpc_code', b'failed_by_grpc_code', 'failed_by_ingest_code', b'failed_by_ingest_code', 'failed_count', b'failed_count', 'successful_count', b'successful_count', 'total_operations_count', b'total_operations_count']) -> None:
        ...
global___ResultSummary = ResultSummary

class UpdateRunError(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    GRPC_CODE_FIELD_NUMBER: builtins.int
    INGEST_CODE_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    FIELD_FIELD_NUMBER: builtins.int
    grpc_code: google_rpc.code_pb2.Code.ValueType
    'grpc error code of the operation.'
    ingest_code: global___IngestCode.ValueType
    'error code of the operation.'
    message: builtins.str
    'error message related to the operation.'
    field: builtins.str
    'field path is set only if a failed operation is a Field Operation.'

    def __init__(self, *, grpc_code: google_rpc.code_pb2.Code.ValueType=..., ingest_code: global___IngestCode.ValueType=..., message: builtins.str=..., field: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['field', b'field', 'grpc_code', b'grpc_code', 'ingest_code', b'ingest_code', 'message', b'message']) -> None:
        ...
global___UpdateRunError = UpdateRunError

class UpdateRunResults(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    OPERATIONS_SUMMARY_FIELD_NUMBER: builtins.int
    UPDATE_ERRORS_FIELD_NUMBER: builtins.int

    @property
    def operations_summary(self) -> global___ResultSummary:
        ...

    @property
    def update_errors(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___UpdateRunError]:
        """Detail error. If the whole batch fails due to wider conditions, per-field errors will not be listed.
        Successful field updates are not reported here, they are only counted in the `operations_summary`.
        """

    def __init__(self, *, operations_summary: global___ResultSummary | None=..., update_errors: collections.abc.Iterable[global___UpdateRunError] | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['operations_summary', b'operations_summary']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['operations_summary', b'operations_summary', 'update_errors', b'update_errors']) -> None:
        ...
global___UpdateRunResults = UpdateRunResults

class BatchResult(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class UpdateRunResultsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str

        @property
        def value(self) -> global___UpdateRunResults:
            ...

        def __init__(self, *, key: builtins.str=..., value: global___UpdateRunResults | None=...) -> None:
            ...

        def HasField(self, field_name: typing_extensions.Literal['value', b'value']) -> builtins.bool:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['key', b'key', 'value', b'value']) -> None:
            ...
    GRPC_CODE_FIELD_NUMBER: builtins.int
    INGEST_CODE_FIELD_NUMBER: builtins.int
    OPERATIONS_SUMMARY_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    CREATE_RUN_RESULTS_FIELD_NUMBER: builtins.int
    UPDATE_RUN_RESULTS_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    grpc_code: google_rpc.code_pb2.Code.ValueType
    "Error code that applies to the whole batch. Used codes:\n    - OK: when the batch is partially successful, but there could be some operations that failed.\n      Operation-specific errors will be listed in `operation_errors`.\n    - UNAUTHENTICATED: when `api_key` is not provided.\n    - PERMISSION_DENIED: when provided `api_key` is not authorized to perform the operations on a provided context.\n    - NOT_FOUND: when `workspace` or `project` does not exist or provided`api_key` doesn't have read access to them.\n    - INVALID_ARGUMENT: when the batch is malformed to a degree that no operation can be performed.\n    - INTERNAL: when an unexpected error occurred.\n    - UNAVAILABLE: when the service is unavailable.\n    - DATA_LOSS: when the service experienced a data loss.\n    "
    ingest_code: global___IngestCode.ValueType

    @property
    def operations_summary(self) -> global___ResultSummary:
        """Summary of the operations performed in the batch."""
    project: builtins.str
    'Project associated with the batch.'

    @property
    def create_run_results(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CreateRunResult]:
        """Reports created runs in the batch. In case the user didn't set their `run_id` in the request, it will be provided
        by the server. Order of the results is preserved.
        """

    @property
    def update_run_results(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___UpdateRunResults]:
        """Run update results."""
    message: builtins.str
    'Error message related to the batch failure.'

    def __init__(self, *, grpc_code: google_rpc.code_pb2.Code.ValueType=..., ingest_code: global___IngestCode.ValueType=..., operations_summary: global___ResultSummary | None=..., project: builtins.str=..., create_run_results: collections.abc.Iterable[global___CreateRunResult] | None=..., update_run_results: collections.abc.Mapping[builtins.str, global___UpdateRunResults] | None=..., message: builtins.str=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['operations_summary', b'operations_summary']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['create_run_results', b'create_run_results', 'grpc_code', b'grpc_code', 'ingest_code', b'ingest_code', 'message', b'message', 'operations_summary', b'operations_summary', 'project', b'project', 'update_run_results', b'update_run_results']) -> None:
        ...
global___BatchResult = BatchResult

class IngestRequest(google.protobuf.message.Message):
    """Ingest Request is a request body for the Ingest method. It contains a list of batches of operations to be performed.
    Each Batch of operations is executed within the provided context.

    We recommend counting the number of atomic changes (points, `assign` operations) in all batches in a single
    request and keeping them between 10 thousand and 20 thousands to avoid performance issues.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BATCHES_FIELD_NUMBER: builtins.int

    @property
    def batches(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___BatchProjectOperations]:
        """Batches of operations to be performed. Each batch is executed within the provided context.

        Multiple batches may be executed together to improve Ingest performance if their operations are found to be
        independent. Batches that don't share the same Context are always considered independent and may be merged.
        """

    def __init__(self, *, batches: collections.abc.Iterable[global___BatchProjectOperations] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['batches', b'batches']) -> None:
        ...
global___IngestRequest = IngestRequest

class IngestResponse(google.protobuf.message.Message):
    """Ingest Response returns a list of errors for each batch of operations"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SUMMARY_FIELD_NUMBER: builtins.int
    ERROR_MESSAGE_FIELD_NUMBER: builtins.int
    BATCH_RESULTS_FIELD_NUMBER: builtins.int

    @property
    def summary(self) -> global___ResultSummary:
        """summary of the results of the operations performed in the request."""
    error_message: builtins.str
    'Error message related to the whole request. Corresponding error code is set in the response header'

    @property
    def batch_results(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___BatchResult]:
        """Batch results. Each batch result corresponds to a single batch in the request.
        The order of the results is preserved.
        """

    def __init__(self, *, summary: global___ResultSummary | None=..., error_message: builtins.str=..., batch_results: collections.abc.Iterable[global___BatchResult] | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['summary', b'summary']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['batch_results', b'batch_results', 'error_message', b'error_message', 'summary', b'summary']) -> None:
        ...
global___IngestResponse = IngestResponse