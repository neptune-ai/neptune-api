#!/usr/bin/env bash

set -euxo pipefail

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
SRC_DIR="${SCRIPT_DIR}/../src"
PROTOBUF_SRC_DIR="${1:-}"

if [ -z "${PROTOBUF_SRC_DIR}" ]; then
    echo "Usage: $0 <protobuf_src_dir>"
    exit 1
fi

python -m grpc_tools.protoc \
  --python_out="${SRC_DIR}/neptune_api/proto" \
  --mypy_out="${SRC_DIR}/neptune_api/proto" \
  --proto_path="${PROTOBUF_SRC_DIR}" \
  "${PROTOBUF_SRC_DIR}/google_rpc/"*".proto" \
  "${PROTOBUF_SRC_DIR}/neptune_pb/ingest/v1/"*".proto" \
  "${PROTOBUF_SRC_DIR}/neptune_pb/ingest/v1/pub/"*".proto"

python -m grpc_tools.protoc \
  --python_out="${SRC_DIR}/neptune_retrieval_api/proto" \
  --mypy_out="${SRC_DIR}/neptune_retrieval_api/proto" \
  --proto_path="${PROTOBUF_SRC_DIR}" \
  "${PROTOBUF_SRC_DIR}/neptune_pb/api/v1/model/"*".proto"

protol --create-package --in-place \
  --python-out "${SRC_DIR}/neptune_api/proto" \
  protoc \
  --proto-path "${PROTOBUF_SRC_DIR}" \
  "${PROTOBUF_SRC_DIR}/google_rpc/"*".proto" \
  "${PROTOBUF_SRC_DIR}/neptune_pb/ingest/v1/"*".proto" \
  "${PROTOBUF_SRC_DIR}/neptune_pb/ingest/v1/pub/"*".proto"

protol --create-package --in-place \
  --python-out "${SRC_DIR}/neptune_retrieval_api/proto" \
  protoc \
  --proto-path "${PROTOBUF_SRC_DIR}" \
  "${PROTOBUF_SRC_DIR}/neptune_pb/api/v1/model/"*".proto"
