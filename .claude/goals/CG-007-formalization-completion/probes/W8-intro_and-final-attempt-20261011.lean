import GodelQ.ZFC.ShCraigElimSetupQ

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.TranslateShiftCompat GodelQ.ShCraigElimBranches
open GodelQ.ShCraigElimNegFilled GodelQ.ShCraigElimSetupQ

set_option maxHeartbeats 800000

namespace GodelQ.ProbeBJ
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- `Derivable.and` 的 s 参数就是「除 p、q 外的余部」，
故要得 `insert (p⋏q) s`，需先有 `insert p s` 与 `insert q s`。
而 `h : insert p (insert q s)` 正好可经 `ofSetEq` 变成 `insert p (insert q s)`——
注意 `insert p (insert q s) ≠ insert p s`。 -/
lemma intro_and {p q s : V} (hp : IsFormula ℒₛₑₜ p) (hq : IsFormula ℒₛₑₜ q)
    (h : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert p (insert q s))) :
    Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert (p ^⋏ q) s) := by
  have hpq : IsFormula ℒₛₑₜ (p ^⋏ q) := IsSemiformula.and.mpr ⟨hp, hq⟩
  have hfs : IsFormulaSet (L := ℒₛₑₜ) (insert p (insert q s)) := by
    intro y hy
    simp only [mem_bitInsert_iff] at hy
    rcases hy with rfl | rfl | hy
    · exact hp
    · exact hq
    · exact h.isFormulaSet y (by simp [hy])
  -- 目标 insert (p⋏q) s；用 and_m（s := s）需要 insert p s 与 insert q s
  -- 从 h 经 wk 到更大的 sequent 再 ofSetEq 收缩？不行。
  -- 正确：用 Derivable.and 的 s := insert (p⋏q) s 形式，即
  --   Derivable (insert p (insert (p⋏q) s)) 与 Derivable (insert q (insert (p⋏q) s))
  -- 这两个从 h 用 wk（子集方向对）：
  --   insert p (insert q s) ⊆ insert p (insert (p⋏q) s)  ✅
  --   insert p (insert q s) ⊆ insert q (insert (p⋏q) s)  ✅
  -- 然后 and 给 insert (p⋏q) (insert (p⋏q) s) = insert (p⋏q) s ✅
  have h1 : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert p (insert (p ^⋏ q) s)) := by
    refine Derivable.wk (T := 𝗭𝗙𝗖) (L := ℒₛₑₜ)
      (s := insert p (insert (p ^⋏ q) s)) (s' := insert p (insert q s)) ?_ ?_ h
    · intro y hy
      simp only [mem_bitInsert_iff] at hy
      rcases hy with rfl | rfl | hy
      · exact hp
      · exact hpq
      · exact hfs y (by simp [hy])
    · intro y hy
      simp only [mem_bitInsert_iff] at hy ⊢
      simp_all only [or_false]
  have h2 : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert q (insert (p ^⋏ q) s)) := by
    refine Derivable.wk (T := 𝗭𝗙𝗖) (L := ℒₛₑₜ)
      (s := insert q (insert (p ^⋏ q) s)) (s' := insert p (insert q s)) ?_ ?_ h
    · intro y hy
      simp only [mem_bitInsert_iff] at hy
      rcases hy with rfl | rfl | hy
      · exact hq
      · exact hpq
      · exact hfs y (by simp [hy])
    · intro y hy
      simp only [mem_bitInsert_iff] at hy ⊢
      simp_all only [or_false]
  -- and 给 insert (p⋏q) (insert (p⋏q) s)
  have h3 := Derivable.and (T := 𝗭𝗙𝗖) (L := ℒₛₑₜ) (p := p) (q := q)
    (s := insert (p ^⋏ q) s) h1 h2
  -- insert (p⋏q) (insert (p⋏q) s) = insert (p⋏q) s
  refine Derivable.ofSetEq (s := insert (p ^⋏ q) s)
    (s' := insert (p ^⋏ q) (insert (p ^⋏ q) s)) ?_ h3
  intro y
  simp only [mem_bitInsert_iff]
  tauto

end GodelQ.ProbeBJ
