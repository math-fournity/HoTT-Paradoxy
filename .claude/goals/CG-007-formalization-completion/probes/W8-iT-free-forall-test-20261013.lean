import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimSetupQ GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFL
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **决定性检验**：`iT_free` 在含 `∀` 的 `p` 上是否成立？

`p = ^∀ (^rel 2 cEqN ?[^#0,^#0])`（层 1，无 fvar）。

* LHS `iT 0 (free p)`：`free p = subst ?[^&0] (shift p)`；`shift p = p`（无 fvar，
  但 bvar 会加一！`^#0 ↦ ^#1`）。故 `free p = subst ?[^&0] (^∀ (^rel 2 cEqN ?[^#1,^#1]))`。
* RHS `free (iT 1 p)`。

本探针把两侧都推到底，用 `trace_state` 看它们是否同形。 -/
example :
    iT (0:V) (free ℒₒᵣ (^∀ (^rel 2 (↑cEqN) (?[^#0, ^#0] : V)) : V))
      = free ℒₛₑₜ (iT (1:V) (^∀ (^rel 2 (↑cEqN) (?[^#0, ^#0] : V)) : V)) := by
  -- 两侧都先展开 `free`
  rw [show free ℒₒᵣ (^∀ (^rel 2 (↑cEqN) (?[^#0, ^#0] : V)) : V)
        = subst ℒₒᵣ (?[^&0] : V) (shift ℒₒᵣ (^∀ (^rel 2 (↑cEqN) (?[^#0, ^#0] : V)) : V))
      from rfl]
  rw [show free ℒₛₑₜ (iT (1:V) (^∀ (^rel 2 (↑cEqN) (?[^#0, ^#0] : V)) : V))
        = subst ℒₛₑₜ (?[^&0] : V)
            (shift ℒₛₑₜ (iT (1:V) (^∀ (^rel 2 (↑cEqN) (?[^#0, ^#0] : V)) : V)))
      from rfl]
  -- RHS 内层：`iT 1 (^∀ X) = ^∀ (imp domZero (iT 2 X))`
  rw [iT_all (n := (1:V)) (by
    rw [IsUFormula.rel]
    exact ⟨by rw [cEqN]; exact codeIn_rel_quote _, by
      rw [show (?[^#0, ^#0] : V) = (^#0 : V) ∷ ((^#0 : V) ∷ (0:V)) from rfl]
      have h1 : IsUTermVec ℒₒᵣ (1:V) ((^#0 : V) ∷ (0:V)) :=
        IsUTermVec.adjoin IsUTermVec.empty (IsUTerm.bvar (z := (0:V)))
      have h2 : IsUTermVec ℒₒᵣ (2:V) ((^#0 : V) ∷ ((^#0 : V) ∷ (0:V))) :=
        IsUTermVec.adjoin h1 (IsUTerm.bvar (z := (0:V)))
      simpa using h2⟩)]
  trace_state
  sorry

end GodelQ.ProbeFL
