#!/bin/bash
#
# Run this script to generate python code based on .proto files in the specified directory.
# See README.md for more information.

set -ex

protobuf_source_dir="${1:-proto}"
orig_cwd=$(pwd)
trap 'cd "$orig_cwd"' exit

# Resolve to absolute path
protobuf_source_dir="$( cd "$protobuf_source_dir" &> /dev/null && pwd )"

script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
src_dir="$script_dir/../src/"

cd "$script_dir/docker"

docker build -t neptune-api-gen-proto_v3 -f Dockerfile.proto_v3 .
docker run --rm \
  -v "$protobuf_source_dir":"/app/proto_dir" \
  -v "$src_dir":"/app/output_dir" \
  neptune-api-gen-proto_v3

docker build -t neptune-api-gen-proto_v4plus -f Dockerfile.proto_v4plus .
docker run --rm \
  -v "$protobuf_source_dir":"/app/proto_dir" \
  -v "$src_dir":"/app/output_dir" \
  neptune-api-gen-proto_v4plus
