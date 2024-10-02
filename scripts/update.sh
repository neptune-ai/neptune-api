#!/usr/bin/env bash

# Show every command and exit on error
set -ex

## Preserve specific files
mkdir -p tmp
cat scripts/preserve_files.txt | while read entry; do
    if [ -d "$entry" ]; then
        # If entry is a directory, copy it recursively
        mkdir -p tmp/$entry
        cp -r $entry/* tmp/$entry/
    elif [ -f "$entry" ]; then
        # If entry is a file, move it
        mkdir -p tmp/$(dirname $entry)
        mv $entry tmp/$entry
    fi
done

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
#
## Convert the Swagger JSON to OpenAPI 3.0
convert_swagger_to_openapi "leaderboard_swagger.json" "leaderboard_openapi.json"
# Add license information using jq
jq '.info.license = {"name": "", "url": ""}' leaderboard_openapi.json > tmp_leaderboard_openapi.json && mv tmp_leaderboard_openapi.json leaderboard_openapi.json


# Generate the client
openapi-python-client generate \
    --overwrite \
    --url "$1/api/client/v1/api-docs" \
    --meta none \
    --custom-template-path=templates/ \
    --config openapi-generator-config.yaml \
    --output-path src/neptune_api

openapi-python-client generate \
    --overwrite \
    --meta none \
    --path "leaderboard_openapi.json" \
    --custom-template-path=templates/ \
    --config openapi-generator-config.yaml \
    --output-path src/neptune_fetch_api


# Restore specific files
cp -R tmp/* .

# Clean tmp directories
rm -rf tmp
