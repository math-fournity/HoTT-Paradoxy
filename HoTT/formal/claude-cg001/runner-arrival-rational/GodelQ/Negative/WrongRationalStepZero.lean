import GodelQ.ZFC.ArrivalRational

/-!
# 负控制 MP-CG001-RUNNER-ARRIVAL-RATIONAL-NEG-001：有理精度下，经典芝诺从第 0 步起就够近

被否定的说法：在每一个 𝗜𝚺₁ 模型里，对每个正有理数 p/q，从第 0 步起就有 q < p·2ⁿ，即步数与精度无关。
这里照搬主包 `models_arriveRatC` 的证明，把步数换成 0。

预期：拒绝。要用到 q ≤ n，而 n 只满足 0 ≤ n。反例：p = q = 1、n = 0 时，1 < 1·2⁰ 不成立。正面定理
`models_arriveRatC`：步数取 q。
-/

namespace GodelQ.ArrivalRat.Negative

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic
open scoped FFL.FirstOrder.Arithmetic
open GodelQ.ArrivalRat

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

theorem step_zero_suffices :
    ∀ p q : V, 0 < p → 0 < q → ∀ n, 0 ≤ n → q < p * Exp.exp n := by
  intro p q hp _ n hn
  have h1 : q < Exp.exp q := lt_exp q
  have h2 : Exp.exp q ≤ Exp.exp n := exp_monotone_le.mpr hn
  have h3 : Exp.exp n ≤ p * Exp.exp n := le_mul_of_one_le_left zero_le (pos_iff_one_le.mp hp)
  exact lt_of_lt_of_le h1 (le_trans h2 h3)

end GodelQ.ArrivalRat.Negative
