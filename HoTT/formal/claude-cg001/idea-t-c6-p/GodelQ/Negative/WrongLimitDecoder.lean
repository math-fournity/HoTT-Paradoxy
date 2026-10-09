import GodelQ.IdeaT

/-! 负控制（C-114 形式一）：硬说只看极限值的接口上存在可靠、完备的“取到”判据——判据取“一律接受”。
完备性平凡成立，可靠性却要对每个过程 s 证明“s 在某个有限阶段取到它的极限”；对稠密跑者这句是假的
（`zeno_form_one`），这里缺少它的证明，Lean 必须拒绝。形式一因此确实用到了接口上的碰撞。 -/

open GodelQ.IdeaT GodelQ.Zeno in
theorem wrong_limit_decoder :
    ∃ A : ℝ → Prop,
      Sound (fun s : ℕ → ℝ => Filter.limUnder Filter.atTop s) A
        (fun s => AttainsAt s (Filter.limUnder Filter.atTop s)) ∧
      Complete (fun s : ℕ → ℝ => Filter.limUnder Filter.atTop s) A
        (fun s => AttainsAt s (Filter.limUnder Filter.atTop s)) :=
  ⟨fun _ => True, fun s _ => by simp [AttainsAt], fun _ _ => trivial⟩
