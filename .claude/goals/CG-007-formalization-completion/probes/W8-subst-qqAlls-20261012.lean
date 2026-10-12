import GodelQ.ZFC.ShCraigElimSetupQ

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat

set_option maxHeartbeats 800000

namespace GodelQ.ProbeIter
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## `subst` 推过 `qqAlls`：用 `ℕ` 迭代陈述以躲开 numeral 匹配

`substs_all` 只给**一层**：`subst w (^∀ p) = ^∀ (subst (qVec w) p)`。
这里把它提升到 `n` 层，RHS 用 `qVec^[n] w`。

**为什么这样能躲开 numeral 问题**：`n : ℕ`，`qqAlls X ↑n` 里的 coercion
由 `Nat.cast_succ` 统一处理，`rw [Nat.cast_succ, qqAlls_succ]` 稳定可过。 -/

lemma subst_qqAlls {X w : V} (hX : IsUFormula ℒₛₑₜ X) :
    ∀ (n : ℕ) (w : V), subst ℒₛₑₜ w (qqAlls X (n : V))
      = qqAlls (subst ℒₛₑₜ ((qVec ℒₛₑₜ)^[n] w) X) (n : V) := by
  intro n w
  induction n generalizing w with
  | zero =>
    simp [qqAlls_zero]
  | succ k ih =>
    have hXk : IsUFormula ℒₛₑₜ (qqAlls X (k : V)) := isUFormula_qqAlls.mpr hX
    -- `(f^[k+1]) w = (f^[k]) (f w)`：用 apply 形式而不是复合形式
    have hit : ((qVec ℒₛₑₜ)^[k + 1] w) = ((qVec ℒₛₑₜ)^[k] (qVec ℒₛₑₜ w)) := by
      rw [Function.iterate_succ_apply]
    rw [Nat.cast_succ, qqAlls_succ, Bootstrapping.substs_all hXk, hit,
      ih (qVec ℒₛₑₜ w), qqAlls_succ]

end GodelQ.ProbeIter
