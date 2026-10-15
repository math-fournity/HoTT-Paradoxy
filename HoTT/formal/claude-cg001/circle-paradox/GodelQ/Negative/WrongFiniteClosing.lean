import GodelQ.Circle.CircleParadox

/-!
# 负控制 MP-CG001-CIRCLE-PARADOX-NEG-001：圆环在某个有限阶段合上

被否定的说法：逐步逼近的合回在某个有限阶段完成，即远端在第 n 步到达拿走的那一点 0。
这里取第 0 步作候选：远端在 ↑(1/2)。

预期：拒绝。要证 ↑(1 − 1/2) = 0，证不出。主包的正面定理 `farEnd_ne_zero` 与
`closing_never_attains`（C-424）证明这个说法本来就不成立。
-/

namespace GodelQ.Circle.Negative

open GodelQ.Circle

theorem closes_at_stage_zero : farEnd 0 = 0 := by
  simp [farEnd, θ]

end GodelQ.Circle.Negative
