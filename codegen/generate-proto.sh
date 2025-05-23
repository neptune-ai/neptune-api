#!/bin/bash
#
# Generate python code based on definitions in ./proto/

set -ex

# Resolve to absolute path
script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
src_dir="$script_dir/../src/"

docker build -t neptune-api-gen-proto_v3 -f Dockerfile.proto_v3 .
docker run --rm \
  -v "$src_dir":"/app/output_dir" \
  neptune-api-gen-proto_v3

docker build -t neptune-api-gen-proto_v4plus -f Dockerfile.proto_v4plus .
docker run --rm \
  -v "$src_dir":"/app/output_dir" \
  neptune-api-gen-proto_v4plus
