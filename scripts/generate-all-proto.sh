#!/bin/bash
#
# Run this script to generate python code based on .proto files in the specified directory.
# See README.md for more information.

set -ex

protobuf_source_dir="${1:-}"
if [ -z "${protobuf_source_dir}" ]; then
  echo "Usage: $0 <protobuf_src_dir>"
  exit 1
fi

orig_cwd=$(pwd)
trap 'cd "$orig_cwd"' exit

git_root=$(git rev-parse --show-toplevel)
cd "$git_root/scripts/docker"

docker build -t neptune-api-gen-proto_v3 -f Dockerfile.proto_v3 .
docker run --rm \
  -v "$protobuf_source_dir":"/app/proto_dir" \
  -v "$git_root/src":"/app/output_dir" \
  neptune-api-gen-proto_v3

docker build -t neptune-api-gen-proto_v4plus -f Dockerfile.proto_v4plus .
docker run --rm \
  -v "$protobuf_source_dir":"/app/proto_dir" \
  -v "$git_root/src":"/app/output_dir" \
  neptune-api-gen-proto_v4plus
