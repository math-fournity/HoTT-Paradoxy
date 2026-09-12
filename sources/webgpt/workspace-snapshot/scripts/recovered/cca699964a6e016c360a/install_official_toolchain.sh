#!/usr/bin/env bash
set -euo pipefail
PREFIX="${PREFIX:-$PWD/.toolchain}"
mkdir -p "$PREFIX/bin" "$PREFIX/src" "$PREFIX/cache"

# Discover the official Linux x86-64 Agda 2.8.0 asset rather than guessing its name.
python3 - "$PREFIX/cache/agda-release.json" <<'PY_DOWNLOAD_META'
import sys, urllib.request
u='https://api.github.com/repos/agda/agda/releases/tags/v2.8.0'
with urllib.request.urlopen(u) as r: data=r.read()
open(sys.argv[1],'wb').write(data)
PY_DOWNLOAD_META
ASSET_URL="$(python3 - "$PREFIX/cache/agda-release.json" <<'PY_SELECT_ASSET'
import json,sys,re
j=json.load(open(sys.argv[1]))
xs=[a['browser_download_url'] for a in j['assets'] if re.search(r'linux',a['name'],re.I) and re.search(r'(x86|amd64)',a['name'],re.I)]
if len(xs)!=1:
    raise SystemExit(f'expected one Linux x86-64 asset, found {xs}')
print(xs[0])
PY_SELECT_ASSET
)"
python3 - "$ASSET_URL" "$PREFIX/cache/agda-2.8.0-asset" <<'PY_DOWNLOAD_ASSET'
import sys,urllib.request
urllib.request.urlretrieve(sys.argv[1],sys.argv[2])
PY_DOWNLOAD_ASSET
file "$PREFIX/cache/agda-2.8.0-asset"
case "$(file -b "$PREFIX/cache/agda-2.8.0-asset")" in
  *gzip*) tar -xzf "$PREFIX/cache/agda-2.8.0-asset" -C "$PREFIX/cache" ;;
  *Zip*) unzip -q "$PREFIX/cache/agda-2.8.0-asset" -d "$PREFIX/cache/agda-unpacked" ;;
  *executable*) cp "$PREFIX/cache/agda-2.8.0-asset" "$PREFIX/bin/agda" ;;
  *) echo 'Unknown Agda asset format' >&2; exit 2 ;;
esac
if [[ ! -x "$PREFIX/bin/agda" ]]; then
  AGDA_BIN="$(find "$PREFIX/cache" -type f -name agda -perm -u+x | head -1)"
  test -n "$AGDA_BIN"
  cp "$AGDA_BIN" "$PREFIX/bin/agda"
fi
chmod +x "$PREFIX/bin/agda"

if [[ ! -d "$PREFIX/src/agda-unimath/.git" ]]; then
  git clone https://github.com/UniMath/agda-unimath.git "$PREFIX/src/agda-unimath"
fi
git -C "$PREFIX/src/agda-unimath" fetch --all --tags
git -C "$PREFIX/src/agda-unimath" checkout --detach 88cfce0ce195ae3b64a9e73e8ec744ae64b4006b

"$PREFIX/bin/agda" --version
git -C "$PREFIX/src/agda-unimath" rev-parse HEAD
