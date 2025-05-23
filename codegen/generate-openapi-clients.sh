#!/bin/bash
# Generate OpenAPI client code based on definitions in ./swagger/

set -ex

# Resolve to absolute path
script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
src_dir="$script_dir/../src/"

docker build -t neptune-api-gen-openapi -f Dockerfile.openapi .
docker run --rm -v "$src_dir":"/app/src" neptune-api-gen-openapi

pre-commit run -a
