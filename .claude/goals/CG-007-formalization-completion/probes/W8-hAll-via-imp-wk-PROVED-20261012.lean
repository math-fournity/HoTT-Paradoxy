import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimSetupQ GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFL
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **决定性测试**：`iT_substs1` 在 `σ = ^rel 2 cEqN ?[^#0,^#0]`（层 1 原子）上。
两侧都归一化到 `^rel 2 cEqN ?[^&0,^&0]`。 -/
example :
    iT (0:V) (subst ℒₒᵣ (?[^&0] : V) (^rel 2 (↑cEqN) (?[^#0, ^#0] : V)))
      = subst ℒₛₑₜ (?[^&0] : V) (iT (1:V) (^rel 2 (↑cEqN) (?[^#0, ^#0] : V))) := by
  have hR : (ℒₒᵣ).IsRel (2:V) (↑cEqN : V) := by rw [cEqN]; exact codeIn_rel_quote _
  rw [Bootstrapping.substs_rel (L := ℒₒᵣ) hR
    (by simpa using (IsUTermVec.adjoin (IsUTermVec.adjoin IsUTermVec.empty
      (IsUTerm.bvar (z := (0:V)))) (IsUTerm.bvar (z := (0:V)))))]
  trace_state
  sorry

end GodelQ.ProbeFL
