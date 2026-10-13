import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimSetupQ GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFL
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`rel` 支（`R` 也特化）**：`R = cEqN`、`k = 2`、`v` 层 1。

`cEqN` 是**字面**（`(cEqN : ℕ) : V`），不是符号，故 `iT_rel` 的 `whnf` 能收敛。 -/
example {v : V} (hv : IsSemitermVec ℒₒᵣ (2:V) (1:V) v) :
    iT (1:V) (subst ℒₒᵣ (?[^#0, ^&0] : V) (^rel 2 (↑cEqN) v))
      = subst ℒₛₑₜ (?[^&0] : V) (iT (1:V) (^rel 2 (↑cEqN) v)) := by
  have hR : (ℒₒᵣ).IsRel (2:V) (↑cEqN : V) := by rw [cEqN]; exact codeIn_rel_quote _
  have hw : IsSemitermVec ℒₒᵣ (2:V) (1:V) (?[^#0, ^&0] : V) :=
    IsSemitermVec.doubleton.mpr
      ⟨IsSemiterm.bvar.mpr (by norm_num),
       IsSemiterm.fvar (L := ℒₒᵣ) (V := V) (n := (1:V)) 0⟩
  rw [Bootstrapping.substs_rel (L := ℒₒᵣ) hR hv.isUTerm]
  have hw' : IsUTermVec ℒₒᵣ (2:V) (termSubstVec ℒₒᵣ (2:V) (?[^#0, ^&0] : V) v) :=
    (IsSemitermVec.termSubstVec (L := ℒₒᵣ) (V := V) hv hw).isUTerm
  rw [show iT (1:V) (^rel 2 (↑cEqN) (termSubstVec ℒₒᵣ (2:V) (?[^#0, ^&0] : V) v))
        = iTR (1:V) (2:V) (↑cEqN) (termSubstVec ℒₒᵣ (2:V) (?[^#0, ^&0] : V) v)
      from iT_rel (V := V) (n := (1:V)) (k := (2:V)) (R := (↑cEqN : V)) hR hw']
  rw [iT_rel (V := V) (n := (1:V)) (k := (2:V)) (R := (↑cEqN : V)) hR hv.isUTerm]
  rw [iTR, iTR]
  trace_state
  sorry

end GodelQ.ProbeFL
