-- CG-009: the opening vector QvecV m = [#0, ..., #(m-1), &0] = qVec^m ?[^&0].
--
-- NOTE: both blueprint clauses inline their graph bodies.  Writing
-- `!(qVecGraph L) y ih` makes elaboration blow up (minutes of unification);
-- inlining keeps the file at ~3s.
--
-- Two copies (one per language) because Foundation's `termBShiftVec` is a
-- per-language `TermRec.Construction`, so `qVec ℒₒᵣ` and `qVec ℒₛₑₜ` are only
-- propositionally — not definitionally — equal, and the `Construction` instances
-- do not elaborate generically.
import GodelQ.ZFC.HAllProof

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.QvecVDefs
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

section SetSide
noncomputable def qqVecsS.blueprint : PR.Blueprint 1 where
  zero := .mkSigma “y x. y = x”
  succ := .mkSigma “y ih n x. ∃ k, !lenDef k ih ∧ ∃ sw, !(termBShiftVecGraph ℒₛₑₜ) sw k ih ∧
    ∃ t, !qqBvarDef t 0 ∧ !adjoinDef y t sw”

noncomputable def qqVecsS.construction : PR.Construction V qqVecsS.blueprint where
  zero := fun x ↦ x 0
  succ := fun _ _ ih ↦ ^#0 ∷ termBShiftVec ℒₛₑₜ (len ih) ih
  zero_defined := .mk fun v ↦ by simp [qqVecsS.blueprint]
  succ_defined := .mk fun v ↦ by simp [qqVecsS.blueprint]

noncomputable def qqVecsS (w k : V) : V := qqVecsS.construction.result ![w] k

@[simp] lemma qqVecsS_zero (w : V) : qqVecsS (V := V) w 0 = w := by
  simp [qqVecsS, qqVecsS.construction]

@[simp] lemma qqVecsS_succ (w k : V) :
    qqVecsS (V := V) w (k + 1) = qVec ℒₛₑₜ (qqVecsS (V := V) w k) := by
  simp [qqVecsS, qqVecsS.construction, qVec]

noncomputable def qqVecsSDef : 𝚺ᴬ₁.Semisentence 3 :=
  qqVecsS.blueprint.resultDef |>.rew (Rew.subst ![#0, #2, #1])

instance qqVecsS_defined : 𝚺ᴬ₁-Function₂ (qqVecsS : V → V → V) via qqVecsSDef := .mk
  fun v ↦ by simp [qqVecsS.construction.result_defined_iff, qqVecsSDef]; rfl

instance qqVecsS_definable : 𝚺ᴬ₁-Function₂ (qqVecsS : V → V → V) := qqVecsS_defined.to_definable

/-- **The opening vector** (built with `ℒₛₑₜ`): `QvecV m = [#0, …, #(m-1), &0]`. -/
noncomputable def QvecV (m : V) : V := qqVecsS (V := V) (?[^&0] : V) m

@[simp] lemma QvecV_zero : QvecV (V := V) 0 = (?[^&0] : V) := by simp [QvecV]

@[simp] lemma QvecV_succ (m : V) :
    QvecV (V := V) (m + 1) = qVec ℒₛₑₜ (QvecV (V := V) m) := by simp [QvecV]
end SetSide

section OrSide
noncomputable def qqVecsO.blueprint : PR.Blueprint 1 where
  zero := .mkSigma “y x. y = x”
  succ := .mkSigma “y ih n x. ∃ k, !lenDef k ih ∧ ∃ sw, !(termBShiftVecGraph ℒₒᵣ) sw k ih ∧
    ∃ t, !qqBvarDef t 0 ∧ !adjoinDef y t sw”

noncomputable def qqVecsO.construction : PR.Construction V qqVecsO.blueprint where
  zero := fun x ↦ x 0
  succ := fun _ _ ih ↦ ^#0 ∷ termBShiftVec ℒₒᵣ (len ih) ih
  zero_defined := .mk fun v ↦ by simp [qqVecsO.blueprint]
  succ_defined := .mk fun v ↦ by simp [qqVecsO.blueprint]

noncomputable def qqVecsO (w k : V) : V := qqVecsO.construction.result ![w] k

@[simp] lemma qqVecsO_zero (w : V) : qqVecsO (V := V) w 0 = w := by
  simp [qqVecsO, qqVecsO.construction]

@[simp] lemma qqVecsO_succ (w k : V) :
    qqVecsO (V := V) w (k + 1) = qVec ℒₒᵣ (qqVecsO (V := V) w k) := by
  simp [qqVecsO, qqVecsO.construction, qVec]

noncomputable def qqVecsODef : 𝚺ᴬ₁.Semisentence 3 :=
  qqVecsO.blueprint.resultDef |>.rew (Rew.subst ![#0, #2, #1])

instance qqVecsO_defined : 𝚺ᴬ₁-Function₂ (qqVecsO : V → V → V) via qqVecsODef := .mk
  fun v ↦ by simp [qqVecsO.construction.result_defined_iff, qqVecsODef]; rfl

instance qqVecsO_definable : 𝚺ᴬ₁-Function₂ (qqVecsO : V → V → V) := qqVecsO_defined.to_definable

/-- **The opening vector** (built with `ℒₒᵣ`): the code `subst ℒₒᵣ` actually sees. -/
noncomputable def QvecVOr (m : V) : V := qqVecsO (V := V) (?[^&0] : V) m

@[simp] lemma QvecVOr_zero : QvecVOr (V := V) 0 = (?[^&0] : V) := by simp [QvecVOr]

@[simp] lemma QvecVOr_succ (m : V) :
    QvecVOr (V := V) (m + 1) = qVec ℒₒᵣ (QvecVOr (V := V) m) := by simp [QvecVOr]
end OrSide

end GodelQ.QvecVDefs
