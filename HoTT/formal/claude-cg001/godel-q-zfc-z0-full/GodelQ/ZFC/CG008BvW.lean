import GodelQ.ZFC.CG008BvZ

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008BvW
open GodelQ.ZFCArith GodelQ.Translate
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 关键：`listMax` 的 `adjoin` 律，避免任何 `nth`
example (x y z : V) (hx : x ≤ z) (hy : y ≤ z) :
    Arithmetic.listMax (Adjoin.adjoin x (Adjoin.adjoin y (0 : V))) ≤ z := by
  rw [Arithmetic.listMax_adjoin, Arithmetic.listMax_adjoin, Arithmetic.listMax_nil]
  -- `max x (max y 0) ≤ z`
  rw [max_le_iff]
  refine ⟨hx, ?_⟩
  rw [max_le_iff]
  exact ⟨hy, by positivity⟩

/-- **`listMax` 的分量界**（`bv_eqAtom_le` 的最后一步）。

**关键**：用 `listMax_adjoin` 直接算，**完全不碰 `nth`**，
绕开 `?[...]` 宏与 `nth` 下标带来的 `Zero ?m`。 -/
theorem listMax_vec₂_le {x y z : V} (hx : x ≤ z) (hy : y ≤ z) :
    Arithmetic.listMax (Adjoin.adjoin x (Adjoin.adjoin y (0 : V))) ≤ z := by
  rw [Arithmetic.listMax_adjoin, Arithmetic.listMax_adjoin, Arithmetic.listMax_nil]
  rw [max_le_iff]
  refine ⟨hx, ?_⟩
  rw [max_le_iff]
  exact ⟨hy, by positivity⟩

-- **`bv_eqAtom_le` 的组装未过**。三步零件都在：
-- ① `bv_rel`（`IsRel` 由 `isRel_quote_quote`，已过）；
-- ② `termBVVec_eqAtom`（`CG008BvZ`，已证）；
-- ③ `listMax_vec₂_le`（本文件，已证）。
-- **卡点**：组装时 `Translate.eqAtom` 展开出的**向量记法**（`?[...]` 或 `∷`）
-- 在 `termBVVec_cons` 的**隐式参数**位置再次触发 `Zero ?m`——
-- 该引理的 `k`/`t`/`ts` 是隐式的，Lean 要从记法推出的类型里找 `Zero`。
-- **下一步**：把 `termBVVec_cons` 的 `k`、`t`、`ts` **全部显式**给出
-- （本文件已试 `(k := …)` 单独给，仍歧义；需连 `t`、`ts` 一并给），
-- 或先在 `Adjoin.adjoin` 形式下证一条 `termBVVec_two` 辅助引理，
-- 让组装处只调用它、不再展开 `termBVVec_cons`。

end GodelQ.CG008BvW

#print axioms GodelQ.CG008BvW.listMax_vec₂_le
