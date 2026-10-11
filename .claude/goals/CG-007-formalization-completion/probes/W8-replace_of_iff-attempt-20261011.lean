import GodelQ.ZFC.ShCraigElimSetupQ

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.TranslateShiftCompat GodelQ.ShCraigElimBranches

set_option maxHeartbeats 800000

namespace GodelQ.ProbeBD
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 完整证法（用 A ↔ B 做两次 cut）：
--   有 hAB : Derivable (insert (imp A B) ∅)   （A → B）
--      hBA : Derivable (insert (imp B A) ∅)   （B → A）
--   Derivable (insert A S) ⟹ Derivable (insert B S)
--
-- 证：
--   cut A 于 (insert B S)
--     (i) insert A (insert B S) ← wk ih ✅
--     (ii) insert (neg A) (insert B S)
--   对 (ii)：用 B → A（= ¬B ⋎ A）
--     在 sequent 里加 ¬B ⋎ A（wk），or_m 给
--       insert (neg B) (insert A (insert (neg A) (insert B S)))
--     它含 A 与 ¬A → axL ✅

lemma replace_of_iff {A B S : V}
    (hAB : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert (imp ℒₛₑₜ A B) ∅))
    (hBA : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert (imp ℒₛₑₜ B A) ∅))
    (hd : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert A S)) :
    Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert B S) := by
  have hA : IsFormula ℒₛₑₜ A := hd.isFormulaSet A (by simp)
  have hS : IsFormulaSet (L := ℒₛₑₜ) S := fun x hx ↦ hd.isFormulaSet x (by simp [hx])
  have hB : IsFormula ℒₛₑₜ B := by
    have := hBA.isFormulaSet (imp ℒₛₑₜ B A) (by simp)
    exact (IsSemiformula.imp.mp this).1
  -- cut A
  refine Derivable.cut A ?_ ?_
  · -- (i) insert A (insert B S) ← wk hd
    refine Derivable.wk ?_ ?_ hd
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
    -- 先把 hBA 的 sequent 弱化进目标，再用 or_m
    -- 目标：Derivable (insert (neg A) (insert B S))
    -- hBA 给 Derivable (insert (neg B ⋎ A) ∅) = Derivable (insert (imp B A) ∅)
    -- 用 wk 把它搬进目标 sequent
    have hBA' : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖
        (insert (neg ℒₛₑₜ B ^⋎ A) (insert (neg ℒₛₑₜ A) (insert B S))) :=
      Derivable.wk (s := insert (neg ℒₛₑₜ B ^⋎ A) (insert (neg ℒₛₑₜ A) (insert B S)))
        (s' := insert (imp ℒₛₑₜ B A) ∅) (by
          intro x hx
          simp only [mem_bitInsert_iff, mem_empty_iff] at hx
          rcases hx with rfl | hx
          · rfl
          · exact absurd hx (by simp))
        (by simpa [imp] using hBA)
    refine Derivable.or_m (s := insert (neg ℒₛₑₜ A) (insert B S))
      (p := neg ℒₛₑₜ B) (q := A) (by simp) ?_
    -- insert (neg B) (insert A (insert (neg A) (insert B S)))
    -- 含 A 与 ¬A → axL
    refine Derivable.em ?_ A (by simp) (by simp)

end GodelQ.ProbeBD
