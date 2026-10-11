#!/bin/zsh
# One-time compilation of the 24 dependency modules into the persistent build dir.
set -e
PKG=/Volumes/D/HoTT_AI_HANDOFF_20260911/HoTT/formal/claude-cg001/godel-q-zfc-z0-full
LEAN=/Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0/bin/lean
BUILD=/tmp/z0work/build
export LEAN_PATH="$BUILD:/Volumes/D/HoTT-toolchain-cache/foundation-build-1fb01b72-v4.34.0/lib/lean:/Volumes/D/HoTT-toolchain-cache/astra-real-geometry-v4.34.0/mathlib4-5ed2965256430c3649e86755f9576b54eca72435/.lake/packages/batteries/.lake/build/lib/lean:/Volumes/D/HoTT-toolchain-cache/astra-real-geometry-v4.34.0/mathlib4-5ed2965256430c3649e86755f9576b54eca72435/.lake/packages/aesop/.lake/build/lib/lean:/Volumes/D/HoTT-toolchain-cache/astra-real-geometry-v4.34.0/mathlib4-5ed2965256430c3649e86755f9576b54eca72435/.lake/packages/Qq/.lake/build/lib/lean:/Volumes/D/HoTT-toolchain-cache/astra-real-geometry-v4.34.0/mathlib4-5ed2965256430c3649e86755f9576b54eca72435/.lake/packages/proofwidgets/.lake/build/lib/lean:/Volumes/D/HoTT-toolchain-cache/astra-real-geometry-v4.34.0/mathlib4-5ed2965256430c3649e86755f9576b54eca72435/.lake/packages/importGraph/.lake/build/lib/lean:/Volumes/D/HoTT-toolchain-cache/astra-real-geometry-v4.34.0/mathlib4-5ed2965256430c3649e86755f9576b54eca72435/.lake/packages/LeanSearchClient/.lake/build/lib/lean:/Volumes/D/HoTT-toolchain-cache/astra-real-geometry-v4.34.0/mathlib4-5ed2965256430c3649e86755f9576b54eca72435/.lake/packages/plausible/.lake/build/lib/lean:/Volumes/D/HoTT-toolchain-cache/astra-real-geometry-v4.34.0/mathlib4-5ed2965256430c3649e86755f9576b54eca72435/.lake/packages/Cli/.lake/build/lib/lean"
cd "$PKG"
for f in GodelQ/ProcessObservation.lean GodelQ/EffectiveTheory.lean GodelQ/GodelZenoRunner.lean GodelQ/FoundationArith.lean GodelQ/ZFC/SetLanguage.lean GodelQ/ZFC/SchemaDelta1.lean GodelQ/ZFC/ReplacementDelta1.lean GodelQ/ZFC/ZFCDelta1.lean GodelQ/ZFC/NumeralCode.lean GodelQ/ZFC/NeverRE.lean GodelQ/ZFC/OmegaArith.lean GodelQ/ZFC/NumeralSemantics.lean GodelQ/ZFC/ArithInterp.lean GodelQ/ZFC/R0Model.lean GodelQ/ZFC/Effective.lean GodelQ/ZFC/Soundness.lean GodelQ/ZFC/OmegaLaws.lean GodelQ/ZFC/PAModel.lean GodelQ/ZFC/Z0Shadow.lean GodelQ/ZFC/Z0PA.lean GodelQ/ZFC/ShRE.lean GodelQ/ZFC/InternalTranslate.lean GodelQ/ZFC/TranslateRE.lean GodelQ/ZFC/Z0Full.lean; do
  out="$BUILD/${f%.lean}"
  mkdir -p "$(dirname "$out")"
  echo "## $f"
  "$LEAN" -DautoImplicit=false -R . -o "$out.olean" -i "$out.ilean" "$f" || exit 1
done
echo DONE
