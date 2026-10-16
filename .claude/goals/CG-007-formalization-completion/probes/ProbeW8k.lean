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

lemma isSemiformula_ve0 {m f : V} (hm : 1 ≤ m) :
    IsSemiformula ℒₛₑₜ m (ve0 0 f) := by
  have h1 : IsSemiformula ℒₛₑₜ 1 (ve0 0 f) := by
    rw [ve0, IsSemiformula.imp]
    refine ⟨IsSemiformula.verum, ?_⟩
    exact IsSemiformula.subst (L := ℒₛₑₜ) (n := 1) (m := 1)
      (isSemiformula_cFunc_arity0 f)
      (isSemitermVec_single_bvar (n := 1) (by simp))
  exact isSemiformula_mono h1 hm

lemma isSemiformula_ve2 {n k f w : V} (hk : k ≠ 0)
    (hw0 : IsSemiformula ℒₛₑₜ (n + 1) w.[0]) (hw1 : IsSemiformula ℒₛₑₜ (n + 1) w.[1]) :
    IsSemiformula ℒₛₑₜ (n + 1) (ve2 n k f w) := by
  have hf : IsSemiformula ℒₛₑₜ 3 (cFunc k f) := isSemiformula_cFunc_arity2 hk f
  rw [ve2]
  refine IsSemiformula.qqAlls (n := n + 1) (k := 2) ?_
  have e : ((n + 1) + 2 : V) = 3 + n := by ring
  rw [e]
  rw [IsSemiformula.imp]
  refine ⟨?_, ?_⟩
  · rw [IsSemiformula.and]
    refine ⟨isSemiformula_conjunct (b := 3) (n := n) (i := 0) hw0 (zero_lt_three_add n), ?_⟩
    rw [IsSemiformula.and]
    exact ⟨isSemiformula_conjunct (b := 3) (n := n) (i := 1) hw1 (one_lt_three_add n),
      IsSemiformula.verum⟩
  · apply IsSemiformula.subst (L := ℒₛₑₜ) (n := 3) (m := 3 + n)
    · exact hf
    · rw [show (^#2 ∷ ?[^#0, ^#1] : V) = (^#2 : V) ∷ (^#0 : V) ∷ (^#1 : V) ∷ 0 from rfl]
      rw [show (3 : V) = 2 + 1 by norm_num, IsSemitermVec.cons_iff]
      refine ⟨IsSemiterm.bvar.mpr ?_, ?_⟩
      · simpa [show (3:V) = 2 + 1 by norm_num, add_assoc] using two_lt_three_add n
      · rw [show (2 : V) = 1 + 1 by norm_num, IsSemitermVec.cons_iff]
        refine ⟨IsSemiterm.bvar.mpr ?_, ?_⟩
        · simpa [show (3:V) = 1 + 1 + 1 by norm_num, add_assoc] using zero_lt_three_add n
        · rw [show (1 : V) = 0 + 1 by norm_num, IsSemitermVec.cons_iff]
          exact ⟨IsSemiterm.bvar.mpr (by
            simpa [add_assoc] using one_lt_three_add n), by simp⟩

lemma k_eq_two_of_func {k f : V} (hkf : (ℒₒᵣ).IsFunc k f) (hk : k ≠ 0) : k = 2 := by
  rcases Arithmetic.isFunc_iff_LOR.mp hkf with h | h | h | h
  · exact absurd h.1 hk
  · exact absurd h.1 hk
  · exact h.1
  · exact h.1

-- [2] 主引理
lemma isSemiformula_iVE {n : V} : ∀ t, IsSemiterm ℒₒᵣ n t →
    IsSemiformula ℒₛₑₜ (n + 1) (iVE n t) := by
  apply IsSemiterm.sigma1_induction (L := ℒₒᵣ) (n := n)
    (P := fun t ↦ IsSemiformula ℒₛₑₜ (n + 1) (iVE n t))
  · definability
  · intro z hz
    rw [show iVE n (^#z) = eqAtom (^#(z + 1)) from by simp [iVE, iVE.construction]]
    exact isSemiformula_eqAtom (by simp)
      (IsSemiterm.bvar.mpr (by
        have h' := add_lt_add_right hz 1
        have e : (1 : V) + z = z + 1 := by ring
        have e2 : (1 : V) + n = n + 1 := by ring
        rwa [e, e2] at h'))
  · intro x
    rw [show iVE n (^&x) = eqAtom (^&x) from by simp [iVE, iVE.construction]]
    exact isSemiformula_eqAtom (by simp) (IsSemiterm.fvar (n + 1) x)
  · intro k f v hkf hv ih
    rw [show iVE n (^func k f v) =
        (if k = 0 then ve0 k f
          else ve2 n k f (iVE.construction.resultVec ℒₒᵣ ![n] k v)) from by
      rw [iVE, iVE.construction.result_func' hkf hv.isUTerm]; rfl]
    split
    · rename_i hk0
      subst hk0
      exact isSemiformula_ve0 (by simp)
    · rename_i hk0
      have hk2 := k_eq_two_of_func hkf hk0
      subst hk2
      apply isSemiformula_ve2 hk0
      · have h0 : (iVE.construction.resultVec ℒₒᵣ ![n] 2 v).[0] = iVE n v.[0] := by
          rw [iVE.construction.nth_resultVec ℒₒᵣ ![n] hv.isUTerm (by simp)]
          simp [iVE]
        rw [h0]
        exact ih 0 (by simp [hv.isUTerm])
      · have h1 : (iVE.construction.resultVec ℒₒᵣ ![n] 2 v).[1] = iVE n v.[1] := by
          rw [iVE.construction.nth_resultVec ℒₒᵣ ![n] hv.isUTerm (by simp)]
          simp [iVE]
        rw [h1]
        exact ih 1 (by simp [hv.isUTerm])

end GodelQ.SeqTranslate
