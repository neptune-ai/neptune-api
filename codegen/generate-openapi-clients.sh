#!/usr/bin/env bash

# Show every command and exit on error
set -ex

tmpdir=$(mktemp -d)
trap 'rm -rf "$tmpdir"' EXIT

script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
src_dir="$script_dir/../src/"

# Convert Swagger 2.0 to OpenAPI 3.0.1
convert_swagger_to_openapi() {
    local input_path=$1
    local tmp_file="$tmpdir/tmp-proto-fix.$RANDOM.json"
    cp "$input_path" "$tmp_file"

    curl -X POST "https://converter.swagger.io/api/convert" \
        -H "Content-Type: application/json" \
        -d @"${tmp_file}" \
        -o "${input_path}"
}

# This function modifies protobuf endpoints within a swagger/OpenAPI spec file to:
#  * remove application/json response type
#  * force binary format
#
# Because openapi-python-client does not support generating protobuf messages
# as responses, if we don't do that, the generated code will read eg:
#
#     response_200 = ProtoAttributesDTO.from_dict(response.json())
#
# which obviously does not work. The returned content will be of type binary,
# and needs to be manually parsed to proto messages by the user.
protobuf_fix() {
  local input_path=$1
  local tmp_file="$tmpdir/tmp-proto-fix.$RANDOM.json"

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
  |
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
' "$input_path" > "$tmp_file" && mv "$tmp_file" "$input_path"
}

# OpenAPI requires a license object, so add an empty one.
add_empty_license() {
  local input_path=$1
  local tmp_file="$tmpdir/tmp-license.$RANDOM.json"

  jq '.info.license = {"name": "", "url": ""}' "$input_path" > "$tmp_file" \
    && cp "$tmp_file" "$input_path"
}

# Process a single swagger/OpenAPI spec file to generate the client.
# Input:
#   $1 - input file path
#   $2 - output directory (eg src/neptune_retrieval_api). This is where the generated
#        code lands.
#   $3 - leave empty if the input path should be converted to OpenAPI format, false
#        if otherwise. Some files are already in OpenAPI format and should not be
#        converted.
process_file() {
  local input_path=$1
  local output_dir=$2
  local convert_to_openapi=${3:-true}
  local working_file

  working_file="$tmpdir/$(basename "$input_path").$RANDOM.json"
  cp "$input_path" "$working_file"

  protobuf_fix "$working_file"

  if [ "$convert_to_openapi" = true ]; then
    convert_swagger_to_openapi "$working_file"
  fi

  add_empty_license "$working_file"
  # Generate the client
  openapi-python-client generate \
      --overwrite \
      --meta none \
      --path "$working_file" \
      --custom-template-path=templates/ \
      --config openapi-generator-config.yaml \
      --output-path "$output_dir"
}

# Process all the known files
process_file swagger/leaderboard.json "$src_dir/neptune_retrieval_api"
process_file swagger/storagebridge_openapi.json "$src_dir/neptune_storage_api" false

# Restore files that could've been overwritten by the generated code
cat preserve_files.txt | while read entry; do
    git checkout HEAD -- "../$entry"
done

pre-commit run -a
