#!/usr/bin/env bash

set -euxo pipefail

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
SRC_DIR="${SCRIPT_DIR}/../src"

for file in $(find "${SRC_DIR}/neptune_api/proto" -name "*.py"); do
    sed -i "" "s/from google.protobuf import descriptor_pool/from neptune_api.proto import descriptor_pool/" "${file}"
done

for file in $(find "${SRC_DIR}/neptune_retrieval_api/proto" -name "*.py"); do
    sed -i "" "s/from google.protobuf import descriptor_pool/from neptune_retrieval_api.proto import descriptor_pool/" "${file}"
done
