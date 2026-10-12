import GodelQ.ZFC.CG008ShiftProof
import GodelQ.ZFC.CG008IVE

/-!
# CG-008 · `bv (iVE n t) ≤ n + 1`——用 `IsSemiterm.induction`

**关键**：`IsUTerm.induction` 的 `bvar` 分支**不给** `z` 的界，
所以 `bv (eqAtom (^#(z+1))) = z + 2 ≤ n + 1` 证不出来。
`IsSemiterm.induction`（`Term/Basic.lean:912`）的 `bvar` 分支给 **`z < n`**——
正是所需。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Bv2
open GodelQ.ZFCArith GodelQ.Translate
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- 分量 0 与 1 的取值。 -/
lemma nth_vec₂_zero (t : V) : (^#0 ∷ t ∷ (0 : V)).[0] = (^#0 : V) := by
  rw [Arithmetic.nth_zero (V := V), Arithmetic.fstIdx_adjoin]

lemma nth_vec₂_one (t : V) : (^#0 ∷ t ∷ (0 : V)).[1] = t := by
  have h1 : (1 : V) = (0 : V) + 1 := by norm_num
  rw [h1, Arithmetic.nth_succ (V := V), Arithmetic.sndIdx_adjoin]
  -- 剩 `(t ∷ 0).[0] = t`
  rw [Arithmetic.nth_zero (V := V), Arithmetic.fstIdx_adjoin]

-- **`bv_eqAtom_le` 未证**。本轮把两条分量引理证出（上面），
-- 并把主证明推进到只剩 `nth_termBVVec` 的**隐式参数合成歧义**
-- （`Zero ?m`：该引理的 `k`/`v` 用隐式参数，在 `V` 上无法自动确定）。
-- **下一步**：把 `nth_termBVVec` 的 `k`、`v`、`hv`、`hi` **全部显式**给出
-- （本文件已试 `(k := 2) (v := …) hv`，仍歧义；疑需连 `L` 一并显式或改走
-- `construction.nth_resultVec` 的原始形式）。

end GodelQ.CG008Bv2

#print axioms GodelQ.CG008Bv2.nth_vec₂_zero
#print axioms GodelQ.CG008Bv2.nth_vec₂_one

