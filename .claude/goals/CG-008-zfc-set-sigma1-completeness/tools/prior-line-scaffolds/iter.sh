#!/bin/zsh
# Fast iteration: compile one module against the persistent build dir.
PKG=/Volumes/D/HoTT_AI_HANDOFF_20260911/HoTT/formal/claude-cg001/godel-q-zfc-z0-full
LEAN=/Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0/bin/lean
BUILD=/tmp/z0work/build
export LEAN_PATH="$BUILD:/Volumes/D/HoTT-toolchain-cache/foundation-build-1fb01b72-v4.34.0/lib/lean:/Volumes/D/HoTT-toolchain-cache/astra-real-geometry-v4.34.0/mathlib4-5ed2965256430c3649e86755f9576b54eca72435/.lake/packages/batteries/.lake/build/lib/lean:/Volumes/D/HoTT-toolchain-cache/astra-real-geometry-v4.34.0/mathlib4-5ed2965256430c3649e86755f9576b54eca72435/.lake/packages/aesop/.lake/build/lib/lean:/Volumes/D/HoTT-toolchain-cache/astra-real-geometry-v4.34.0/mathlib4-5ed2965256430c3649e86755f9576b54eca72435/.lake/packages/Qq/.lake/build/lib/lean:/Volumes/D/HoTT-toolchain-cache/astra-real-geometry-v4.34.0/mathlib4-5ed2965256430c3649e86755f9576b54eca72435/.lake/packages/proofwidgets/.lake/build/lib/lean:/Volumes/D/HoTT-toolchain-cache/astra-real-geometry-v4.34.0/mathlib4-5ed2965256430c3649e86755f9576b54eca72435/.lake/packages/importGraph/.lake/build/lib/lean:/Volumes/D/HoTT-toolchain-cache/astra-real-geometry-v4.34.0/mathlib4-5ed2965256430c3649e86755f9576b54eca72435/.lake/packages/LeanSearchClient/.lake/build/lib/lean:/Volumes/D/HoTT-toolchain-cache/astra-real-geometry-v4.34.0/mathlib4-5ed2965256430c3649e86755f9576b54eca72435/.lake/packages/plausible/.lake/build/lib/lean:/Volumes/D/HoTT-toolchain-cache/astra-real-geometry-v4.34.0/mathlib4-5ed2965256430c3649e86755f9576b54eca72435/.lake/packages/Cli/.lake/build/lib/lean"
cd "$PKG"
out="$BUILD/${1%.lean}"
mkdir -p "$(dirname "$out")"
"$LEAN" -DautoImplicit=false -R . -o "$out.olean" -i "$out.ilean" "$1"
