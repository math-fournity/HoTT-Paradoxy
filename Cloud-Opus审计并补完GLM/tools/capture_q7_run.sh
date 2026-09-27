#!/usr/bin/env bash
# Q7 annotated replay run (Cloud-Opus audit, 2026-09-27).
set -u
cd "$(dirname "$0")/../.."
G=HoTT/formal/glm-russell
A=HoTT/formal/cloud-opus-glm-audit
python3 -B Cloud-Opus审计并补完GLM/tools/capture_copus_run.py --run-id 20260927-COPUS-GLM-REPAIR-Q7-01 --proof-id MP-COPUS-Q7-001 --claim-id COPUS-Q7-C01 \
  --source $A/glm-repairs/Q7AnnotatedReplay.agda --include $G/groupoid-universe --manifest-file $G/groupoid-universe/NoHitGroupoidUniverse.agda --expect ACCEPT \
  --scope "Q7 final review: every intermediate step of GLM's ¬universeIsGroupoid restated with explicit types (isOfHLevel 3 ≡ isGroupoid; a (tt,tt) ≡ (ff,tt); cong fst τ ≡ ua ea; τ≠refl chain (tt,tt) ≡ transport refl ≡ transport (ua ea) ≡ (ff,tt); cong fst (FAM x) ≡ snd x; evaluation of equivEq (funExt FAM) at a point is FAM there; isSet (Loop ≃ Loop) from a groupoid universe) and accepted by the kernel." \
  --non-goal "Checks the auditor's reading of GLM's proof; adds no new mathematics"
echo "Q7_CAPTURE_DONE"
O=HoTT/formal/claude-cg001
python3 -B Cloud-Opus审计并补完GLM/tools/capture_copus_run.py --run-id 20260927-COPUS-HITSCAN-CERT-OPUS-02 --proof-id MP-COPUS-HITSCAN-004 --claim-id COPUS-R1-C06 \
  --source $A/hitscan/CertC71.agda --include $O/hset-universe \
  --manifest-file $A/hitscan/HITScan.agda --manifest-file $O/hset-universe/HSetNotSet.agda \
  --agda-flag=-v --agda-flag=hitscan:10 --expect ACCEPT \
  --scope "Name-level closure of C-71 hSetNotSet (the KS base case, hSet ℓ-zero is not a set): 149 names, no HIT."
echo "C71_CAPTURE_DONE"
