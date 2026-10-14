-- Master assembly PoC (2026-10-14): end-to-end.
--
-- Goal: the FIRST unconditional `AllBlockerQ`, assembled from two verified pieces:
--   1. 9276's `allKey_of_bridge` / `allBlockerQ_of_key` (five theorems, Master-verified);
--   2. nice-lovelace's `ITSubstOpen9.iT_subst_open` general law (Master-verified),
--      whose m = 0 instance (up to QvecVOr_zero/QvecV_zero) is exactly the `hB` shape.
import GodelQ.ZFC.ShCraigElimSetupQ
import GodelQ.ZFC.ITSubstOpen9

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.MasterAssemblyProbe
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- Bridge B — the `hB` parameter shape of `allKey_of_bridge`,
    discharged by the m = 0 instance of the general opening law. -/
theorem bridgeB (q : V) (hq : IsSemiformula ℒₒᵣ (1 : V) q) :
    subst ℒₛₑₜ (?[^&0] : V) (iT (1 : V) q) =
      iT (0 : V) (subst ℒₒᵣ (?[^&0] : V) q) := by
  have h1 : IsSemiformula ℒₒᵣ ((0 : V) + 1) q := by
    rw [show (0 : V) + 1 = 1 from _root_.zero_add 1]
    exact hq
  have h := GodelQ.ITSubstOpen9.iT_subst_open (V := V) (0 : V) q h1
  rw [GodelQ.QvecVDefs.QvecVOr_zero, GodelQ.QvecVDefs.QvecV_zero] at h
  rw [show (0 : V) + 1 = 1 from _root_.zero_add 1] at h
  exact h.symm

/-- `AllKey`, unconditional. -/
theorem allKey_uncond : GodelQ.ShCraigElimSetupQ.AllKey (V := V) :=
  GodelQ.ShCraigElimSetupQ.allKey_of_bridge (fun {q} hq => bridgeB q hq)

/-- ★ `AllBlockerQ`, unconditional — the `hAll` branch's chain closed. -/
theorem allBlockerQ_uncond : GodelQ.ShCraigElimSetupQ.AllBlockerQ (V := V) :=
  GodelQ.ShCraigElimSetupQ.allBlockerQ_of_key allKey_uncond

end GodelQ.MasterAssemblyProbe

#print axioms GodelQ.MasterAssemblyProbe.bridgeB
#print axioms GodelQ.MasterAssemblyProbe.allKey_uncond
#print axioms GodelQ.MasterAssemblyProbe.allBlockerQ_uncond
