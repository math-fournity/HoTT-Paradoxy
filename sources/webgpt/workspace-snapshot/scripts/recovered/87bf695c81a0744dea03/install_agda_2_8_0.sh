#!/usr/bin/env bash
set -euo pipefail
# Reproducible installer helper. It is not invoked automatically by run_all.
URL='https://github.com/agda/agda/releases/download/v2.8.0/Agda-v2.8.0-linux.tar.xz'
EXPECTED='824081b8dcbe431289a50ac6bd83e451f390c51c3884ac7a8c4a5c0df2632faf'
DEST="${1:-$PWD/.toolchain/agda-2.8.0}"
mkdir -p "$DEST"
ARCHIVE="$DEST/Agda-v2.8.0-linux.tar.xz"
printf 'Downloading %s\n' "$URL"
curl --fail --location --retry 3 --output "$ARCHIVE" "$URL"
echo "$EXPECTED  $ARCHIVE" | sha256sum --check -
tar -xJf "$ARCHIVE" -C "$DEST"
find "$DEST" -type f -name agda -perm -u+x -print
