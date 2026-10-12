import GodelQ.ZFC.ShCraigElimSetupQ

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat

set_option maxHeartbeats 800000

namespace GodelQ.ProbeY
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## 干净解法：把 `subst` 推过 `qqAlls` 写成**递归引理**，全程 `k+1`

反复失败的原因是「多处 numeral + `qqAlls_succ` 要 `k+1`」互相牵制。
**绕开办法**：把这条推入写成**对 `k` 的递归引理**，陈述里只有 `k + 1`，
没有字面量 `2`；用 `Nat` 归纳，每步只出现一次 `k+1`。 -/

/-- `subst` 推过 `qqAlls`：`subst w (qqAlls X k) = qqAlls (subst ((qVec L)^[k] w) X) k`。 -/
lemma substs_qqAlls : ∀ (k : ℕ) (X w : V), IsUFormula ℒₛₑₜ X →
    subst ℒₛₑₜ w (qqAlls X (k : V))
      = qqAlls (subst ℒₛₑₜ ((qVec ℒₛₑₜ)^[k] w) X) (k : V) := by
  intro k
  induction k with
  | zero =>
    intro X w _
    simp
  | succ j ih =>
    intro X w hX
    rw [show ((j + 1 : ℕ) : V) = (j : V) + 1 by push_cast; ring]
    rw [qqAlls_succ]
    have hu : IsUFormula ℒₛₑₜ (qqAlls X (j : V)) := isUFormula_qqAlls.mpr hX
    rw [Bootstrapping.substs_all (L := ℒₛₑₜ) hu]
    rw [ih X (qVec ℒₛₑₜ w) hX]
    rw [qqAlls_succ]
    -- 目标：`^∀ qqAlls (subst ((qVec)^[j] (qVec w)) X) j
    --      = ^∀ qqAlls (subst ((qVec)^[j+1] w) X) j`
    congr 3

end GodelQ.ProbeY
