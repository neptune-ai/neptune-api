#!/usr/bin/env bash

# Use with python 3.8

# Show every command and exit on error
set -ex

openapi-python-client generate \
    --overwrite \
    --url "$1/api/client/v1/api-docs" \
    --meta none \
    --custom-template-path=templates/ \
    --config openapi-generator-config.yaml \
    --output-path src/neptune_api

cat scripts/preserve_files.txt | while read entry; do
    git checkout HEAD -- $entry
done

pre-commit run --all-files
