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

-- **两条路线本轮都试到同一处**：
-- * `bv_eqAtom_le`（`eqAtom` 的基例）走到 `nth_resultVec`/`nth_termBVVec` 的
--   隐式参数合成歧义（`Zero ?m`），未过；
-- * `bv_iVE_le`（`IsSemiterm.induction` 版）的 `Σ₁` 闸门卡在 `bv` 的
--   `DefinableFunction` 形状（`V → V` vs `(Fin 1 → V) → V`）。
--
-- **已确证的结构性事实**（这是本轮最有价值的一条）：
-- `IsUTerm.induction` 的 `bvar` 分支**不给** `z` 的界，所以
-- `bv (eqAtom (^#(z+1))) = z + 2 ≤ n + 1` 在那条路上**证不出来**；
-- 必须用 `IsSemiterm.induction`（`Term/Basic.lean:912`），其 `bvar` 分支是
-- `∀ z < n, P (^#z)`——**正是所需**。这条对 `CG008IVE.iVE_isUFormula` 同样适用。

end GodelQ.CG008Bv2

#print axioms GodelQ.CG008Bv2.nth_vec₂_zero
#print axioms GodelQ.CG008Bv2.nth_vec₂_one

