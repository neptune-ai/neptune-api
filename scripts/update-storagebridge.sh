#!/usr/bin/env bash

if [ ! -f "storagebridge_swagger.json" ]; then
  echo "storagebridge_swagger.json not found. Make sure it's in CWD when running the script"
  exit 1
fi

# Show every command and exit on error
set -ex

## Preserve specific files
mkdir -p tmp

# Modify the Swagger JSON to support application/x-protobuf
jq '
  .paths |= with_entries(
    .value |= with_entries(
      if .value.produces? and (.value.produces | index("application/json")) and (.value.produces | index("application/x-protobuf"))
      then
        .value.produces = ["application/x-protobuf"]
      else
        .
      end
    )
  )
' storagebridge_swagger.json > tmp/storagebridge_swagger.json && mv tmp/storagebridge_swagger.json storagebridge_swagger.json

jq '
  .paths |= with_entries(
    .value |= with_entries(
      if .value.produces? and (.value.produces | index("application/x-protobuf"))
      then
        .value.responses."200".schema = {
          "type": "string",
          "format": "binary"
        }
      else
        .
      end
    )
  )
' storagebridge_swagger.json > tmp/storagebridge_swagger.json && mv tmp/storagebridge_swagger.json storagebridge_swagger.json

# Add license information using jq
jq '.info.license = {"name": "", "url": ""}' storagebridge_swagger.json > tmp_storagebridge_swagger.json && mv tmp_storagebridge_swagger.json storagebridge_swagger.json


openapi-python-client generate \
    --overwrite \
    --meta none \
    --path "storagebridge_swagger.json" \
    --custom-template-path=templates/ \
    --config openapi-generator-config.yaml \
    --output-path src/neptune_storage_api


# Clean tmp directories
rm -rf tmp


cat scripts/preserve_files.txt | while read entry; do
    git checkout HEAD -- $entry
done

pre-commit run insert-license --all-files
