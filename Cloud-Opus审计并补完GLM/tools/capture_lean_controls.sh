#!/usr/bin/env bash
# Supplementary Lean controls from the self-audit of 2026-09-27
# (HoTT/formal/cloud-opus-glm-audit/lean-controls/, see its CLAIM.md):
#   * an endpoint negative control for CG001-C-65 (the original WrongRoute.lean
#     is rejected at an argument, so it does not show the endpoint check it
#     claims to show);
#   * kernel-level twins for CG001-C-65 and CG001-C-72: the same terms handed
#     straight to the Lean kernel with Lean.addDecl, accepted when right and
#     rejected with a "(kernel)" error when wrong.
# Toolchain record: HoTT/formal/cloud-opus-glm-audit/LEAN_TOOLCHAIN_META.linux-x86_64.json
# (the base record plus the Lean and Std libraries that `import Lean` needs).
# Idempotent per run id (the capture tool refuses an existing run directory).
set -u
cd "$(dirname "$0")/../.."
L="python3 -B Cloud-Opus审计并补完GLM/tools/capture_copus_lean_run.py --toolchain HoTT/formal/cloud-opus-glm-audit/LEAN_TOOLCHAIN_META.linux-x86_64.json"
O=HoTT/formal/claude-cg001
K=HoTT/formal/cloud-opus-glm-audit/lean-controls
NOTE="Self-audit control of 2026-09-27 (Cloud-Opus): Lean 4.34.0 Linux release asset, same source commit 293d5d0c as the macOS toolchain of the Opus runs; the CG-001 driver lean_check.py is used unchanged."

$L --run-id 20260927-COPUS-LEAN-C65-ENDPOINT-NEG-01 --proof-id MP-COPUS-LEAN-C65-ENDPOINT-NEG-001 --claim-id CG001-C-65 \
  --source $O/wild-sst-lean/WildSSTUIP.lean --source $K/WrongRouteEndpoint.lean --manifest-file $K/CLAIM.md --manifest-file $O/wild-sst-lean/CLAIM.md --expect REJECT \
  --scope "routeA whose third step (accepted on its own as stepThreeWrongFace) is the right rewrite under the wrong outer face map S.d m i instead of S.d m k: rejected at wrongRouteEndpoint by the elaborator, with a type mismatch at the joint between step two and step three." \
  --non-goal "Shows that the elaborator checks the endpoints of the chain; the kernel-level twin is 20260927-COPUS-LEAN-C65-KERNEL-NEG-01" --audit-note "$NOTE"
$L --run-id 20260927-COPUS-LEAN-C65-KERNEL-01 --proof-id MP-COPUS-LEAN-C65-KERNEL-001 --claim-id COPUS-LEAN-C01 \
  --source $O/wild-sst-lean/WildSSTUIP.lean --source $K/KernelRoute.lean --leanchecker --manifest-file $K/CLAIM.md --expect ACCEPT \
  --scope "kernelRouteA: Eq.trans stepOne (Eq.trans stepTwo stepThree) assembled with mkAppN, every endpoint explicit, handed to the kernel with Lean.addDecl under the statement of routeA, is accepted; kernelRouteA_states_routeA : @kernelRouteA = @routeA := rfl; no axioms; leanchecker --fresh replays the module." \
  --non-goal "A statement in a type theory with UIP; adds no mathematics to CG001-C-65 (kernelRouteA and routeA prove the same proposition)" --audit-note "$NOTE"
$L --run-id 20260927-COPUS-LEAN-C65-KERNEL-NEG-01 --proof-id MP-COPUS-LEAN-C65-KERNEL-NEG-001 --claim-id COPUS-LEAN-C01 \
  --source $O/wild-sst-lean/WildSSTUIP.lean --source $K/KernelRoute.lean --source $K/KernelRouteEndpoint.lean --manifest-file $K/CLAIM.md --expect REJECT \
  --scope "The same builder addRoute with the third step replaced by stepThreeWrong (accepted on its own; the right rewrite under the wrong outer face map): the kernel itself rejects kernelRouteWrong with a '(kernel) application type mismatch' at the joint between step two and step three." \
  --non-goal "Shows that the kernel checks this chain; does not certify the Lean kernel in general" --audit-note "$NOTE"
$L --run-id 20260927-COPUS-LEAN-C72-KERNEL-01 --proof-id MP-COPUS-LEAN-C72-KERNEL-001 --claim-id COPUS-LEAN-C02 \
  --source $O/universe-set-lean/UniverseIsSet.lean --source $K/KernelCast.lean --leanchecker --manifest-file $K/CLAIM.md --expect ACCEPT \
  --scope "kernelCastIsId : ∀ (p : Bool = Bool), cast p true = true, with the proof term fun p => Eq.refl true handed to the kernel with Lean.addDecl, is accepted; kernelCastIsId_states_castIsId; no axioms; leanchecker --fresh replays the module." \
  --non-goal "A statement in a type theory with UIP, used as a contrast; not a HoTT statement" --audit-note "$NOTE"
$L --run-id 20260927-COPUS-LEAN-C72-KERNEL-NEG-01 --proof-id MP-COPUS-LEAN-C72-KERNEL-NEG-001 --claim-id COPUS-LEAN-C02 \
  --source $O/universe-set-lean/UniverseIsSet.lean --source $K/KernelCast.lean --source $K/KernelCastFlips.lean --manifest-file $K/CLAIM.md --expect REJECT \
  --scope "The same builder addCastDecl with r = false: the statement ∀ (p : Bool = Bool), cast p true = false with the proof term fun p => Eq.refl false is rejected by the kernel itself ('(kernel) declaration type mismatch'): the kernel computes cast p true to true." \
  --non-goal "Shows that the kernel makes this definitional judgement; does not certify the Lean kernel in general" --audit-note "$NOTE"
