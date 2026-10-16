import GodelQ.ZFC.SeqTranslateFormula

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.SeqTranslate

open GodelQ.Translate GodelQ.ZFCArith

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

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

-- ve2 公式性
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
      · have h := two_lt_three_add n
        have e : (2:V) < 2 + 1 + n := by simpa [show (3:V) = 2 + 1 by norm_num, add_assoc] using h
        rwa [show (2 : V) + 1 + n = 2 + 1 + n from rfl]
      · rw [show (2 : V) = 1 + 1 by norm_num, IsSemitermVec.cons_iff]
        refine ⟨IsSemiterm.bvar.mpr ?_, ?_⟩
        · have h := zero_lt_three_add n
          have e : (0:V) < 1 + 1 + n := by simpa [show (3:V) = 1 + 1 + 1 by norm_num, add_assoc] using h
          simpa using e
        · rw [show (1 : V) = 0 + 1 by norm_num, IsSemitermVec.cons_iff]
          exact ⟨IsSemiterm.bvar.mpr (by
            have h := one_lt_three_add n
            have e : (1:V) < 1 + 1 + 1 + n := by simpa [add_assoc] using h
            simpa using e), by simp⟩

end GodelQ.SeqTranslate
