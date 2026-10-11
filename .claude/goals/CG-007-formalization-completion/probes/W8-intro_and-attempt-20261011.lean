import GodelQ.ZFC.ProbeBG

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.TranslateShiftCompat GodelQ.ShCraigElimBranches
open GodelQ.ShCraigElimNegFilled GodelQ.ProbeBG

set_option maxHeartbeats 800000

namespace GodelQ.ProbeBH
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- 对偶：`and` 的引入（从 `insert p (insert q s)` 得 `insert (p ⋏ q) s`）。 -/
lemma intro_and {p q s : V} (hp : IsFormula ℒₛₑₜ p) (hq : IsFormula ℒₛₑₜ q)
    (h : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert p (insert q s))) :
    Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert (p ^⋏ q) s) := by
  have hpq : IsFormula ℒₛₑₜ (p ^⋏ q) := IsSemiformula.and.mpr ⟨hp, hq⟩
  -- 关键：用 em 引入 (p⋏q) 与它的否定，两次 or_m 消去否定支
  -- 目标 sequent S₀ := insert (p⋏q) s
  -- cut (p⋏q)：
  --   (i) insert (p⋏q) (insert (neg (p⋏q)) S₀) ← em
  --   (ii) insert (neg (p⋏q)) S₀ = insert (neg p ⋎ neg q) S₀ ← 从 h 弱化
  refine Derivable.cut (p ^⋏ q) ?_ ?_
  · refine Derivable.em (s := insert (p ^⋏ q) (insert (neg ℒₛₑₜ (p ^⋏ q)) s)) ?_ (p ^⋏ q) ?_ ?_
    · intro y hy
      simp only [mem_bitInsert_iff] at hy
      rcases hy with rfl | rfl | hy
      · exact hpq
      · exact hpq.neg
      · exact h.isFormulaSet y (by simp [hy])
    · simp [mem_bitInsert_iff]
    · simp [mem_bitInsert_iff]
  · -- insert (neg (p⋏q)) s，用 neg_and 与 or_m
    rw [neg_and hp.isUFormula hq.isUFormula]
    -- insert (neg p ⋎ neg q) s ← 从 h 弱化（h 的 sequent 更大）
    refine Derivable.wk (s := insert (neg ℒₛₑₜ p ^⋎ neg ℒₛₑₜ q) s)
      (s' := insert p (insert q s)) ?_ ?_ h
    · intro y hy
      simp only [mem_bitInsert_iff] at hy
      rcases hy with rfl | rfl | hy
      · exact hp
      · exact hq
      · exact h.isFormulaSet y (by simp [hy])
    · intro y hy
      simp only [mem_bitInsert_iff] at hy ⊢
      -- h 的 sequent 是 insert p (insert q s)，目标是 insert (neg p ⋎ neg q) s
      -- 这两个集合无关！wk 方向错了。
      tauto

end GodelQ.ProbeBH
