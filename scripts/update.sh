#!/usr/bin/env bash

# Show every command and exit on error
set -ex

# Clean tmp directories
rm -rf neptune_api
rm -rf tmp

# Preserve package structure
mv src/neptune_api neptune_api

# Preserve specific files
mkdir -p tmp
cat scripts/preserve_files.txt | while read file; do
    mkdir -p tmp/$(dirname $file) | true
    mv $file tmp/$file
done

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

# Restore specific files
cat scripts/preserve_files.txt | while read file; do
    mkdir -p $(dirname $file) | true
    mv tmp/$file $file
done
rm -rf tmp

# Restore package structure
mv neptune_api src/neptune_api
