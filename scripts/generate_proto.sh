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
  "${NEPTUNE_PROJECT_DIR}/libs/models/leaderboard-proto/src/main/proto/google_rpc/"*".proto" \
  "${NEPTUNE_PROJECT_DIR}/libs/models/leaderboard-proto/src/main/proto/neptune_pb/ingest/v1/"*".proto" \
  "${NEPTUNE_PROJECT_DIR}/libs/models/leaderboard-proto/src/main/proto/neptune_pb/ingest/v1/pub/"*".proto"

python -m grpc_tools.protoc \
  --python_out="${SRC_DIR}/neptune_retrieval_api/proto" \
  --mypy_out="${SRC_DIR}/neptune_retrieval_api/proto" \
  --proto_path="${NEPTUNE_PROJECT_DIR}/libs/models/leaderboard-proto/src/main/proto" \
  "${NEPTUNE_PROJECT_DIR}/libs/models/leaderboard-proto/src/main/proto/neptune_pb/api/v1/model/"*".proto"

protol --create-package --in-place \
  --python-out "${SRC_DIR}/neptune_api/proto" \
  protoc \
  --proto-path "${NEPTUNE_PROJECT_DIR}/libs/models/leaderboard-proto/src/main/proto" \
  "${NEPTUNE_PROJECT_DIR}/libs/models/leaderboard-proto/src/main/proto/google_rpc/"*".proto" \
  "${NEPTUNE_PROJECT_DIR}/libs/models/leaderboard-proto/src/main/proto/neptune_pb/ingest/v1/"*".proto" \
  "${NEPTUNE_PROJECT_DIR}/libs/models/leaderboard-proto/src/main/proto/neptune_pb/ingest/v1/pub/"*".proto"

protol --create-package --in-place \
  --python-out "${SRC_DIR}/neptune_retrieval_api/proto" \
  protoc \
  --proto-path "${NEPTUNE_PROJECT_DIR}/libs/models/leaderboard-proto/src/main/proto" \
  "${NEPTUNE_PROJECT_DIR}/libs/models/leaderboard-proto/src/main/proto/neptune_pb/api/v1/model/"*".proto"
