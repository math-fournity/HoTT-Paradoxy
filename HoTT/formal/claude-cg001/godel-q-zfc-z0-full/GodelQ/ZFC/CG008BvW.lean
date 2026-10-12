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

/-- **`termBVVec` 在二元向量上的取值**（显式 `Adjoin.adjoin` 形式，组装处只调它）。 -/
theorem termBVVec_two (x y : V) (hx : Bootstrapping.IsUTerm ℒₛₑₜ x)
    (hy : Bootstrapping.IsUTerm ℒₛₑₜ y) :
    Bootstrapping.termBVVec ℒₛₑₜ 2 (Adjoin.adjoin x (Adjoin.adjoin y (0 : V)))
      = Adjoin.adjoin (Bootstrapping.termBV ℒₛₑₜ x)
          (Adjoin.adjoin (Bootstrapping.termBV ℒₛₑₜ y) (0 : V)) := by
  rw [show (2 : V) = 0 + 1 + 1 by norm_num]
  rw [Bootstrapping.termBVVec_cons (k := (0 : V) + 1) (t := x)
    (ts := Adjoin.adjoin y (0 : V)) hx
    (Bootstrapping.IsUTermVec.adjoin
      (Bootstrapping.IsUTermVec.empty (V := V) (L := ℒₛₑₜ)) hy)]
  rw [Bootstrapping.termBVVec_cons (k := (0 : V)) (t := y) (ts := (0 : V)) hy
    (Bootstrapping.IsUTermVec.empty (V := V) (L := ℒₛₑₜ))]
  rw [GodelQ.CG008BvZ.termBVVec_nil']

-- **`bv_eqAtom_le` 的组装仍未过**。三个零件都是定理：
-- `bv_rel` + `isRel_quote_quote`（`IsRel 2 cEqN`）、`termBVVec_two`、`listMax_vec₂_le`。
-- **卡点已精确定位**：`rw [termBVVec_two …]` 在目标上匹配时，Lean 要从
-- `Adjoin.adjoin` 的**记法**里合成 `Zero ?m`（`Adjoin V V` 实例本身是无条件的，
-- 但 `rw` 的 `isDefEq` 会先把项展开成 `⟪·,·⟫ + 1` 再找 `0` 的实例）。
-- **下一步（已试到的最接近的一条）**：`conv_lhs` 能过前两步
-- （`rw [he]`、`rw [bv_rel]`），**第三步 `rw [termBVVec_two]` 触发该歧义**；
-- 可行修法：把 `termBVVec_two` 的**左边写成 `⟪·,·⟫ + 1` 的展开形式**
-- （与 `rw` 展开后的目标逐字相同），或在 `conv` 里用 `change` 先换成展开形式。

end GodelQ.CG008BvW

#print axioms GodelQ.CG008BvW.termBVVec_two
#print axioms GodelQ.CG008BvW.listMax_vec₂_le
