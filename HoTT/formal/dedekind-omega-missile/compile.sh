#!/bin/sh
# 金形态 cut 编译脚手架
# 用法: compile.sh <Module.agda> [--ignore-interfaces]
AGDA=/Volumes/D/HoTT-toolchain-cache/agda-v2.8.0-macos-arm64/agda
XDG=/Volumes/D/HoTT-toolchain-cache/agda-v2.8.0-macos-arm64
ROOT=/Volumes/D/HoTT_AI_HANDOFF_20260911
MISSILE=$ROOT/HoTT/formal/dedekind-omega-missile
cd "$ROOT" || exit 99
/usr/bin/env XDG_DATA_HOME=$XDG/xdg-data XDG_CONFIG_HOME=$XDG/xdg-config TMPDIR=$XDG/tmp \
  "$AGDA" ${2:-} --library-file="$MISSILE/AGDA_LIBRARIES" -l cubical-0.9 -i "$MISSILE" \
  "HoTT/formal/dedekind-omega-missile/$1"
