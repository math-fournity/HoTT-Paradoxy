#!/usr/bin/env bash
# Capture driver for the product-questioning package (CG001-C-81, C-82).
# bash arrays so that every flag is its own argument (zsh does not split
# unquoted variables; the first attempt failed at argument parsing for that
# reason and created no run directory).
set -u
cd /Volumes/D/HoTT_AI_HANDOFF_20260911
TOOL=.claude/goals/CG-001-targeted-overview/tools/capture_cg001_agda_macos_run.py
PKG=HoTT/formal/claude-cg001/product-questioning
P=HoTT/formal/claude-cg001
INC=(--include "$P/questioning-delay" --include "$P/pedometer-semantics" --include "$P/universe-questioning")
DEPS=(--manifest-file "$PKG/CLAIM.md"
      --manifest-file "$P/questioning-delay/QuestioningDelay.agda"
      --manifest-file "$P/pedometer-semantics/PedometerSemantics.agda"
      --manifest-file "$P/pedometer-semantics/DelayMonad.agda"
      --manifest-file "$P/universe-questioning/UniverseHasNoLevel.agda")
MAINDEP=(--manifest-file "$PKG/ProductQuestioning.agda")
NG1="Not an inconsistency of HoTT and not a proof that the product does not exist; the interpretation bridge and the reality-side premise are left to the user and to community audit."
NG2="Higher inductive types (Eilenberg-MacLane spaces) and univalence (inside the loop computations of C-75) are used; the universe appears as the codomain of the family K : N -> Type; nothing is claimed about type theory without universes."
NG3="The judge answers immediately; never is read through finite-fuel runs only; the product result is HoTT Book Example 8.8.6 with K n in place of S^n (no originality claimed); captured and replayed on macOS only."

python3 -B "$TOOL" --run-id 20260930-CG001-PRODUCT-QUESTIONING-01 \
  --proof-id MP-CG001-PRODUCT-QUESTIONING-001 --claim-id CG001-C-81 --claim-id CG001-C-82 \
  --source "$PKG/ProductQuestioning.agda" "${INC[@]}" "${DEPS[@]}" --expect ACCEPT \
  --scope "Cubical Agda: the questioning program Q of C-77 run on a type that is not the universe. HoTT Book Example 8.8.6 with K n = EM Z (1+n): the product (n : N) -> K n is not of h-level m for any m (the loop of C-75 is nontrivial at the base point; loops of a product are the product of loops); for every judge Q on the product is never, a judge exists and every judge equals it, the kernel runs fuel 1000 by refl, and the question 'settled at some level at all?' answers no at fuel 0. Control: the same product with bounded height, (n : N) -> K b, is of h-level 3+b and not of h-level 2+b, and for every judge Q returns 2+b at fuel 1+b and nothing at smaller fuel (it stops at stage 2+b)." \
  --non-goal "$NG1" --non-goal "$NG2" --non-goal "$NG3"

python3 -B "$TOOL" --run-id 20260930-CG001-PRODUCT-QUESTIONING-NEG-01 \
  --proof-id MP-CG001-PRODUCT-QUESTIONING-NEG-001 --claim-id CG001-C-81 \
  --source "$PKG/WrongProductAnswersEarly.agda" "${INC[@]}" "${MAINDEP[@]}" "${DEPS[@]}" --expect REJECT \
  --scope "Negative control for CG001-C-81: claims by refl that Q on the product (n : N) -> K n with judgeProd returns level 1 at fuel 1; expected rejection nothing != just 1 (the kernel runs the program and the judge answers no)." \
  --non-goal "Rejection shows the claimed value is wrong for this run; it is not by itself a proof of non-halting."

python3 -B "$TOOL" --run-id 20260930-CG001-PRODUCT-QUESTIONING-NEG-02 \
  --proof-id MP-CG001-PRODUCT-QUESTIONING-NEG-002 --claim-id CG001-C-81 \
  --source "$PKG/WrongProductNeverByRefl.agda" "${INC[@]}" "${MAINDEP[@]}" "${DEPS[@]}" --expect REJECT \
  --scope "Negative control for CG001-C-81: claims by refl that Q on the product equals never; expected rejection (askFrom Prod judgeProd 1 != never): computation alone does not show non-halting, so C-81 (c) needs the corecursive proof of C-77." \
  --non-goal "Rejection is about definitional equality only; it says nothing against the proved path equality."

python3 -B "$TOOL" --run-id 20260930-CG001-PRODUCT-QUESTIONING-NEG-03 \
  --proof-id MP-CG001-PRODUCT-QUESTIONING-NEG-003 --claim-id CG001-C-82 \
  --source "$PKG/WrongBoundedSilent.agda" "${INC[@]}" "${MAINDEP[@]}" "${DEPS[@]}" --expect REJECT \
  --scope "Negative control for CG001-C-82: claims by refl that Q on the bounded product (n : N) -> K 0 with judgeBounded 0 is still silent at fuel 1; expected rejection just 2 != nothing (the judge answers no at stage 1 and yes at stage 2)." \
  --non-goal "Only the instance b = 0 is run here."

python3 -B "$TOOL" --run-id 20260930-CG001-PRODUCT-QUESTIONING-NEG-04 \
  --proof-id MP-CG001-PRODUCT-QUESTIONING-NEG-004 --claim-id CG001-C-82 \
  --source "$PKG/WrongBoundedStopsEarly.agda" "${INC[@]}" "${MAINDEP[@]}" "${DEPS[@]}" --expect REJECT \
  --scope "Negative control for CG001-C-82: claims by refl that Q on the bounded product (n : N) -> K 0 stops at stage 1 (fuel 0 returns 1); expected rejection nothing != just 1 (the bounded product is not a set)." \
  --non-goal "Only the instance b = 0 is run here."

echo "ALL_DONE"
