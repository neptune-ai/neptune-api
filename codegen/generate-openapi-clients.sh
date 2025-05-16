#!/usr/bin/env bash

# Show every command and exit on error
set -ex

tmpdir=tmp
rm -fr "$tmpdir"
mkdir "$tmpdir"

script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
src_dir="$script_dir/../src/"

# Convert Swagger 2.0 to OpenAPI 3.1
convert_swagger_to_openapi() {
    local file_path=$1
    local tmp_file="$tmpdir/to-openapi.$RANDOM.json"

    curl -X POST "https://converter.swagger.io/api/convert" \
        -H "Content-Type: application/json" \
        -d @"${file_path}" \
        -o "${tmp_file}"

    openapi-format "${tmp_file}" -o "${file_path}" --convertTo "3.1"
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
  local file_path=$1
  local tmp_file="$tmpdir/protobuf-fix.$RANDOM.json"

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
' "$file_path" > "$tmp_file" && cp "$tmp_file" "$file_path"
}

# OpenAPI requires a license object, so add an empty one.
add_empty_license() {
  local file_path=$1
  local tmp_file="$tmpdir/add-license.$RANDOM.json"

  jq '.info.license = {"name": "", "url": ""}' "$file_path" > "$tmp_file" \
    && cp "$tmp_file" "$file_path"
}

filter_endpoints() {
  local file_path=$1
  local api=$2
  local tmp_file="$tmpdir/filter-endpoints-$api.$RANDOM.json"

  redocly bundle "$api" -o "$tmp_file" --remove-unused-components
  cp "$tmp_file" "$file_path"
}

set_tag_on_all_endpoints() {
  local file_path=$1
  local tag=$2
  local tmp_file="$tmpdir/set-tag.$RANDOM.json"

  jq --arg tag "$tag" '
  .paths |= with_entries(
    .value |= with_entries(
      if .key | test("^(get|post|put|delete|patch|options|head)$")
      then .value.tags = [$tag] | .
      else .
      end
    )
  )
  ' "$file_path" > "$tmp_file" && cp "$tmp_file" "$file_path"
}

pre_process_file() {
  local input_path=$1
  local api=$2
  local convert_to_openapi=${3:-true}

  local file_path="$tmpdir/$api.json"
  cp "$input_path" "$file_path"

  if [ "$convert_to_openapi" = true ]; then
    convert_swagger_to_openapi "$file_path"
  fi

  protobuf_fix "$file_path"
  filter_endpoints "$file_path" "$api"
  set_tag_on_all_endpoints "$file_path" "$api"
  add_empty_license "$file_path"
}

# Prepare all the API specs for bundling into the final client spec.
pre_process_file swagger/leaderboard.json "leaderboard"
pre_process_file swagger/backend.json "backend"
pre_process_file swagger/storagebridge_openapi.json "storage" false

redocly join -o "$tmpdir/neptune.json" \
  "$tmpdir/leaderboard.json" \
  "$tmpdir/backend.json" \
  "$tmpdir/storage.json"

add_empty_license "$tmpdir/neptune.json"
openapi-python-client generate \
    --overwrite \
    --meta none \
    --path "$tmpdir/neptune.json" \
    --custom-template-path=templates/ \
    --config openapi-generator-config.yaml \
    --output-path "$src_dir/neptune_api"

# Restore files that could've been overwritten by the generated code
cat preserve_files.txt | while read entry; do
    git checkout HEAD -- "../$entry"
done
pre-commit run -a
