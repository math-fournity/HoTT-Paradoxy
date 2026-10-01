#!/usr/bin/env bash
# Capture driver for the truncation-questioning package (CG001-C-83).
# bash arrays so that every flag is its own argument (zsh does not split
# unquoted variables).  Usage: capture_truncation.sh main|neg
set -u
cd /Volumes/D/HoTT_AI_HANDOFF_20260911
TOOL=.claude/goals/CG-001-targeted-overview/tools/capture_cg001_agda_macos_run.py
PKG=HoTT/formal/claude-cg001/truncation-questioning
P=HoTT/formal/claude-cg001
INC=(--include "$P/product-questioning" --include "$P/questioning-delay" --include "$P/pedometer-semantics" --include "$P/universe-questioning")
DEPS=(--manifest-file "$PKG/CLAIM.md"
      --manifest-file "$P/product-questioning/ProductQuestioning.agda"
      --manifest-file "$P/questioning-delay/QuestioningDelay.agda"
      --manifest-file "$P/pedometer-semantics/PedometerSemantics.agda"
      --manifest-file "$P/pedometer-semantics/DelayMonad.agda"
      --manifest-file "$P/universe-questioning/UniverseHasNoLevel.agda")
MAINDEP=(--manifest-file "$PKG/TruncationQuestioning.agda")
NG1="Not an inconsistency of HoTT and not a claim that truncation is wrong: set truncation is a legitimate construction; the package records how it makes the questioning stop and what it costs."
NG2="Does not decide whether asking about the set truncation is the same task as asking about the universe; task fidelity is left to the user (CN-049 section 4, CN-050)."
NG3="No judge is constructed for the truncated product (stage 0 would decide whether it is a proposition, which involves countable choice); higher inductive types (set and propositional truncation, and via C-81 Eilenberg-MacLane spaces) and univalence (notEq) are used; standard HoTT facts, no originality claimed; captured and replayed on macOS only."

case "${1:-}" in
main)
python3 -B "$TOOL" --run-id 20260930-CG001-TRUNCATION-QUESTIONING-01 \
  --proof-id MP-CG001-TRUNCATION-QUESTIONING-001 --claim-id CG001-C-83 \
  --source "$PKG/TruncationQuestioning.agda" "${INC[@]}" "${DEPS[@]}" --expect ACCEPT \
  --scope "Cubical Agda: the textbook dissolution as a control. The questioning program Q of C-77, run on the set truncation of any type, returns 1 at fuel 0 for every judge (stage 1). The truncated universe is not a proposition, a judge exists and every judge equals it, and the kernel runs Q with it and gets 1 at fuel 0 by refl; side by side, Q on the universe itself is never (C-78) and Q on the product of C-81 is never while Q on its set truncation stops at stage 1. Cost: transport along notEq sends true to false, so notEq is not refl; after truncation cong |_|2 notEq equals refl (squash2); no function decodes the truncated universe back (it would make the universe a set)." \
  --non-goal "$NG1" --non-goal "$NG2" --non-goal "$NG3"
;;
neg)
python3 -B "$TOOL" --run-id 20260930-CG001-TRUNCATION-QUESTIONING-NEG-01 \
  --proof-id MP-CG001-TRUNCATION-QUESTIONING-NEG-001 --claim-id CG001-C-83 \
  --source "$PKG/WrongTruncSilent.agda" "${INC[@]}" "${MAINDEP[@]}" "${DEPS[@]}" --expect REJECT \
  --scope "Negative control for CG001-C-83: claims by refl that Q on the set truncation of the universe with judgeTU is still silent at fuel 0; expected rejection just 1 != nothing (the kernel runs the program and the judge answers yes at stage 1)." \
  --non-goal "Rejection shows the claimed value is wrong for this run; the general statement (a) is proved in the main package."

python3 -B "$TOOL" --run-id 20260930-CG001-TRUNCATION-QUESTIONING-NEG-02 \
  --proof-id MP-CG001-TRUNCATION-QUESTIONING-NEG-002 --claim-id CG001-C-83 \
  --source "$PKG/WrongNotEqTrivial.agda" "${INC[@]}" "${MAINDEP[@]}" "${DEPS[@]}" --expect REJECT \
  --scope "Negative control for CG001-C-83 (d): claims by refl that transport along notEq leaves true unchanged before any truncation; expected rejection false != true (the kernel computes the transport to false)." \
  --non-goal "Only the value at true is checked here; notEqNotRefl in the main package is the general statement."
;;
*) echo "usage: $0 main|neg"; exit 2;;
esac
echo "ALL_DONE $1"
