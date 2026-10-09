import GodelQ.PTwoSides

/-! 负控制（C-116）：硬说实数轴上语义 P₁ 在终点 1 成立（每个极限意义到达 1 的过程都在某个有限阶段取到 1），
并借格点上的定理 `grid_attains` 去证。那要每个过程都取值在某个格点上；一般的实数过程（例如稠密跑者）不是，
这里缺少它的证明，Lean 必须拒绝。语义 P₁ 的成立因此确实依赖量子化，在稠密的 ℝ 上不成立。 -/

open GodelQ.Zeno GodelQ.PTwoSides in
theorem wrong_real_p1 : SemanticP1 (fun s : ℕ → ℝ => ArrivesAt s 1) (fun s => AttainsAt s 1) :=
  fun s h => grid_attains (m := 0) (fun n => by simp [grid]) h
