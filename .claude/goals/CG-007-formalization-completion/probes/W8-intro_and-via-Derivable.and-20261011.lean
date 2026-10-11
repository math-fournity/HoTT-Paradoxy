import GodelQ.ZFC.ShCraigElimSetupQ

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.TranslateShiftCompat GodelQ.ShCraigElimBranches
open GodelQ.ShCraigElimNegFilled GodelQ.ShCraigElimSetupQ

set_option maxHeartbeats 800000

namespace GodelQ.ProbeBI
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- intro_and 的对偶证法（照 split_or 的写法）：
-- 目标：Derivable (insert (p⋏q) s)，给定 Derivable (insert p (insert q s))
-- cut (p⋏q)：
--   (i) insert (p⋏q) (insert (neg (p⋏q)) s) ← em
--   (ii) insert (neg (p⋏q)) s ← 从 h 弱化？
-- 但 h 的 sequent 是 insert p (insert q s)，与 insert (neg (p⋏q)) s 无关。
--
-- **正确方向**：h 的 sequent 含 p 与 q，目标 sequent 含 p⋏q。
-- 两者由「p 与 q 都在 ⟹ p⋏q 可用」联系，即 **and_m 的反向**。
-- 实际上这正是 `Derivable.and`（Foundation 已备）：
--   Derivable.and : Derivable (insert p s) → Derivable (insert q s) → Derivable (insert (p ⋏ q) s)
-- 而 h : Derivable (insert p (insert q s))。
-- 需要：Derivable (insert p (insert (p⋏q) s)) 与 Derivable (insert q (insert (p⋏q) s))。
-- 这两个都从 h 用 **wk** 得到（把 p⋏q 加进 sequent）：
--   insert p (insert q s) ⊆ insert p (insert (p⋏q) s) ✅
--   insert p (insert q s) ⊆ insert q (insert (p⋏q) s) ✅
-- 这就是正解！

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
  refine Derivable.and (T := 𝗭𝗙𝗖) (L := ℒₛₑₜ) (p := p) (q := q) (s := s) ?_ ?_
  · -- insert p (insert (p⋏q) s)
    refine Derivable.wk (T := 𝗭𝗙𝗖) (L := ℒₛₑₜ) (s := insert p (insert (p ^⋏ q) s))
      (s' := insert p (insert q s)) ?_ ?_ h
    · intro y hy
      simp only [mem_bitInsert_iff] at hy
      rcases hy with rfl | rfl | hy
      · exact hp
      · exact hpq
      · exact hfs y (by simp [hy])
    · intro y hy
      simp only [mem_bitInsert_iff] at hy ⊢
      tauto
  · -- insert q (insert (p⋏q) s)
    refine Derivable.wk (T := 𝗭𝗙𝗖) (L := ℒₛₑₜ) (s := insert q (insert (p ^⋏ q) s))
      (s' := insert p (insert q s)) ?_ ?_ h
    · intro y hy
      simp only [mem_bitInsert_iff] at hy
      rcases hy with rfl | rfl | hy
      · exact hq
      · exact hpq
      · exact hfs y (by simp [hy])
    · intro y hy
      simp only [mem_bitInsert_iff] at hy ⊢
      tauto

end GodelQ.ProbeBI
