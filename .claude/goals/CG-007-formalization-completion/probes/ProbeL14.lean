import GodelQ.ZFC.SeqTranslateFormula

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.SeqTranslate

open GodelQ.Translate GodelQ.ZFCArith

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

instance shiftVec_definable : 𝚺ᴬ₁-Function₂ (shiftVec : V → V → V) := shiftVec_defined.to_definable

instance shiftVec_definable' (Γ m) : Γᴬ_[m + 1]-Function₂[V] shiftVec :=
  shiftVec_definable.of_sigmaOne

lemma isSemitermVec_shiftVec_V (b : V) : ∀ n : V,
    IsSemitermVec ℒₛₑₜ n (b + n) (shiftVec b n) := by
  intro n
  induction n using ISigma1.sigma1_succ_induction
  · definability
  case zero => simp
  case succ n ih =>
    rw [shiftVec_succ, IsSemitermVec.cons_iff]
    refine ⟨?_, ?_⟩
    · rw [IsSemiterm.bvar]
      calc b < n + b + 1 := lt_add_self_add_one b n
        _ = b + (n + 1) := by ring
    · have h := IsSemitermVec.termBShiftVec (L := ℒₛₑₜ) ih
      simpa only [add_assoc] using h

lemma isSemiformula_conjunct {b n i y : V} (hy : IsSemiformula ℒₛₑₜ (n + 1) y)
    (hi : i < b + n) : IsSemiformula ℒₛₑₜ (b + n) (conjunct b n i y) := by
  rw [conjunct, IsSemiformula.and]
  refine ⟨?_, ?_⟩
  · exact IsSemiformula.subst (L := ℒₛₑₜ) isSemiformula_cDomN
      (isSemitermVec_single_bvar (n := b + n) hi)
  · refine IsSemiformula.subst (L := ℒₛₑₜ) hy ?_
    rw [IsSemitermVec.cons_iff]
    exact ⟨IsSemiterm.bvar.mpr hi, isSemitermVec_shiftVec_V b n⟩

end GodelQ.SeqTranslate
