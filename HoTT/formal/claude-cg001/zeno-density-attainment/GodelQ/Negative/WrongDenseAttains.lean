import GodelQ.Zeno.Runners

/-! 负控制：在稠密的 ℝ 里，硬把终点 1 当作孤立点，去推出稠密跑者在某个有限阶段取到 1。
1 在 ℝ 中不孤立（`real_not_isolated`），这里缺少 `Isolated (1 : ℝ)` 的证明，Lean 必须拒绝。
归因定理因此确实用到了“终点孤立”这一条：去掉它（稠密），贴近推不出取到。 -/

open GodelQ.Zeno in
theorem wrong_dense_attains : AttainsAt densePos 1 :=
  attains_of_isolated (x := (1 : ℝ)) (by simp [Isolated]) densePos_arrives
