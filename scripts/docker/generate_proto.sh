#!/usr/bin/env bash

set -euxo pipefail

PROTOBUF_SRC_DIR="${1:-}"
OUTPUT_DIR_BASE="${2:-}"
OUTPUT_SUBMODULE_DIR="${3:-}"

if [ -z "${PROTOBUF_SRC_DIR}" ] || [ -z "${OUTPUT_DIR_BASE}" ] || [ -z "${OUTPUT_SUBMODULE_DIR}" ]; then
    echo "Usage: $0 <protobuf_src_dir> <output_src_dir> <output_submodule_dir>"
    exit 1
fi

python -m grpc_tools.protoc \
  --python_out="${OUTPUT_DIR_BASE}/neptune_api/proto/$OUTPUT_SUBMODULE_DIR" \
  --mypy_out="${OUTPUT_DIR_BASE}/neptune_api/proto/$OUTPUT_SUBMODULE_DIR" \
  --proto_path="${PROTOBUF_SRC_DIR}" \
  "${PROTOBUF_SRC_DIR}/google_rpc/"*".proto" \
  "${PROTOBUF_SRC_DIR}/neptune_pb/ingest/v1/"*".proto" \
  "${PROTOBUF_SRC_DIR}/neptune_pb/ingest/v1/pub/"*".proto"

python -m grpc_tools.protoc \
  --python_out="${OUTPUT_DIR_BASE}/neptune_retrieval_api/proto/$OUTPUT_SUBMODULE_DIR" \
  --mypy_out="${OUTPUT_DIR_BASE}/neptune_retrieval_api/proto/$OUTPUT_SUBMODULE_DIR" \
  --proto_path="${PROTOBUF_SRC_DIR}" \
  "${PROTOBUF_SRC_DIR}/neptune_pb/api/v1/model/"*".proto"

# Note that we're passing the protoc-path argument to protol, which makes sure
# it's using the same protoc as above, instead of a system-wide installation.
protol --create-package --in-place \
  --python-out "${OUTPUT_DIR_BASE}/neptune_api/proto/$OUTPUT_SUBMODULE_DIR" \
  protoc \
  --protoc-path="python -m grpc_tools.protoc" \
  --proto-path "${PROTOBUF_SRC_DIR}" \
  "${PROTOBUF_SRC_DIR}/google_rpc/"*".proto" \
  "${PROTOBUF_SRC_DIR}/neptune_pb/ingest/v1/"*".proto" \
  "${PROTOBUF_SRC_DIR}/neptune_pb/ingest/v1/pub/"*".proto"

protol --create-package --in-place \
  --python-out "${OUTPUT_DIR_BASE}/neptune_retrieval_api/proto/$OUTPUT_SUBMODULE_DIR" \
  protoc \
  --protoc-path="python -m grpc_tools.protoc" \
  --proto-path "${PROTOBUF_SRC_DIR}" \
  "${PROTOBUF_SRC_DIR}/neptune_pb/api/v1/model/"*".proto"
