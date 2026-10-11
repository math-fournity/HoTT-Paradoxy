import GodelQ.ZFC.SeqTranslateFormula

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.SeqTranslate

open GodelQ.Translate GodelQ.ZFCArith

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

instance iVE_definable : 𝚺ᴬ₁-Function₂ (iVE : V → V → V) := iVE_defined.to_definable
instance iVE_definable' (Γ m) : Γᴬ_[m + 1]-Function₂[V] iVE := iVE_definable.of_sigmaOne

lemma isSemiformula_mono {n m p : V} (h : IsSemiformula ℒₛₑₜ n p) (hnm : n ≤ m) :
    IsSemiformula ℒₛₑₜ m p := ⟨h.isUFormula, le_trans h.bv_le hnm⟩

lemma isSemiformula_eqAtom {n t : V} (hn : 0 < n) (ht : IsSemiterm ℒₛₑₜ n t) :
    IsSemiformula ℒₛₑₜ n (eqAtom t) := by
  rw [eqAtom, IsSemiformula.rel]
  refine ⟨?_, ?_⟩
  · rw [cEqN]; exact codeIn_rel_quote _
  · rw [show (?[^#0, t] : V) = (^#0 : V) ∷ (t ∷ 0) from rfl]
    rw [show (2 : V) = 1 + 1 by norm_num, IsSemitermVec.cons_iff]
    refine ⟨IsSemiterm.bvar.mpr hn, ?_⟩
    rw [show (1 : V) = 0 + 1 by norm_num, IsSemitermVec.cons_iff]
    exact ⟨ht, by simp⟩

lemma zero_lt_three_add (n : V) : (0:V) < 3 + n := by
  have h := lt_add_self_add_one (0 : V) (n + 2)
  have e : n + 2 + 0 + 1 = 3 + n := by ring
  rwa [e] at h

lemma one_lt_three_add (n : V) : (1:V) < 3 + n := by
  have h := lt_add_self_add_one (1 : V) (n + 1)
  have e : n + 1 + 1 + 1 = 3 + n := by ring
  rwa [e] at h

lemma two_lt_three_add (n : V) : (2:V) < 3 + n := by
  have h := lt_add_self_add_one (2 : V) n
  have e : n + 2 + 1 = 3 + n := by ring
  rwa [e] at h

-- ve0 公式性（k = 0，层数 m ≥ 1）
lemma isSemiformula_ve0 {m k f : V} (hk : k = 0) (hm : 1 ≤ m) :
    IsSemiformula ℒₛₑₜ m (ve0 k f) := by
  subst hk
  have h1 : IsSemiformula ℒₛₑₜ 1 (ve0 0 f) := by
    rw [ve0, IsSemiformula.imp]
    refine ⟨IsSemiformula.verum, ?_⟩
    exact IsSemiformula.subst (L := ℒₛₑₜ) (n := 1) (m := 1)
      (isSemiformula_cFunc_arity0 f)
      (isSemitermVec_single_bvar (n := 1) (by simp))
  exact isSemiformula_mono h1 hm

end GodelQ.SeqTranslate
