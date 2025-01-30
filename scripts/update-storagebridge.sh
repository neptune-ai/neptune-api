#!/usr/bin/env bash

if [ ! -f "storagebridge_swagger.json" ]; then
  echo "storagebridge_swagger.json not found. Make sure it's in CWD when running the script"
  exit 1
fi

# Show every command and exit on error
set -ex

## Preserve specific files
mkdir -p tmp


# Function to download Swagger JSON
download_swagger() {
    local swagger_url=$1
    local output_file=$2

    curl -o "${output_file}" "${swagger_url}"
}

# Function to convert Swagger 2.0 to OpenAPI 3.0
convert_swagger_to_openapi() {
    local input_file=$1
    local output_file=$2

    curl -X POST "https://converter.swagger.io/api/convert" \
        -H "Content-Type: application/json" \
        -d @"${input_file}" \
        -o "${output_file}"
}


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

## Convert the Swagger JSON to OpenAPI 3.0
convert_swagger_to_openapi "storagebridge_swagger.json" "storagebridge_openapi.json"
# Add license information using jq
jq '.info.license = {"name": "", "url": ""}' storagebridge_openapi.json > tmp_storagebridge_openapi.json && mv tmp_storagebridge_openapi.json storagebridge_openapi.json


openapi-python-client generate \
    --overwrite \
    --meta none \
    --path "storagebridge_openapi.json" \
    --custom-template-path=templates/ \
    --config openapi-generator-config.yaml \
    --output-path src/neptune_storage_api


# Clean tmp directories
rm -rf tmp


cat scripts/preserve_files.txt | while read entry; do
    git checkout HEAD -- $entry
done
