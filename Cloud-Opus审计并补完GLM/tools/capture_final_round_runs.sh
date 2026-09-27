#!/usr/bin/env bash
# Final-verdict round (2026-09-27): runs added after the 21 runs of capture_all_runs.sh.
# Idempotent per run id (the capture tool refuses an existing run directory).
set -u
cd "$(dirname "$0")/../.."
C="python3 -B Cloud-Opus审计并补完GLM/tools/capture_copus_run.py"
A=HoTT/formal/cloud-opus-glm-audit

$C --run-id 20260927-COPUS-KS-CATALOG-OF-SETS-01 --proof-id MP-COPUS-KS-TOWER-002 --claim-id COPUS-KS-C06 \
  --source $A/ks-universe-tower/CatalogOfSetsTwoSteps.agda --manifest-file $A/ks-universe-tower/KSUniverseTower.agda --expect ACCEPT \
  --scope "catalogOfSetsTwoSteps : isOfHLevel 3 (hSet ℓ-zero) × (¬ isSet (hSet ℓ-zero)), proved as KS-Theorem-5-10-U≤ 0 (T (lvl 0) 0 = TypeOfHLevel ℓ-zero (2 + 0) = hSet ℓ-zero definitionally). The adjacent control of the Russell-face final verdict: the level-by-level questioning of the catalog of all sets answers NO at step 1 and YES at step 2." \
  --non-goal "Says nothing about Type ℓ-zero itself (that is C-75, which uses HITs)" \
  --non-goal "'Questioning' and 'stops at step two' are readings of the two components, not formal content" \
  --audit-note "First type-checked as a scratchpad one-liner (no receipt); moved into the repository and captured on the user's instruction that all code of this work be tracked."

$C --run-id 20260927-COPUS-KS-CATALOG-OF-SETS-NEG-01 --proof-id MP-COPUS-KS-TOWER-NEG-003 --claim-id COPUS-KS-C06 \
  --source $A/ks-universe-tower/KSNegCatalogOfSetsIsSet.agda --manifest-file $A/ks-universe-tower/KSUniverseTower.agda --expect REJECT \
  --scope "Bookkeeping near miss: reading the first component of KS-Theorem-5-10-U≤ 0 (h-level 3) as 'hSet ℓ-zero is a set' (h-level 2) must be rejected at type checking; the questioning of the catalog of sets does not stop at step 1."
