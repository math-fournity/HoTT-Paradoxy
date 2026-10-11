import GodelQ.ZFC.ShCraigElimBranches

namespace GodelQ.ShCraigElimTest

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- hAnd attempt using Derivable.and_m
lemma hAnd_test {s p q dp dq : V} (hs : IsFormulaSet (L := ℒₒᵣ) s)
    (hpq : p ^⋏ q ∈ s) (ihp : Q dp) (ihq : Q dq) : Q (andIntro s p q dp dq) := by
  simp only [Q, fstIdx_andIntro]
  have hpU : IsUFormula ℒₒᵣ p := (hs p hpq).isUFormula.and.left
  have hqU : IsUFormula ℒₒᵣ q := (hs p hpq).isUFormula.and.right
  have hmem : iT (0 : V) (p ^⋏ q) ∈ translateSeq s :=
    mem_translateSeq_iff.mpr ⟨p ^⋏ q, hpq, rfl⟩
  rw [iT_and hpU hqU] at hmem
  exact Derivable.and_m (by exact hmem) ihp ihq

end GodelQ.ShCraigElimTest
