import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimSetupQ GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFL
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- 两个 bvar 的向量（层 2）——`adjoin` 是证明项，用 `simpa using` 桥。 -/
lemma vec2 : IsUTermVec ℒₒᵣ (2:V) (?[^#0, ^#0] : V) := by
  have h1 : IsUTermVec ℒₒᵣ (1:V) ((^#0 : V) ∷ (0:V)) :=
    IsUTermVec.adjoin (L := ℒₒᵣ) (V := V) (k := (1:V)) (n := (0:V))
      IsUTermVec.empty (IsUTerm.bvar (z := (0:V)))
  have h2 : IsUTermVec ℒₒᵣ (2:V) ((^#0 : V) ∷ ((^#0 : V) ∷ (0:V))) :=
    IsUTermVec.adjoin (L := ℒₒᵣ) (V := V) (k := (2:V)) (n := (1:V))
      h1 (IsUTerm.bvar (z := (0:V)))
  simpa using h2

/-- `^∀ (^rel 2 cEqN ?[^#0,^#0])` 的 `IsUFormula`。 -/
lemma huAll : IsUFormula ℒₒᵣ (^∀ (^rel 2 (↑cEqN) (?[^#0, ^#0] : V)) : V) := by
  rw [IsUFormula.all]
  rw [IsUFormula.rel]
  exact ⟨by rw [cEqN]; exact codeIn_rel_quote _, vec2⟩

/-- **`iT_free` 含 `∀` 的检验**。 -/
example :
    iT (0:V) (free ℒₒᵣ (^∀ (^rel 2 (↑cEqN) (?[^#0, ^#0] : V)) : V))
      = free ℒₛₑₜ (iT (1:V) (^∀ (^rel 2 (↑cEqN) (?[^#0, ^#0] : V)) : V)) := by
  rw [show free ℒₒᵣ (^∀ (^rel 2 (↑cEqN) (?[^#0, ^#0] : V)) : V)
        = subst ℒₒᵣ (?[^&0] : V) (shift ℒₒᵣ (^∀ (^rel 2 (↑cEqN) (?[^#0, ^#0] : V)) : V))
      from rfl]
  rw [show free ℒₛₑₜ (iT (1:V) (^∀ (^rel 2 (↑cEqN) (?[^#0, ^#0] : V)) : V))
        = subst ℒₛₑₜ (?[^&0] : V)
            (shift ℒₛₑₜ (iT (1:V) (^∀ (^rel 2 (↑cEqN) (?[^#0, ^#0] : V)) : V)))
      from rfl]
  rw [show iT (1:V) (^∀ (^rel 2 (↑cEqN) (?[^#0, ^#0] : V)) : V)
        = (^∀ (imp ℒₛₑₜ domZero (iT (1 + 1) (^rel 2 (↑cEqN) (?[^#0, ^#0] : V)))) : V)
      from iT_all (n := (1:V)) huAll]
  -- 两侧各推 `shift`
  rw [Bootstrapping.shift_all (L := ℒₒᵣ) huAll]
  rw [Bootstrapping.shift_all (L := ℒₛₑₜ)
      (IsUFormula.imp.mpr ⟨isUFormula_domZero2, ?_⟩)]
  · trace_state
    sorry
  · sorry

end GodelQ.ProbeFL
