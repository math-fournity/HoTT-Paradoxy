import GodelQ.ZFC.ShCraigElimSetupQ

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.TranslateShiftCompat GodelQ.ShCraigElimBranches
open GodelQ.ShCraigElimNegFilled

set_option maxHeartbeats 800000

namespace GodelQ.ProbeBF
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **析取分裂**：`Derivable (insert (p ⋎ q) s) → Derivable (insert p (insert q s))`。

在单边 LK 里这是 ∨R 的可逆性：用 `cut (p⋎q)` 配 `neg (p⋎q) = neg p ⋏ neg q`。 -/
lemma split_or {p q s : V} (hp : IsFormula ℒₛₑₜ p) (hq : IsFormula ℒₛₑₜ q)
    (h : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert (p ^⋎ q) s)) :
    Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert p (insert q s)) := by
  refine Derivable.cut (p ^⋎ q) ?_ ?_
  · -- insert (p⋎q) (insert p (insert q s)) ← wk h
    refine Derivable.wk (s := insert (p ^⋎ q) (insert p (insert q s)))
      (s' := insert (p ^⋎ q) s) ?_ ?_ h
    · intro x hx
      simp only [mem_bitInsert_iff] at hx
      rcases hx with rfl | rfl | rfl | hx
      · exact IsSemiformula.or.mpr ⟨hp, hq⟩
      · exact hp
      · exact hq
      · exact h.isFormulaSet x (by simp [hx])
    · intro x hx
      simp only [mem_bitInsert_iff] at hx ⊢
      tauto
  · -- insert (neg (p⋎q)) (insert p (insert q s))
    have hneg : neg ℒₛₑₜ (p ^⋎ q) = neg ℒₛₑₜ p ^⋏ neg ℒₛₑₜ q := neg_or hp.isUFormula hq.isUFormula
    rw [hneg]
    refine Derivable.and_m (s := insert (neg ℒₛₑₜ p ^⋏ neg ℒₛₑₜ q) (insert p (insert q s)))
      (p := neg ℒₛₑₜ p) (q := neg ℒₛₑₜ q) (by simp) ?_ ?_
    · -- and_m 的两个子目标：insert (neg p) T 与 insert (neg q) T
      -- 其中 T := insert (neg p ⋏ neg q) (insert p (insert q s))
      -- 第一个：insert (neg p) T 含 p 与 ¬p → em
      refine Derivable.em (s := insert (neg ℒₛₑₜ p) (insert (neg ℒₛₑₜ p ^⋏ neg ℒₛₑₜ q)
          (insert p (insert q s)))) ?_ p ?_ ?_
      · intro x hx
        simp only [mem_bitInsert_iff] at hx
        rcases hx with rfl | rfl | rfl | rfl | rfl | hx
        · exact hp.neg
        · exact IsSemiformula.and.mpr ⟨hp.neg, hq.neg⟩
        · exact hp
        · exact hq
        · exact IsSemiformula.and.mpr ⟨hp.neg, hq.neg⟩
        · exact h.isFormulaSet x (by simp [hx])
      · simp only [mem_bitInsert_iff]; exact Or.inr (Or.inr (Or.inl rfl))
      · simp only [mem_bitInsert_iff]; exact Or.inl rfl
    · -- 第二个：insert (neg q) T 含 q 与 ¬q → em
      refine Derivable.em (s := insert (neg ℒₛₑₜ q) (insert (neg ℒₛₑₜ p ^⋏ neg ℒₛₑₜ q)
          (insert p (insert q s)))) ?_ q ?_ ?_
      · intro x hx
        simp only [mem_bitInsert_iff] at hx
        rcases hx with rfl | rfl | rfl | rfl | rfl | hx
        · exact hq.neg
        · exact IsSemiformula.and.mpr ⟨hp.neg, hq.neg⟩
        · exact hp
        · exact hq
        · exact IsSemiformula.and.mpr ⟨hp.neg, hq.neg⟩
        · exact h.isFormulaSet x (by simp [hx])
      · simp only [mem_bitInsert_iff]; exact Or.inr (Or.inr (Or.inr (Or.inl rfl)))
      · simp only [mem_bitInsert_iff]; exact Or.inr (Or.inr (Or.inl rfl))

end GodelQ.ProbeBF
