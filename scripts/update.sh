#!/usr/bin/env bash

# Show every command and exit on error
set -ex

# Preserve package structure
mv src/neptune_api neptune_api

# To generate in the same directory
INITIAL_DIRECTORY=$(pwd)
cd ../

# Generate the client
openapi-python-client update \
    --url $1 \
    --custom-template-path=neptune-api/templates/ \
    --config neptune-api/openapi-generator-config.yaml

# Restore the initial directory
cd $INITIAL_DIRECTORY

# Restore package structure
mv neptune_api src/neptune_api
