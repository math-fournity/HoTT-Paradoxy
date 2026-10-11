import GodelQ.ZFC.ShCraigElimSetupQ

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.TranslateShiftCompat GodelQ.ShCraigElimBranches

set_option maxHeartbeats 800000

namespace GodelQ.ProbeBE
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **替换引理**：若 `A ↔ B` 都可导，则 `insert A S` 与 `insert B S` 互相可导（单向）。 -/
lemma replace_of_iff {A B S : V}
    (hAB : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert (imp ℒₛₑₜ A B) ∅))
    (hBA : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert (imp ℒₛₑₜ B A) ∅))
    (hd : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert A S)) :
    Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert B S) := by
  have hA : IsFormula ℒₛₑₜ A := hd.isFormulaSet A (by simp)
  have hS : IsFormulaSet (L := ℒₛₑₜ) S := fun x hx ↦ hd.isFormulaSet x (by simp [hx])
  have hB : IsFormula ℒₛₑₜ B := by
    have h := hBA.isFormulaSet (imp ℒₛₑₜ B A) (by simp)
    exact (IsSemiformula.imp.mp h).1
  -- cut A
  refine Derivable.cut A ?_ ?_
  · -- (i) insert A (insert B S) ← wk hd
    refine Derivable.wk (s := insert A (insert B S)) (s' := insert A S) ?_ ?_ hd
    · intro x hx
      simp only [mem_bitInsert_iff] at hx
      rcases hx with rfl | rfl | hx
      · exact hA
      · exact hB
      · exact hS x hx
    · intro x hx
      simp only [mem_bitInsert_iff] at hx ⊢
      tauto
  · -- (ii) insert (neg A) (insert B S)
    -- 用 hBA（imp B A = neg B ⋎ A）
    have hBA' : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖
        (insert (neg ℒₛₑₜ B ^⋎ A) (insert (neg ℒₛₑₜ A) (insert B S))) := by
      refine Derivable.wk (s := insert (neg ℒₛₑₜ B ^⋎ A) (insert (neg ℒₛₑₜ A) (insert B S)))
        (s' := insert (imp ℒₛₑₜ B A) ∅) ?_ ?_ hBA
      · intro x hx
        simp only [mem_bitInsert_iff] at hx
        rcases hx with rfl | rfl | rfl | rfl | hx
        · exact IsSemiformula.or.mpr ⟨hB.neg, hA⟩
        · exact hA.neg
        · exact hB
        · exact hS x hx
        · exact absurd hx (by simp)
      · intro x hx
        simp only [mem_bitInsert_iff] at hx ⊢
        rcases hx with rfl | hx
        · right; left; rfl
        · exact absurd hx (by simp)
    -- or_m 于 (neg B ⋎ A)，注意 s 必须是**含它**的 sequent
    refine Derivable.or_m (s := insert (neg ℒₛₑₜ B ^⋎ A) (insert (neg ℒₛₑₜ A) (insert B S)))
      (p := neg ℒₛₑₜ B) (q := A) (by simp) ?_
    -- 但结论要的是 Derivable (insert (neg A) (insert B S))——用 ofSetEq 收窄
    -- 目标：Derivable (insert (neg B) (insert A (insert (neg A) (insert B S))))
    -- 含 A 与 ¬A → em
    refine Derivable.em ?_ A (by simp) (by simp)
    intro x hx
    simp only [mem_bitInsert_iff] at hx
    rcases hx with rfl | rfl | rfl | rfl | hx
    · exact hB.neg
    · exact hA
    · exact hA.neg
    · exact hB
    · exact hS x hx

end GodelQ.ProbeBE
