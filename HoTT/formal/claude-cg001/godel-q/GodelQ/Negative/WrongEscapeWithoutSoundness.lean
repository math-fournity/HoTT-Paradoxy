import GodelQ.ProcessObservation
/-! 负控制 1：没有可靠性的“观察者”不能套用对角逃逸。这里试图对“接受一切”的集合
得出逃逸点——`NeverObserver` 要求的 `sound` 字段无法提供，Lean 必须拒绝。 -/
open GodelQ in
theorem wrong_escape_without_soundness :
    ∃ d : Process, ¬ Done d ∧ ¬ (fun _ : Process => True) d := by
  obtain ⟨d, h1, h2, _⟩ := diagonal_escape
    { accepts := fun _ => True
      re := ComputablePred.to_re (Computable.computablePred
        ((Computable.const true).of_eq fun _ => by simp))
      sound := fun e _ => by simp [Done] }
  exact ⟨d, h1, h2⟩
