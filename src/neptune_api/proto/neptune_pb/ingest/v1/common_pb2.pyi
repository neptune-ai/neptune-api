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
import google.protobuf.timestamp_pb2
import sys
import typing
if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _SET_OPERATION:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _SET_OPERATIONEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_SET_OPERATION.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    NOOP: _SET_OPERATION.ValueType
    ADD: _SET_OPERATION.ValueType
    REMOVE: _SET_OPERATION.ValueType

class SET_OPERATION(_SET_OPERATION, metaclass=_SET_OPERATIONEnumTypeWrapper):
    """SET_OPERATION is used to describe the operation to be performed on a set."""
NOOP: SET_OPERATION.ValueType
ADD: SET_OPERATION.ValueType
REMOVE: SET_OPERATION.ValueType
global___SET_OPERATION = SET_OPERATION

@typing.final
class Step(google.protobuf.message.Message):
    """Step is used to measure computational progress of the Run and it's used to stamp its state.
    For example, to express Step `3.5`, use `Step{whole: 3, micro: 500_000`}.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    WHOLE_FIELD_NUMBER: builtins.int
    MICRO_FIELD_NUMBER: builtins.int
    whole: builtins.int
    'Whole step index.'
    micro: builtins.int
    'Fractional part of a step expressed as number of micro steps.\n    Expression `0 <= micro < 1_000_000` must be true at all times.\n    '

    def __init__(self, *, whole: builtins.int=..., micro: builtins.int=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['micro', b'micro', 'whole', b'whole']) -> None:
        ...
global___Step = Step

@typing.final
class ForkPoint(google.protobuf.message.Message):
    """ForkPoint is used to mark the parent and its last inherited state during Forking."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PARENT_PROJECT_FIELD_NUMBER: builtins.int
    PARENT_RUN_ID_FIELD_NUMBER: builtins.int
    STEP_FIELD_NUMBER: builtins.int
    REQUESTED_PARENT_ID_FIELD_NUMBER: builtins.int
    parent_project: builtins.str
    'Optional. Parent project qualified name. If not set, it will default to the context project.'
    parent_run_id: builtins.str
    'Required. The id of the parent run within the parent project.'
    requested_parent_id: builtins.str
    'Internal. requested parent_id of the run.'

    @property
    def step(self) -> global___Step:
        """Fork Step, which is the last step that a new run will inherit from its parent.
        If not set, it will default to the last seen step of the parent run by the server at the time of forking.
        New run may start numbering steps from the next micro step after the fork step.
        """

    def __init__(self, *, parent_project: builtins.str=..., parent_run_id: builtins.str=..., step: global___Step | None=..., requested_parent_id: builtins.str | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['_requested_parent_id', b'_requested_parent_id', 'requested_parent_id', b'requested_parent_id', 'step', b'step']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['_requested_parent_id', b'_requested_parent_id', 'parent_project', b'parent_project', 'parent_run_id', b'parent_run_id', 'requested_parent_id', b'requested_parent_id', 'step', b'step']) -> None:
        ...

    def WhichOneof(self, oneof_group: typing.Literal['_requested_parent_id', b'_requested_parent_id']) -> typing.Literal['requested_parent_id'] | None:
        ...
global___ForkPoint = ForkPoint

@typing.final
class StringSet(google.protobuf.message.Message):
    """StringSet represents a set of strings. The order of strings is irrelevant and duplicates are ignored."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VALUES_FIELD_NUMBER: builtins.int

    @property
    def values(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        ...

    def __init__(self, *, values: collections.abc.Iterable[builtins.str] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['values', b'values']) -> None:
        ...
global___StringSet = StringSet

@typing.final
class Value(google.protobuf.message.Message):
    """Value is a union of all supported types that can be used to update a field.
    Different types of operations support different subset of this field, so please refer to the documentation.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FLOAT64_FIELD_NUMBER: builtins.int
    INT64_FIELD_NUMBER: builtins.int
    BOOL_FIELD_NUMBER: builtins.int
    STRING_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    STRING_SET_FIELD_NUMBER: builtins.int
    float64: builtins.float
    int64: builtins.int
    bool: builtins.bool
    string: builtins.str

    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp:
        ...

    @property
    def string_set(self) -> global___StringSet:
        ...

    def __init__(self, *, float64: builtins.float=..., int64: builtins.int=..., bool: builtins.bool=..., string: builtins.str=..., timestamp: google.protobuf.timestamp_pb2.Timestamp | None=..., string_set: global___StringSet | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['bool', b'bool', 'float64', b'float64', 'int64', b'int64', 'string', b'string', 'string_set', b'string_set', 'timestamp', b'timestamp', 'value', b'value']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['bool', b'bool', 'float64', b'float64', 'int64', b'int64', 'string', b'string', 'string_set', b'string_set', 'timestamp', b'timestamp', 'value', b'value']) -> None:
        ...

    def WhichOneof(self, oneof_group: typing.Literal['value', b'value']) -> typing.Literal['float64', 'int64', 'bool', 'string', 'timestamp', 'string_set'] | None:
        ...
global___Value = Value

@typing.final
class ModifyStringSet(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class ValuesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: global___SET_OPERATION.ValueType

        def __init__(self, *, key: builtins.str=..., value: global___SET_OPERATION.ValueType=...) -> None:
            ...

        def ClearField(self, field_name: typing.Literal['key', b'key', 'value', b'value']) -> None:
            ...
    VALUES_FIELD_NUMBER: builtins.int

    @property
    def values(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, global___SET_OPERATION.ValueType]:
        ...

    def __init__(self, *, values: collections.abc.Mapping[builtins.str, global___SET_OPERATION.ValueType] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['values', b'values']) -> None:
        ...
global___ModifyStringSet = ModifyStringSet

@typing.final
class ModifySet(google.protobuf.message.Message):
    """Allows to update tag values in an incremental way."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    STRING_FIELD_NUMBER: builtins.int

    @property
    def string(self) -> global___ModifyStringSet:
        ...

    def __init__(self, *, string: global___ModifyStringSet | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['string', b'string', 'type', b'type']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['string', b'string', 'type', b'type']) -> None:
        ...

    def WhichOneof(self, oneof_group: typing.Literal['type', b'type']) -> typing.Literal['string'] | None:
        ...
global___ModifySet = ModifySet

@typing.final
class Owner(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    USER_ID_FIELD_NUMBER: builtins.int
    SERVICE_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    user_id: builtins.str
    'Id of a person\'s account. It will appear in the "sys/owner" field.'
    service_account_id: builtins.str
    'Id of a service account used for automation.\n    When set to "myaccount", in the "sys/owner" it will appear as "myaccount@myorganization".\n    '

    def __init__(self, *, user_id: builtins.str=..., service_account_id: builtins.str=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['owner_type', b'owner_type', 'service_account_id', b'service_account_id', 'user_id', b'user_id']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['owner_type', b'owner_type', 'service_account_id', b'service_account_id', 'user_id', b'user_id']) -> None:
        ...

    def WhichOneof(self, oneof_group: typing.Literal['owner_type', b'owner_type']) -> typing.Literal['user_id', 'service_account_id'] | None:
        ...
global___Owner = Owner

@typing.final
class Run(google.protobuf.message.Message):
    """CreateRun can be used to create a new run. This can be done in two ways:
    1. Create a new run with no inherited state. You may specify a new run family that will be
       inherited by future runs forking from this one, otherwise the new family will be selected by the server.
    2. Create a new run that inherits state from the parent run up to a specific step. You may specify
       a new run family that will be inherited by future runs forking from this one. By default, the new run
       will be in the same Family as the parent run.
    CreateRun is idempotent, as long as `fork_point` and `family` parameters are the same. In case pf conflict,
    the second operation will fail.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RUN_ID_FIELD_NUMBER: builtins.int
    EXPERIMENT_ID_FIELD_NUMBER: builtins.int
    FORK_POINT_FIELD_NUMBER: builtins.int
    FAMILY_FIELD_NUMBER: builtins.int
    CREATION_TIME_FIELD_NUMBER: builtins.int
    OWNER_FIELD_NUMBER: builtins.int
    REQUEST_ID_FIELD_NUMBER: builtins.int
    run_id: builtins.str
    'Id of the run to be created. Optional if parent context has already specified run_id. If both are set, they\n    must be equal, otherwise the operation will fail.\n    '
    experiment_id: builtins.str
    'Experiment Id to assign to this Run. If Experiment Id is already assigned to another Run, specifying it in this\n    field will move it from the previous Run, so that at most one Run in given project has a given Experiment Id.\n    Note: Experiment Id is currently exposed as "sys/name" field in the Run metadata.\n    '
    family: builtins.str
    'Specifies Family for the new run. Run Family is used to group forking runs that share common ancestry.\n    By default, the new forking run will be in the same family as the parent run.\n    '
    request_id: builtins.str
    'Optional. The request ID generated by the Neptune client, used for tracking outcome of run creation.'

    @property
    def fork_point(self) -> global___ForkPoint:
        """Optional. ForkPoint is used to identify the exact point in the parent history from which the new run continues.
        If not specified, the new run will start with no inherited state.
        """

    @property
    def creation_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """User-specified creation time for the new run. This is especially useful for getting consistent relative timestamps
        for series.
        If not specified, server will use its current time instead when processing the request.
        """

    @property
    def owner(self) -> global___Owner:
        """User that is the owner of the run/experiment being created.
        If not specified, it will be set to a user named "unspecified".
        """

    def __init__(self, *, run_id: builtins.str | None=..., experiment_id: builtins.str | None=..., fork_point: global___ForkPoint | None=..., family: builtins.str | None=..., creation_time: google.protobuf.timestamp_pb2.Timestamp | None=..., owner: global___Owner | None=..., request_id: builtins.str | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['_creation_time', b'_creation_time', '_experiment_id', b'_experiment_id', '_family', b'_family', '_owner', b'_owner', '_request_id', b'_request_id', '_run_id', b'_run_id', 'creation_time', b'creation_time', 'experiment_id', b'experiment_id', 'family', b'family', 'fork_point', b'fork_point', 'owner', b'owner', 'request_id', b'request_id', 'run_id', b'run_id']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['_creation_time', b'_creation_time', '_experiment_id', b'_experiment_id', '_family', b'_family', '_owner', b'_owner', '_request_id', b'_request_id', '_run_id', b'_run_id', 'creation_time', b'creation_time', 'experiment_id', b'experiment_id', 'family', b'family', 'fork_point', b'fork_point', 'owner', b'owner', 'request_id', b'request_id', 'run_id', b'run_id']) -> None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_creation_time', b'_creation_time']) -> typing.Literal['creation_time'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_experiment_id', b'_experiment_id']) -> typing.Literal['experiment_id'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_family', b'_family']) -> typing.Literal['family'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_owner', b'_owner']) -> typing.Literal['owner'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_request_id', b'_request_id']) -> typing.Literal['request_id'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_run_id', b'_run_id']) -> typing.Literal['run_id'] | None:
        ...
global___Run = Run

@typing.final
class UpdateRunSnapshot(google.protobuf.message.Message):
    """Stores Snapshot information about updated fields for a single step. Only passed fields will be updated."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class AssignEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str

        @property
        def value(self) -> global___Value:
            ...

        def __init__(self, *, key: builtins.str=..., value: global___Value | None=...) -> None:
            ...

        def HasField(self, field_name: typing.Literal['value', b'value']) -> builtins.bool:
            ...

        def ClearField(self, field_name: typing.Literal['key', b'key', 'value', b'value']) -> None:
            ...

    @typing.final
    class ModifySetsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str

        @property
        def value(self) -> global___ModifySet:
            ...

        def __init__(self, *, key: builtins.str=..., value: global___ModifySet | None=...) -> None:
            ...

        def HasField(self, field_name: typing.Literal['value', b'value']) -> builtins.bool:
            ...

        def ClearField(self, field_name: typing.Literal['key', b'key', 'value', b'value']) -> None:
            ...

    @typing.final
    class AppendEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str

        @property
        def value(self) -> global___Value:
            ...

        def __init__(self, *, key: builtins.str=..., value: global___Value | None=...) -> None:
            ...

        def HasField(self, field_name: typing.Literal['value', b'value']) -> builtins.bool:
            ...

        def ClearField(self, field_name: typing.Literal['key', b'key', 'value', b'value']) -> None:
            ...
    STEP_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    ASSIGN_FIELD_NUMBER: builtins.int
    MODIFY_SETS_FIELD_NUMBER: builtins.int
    APPEND_FIELD_NUMBER: builtins.int
    REQUEST_ID_FIELD_NUMBER: builtins.int
    request_id: builtins.str
    'Optional. The request ID generated by the Neptune client, used for tracking outcome of run update.'

    @property
    def step(self) -> global___Step:
        """Optional. Step value within the run. If not set, it will default to next full step of the run
        (highest step across step values).
        """

    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Timestamp field common to all included operations"""

    @property
    def assign(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___Value]:
        """Assigns values for fields. Fields `field_path` is used as a key. Example:
        ```
        {assign: {
          "parameters/learning_rate":  {float64: 0.01},
          "parameters/optimizer":      {string: "sgd"}}}
        ```
        Note: when using a StringSet value, this action will override the whole Set with the new values.
              If you want to add or remove tags individually, use `modify_set.string` instead.
        """

    @property
    def modify_sets(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___ModifySet]:
        """Modify string sets with incremental changes. For example:
        ```
        {modify_sets: {
             "sys/tags": {
               "string": {
                 values: {
                   "new_tag1":  ADD,
                   "prev_tag1": REMOVE,
                   "new_tag2":  ADD}}}}
        ```
        """

    @property
    def append(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___Value]:
        """Appends values for Series fields. Fields `field_path` is used as a key. Example:
        ```
        {assign: {
          "metrics/recall":    {float64: 0.6},
          "metrics/precision": {float64: 0.72}}}
        ```
        Note: when using a StringSet value, this action will override the whole Set with the new values.
              If you want to add or remove tags individually, use `modify_set.string` instead.
        """

    def __init__(self, *, step: global___Step | None=..., timestamp: google.protobuf.timestamp_pb2.Timestamp | None=..., assign: collections.abc.Mapping[builtins.str, global___Value] | None=..., modify_sets: collections.abc.Mapping[builtins.str, global___ModifySet] | None=..., append: collections.abc.Mapping[builtins.str, global___Value] | None=..., request_id: builtins.str | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['_request_id', b'_request_id', 'request_id', b'request_id', 'step', b'step', 'timestamp', b'timestamp']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['_request_id', b'_request_id', 'append', b'append', 'assign', b'assign', 'modify_sets', b'modify_sets', 'request_id', b'request_id', 'step', b'step', 'timestamp', b'timestamp']) -> None:
        ...

    def WhichOneof(self, oneof_group: typing.Literal['_request_id', b'_request_id']) -> typing.Literal['request_id'] | None:
        ...
global___UpdateRunSnapshot = UpdateRunSnapshot

@typing.final
class UpdateRunSnapshots(google.protobuf.message.Message):
    """UpdateSnapshots updates fields for a given step. Used to update current state of the run in a single step.
    It's especially useful when user updates a large number of disparate fields in a single or few steps.
    All fields that were seen in a single snapshot will be aligned to the same step. In case the step is not set,
    it will select the successor of the highest step across applicable individual metric leaders for this run.
    Example:
    ```
    [{step: {whole: 1},
     timestamp: "2020-01-01T00:00:00Z",
     assign: {
       "parameters/learning_rate":  {float64: 0.001},
       "parameters/param1":         {float64: 0.1}},
     append: {
       "metrics/precision":         {float64: 0.72}}},
    {step: {whole: 2},
     timestamp: "2020-01-01T00:00:00Z",
     append: {
       "metrics/recall":     {float64: 0.6},
       "metrics/precision":  {float64: 0.74}}}]

    ```
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SNAPSHOTS_FIELD_NUMBER: builtins.int

    @property
    def snapshots(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___UpdateRunSnapshot]:
        ...

    def __init__(self, *, snapshots: collections.abc.Iterable[global___UpdateRunSnapshot] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['snapshots', b'snapshots']) -> None:
        ...
global___UpdateRunSnapshots = UpdateRunSnapshots