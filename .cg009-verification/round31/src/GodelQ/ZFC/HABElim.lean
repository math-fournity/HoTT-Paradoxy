-- CG-009: **hAB 已消去** —— `HAllProof.hAll_uncond` 的最后前提。
--
-- `hAB` 是 `Derivable (neg A ⋎ B) (∅ : V)`，其中
--   A := iT 0 (free ℒₒᵣ p)
--   B := free ℒₛₑₜ (imp domZero (iT 1 p))
--
-- ## 关键等式（两条）
--
-- 1. `A = subst ?[^&0] (iT 1 (shift ℒₒᵣ p))`  —— `HABKey.iT_free_eq`（= 开口律 m=0 实例）
-- 2. `free ℒₛₑₜ (iT 1 p) = subst ?[^&0] (iT 1 (shift ℒₒᵣ p))`  —— `iT_shift` + `free` 展开
--    于是 `B = imp (subst ?[^&0] domZero) A`（`free_imp_domZero`）
--
-- ## 结论
--
-- `neg A ⋎ B = imp A B = imp A (imp C A)`，其中 `C := subst ?[^&0] domZero`。
-- `¬A ⋎ (¬C ⋎ A)` 是命题重言式，故可导：
--     Derivable.or  : insert (¬A ⋎ (¬C ⋎ A)) (∅ : V)   ← insert (¬A) (insert (¬C ⋎ A) (∅ : V))
--     Derivable.or  : insert (¬A) (insert (¬C ⋎ A) (∅ : V))
--                      ← insert (¬A) (insert (¬C) (insert A (∅ : V)))
--     Derivable.em  : insert (¬A) (insert (¬C) (insert A (∅ : V))   （`¬A` 与 `A` 同时在场）
import GodelQ.ZFC.HABKey

open FFL FFL.FirstOrder FFL FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate
open GodelQ.HABKey GodelQ.TranslateShiftCompat

namespace GodelQ.HABElim
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- `insert_iff` 的三分流（(∅ : V) 情形只可能命中两处）。 -/
lemma mem_insert_empty {p x : V} (hp : x = p) : x ∈ (insert p ((∅ : V) : V)) := by
  simp [hp]

/-- `free (iT 1 p)` 的展开：`shift` 相容律 + `free` 定义。 -/
lemma free_iT (p : V) (hp : IsSemiformula ℒₒᵣ 1 p) :
    free ℒₛₑₜ (iT (1 : V) p) = iT (0 : V) (free (L := ℒₒᵣ) p) := by
  have hs : free ℒₛₑₜ (iT (1 : V) p)
      = subst ℒₛₑₜ ?[^&0] (iT (1 : V) (shift (L := ℒₒᵣ) p)) := by
    show substs1 ℒₛₑₜ (^&0) (shift ℒₛₑₜ (iT (1 : V) p)) = _
    rw [show (substs1 ℒₛₑₜ (^&0) : V → V) = subst ℒₛₑₜ (?[^&0] : V) from rfl]
    rw [show shift ℒₛₑₜ (iT (1 : V) p) = iT (1 : V) (shift (L := ℒₒᵣ) p) from
      (iT_shift (n := 1) p hp).symm]
  have hf : iT (0 : V) (free (L := ℒₒᵣ) p)
      = subst ℒₛₑₜ ?[^&0] (iT (1 : V) (shift (L := ℒₒᵣ) p)) :=
    iT_free_eq p hp
  rw [hs, hf]

/-- **`hAB` 可导**：`¬A ⋎ B` 在 ZFC 里空 sequent 可导（命题重言式）。 -/
theorem hAB_derivable (p : V) (hp : IsSemiformula ℒₒᵣ 1 p) :
    Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖
      (insert (neg ℒₛₑₜ (iT (0 : V) (free (L := ℒₒᵣ) p))
        ^⋎ free ℒₛₑₜ (imp ℒₛₑₜ (domZero (V := V)) (iT (1 : V) p))) (∅ : V)) := by
  -- 命名
  set A : V := iT (0 : V) (free (L := ℒₒᵣ) p)
  set C : V := subst ℒₛₑₜ (?[^&0] : V) (domZero (V := V))
  -- B = imp C A
  have hB : free ℒₛₑₜ (imp ℒₛₑₜ (domZero (V := V)) (iT (1 : V) p))
      = imp ℒₛₑₜ C A := by
    have h1 := free_imp_domZero (X := iT (1 : V) p)
      (isSemiformula_iT p hp)
    rw [free_iT p hp] at h1
    -- h1 : imp (subst ?[^&0] domZero) (free (iT 1 p)) = imp (subst ?[^&0] domZero) A
    exact h1
  -- 目标 = insert (neg A ⋎ (neg C ⋎ A)) (∅ : V)
  rw [hB]
  show Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖
    (insert (neg ℒₛₑₜ A ^⋎ neg ℒₛₑₜ C ^⋎ A) ((∅ : V) : V))
  -- imp 展开：neg A ⋎ (neg C ⋎ A) 已是 ⋎ 形式（imp p q = neg p ⋎ q）
  -- 公式性
  have hA : IsFormula ℒₛₑₜ A := by
    have h := isSemiformula_iT (free (L := ℒₒᵣ) p) (IsSemiformula.free hp)
    exact ⟨h.isUFormula, by simpa using h.bv_le⟩
  have hC : IsFormula ℒₛₑₜ C := by
    exact (IsSemiformula.subst (L := ℒₛₑₜ)
      GodelQ.TranslateShiftCompat.isSemiformula_domZero'
      ((IsSemitermVec.singleton (L := ℒₛₑₜ) (n := (0 : V))).mpr
        (IsSemiterm.fvar (L := ℒₛₑₜ) (0 : V) 0)))
  -- 三层 insert 是公式集（`rcases rfl` 的首支给 `y = neg C`，次支给 `y = A`）
  have hfs3 : IsFormulaSet (L := ℒₛₑₜ) (insert (neg ℒₛₑₜ C) (insert A (∅ : V))) := by
    have hAn : IsFormula ℒₛₑₜ (neg ℒₛₑₜ A) := IsSemiformula.neg hA
    have hCn : IsFormula ℒₛₑₜ (neg ℒₛₑₜ C) := IsSemiformula.neg hC
    intro y hy
    simp only [mem_bitInsert_iff] at hy
    rcases hy with rfl | rfl | hy
    · exact hCn
    · exact hA
    · exact absurd hy (by simp)
  -- `^⋎` 的优先级 `p:68 " ^⋎ " q:69` ⟹ **左结合**：
  --   `¬A ⋎ ¬C ⋎ A` 解析成 `(¬A ⋎ ¬C) ⋎ A`。
  -- 于是构造路线（自底向上）：
  --   ① em       : insert (¬A) (insert (¬C) (insert A ∅))
  --   ② or       : insert (¬C) (insert A ∅)          —— 合并最内两层的 ¬C 与 A
  --   ③ exchange : insert (¬A ⋎ ¬C) (insert A ∅)      —— 合并最外两层的 ¬A 与 (¬C ⋎ A)
  -- `^⋎` 优先级是 `p:68 " ^⋎ " q:69` ⟹ **左结合**：
  --   `¬A ⋎ ¬C ⋎ A` 解析成 `(¬A ⋎ ¬C) ⋎ A`。
  -- 路线（自底向上）：
  --   ① em       : insert (¬A) (insert (¬C) (insert A ∅))
  --   ② or       : insert (¬C) (insert (¬A) (insert (¬C ⋎ A) ∅))
  -- `^⋎` 右结合（definitional）。`Derivable.or` **只合并最前两个** insertion，
  -- 但 `s` 可显式指定。路线：
  --   ① em       : ¬C ⫽ ¬A ⫽ A ⫽ ∅          （A 与 ¬A 同时在，矛盾）
  --   ② or(s:=¬A): ¬A ⫽ (¬C ⋎ A) ⫽ ∅          （合并前两件 ¬C、A，余 ¬A）
  --   ③ exchange : (¬C ⋎ A) ⫽ ¬A ⫽ ∅ → ¬A ⫽ (¬C ⋎ A) ⫽ ∅
  --   ④ or(s:=∅) : (¬A ⋎ (¬C ⋎ A)) ⫽ ∅         ← 目标
  have h0 : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖
      (insert (neg ℒₛₑₜ C) (insert A (insert (neg ℒₛₑₜ A) (∅ : V)))) := by
    have hfs0 : IsFormulaSet (L := ℒₛₑₜ)
        (insert (neg ℒₛₑₜ C) (insert A (insert (neg ℒₛₑₜ A) (∅ : V)))) := by
      intro y hy
      simp only [mem_bitInsert_iff] at hy
      rcases hy with rfl | rfl | rfl | hy
      · exact IsSemiformula.neg hC
      · exact hA
      · exact IsSemiformula.neg hA
      · exact absurd hy (by simp)
    exact Derivable.em (V := V) (T := 𝗭𝗙𝗖) hfs0 A (by simp) (by simp)
  -- ② or：合并最前两件 (¬C) 与 (A)，余下 ¬A 留在 s 里
  have h1 : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖
      (insert (neg ℒₛₑₜ C ^⋎ A) (insert (neg ℒₛₑₜ A) (∅ : V))) :=
    Derivable.or (V := V) (T := 𝗭𝗙𝗖) (s := insert (neg ℒₛₑₜ A) (∅ : V))
      (p := neg ℒₛₑₜ C) (q := A) (hpq := h0)
  -- ③ exchange：¬A 与 (¬C ⋎ A) 换位
  have h2 : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖
      (insert (neg ℒₛₑₜ A) (insert (neg ℒₛₑₜ C ^⋎ A) (∅ : V))) :=
    Derivable.exchange (V := V) (T := 𝗭𝗙𝗖) (p := (neg ℒₛₑₜ C ^⋎ A))
      (q := neg ℒₛₑₜ A) (s := (∅ : V)) h1
  -- ④ or：合并 ¬A 与 (¬C ⋎ A) 得目标
  exact Derivable.or (V := V) (T := 𝗭𝗙𝗖) (s := (∅ : V))
    (p := neg ℒₛₑₜ A) (q := (neg ℒₛₑₜ C ^⋎ A)) (hpq := h2)

end GodelQ.HABElim

#print axioms GodelQ.HABElim.hAB_derivable
