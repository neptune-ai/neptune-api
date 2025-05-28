#!/bin/bash
# Generate OpenAPI client code based on definitions in ./swagger/

set -ex

orig_dir="$(pwd)"
trap 'cd "$orig_dir"' EXIT

# Resolve to absolute path
script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd "$script_dir"
src_dir="$script_dir/../src/"

docker build -t neptune-api-gen-openapi -f Dockerfile.openapi .
docker run --rm \
  -v "$src_dir":"/app/src" \
  -v "$script_dir/swagger":"/app/swagger" \
  -v "$script_dir/templates":"/app/templates" \
  neptune-api-gen-openapi

pre-commit run -a
