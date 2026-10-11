import GodelQ.ZFC.SeqTranslateFormula

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.SeqTranslate

open GodelQ.Translate GodelQ.ZFCArith

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

instance iVE_definable : 𝚺ᴬ₁-Function₂ (iVE : V → V → V) := iVE_defined.to_definable
instance iVE_definable' (Γ m) : Γᴬ_[m + 1]-Function₂[V] iVE := iVE_definable.of_sigmaOne

lemma isSemiformula_eqAtom {n t : V} (hn : 0 < n) (ht : IsSemiterm ℒₛₑₜ n t) :
    IsSemiformula ℒₛₑₜ n (eqAtom t) := by
  rw [eqAtom, IsSemiformula.rel]
  refine ⟨?_, ?_⟩
  · rw [cEqN]
    exact codeIn_rel_quote _
  · rw [show (?[^#0, t] : V) = (^#0 : V) ∷ (t ∷ 0) from rfl]
    rw [show (2 : V) = 1 + 1 by simp [one_add_one_eq_two], IsSemitermVec.cons_iff]
    refine ⟨IsSemiterm.bvar.mpr hn, ?_⟩
    rw [show (1 : V) = 0 + 1 by simp, IsSemitermVec.cons_iff]
    exact ⟨ht, by simp⟩

end GodelQ.SeqTranslate
