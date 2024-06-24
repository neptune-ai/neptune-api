#!/usr/bin/env bash

# Show every command and exit on error
set -ex

# Preserve package structure
mv src/neptune_api neptune_api

# Preserve specific files
mkdir -p tmp
cat scripts/preserve_files.txt | while read file; do
    mkdir --parents $(dirname $file)
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
    mkdir --parents $(dirname $file)
    mv tmp/$file $file
done
rm -rf tmp

# Restore package structure
mv neptune_api src/neptune_api
