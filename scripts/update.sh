#!/usr/bin/env bash

set -ex

mv src/neptune_api neptune_api

cd ../

openapi-python-client update \
    --url $1 \
    --custom-template-path=neptune-api/templates/ \
    --config neptune-api/openapi-generator-config.yaml

cd neptune-api

mv neptune_api src/neptune_api
