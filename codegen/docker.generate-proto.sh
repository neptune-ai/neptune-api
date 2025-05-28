#!/usr/bin/env bash
# Executed in docker container to generate Python proto code
# See Dockerfile.proto*.

set -euxo pipefail

OUTPUT_DIR_BASE="${1:-}"
OUTPUT_SUBMODULE_DIR="${2:-}"

if [ -z "${OUTPUT_DIR_BASE}" ] || [ -z "${OUTPUT_SUBMODULE_DIR}" ]; then
    echo "Usage: $0 <output_src_dir> <output_submodule_dir>"
    exit 1
fi

mkdir -p "${OUTPUT_DIR_BASE}/neptune_api/proto/$OUTPUT_SUBMODULE_DIR"

python -m grpc_tools.protoc \
  --python_out="${OUTPUT_DIR_BASE}/neptune_api/proto/$OUTPUT_SUBMODULE_DIR" \
  --mypy_out="${OUTPUT_DIR_BASE}/neptune_api/proto/$OUTPUT_SUBMODULE_DIR" \
  --proto_path="./proto/" \
  "./proto/google_rpc/"*".proto" \
  "./proto/neptune_pb/ingest/v1/"*".proto" \
  "./proto/neptune_pb/ingest/v1/pub/"*".proto" \
  "./proto/neptune_pb/api/v1/model/"*".proto"

# Note that we're passing the protoc-path argument to protol, which makes sure
# it's using the same protoc as above, instead of a system-wide installation.
protol --create-package --in-place \
  --python-out "${OUTPUT_DIR_BASE}/neptune_api/proto/$OUTPUT_SUBMODULE_DIR" \
  protoc \
  --protoc-path="python -m grpc_tools.protoc" \
  --proto-path "./proto" \
  "./proto/google_rpc/"*".proto" \
  "./proto/neptune_pb/ingest/v1/"*".proto" \
  "./proto/neptune_pb/ingest/v1/pub/"*".proto" \
  "./proto/neptune_pb/api/v1/model/"*".proto"
