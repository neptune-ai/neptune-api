# Introduction

Always run the scripts from within the `codegen` directory.

# OpenAPI client libraries

Make sure the updated definitions are present in the `codegen/swagger` directory
and are in line with the paths in `generate-openapi-clients.sh`.

From within the `codegen` directory, run:

```commandline
./generate-openapi-clients.sh
```

This will output the code in `src/` at the root of the repository.

# Protobuf code

## Generating code from .proto files

```commandline
./generate-proto.sh
```

This command builds and runs a Docker container that generates protobuf code
using toolchains compatible with protobuf==5.29.4 (effectively protobuf 4+).

We run the generation tools in a Docker container, to ensure specific versions: grpcio-tools
and Python in particular.
