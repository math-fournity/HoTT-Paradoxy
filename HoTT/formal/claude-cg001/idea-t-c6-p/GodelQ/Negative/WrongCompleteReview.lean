import GodelQ.C6Review

/-! 负控制（C-115）：照真值裁决的审查可靠且完备（`truth_review_complete`），但它不是有效的审查。
硬把它当成 `Review`，就要证明“标准解不充分”的跑者集可枚举；那恰是永不停机集（`inadequate_iff`），
不可枚举。这里缺少它的证明，Lean 必须拒绝。C6 定理因此确实用到了“有效”这一条。 -/

open GodelQ GodelQ.C6 in
theorem wrong_complete_review : ∃ R : Review, R.Complete :=
  ⟨{ provesAdequate := Adequate
     provesInadequate := fun d => ¬ Adequate d
     sound_adequate := fun _ h => h
     sound_inadequate := fun _ h => h
     re_inadequate := by simp },
   fun d => em (Adequate d)⟩
