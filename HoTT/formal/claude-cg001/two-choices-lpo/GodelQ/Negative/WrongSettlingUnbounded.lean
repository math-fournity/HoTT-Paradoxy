import GodelQ.TwoChoices.Core

/-!
# 负控制 MP-CG001-TWO-CHOICES-LPO-NEG-002：去掉“有界”，LPO 仍给出终值

被否定的说法：有了 LPO，每个单调的自然数序列（不要求有界）都有落定的一步。
证明照搬主包的 `settles_of_lpo_gap`，可它要一个“还能再升几格”的上界，这里给不出。

预期：拒绝。`omega` 证不出 `x n ≤ x 0 + x 0`。主包的正面定理 `unbounded_settling_false`（C-418）
证明这个结论本来就不成立：`x n = n` 永不落定。
-/

namespace GodelQ.TwoChoices.Negative

open GodelQ.TwoChoices

theorem settles_unbounded (h : LPO) (x : Nat → Nat) (hx : MonoNat x) : ∃ N, SettlesAt x N :=
  settles_of_lpo_gap h (x 0) x hx (fun n => by omega)

end GodelQ.TwoChoices.Negative
