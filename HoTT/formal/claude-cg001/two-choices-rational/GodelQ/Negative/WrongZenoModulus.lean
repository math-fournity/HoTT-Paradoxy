import GodelQ.TwoChoices.RationalConstructive

/-!
# 负控制 MP-CG001-TWO-CHOICES-RATIONAL-NEG-002：芝诺数列的柯西步可以一律取第 0 步

被否定的说法：芝诺位置 1 − 2⁻ⁿ 的柯西步与精度无关，一律取第 0 步，此后两两之差都小于 1/(k+1)。
这里照搬主包 `zenoQp_cauchy` 的证明，把步数换成 0。

预期：拒绝。`omega` 证不出 `k + 1 ≤ m`。反例：精度 1/2（k = 1）时，第 0 步的位置是 0，第 n 步的
位置 1 − 2⁻ⁿ 可以任意接近 1。正面定理：`zenoQp_cauchy`，步数由公式 k + 1 给出；
`zeno_modulus_zero_false`，这个说法是错的（第 0 步与第 2 步相差 3/4）。
-/

namespace GodelQ.TwoChoices.Negative

open GodelQ.TwoChoices

theorem zeno_modulus_zero :
    ∀ k m n : Nat, 0 ≤ m → 0 ≤ n → CloseQ ((k : Int) + 1) (zenoQp m) (zenoQp n) := by
  intro k m n _ _
  exact zenoQp_cauchy k m n (by omega) (by omega)

end GodelQ.TwoChoices.Negative
