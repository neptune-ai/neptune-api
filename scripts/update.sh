#!/usr/bin/env bash

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


# Download the Swagger JSON
download_swagger "$1/api/leaderboard/swagger.json" "leaderboard_swagger.json"
download_swagger "$1/api/backend/swagger.json" "backend_swagger.json"


# Modify the Swagger JSON to support application/x-protobuf
# jq '
#   .paths |= with_entries(
#     .value |= with_entries(
#       if .value.produces? and (.value.produces | index("application/json")) and (.value.produces | index("application/x-protobuf"))
#       then
#         .value.produces = ["application/x-protobuf"]
#       else
#         .
#       end
#     )
#   )
# ' leaderboard_swagger.json > tmp/leaderboard_swagger.json && mv tmp/leaderboard_swagger.json leaderboard_swagger.json

# jq '
#   .paths |= with_entries(
#     .value |= with_entries(
#       if .value.produces? and (.value.produces | index("application/x-protobuf"))
#       then
#         .value.responses."200".schema = {
#           "type": "string",
#           "format": "binary"
#         }
#       else
#         .
#       end
#     )
#   )
# ' leaderboard_swagger.json > tmp/leaderboard_swagger.json && mv tmp/leaderboard_swagger.json leaderboard_swagger.json

## Convert the Swagger JSON to OpenAPI 3.0
convert_swagger_to_openapi "leaderboard_swagger.json" "leaderboard_openapi.json"
convert_swagger_to_openapi "backend_swagger.json" "backend_openapi.json"


redocly join leaderboard_openapi.json backend_openapi.json -o test.json
redocly bundle main --output filtered.json --remove-unused-components

# Add license information using jq
jq '.info.license = {"name": "", "url": ""}' filtered.json > tmp_leaderboard_openapi.json && mv tmp_leaderboard_openapi.json filtered.json


# Generate the client
openapi-python-client generate \
    --overwrite \
    --path "filtered.json" \
    --meta none \
    --custom-template-path=templates/ \
    --config openapi-generator-config.yaml \
    --output-path src/neptune_api



# Clean tmp directories
rm -rf tmp


cat scripts/preserve_files.txt | while read entry; do
    git checkout HEAD -- $entry
done
