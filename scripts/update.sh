#!/usr/bin/env bash

# Usage: ./scripts/update.sh leaderboardSwagger.json neptune_retrieval_api
# (with python 3.8)

# Show every command and exit on error
set -ex

# Function to convert Swagger 2.0 to OpenAPI 3.0
convert_swagger_to_openapi() {
    local input_file=$1
    local output_file=$2

    curl -X POST "https://converter.swagger.io/api/convert" \
        -H "Content-Type: application/json" \
        -d @"${input_file}" \
        -o "${output_file}"
}

cp "${1}" swagger.json

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
' swagger.json > tmp_swagger.json && mv tmp_swagger.json swagger.json

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
' swagger.json > tmp_swagger.json && mv tmp_swagger.json swagger.json

## Convert the Swagger JSON to OpenAPI 3.0
convert_swagger_to_openapi "swagger.json" "openapi.json"
# Add license information using jq
jq '.info.license = {"name": "", "url": ""}' openapi.json > tmp_openapi.json && mv tmp_openapi.json openapi.json


# Generate the client
openapi-python-client generate \
    --overwrite \
    --meta none \
    --path "openapi.json" \
    --custom-template-path=templates/ \
    --config openapi-generator-config.yaml \
    --output-path "src/${2}"


cat scripts/preserve_files.txt | while read entry; do
    git checkout HEAD -- $entry
done

pre-commit run --all-files
