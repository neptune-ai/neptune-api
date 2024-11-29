#!/usr/bin/env bash

set -euxo pipefail

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
SRC_DIR="${SCRIPT_DIR}/../src"
NEPTUNE_PROJECT_DIR="${1:-}"

if [ -z "${NEPTUNE_PROJECT_DIR}" ]; then
    echo "Usage: $0 <neptune_project_dir>"
    exit 1
fi

python -m grpc_tools.protoc \
  --python_out="${SRC_DIR}/neptune_api/proto" \
  --mypy_out="${SRC_DIR}/neptune_api/proto" \
  --proto_path="${NEPTUNE_PROJECT_DIR}/libs/models/leaderboard-proto/src/main/proto" \
  "${NEPTUNE_PROJECT_DIR}/libs/models/leaderboard-proto/src/main/proto/neptune_pb/ingest/v1/"*".proto" \
  "${NEPTUNE_PROJECT_DIR}/libs/models/leaderboard-proto/src/main/proto/neptune_pb/ingest/v1/pub/"*".proto"

python -m grpc_tools.protoc \
  --python_out="${SRC_DIR}/neptune_retrieval_api/proto" \
  --mypy_out="${SRC_DIR}/neptune_retrieval_api/proto" \
  --proto_path="${NEPTUNE_PROJECT_DIR}/libs/models/leaderboard-proto/src/main/proto" \
  "${NEPTUNE_PROJECT_DIR}/libs/models/leaderboard-proto/src/main/proto/neptune_pb/api/model/"*".proto"

protol --create-package --in-place \
  --python-out "${SRC_DIR}/neptune_api/proto" \
  protoc \
  --proto-path "${NEPTUNE_PROJECT_DIR}/libs/models/leaderboard-proto/src/main/proto" \
  "${NEPTUNE_PROJECT_DIR}/libs/models/leaderboard-proto/src/main/proto/neptune_pb/ingest/v1/"*".proto" \
  "${NEPTUNE_PROJECT_DIR}/libs/models/leaderboard-proto/src/main/proto/neptune_pb/ingest/v1/pub/"*".proto"

protol --create-package --in-place \
  --python-out "${SRC_DIR}/neptune_retrieval_api/proto" \
  protoc \
  --proto-path "${NEPTUNE_PROJECT_DIR}/libs/models/leaderboard-proto/src/main/proto" \
  "${NEPTUNE_PROJECT_DIR}/libs/models/leaderboard-proto/src/main/proto/neptune_pb/api/model/"*".proto"

for file in $(find "${SRC_DIR}/neptune_api/proto" -name "*.py" -not -name 'descriptor_pool.py'); do
    sed -i "" "s/from google.protobuf import descriptor_pool/from neptune_api.proto import descriptor_pool/" "${file}"
done

for file in $(find "${SRC_DIR}/neptune_retrieval_api/proto" -name "*.py" -not -name 'descriptor_pool.py'); do
    sed -i "" "s/from google.protobuf import descriptor_pool/from neptune_retrieval_api.proto import descriptor_pool/" "${file}"
done
