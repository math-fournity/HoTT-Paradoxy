import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimSetupQ GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFL
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`iT_substs1_samelevel` 的 `rel` 支（`k = 2` 特化）**。

目标：`iT 1 (subst ?[^#0,^&0] (^rel 2 R v)) = subst ?[^&0] (iT 1 (^rel 2 R v))`，
`v` 层 1、`R` 是二元关系符号。

**已证的特例**（`iT_substs1_atom`）就是 `R = cEqN`、`v = ?[^#0,^#0]`。
本探针把 `v` 放开到一般层 1 向量。 -/
example {R v : V} (hR : (ℒₒᵣ).IsRel (2:V) R) (hv : IsSemitermVec ℒₒᵣ (2:V) (1:V) v) :
    iT (1:V) (subst ℒₒᵣ (?[^#0, ^&0] : V) (^rel 2 R v))
      = subst ℒₛₑₜ (?[^&0] : V) (iT (1:V) (^rel 2 R v)) := by
  have hw : IsSemitermVec ℒₒᵣ (2:V) (1:V) (?[^#0, ^&0] : V) :=
    IsSemitermVec.doubleton.mpr
      ⟨IsSemiterm.bvar.mpr (by norm_num),
       IsSemiterm.fvar (L := ℒₒᵣ) (V := V) (n := (1:V)) 0⟩
  rw [Bootstrapping.substs_rel (L := ℒₒᵣ) hR hv.isUTerm]
  have hw' : IsUTermVec ℒₒᵣ (2:V) (termSubstVec ℒₒᵣ (2:V) (?[^#0, ^&0] : V) v) :=
    (IsSemitermVec.termSubstVec (L := ℒₒᵣ) (V := V) hv hw).isUTerm
  -- 两侧都换成 `iTR`
  have eL : iT (1:V) (^rel 2 R (termSubstVec ℒₒᵣ (2:V) (?[^#0, ^&0] : V) v))
      = iTR (1:V) (2:V) R (termSubstVec ℒₒᵣ (2:V) (?[^#0, ^&0] : V) v) :=
    iT_rel (V := V) (n := (1:V)) (k := (2:V)) (R := R) hR hw'
  have eR : iT (1:V) (^rel 2 R v) = iTR (1:V) (2:V) R v :=
    iT_rel (V := V) (n := (1:V)) (k := (2:V)) (R := R) hR hv.isUTerm
  rw [eL, eR]
  rw [iTR, iTR]
  trace_state
  sorry

end GodelQ.ProbeFL
