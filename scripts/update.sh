#!/usr/bin/env bash

# Show every command and exit on error
set -ex

# Clean tmp directories
rm -rf neptune_api tmp || true

# Preserve package structure
mv src/neptune_api neptune_api

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
cp -R tmp/* neptune_api/

# Clean tmp directories
rm -rf tmp

# Restore package structure
mv neptune_api src/neptune_api
