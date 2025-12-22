#!/usr/bin/env bash
# Executed in docker container to generate Python proto code
# See Dockerfile.proto*.

set -euxo pipefail

OUTPUT_DIR_BASE="${1:-}"

if [ -z "${OUTPUT_DIR_BASE}" ]; then
    echo "Usage: $0 <output_src_dir>"
    exit 1
fi

mkdir -p "${OUTPUT_DIR_BASE}/neptune_api/proto"

python -m grpc_tools.protoc \
  --python_out="${OUTPUT_DIR_BASE}/neptune_api/proto" \
  --mypy_out="${OUTPUT_DIR_BASE}/neptune_api/proto" \
  --proto_path="./proto/" \
  "./proto/google_rpc/"*".proto" \
  "./proto/neptune_pb/ingest/v1/"*".proto" \
  "./proto/neptune_pb/ingest/v1/pub/"*".proto" \
  "./proto/neptune_pb/api/v1/model/"*".proto"

# Note that we're passing the protoc-path argument to protol, which makes sure
# it's using the same protoc as above, instead of a system-wide installation.
protol --create-package --in-place \
  --python-out "${OUTPUT_DIR_BASE}/neptune_api/proto" \
  protoc \
  --protoc-path="python -m grpc_tools.protoc" \
  --proto-path "./proto" \
  "./proto/google_rpc/"*".proto" \
  "./proto/neptune_pb/ingest/v1/"*".proto" \
  "./proto/neptune_pb/ingest/v1/pub/"*".proto" \
  "./proto/neptune_pb/api/v1/model/"*".proto"
