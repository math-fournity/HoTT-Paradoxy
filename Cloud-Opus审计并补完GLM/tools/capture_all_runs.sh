#!/usr/bin/env bash
# Capture every run of the Cloud-Opus audit (2026-09-27). Idempotent per run id
# (the capture tool refuses an existing run directory).
set -u
cd "$(dirname "$0")/../.."
C="python3 -B Cloud-Opus审计并补完GLM/tools/capture_copus_run.py"
G=HoTT/formal/glm-russell
O=HoTT/formal/claude-cg001
A=HoTT/formal/cloud-opus-glm-audit
REPLAY_NOTE="Linux replay (Agda v2.8.0 Linux asset, cubical v0.9 byte-identical) of the GLM run of 2026-09-26; GLM's original receipt is left untouched (hash-locked)."

$C --run-id 20260927-COPUS-REPLAY-GLM-IOTA-SYNTAX-01 --proof-id MP-GLM-RUSSELL-IOTA-001 --claim-id GLM-R1-C02 --claim-id GLM-R1-C03 \
  --source $G/iota-syntax/ArtificialEquationControl.agda --manifest-file $G/iota-syntax/RealisticIotaSyntax.agda --expect ACCEPT \
  --scope "Replay of 20260926-GLM-IOTA-SYNTAX-01. Kernel facts: valReflT/valReflF (refl ≡ refl in Path Bool (val (cond (lit b) t s)) (val t), i.e. only that the endpoints agree definitionally) and ¬isSetTmA. Audit reading: GLM-R1-C02 as DECLARED (ι path constructors interpreted as refl) is NOT what valReflT states; the faithful statement is COPUS-GLM-FIX-C02a." \
  --non-goal "Does not certify cong val (betaT t s) ≡ refl (see MP-COPUS-GLM-FIX-001)" --non-goal "Toy first-order ι fragment only" --audit-note "$REPLAY_NOTE"

$C --run-id 20260927-COPUS-REPLAY-GLM-IOTA-SYNTAX-NEG-01 --proof-id MP-GLM-RUSSELL-IOTA-NEG-001 --claim-id GLM-R1-C03 \
  --source $G/iota-syntax/WrongArtIsRefl.agda --manifest-file $G/iota-syntax/ArtificialEquationControl.agda --manifest-file $G/iota-syntax/RealisticIotaSyntax.agda --expect REJECT \
  --scope "Replay of 20260926-GLM-IOTA-SYNTAX-NEG-01: art ≡ refl by refl is rejected (art i != boolTy). Audit reading: this control only shows art is not definitionally refl; it does not test the C03 argument (see MP-COPUS-GLM-FIX-NEG-003)." \
  --audit-note "$REPLAY_NOTE"

$C --run-id 20260927-COPUS-REPLAY-GLM-IOTA-SYNTAX-02 --proof-id MP-GLM-RUSSELL-IOTA-002 --claim-id GLM-R1-C01 \
  --source $G/iota-syntax/RealisticIotaSyntaxSet.agda --manifest-file $G/iota-syntax/RealisticIotaSyntax.agda --expect ACCEPT \
  --scope "Replay of 20260926-GLM-IOTA-SYNTAX-02: realisticIotaSyntaxIsASet : isSet Tm (Tm is a HIT with two ι path constructors; Tm ≃ Bool). Audit reading: a set-level fact about a degenerate toy syntax; not 'the theory's own representation settles'." \
  --non-goal "No substitution, context or dependency; not a self-interpretation" --audit-note "$REPLAY_NOTE"

$C --run-id 20260927-COPUS-REPLAY-GLM-ASCENT-STALL-01 --proof-id MP-GLM-RUSSELL-STALL-001 --claim-id GLM-R2-C01 --claim-id GLM-R2-C02 \
  --source $G/universe-ascent-stall/AscentStallAtSets.agda --expect ACCEPT \
  --scope "Replay of 20260926-GLM-ASCENT-STALL-01: for a set X, isSet (X ≡ X) in Type ℓ and isContr (Ω²(Type ℓ, X)). HIT-free at name level (COPUS-R1-C02/C03). The 'engine stalls' reading uses the HIT-free bridge localGlobal (COPUS-R6-C01) and is an interpretation." \
  --non-goal "Does not show HITs are necessary for any ascent (KS tower ascends HIT-free: COPUS-KS-C01)" --audit-note "$REPLAY_NOTE"

$C --run-id 20260927-COPUS-REPLAY-GLM-GROUPOID-UNIVERSE-01 --proof-id MP-GLM-RUSSELL-GROUPOID-001 --claim-id GLM-R3-C01 \
  --source $G/groupoid-universe/NoHitGroupoidUniverse.agda --expect ACCEPT \
  --scope "Replay of 20260926-GLM-GROUPOID-UNIVERSE-01: ¬universeIsGroupoid : ¬ isOfHLevel 3 (Type (ℓ-suc ℓ-zero)). Audit reading: a faithful cubical replay of Kraus–Sattler's n = 1 case (Lemma 5.8 step at m = 0 with d_q = q⁻¹·q·q, Thm 5.9 at n = 1), base loop on Bool×Bool instead of 2; HIT-free at name level (COPUS-R1-C01)." \
  --non-goal "General n is COPUS-KS-C01/C02, not this package" --audit-note "$REPLAY_NOTE"

$C --run-id 20260927-COPUS-REPLAY-GLM-GROUPOID-UNIVERSE-NEG-01 --proof-id MP-GLM-RUSSELL-GROUPOID-NEG-001 --claim-id GLM-R3-C01 \
  --source $G/groupoid-universe/WrongGroupoidWitness.agda --manifest-file $G/groupoid-universe/NoHitGroupoidUniverse.agda --expect REJECT \
  --scope "Replay of 20260926-GLM-GROUPOID-UNIVERSE-NEG-01. Observed rejection is [NotInScope] true, at scope checking: the file never reaches the type checker, so it does NOT test the claimed arithmetic a (tt,tt) ≠ (tt,tt). Repaired control: MP-COPUS-GLM-FIX-NEG-001." \
  --audit-note "$REPLAY_NOTE" --audit-note "GLM's own receipt of 2026-09-26 shows the same NotInScope error; its status KERNEL_REJECTED_AS_EXPECTED and the work-log phrase 'rejected for the correct reason' are wrong."

$C --run-id 20260927-COPUS-KS-UNIVERSE-TOWER-01 --proof-id MP-COPUS-KS-TOWER-001 \
  --claim-id COPUS-KS-C01 --claim-id COPUS-KS-C02 --claim-id COPUS-KS-C03 --claim-id COPUS-KS-C04 --claim-id COPUS-KS-C05 \
  --source $A/ks-universe-tower/KSUniverseTower.agda --expect ACCEPT \
  --scope "Kraus–Sattler 1311.4002 Section 5 replayed for all n: KS-Theorem-5-9 : (n : ℕ) → ¬ isOfHLevel (2 + n) (Type (lvl n)); workOrderForm : (n : ℕ) → ¬ isOfHLevel (n + 2) (Type (iterSuc n ℓ-zero)); KS-Theorem-5-10-U≤ and -Loop (strict (n+1)-types); generic step at arbitrary (L, k). HIT-free at name level (COPUS-R1-C05)." \
  --non-goal "Known theorem (KS 2015), replayed; not new mathematics" --non-goal "No fixed universe is shown to lack an h-level without HITs (KS §6 consistency remark)" --non-goal "Interpretive readings (never halts, infinite regress) are not formal content"

$C --run-id 20260927-COPUS-KS-UNIVERSE-TOWER-NEG-01 --proof-id MP-COPUS-KS-TOWER-NEG-001 --claim-id COPUS-KS-C01 \
  --source $A/ks-universe-tower/KSNegTrivialBase.agda --manifest-file $A/ks-universe-tower/KSUniverseTower.agda --expect REJECT \
  --scope "Near-miss control: the non-triviality script of the KS base case applied to the trivial loop refl must be rejected (false != true)."

$C --run-id 20260927-COPUS-KS-UNIVERSE-TOWER-NEG-02 --proof-id MP-COPUS-KS-TOWER-NEG-002 --claim-id COPUS-KS-C01 \
  --source $A/ks-universe-tower/KSNegOvershoot.agda --manifest-file $A/ks-universe-tower/KSUniverseTower.agda --expect REJECT \
  --scope "Bookkeeping control: the level-exact certificate tower n cannot yield 'U_n is not an (n+1)-type' (NT (lvl n) n vs NT (lvl n) (suc n))."

$C --run-id 20260927-COPUS-HITSCAN-CERT-GLM-01 --proof-id MP-COPUS-HITSCAN-001 --claim-id COPUS-R1-C01 --claim-id COPUS-R1-C02 --claim-id COPUS-R1-C03 \
  --source $A/hitscan/CertGLM.agda --include $G/groupoid-universe --include $G/universe-ascent-stall \
  --manifest-file $A/hitscan/HITScan.agda --manifest-file $G/groupoid-universe/NoHitGroupoidUniverse.agda --manifest-file $G/universe-ascent-stall/AscentStallAtSets.agda \
  --agda-flag=-v --agda-flag=hitscan:10 --expect ACCEPT \
  --scope "Name-level closures of GLM-R3-C01 (251 names), GLM-R2-C01 (189), GLM-R2-C02 (190) contain no HIT; full closures printed to stdout."

$C --run-id 20260927-COPUS-HITSCAN-CERT-OPUS-01 --proof-id MP-COPUS-HITSCAN-002 --claim-id COPUS-R1-C04 --claim-id COPUS-R6-C01 \
  --source $A/hitscan/CertOpus.agda --include $O/uip-escape --include $O/universe-questioning \
  --manifest-file $A/hitscan/HITScan.agda --manifest-file $O/uip-escape/UIPEscape.agda --manifest-file $O/universe-questioning/UniverseHasNoLevel.agda \
  --agda-flag=-v --agda-flag=hitscan:10 --expect ACCEPT \
  --scope "Name-level closures of C-63 typeIsNotASet (101 names) and of the C-75 bridge localGlobal (201 names) contain no HIT."

$C --run-id 20260927-COPUS-HITSCAN-CERT-KS-01 --proof-id MP-COPUS-HITSCAN-003 --claim-id COPUS-R1-C05 \
  --source $A/hitscan/CertKS.agda --include $A/ks-universe-tower \
  --manifest-file $A/hitscan/HITScan.agda --manifest-file $A/ks-universe-tower/KSUniverseTower.agda \
  --agda-flag=-v --agda-flag=hitscan:10 --expect ACCEPT \
  --scope "Name-level closures of KS-Theorem-5-9 (363), workOrderForm (364), KS-Theorem-5-10-U≤ (363), KS-Theorem-5-10-Loop (364) contain no HIT."

$C --run-id 20260927-COPUS-HITSCAN-NEG-01 --proof-id MP-COPUS-HITSCAN-NEG-001 --claim-id COPUS-R1-C01 \
  --source $A/hitscan/NegCertIota.agda --include $G/iota-syntax \
  --manifest-file $A/hitscan/HITScan.agda --manifest-file $G/iota-syntax/RealisticIotaSyntaxSet.agda --manifest-file $G/iota-syntax/RealisticIotaSyntax.agda --expect REJECT \
  --scope "Scanner teeth: 'isSet Tm has a HIT-free closure' must be rejected, naming Tm."

$C --run-id 20260927-COPUS-HITSCAN-NEG-02 --proof-id MP-COPUS-HITSCAN-NEG-002 --claim-id COPUS-R6-C01 \
  --source $A/hitscan/NegCertC75.agda --include $O/universe-questioning \
  --manifest-file $A/hitscan/HITScan.agda --manifest-file $O/universe-questioning/UniverseHasNoLevel.agda --expect REJECT \
  --scope "Scanner teeth: 'C-75 universeHasNoLevel is HIT-free' must be rejected, naming the Eilenberg–MacLane HITs."

$C --run-id 20260927-COPUS-HITSCAN-NEG-03 --proof-id MP-COPUS-HITSCAN-NEG-003 --claim-id COPUS-R1-C01 \
  --source $A/hitscan/NegCertPT.agda --manifest-file $A/hitscan/HITScan.agda --expect REJECT \
  --scope "Scanner teeth: a one-line use of ∥_∥₁ must be rejected, naming ∥_∥₁."

$C --run-id 20260927-COPUS-GLM-REPAIR-01 --proof-id MP-COPUS-GLM-FIX-001 --claim-id COPUS-GLM-FIX-C02a --claim-id COPUS-GLM-FIX-C02b \
  --source $A/glm-repairs/IotaC02Faithful.agda --include $G/iota-syntax \
  --manifest-file $G/iota-syntax/RealisticIotaSyntax.agda --manifest-file $G/iota-syntax/ArtificialEquationControl.agda --expect ACCEPT \
  --scope "Faithful GLM-R1-C02: cong val (betaT t s) ≡ refl (and betaF), by refl; rupture exhibit: GLM's statement form also holds at the artificial equation art while the faithful form is refuted there."

$C --run-id 20260927-COPUS-GLM-REPAIR-NEG-01 --proof-id MP-COPUS-GLM-FIX-NEG-001 --claim-id GLM-R3-C01 \
  --source $A/glm-repairs/GroupoidNegFixed.agda --include $G/groupoid-universe --manifest-file $G/groupoid-universe/NoHitGroupoidUniverse.agda --expect REJECT \
  --scope "Repaired GLM negative control: a (true , true) ≡ (true , true) rejected by the type checker for the claimed reason (false != true)."

$C --run-id 20260927-COPUS-GLM-REPAIR-NEG-02 --proof-id MP-COPUS-GLM-FIX-NEG-002 --claim-id GLM-R3-C01 \
  --source $A/glm-repairs/GroupoidNegTrivialLoop.agda --include $G/groupoid-universe --manifest-file $G/groupoid-universe/NoHitGroupoidUniverse.agda --expect REJECT \
  --scope "Near-miss control: GLM's τ≠refl script applied to the identity-equivalence loop is rejected (true != false)."

$C --run-id 20260927-COPUS-GLM-REPAIR-NEG-03 --proof-id MP-COPUS-GLM-FIX-NEG-003 --claim-id GLM-R1-C03 \
  --source $A/glm-repairs/IotaC03NegTrivialInterp.agda --include $G/iota-syntax \
  --manifest-file $G/iota-syntax/RealisticIotaSyntax.agda --manifest-file $G/iota-syntax/ArtificialEquationControl.agda --expect REJECT \
  --scope "Near-miss control: GLM's ¬isSetTmA script with art interpreted as a constant path is rejected (cong f' art is refl)."
echo "ALL_CAPTURES_DONE"
