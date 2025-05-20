#!/usr/bin/env bash

# Show every command and exit on error
set -ex

tmpdir=tmp
rm -fr "$tmpdir"
mkdir "$tmpdir"


script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
src_dir="$script_dir/../src/"

# Convert Swagger 2.0 to OpenAPI 3.1. We need two steps to do that:
# - convert from swagger 2.0 to OpenAPI 3.0.1 using swagger-converter
# - convert from OpenAPI 3.0.1 to OpenAPI 3.1 using openapi-format
convert_swagger_to_openapi() {
    local file_path=$1
    local tmp_file="$tmpdir/to-openapi.$RANDOM.json"

    curl -X POST "https://converter.swagger.io/api/convert" \
        -H "Content-Type: application/json" \
        -d @"${file_path}" \
        -o "${tmp_file}"

    openapi-format "${tmp_file}" -o "${file_path}" --convertTo "3.1"
}

# This function modifies endpoints within a Swagger 2.0 spec file to:
#
#  * If an endpoint defines more than one response content type and one of them is protobuf,
#    keep only the application/x-protobuf content type & force binary format
#  * If no content type is defined, set the content type to application/json
#
# Because openapi-python-client does not support generating protobuf messages
# as responses, and an endpoint declares an application/json content type along with
# protobuf content type, the generated code will read eg:
#
#     response_200 = ProtoAttributesDTO.from_dict(response.json())
#
# which obviously does not work.
#
# Keeping protobuf content type only, will result in generating code that simply returns
# binary content, which then the library users parse manually as protobuf messages.
#
# On the other hand, some endpoints do not have a content type defined, which makes
# the generated code NOT produce response objects as defined in the schema.
# This is why we always set application/json as the default content type, if it's
# not already specified.
fix_content_types() {
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
 |
  .paths |= with_entries(
    .value |= with_entries(
      if (.value.produces | not)
      then .value.produces = ["application/json"]
      else .
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

# Filter endpoints using redocly to keep only the ones that are
# defined in redocly.yml
filter_endpoints() {
  local file_path=$1
  local api=$2
  local tmp_file="$tmpdir/filter-endpoints-$api.$RANDOM.json"

  redocly bundle "$api" -o "$tmp_file" --remove-unused-components
  cp "$tmp_file" "$file_path"
}

# Set the specified tag on all endpoints in a given file. This step
# is required to ensure proper package structure that openapi-python-client
# generates. The tag is used to construct the submodule path:
#   src/neptune_api/api/<tag>/
# which in turn translates to python package structure:
#   from neptune_api.api.storage import signed_url
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

# Prepare an input file from swagger/ to be used in the final client spec.
# This function will:
# - apply protobuf fix for all the endpints (see above)
# - convert input to OpenAPI 3.1
# - filter endpoints to keep only the ones that are defined in redocly.yml
# - set the <api> tag on all endpoints to the specified one
# - add empty license information to be OpenAPI 3.1 compliant
#
# The final output will be stored in $tmpdir/<api>.json. Note that this output
# path must match what is defined in redocly.yml
pre_process_file() {
  local input_path=$1
  local api=$2
  local convert_to_openapi=${3:-true}

  local file_path="$tmpdir/$api.json"
  cp "$input_path" "$file_path"

  fix_content_types "$file_path"

  if [ "$convert_to_openapi" = true ]; then
    convert_swagger_to_openapi "$file_path"
  fi

  filter_endpoints "$file_path" "$api"
  set_tag_on_all_endpoints "$file_path" "$api"
  add_empty_license "$file_path"
}

# Prepare all the API specs for bundling into the final client spec.
pre_process_file swagger/leaderboard.json "leaderboard"
pre_process_file swagger/backend.json "backend"
pre_process_file swagger/storagebridge_openapi.json "storage" false

# Join all the API specs into a single one
redocly join -o "$tmpdir/neptune.json" \
  "$tmpdir/leaderboard.json" \
  "$tmpdir/backend.json" \
  "$tmpdir/storage.json"

# Add empty license to the final file
add_empty_license "$tmpdir/neptune.json"

# Generate python code from the OpenAPI spec
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

set +ex

# Final processing via pre-commit (license, newlines, etc.)
pre-commit run -a
rm -fr "$tmpdir"
