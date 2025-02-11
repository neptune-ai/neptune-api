
'\n@generated by mypy-protobuf.  Do not edit manually!\nisort:skip_file\nCopyright 2022 Google LLC\n\nLicensed under the Apache License, Version 2.0 (the "License");\nyou may not use this file except in compliance with the License.\nYou may obtain a copy of the License at\n\n    http://www.apache.org/licenses/LICENSE-2.0\n\nUnless required by applicable law or agreed to in writing, software\ndistributed under the License is distributed on an "AS IS" BASIS,\nWITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\nSee the License for the specific language governing permissions and\nlimitations under the License.\n'
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import sys
import typing
if (sys.version_info >= (3, 10)):
    import typing as typing_extensions
else:
    import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _Code():
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _CodeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Code.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    OK: _Code.ValueType
    'Not an error; returned on success.\n\n    HTTP Mapping: 200 OK\n    '
    CANCELLED: _Code.ValueType
    'The operation was cancelled, typically by the caller.\n\n    HTTP Mapping: 499 Client Closed Request\n    '
    UNKNOWN: _Code.ValueType
    'Unknown error.  For example, this error may be returned when\n    a `Status` value received from another address space belongs to\n    an error space that is not known in this address space.  Also\n    errors raised by APIs that do not return enough error information\n    may be converted to this error.\n\n    HTTP Mapping: 500 Internal Server Error\n    '
    INVALID_ARGUMENT: _Code.ValueType
    'The client specified an invalid argument.  Note that this differs\n    from `FAILED_PRECONDITION`.  `INVALID_ARGUMENT` indicates arguments\n    that are problematic regardless of the state of the system\n    (e.g., a malformed file name).\n\n    HTTP Mapping: 400 Bad Request\n    '
    DEADLINE_EXCEEDED: _Code.ValueType
    'The deadline expired before the operation could complete. For operations\n    that change the state of the system, this error may be returned\n    even if the operation has completed successfully.  For example, a\n    successful response from a server could have been delayed long\n    enough for the deadline to expire.\n\n    HTTP Mapping: 504 Gateway Timeout\n    '
    NOT_FOUND: _Code.ValueType
    'Some requested entity (e.g., file or directory) was not found.\n\n    Note to server developers: if a request is denied for an entire class\n    of users, such as gradual feature rollout or undocumented allowlist,\n    `NOT_FOUND` may be used. If a request is denied for some users within\n    a class of users, such as user-based access control, `PERMISSION_DENIED`\n    must be used.\n\n    HTTP Mapping: 404 Not Found\n    '
    ALREADY_EXISTS: _Code.ValueType
    'The entity that a client attempted to create (e.g., file or directory)\n    already exists.\n\n    HTTP Mapping: 409 Conflict\n    '
    PERMISSION_DENIED: _Code.ValueType
    'The caller does not have permission to execute the specified\n    operation. `PERMISSION_DENIED` must not be used for rejections\n    caused by exhausting some resource (use `RESOURCE_EXHAUSTED`\n    instead for those errors). `PERMISSION_DENIED` must not be\n    used if the caller can not be identified (use `UNAUTHENTICATED`\n    instead for those errors). This error code does not imply the\n    request is valid or the requested entity exists or satisfies\n    other pre-conditions.\n\n    HTTP Mapping: 403 Forbidden\n    '
    UNAUTHENTICATED: _Code.ValueType
    'The request does not have valid authentication credentials for the\n    operation.\n\n    HTTP Mapping: 401 Unauthorized\n    '
    RESOURCE_EXHAUSTED: _Code.ValueType
    'Some resource has been exhausted, perhaps a per-user quota, or\n    perhaps the entire file system is out of space.\n\n    HTTP Mapping: 429 Too Many Requests\n    '
    FAILED_PRECONDITION: _Code.ValueType
    'The operation was rejected because the system is not in a state\n    required for the operation\'s execution.  For example, the directory\n    to be deleted is non-empty, an rmdir operation is applied to\n    a non-directory, etc.\n\n    Service implementors can use the following guidelines to decide\n    between `FAILED_PRECONDITION`, `ABORTED`, and `UNAVAILABLE`:\n     (a) Use `UNAVAILABLE` if the client can retry just the failing call.\n     (b) Use `ABORTED` if the client should retry at a higher level. For\n         example, when a client-specified test-and-set fails, indicating the\n         client should restart a read-modify-write sequence.\n     (c) Use `FAILED_PRECONDITION` if the client should not retry until\n         the system state has been explicitly fixed. For example, if an "rmdir"\n         fails because the directory is non-empty, `FAILED_PRECONDITION`\n         should be returned since the client should not retry unless\n         the files are deleted from the directory.\n\n    HTTP Mapping: 400 Bad Request\n    '
    ABORTED: _Code.ValueType
    'The operation was aborted, typically due to a concurrency issue such as\n    a sequencer check failure or transaction abort.\n\n    See the guidelines above for deciding between `FAILED_PRECONDITION`,\n    `ABORTED`, and `UNAVAILABLE`.\n\n    HTTP Mapping: 409 Conflict\n    '
    OUT_OF_RANGE: _Code.ValueType
    'The operation was attempted past the valid range.  E.g., seeking or\n    reading past end-of-file.\n\n    Unlike `INVALID_ARGUMENT`, this error indicates a problem that may\n    be fixed if the system state changes. For example, a 32-bit file\n    system will generate `INVALID_ARGUMENT` if asked to read at an\n    offset that is not in the range [0,2^32-1], but it will generate\n    `OUT_OF_RANGE` if asked to read from an offset past the current\n    file size.\n\n    There is a fair bit of overlap between `FAILED_PRECONDITION` and\n    `OUT_OF_RANGE`.  We recommend using `OUT_OF_RANGE` (the more specific\n    error) when it applies so that callers who are iterating through\n    a space can easily look for an `OUT_OF_RANGE` error to detect when\n    they are done.\n\n    HTTP Mapping: 400 Bad Request\n    '
    UNIMPLEMENTED: _Code.ValueType
    'The operation is not implemented or is not supported/enabled in this\n    service.\n\n    HTTP Mapping: 501 Not Implemented\n    '
    INTERNAL: _Code.ValueType
    'Internal errors.  This means that some invariants expected by the\n    underlying system have been broken.  This error code is reserved\n    for serious errors.\n\n    HTTP Mapping: 500 Internal Server Error\n    '
    UNAVAILABLE: _Code.ValueType
    'The service is currently unavailable.  This is most likely a\n    transient condition, which can be corrected by retrying with\n    a backoff. Note that it is not always safe to retry\n    non-idempotent operations.\n\n    See the guidelines above for deciding between `FAILED_PRECONDITION`,\n    `ABORTED`, and `UNAVAILABLE`.\n\n    HTTP Mapping: 503 Service Unavailable\n    '
    DATA_LOSS: _Code.ValueType
    'Unrecoverable data loss or corruption.\n\n    HTTP Mapping: 500 Internal Server Error\n    '

class Code(_Code, metaclass=_CodeEnumTypeWrapper):
    'The canonical error codes for gRPC APIs.\n\n\n    Sometimes multiple error codes may apply.  Services should return\n    the most specific error code that applies.  For example, prefer\n    `OUT_OF_RANGE` over `FAILED_PRECONDITION` if both codes apply.\n    Similarly prefer `NOT_FOUND` or `ALREADY_EXISTS` over `FAILED_PRECONDITION`.\n    '
OK: Code.ValueType
'Not an error; returned on success.\n\nHTTP Mapping: 200 OK\n'
CANCELLED: Code.ValueType
'The operation was cancelled, typically by the caller.\n\nHTTP Mapping: 499 Client Closed Request\n'
UNKNOWN: Code.ValueType
'Unknown error.  For example, this error may be returned when\na `Status` value received from another address space belongs to\nan error space that is not known in this address space.  Also\nerrors raised by APIs that do not return enough error information\nmay be converted to this error.\n\nHTTP Mapping: 500 Internal Server Error\n'
INVALID_ARGUMENT: Code.ValueType
'The client specified an invalid argument.  Note that this differs\nfrom `FAILED_PRECONDITION`.  `INVALID_ARGUMENT` indicates arguments\nthat are problematic regardless of the state of the system\n(e.g., a malformed file name).\n\nHTTP Mapping: 400 Bad Request\n'
DEADLINE_EXCEEDED: Code.ValueType
'The deadline expired before the operation could complete. For operations\nthat change the state of the system, this error may be returned\neven if the operation has completed successfully.  For example, a\nsuccessful response from a server could have been delayed long\nenough for the deadline to expire.\n\nHTTP Mapping: 504 Gateway Timeout\n'
NOT_FOUND: Code.ValueType
'Some requested entity (e.g., file or directory) was not found.\n\nNote to server developers: if a request is denied for an entire class\nof users, such as gradual feature rollout or undocumented allowlist,\n`NOT_FOUND` may be used. If a request is denied for some users within\na class of users, such as user-based access control, `PERMISSION_DENIED`\nmust be used.\n\nHTTP Mapping: 404 Not Found\n'
ALREADY_EXISTS: Code.ValueType
'The entity that a client attempted to create (e.g., file or directory)\nalready exists.\n\nHTTP Mapping: 409 Conflict\n'
PERMISSION_DENIED: Code.ValueType
'The caller does not have permission to execute the specified\noperation. `PERMISSION_DENIED` must not be used for rejections\ncaused by exhausting some resource (use `RESOURCE_EXHAUSTED`\ninstead for those errors). `PERMISSION_DENIED` must not be\nused if the caller can not be identified (use `UNAUTHENTICATED`\ninstead for those errors). This error code does not imply the\nrequest is valid or the requested entity exists or satisfies\nother pre-conditions.\n\nHTTP Mapping: 403 Forbidden\n'
UNAUTHENTICATED: Code.ValueType
'The request does not have valid authentication credentials for the\noperation.\n\nHTTP Mapping: 401 Unauthorized\n'
RESOURCE_EXHAUSTED: Code.ValueType
'Some resource has been exhausted, perhaps a per-user quota, or\nperhaps the entire file system is out of space.\n\nHTTP Mapping: 429 Too Many Requests\n'
FAILED_PRECONDITION: Code.ValueType
'The operation was rejected because the system is not in a state\nrequired for the operation\'s execution.  For example, the directory\nto be deleted is non-empty, an rmdir operation is applied to\na non-directory, etc.\n\nService implementors can use the following guidelines to decide\nbetween `FAILED_PRECONDITION`, `ABORTED`, and `UNAVAILABLE`:\n (a) Use `UNAVAILABLE` if the client can retry just the failing call.\n (b) Use `ABORTED` if the client should retry at a higher level. For\n     example, when a client-specified test-and-set fails, indicating the\n     client should restart a read-modify-write sequence.\n (c) Use `FAILED_PRECONDITION` if the client should not retry until\n     the system state has been explicitly fixed. For example, if an "rmdir"\n     fails because the directory is non-empty, `FAILED_PRECONDITION`\n     should be returned since the client should not retry unless\n     the files are deleted from the directory.\n\nHTTP Mapping: 400 Bad Request\n'
ABORTED: Code.ValueType
'The operation was aborted, typically due to a concurrency issue such as\na sequencer check failure or transaction abort.\n\nSee the guidelines above for deciding between `FAILED_PRECONDITION`,\n`ABORTED`, and `UNAVAILABLE`.\n\nHTTP Mapping: 409 Conflict\n'
OUT_OF_RANGE: Code.ValueType
'The operation was attempted past the valid range.  E.g., seeking or\nreading past end-of-file.\n\nUnlike `INVALID_ARGUMENT`, this error indicates a problem that may\nbe fixed if the system state changes. For example, a 32-bit file\nsystem will generate `INVALID_ARGUMENT` if asked to read at an\noffset that is not in the range [0,2^32-1], but it will generate\n`OUT_OF_RANGE` if asked to read from an offset past the current\nfile size.\n\nThere is a fair bit of overlap between `FAILED_PRECONDITION` and\n`OUT_OF_RANGE`.  We recommend using `OUT_OF_RANGE` (the more specific\nerror) when it applies so that callers who are iterating through\na space can easily look for an `OUT_OF_RANGE` error to detect when\nthey are done.\n\nHTTP Mapping: 400 Bad Request\n'
UNIMPLEMENTED: Code.ValueType
'The operation is not implemented or is not supported/enabled in this\nservice.\n\nHTTP Mapping: 501 Not Implemented\n'
INTERNAL: Code.ValueType
'Internal errors.  This means that some invariants expected by the\nunderlying system have been broken.  This error code is reserved\nfor serious errors.\n\nHTTP Mapping: 500 Internal Server Error\n'
UNAVAILABLE: Code.ValueType
'The service is currently unavailable.  This is most likely a\ntransient condition, which can be corrected by retrying with\na backoff. Note that it is not always safe to retry\nnon-idempotent operations.\n\nSee the guidelines above for deciding between `FAILED_PRECONDITION`,\n`ABORTED`, and `UNAVAILABLE`.\n\nHTTP Mapping: 503 Service Unavailable\n'
DATA_LOSS: Code.ValueType
'Unrecoverable data loss or corruption.\n\nHTTP Mapping: 500 Internal Server Error\n'
global___Code = Code
