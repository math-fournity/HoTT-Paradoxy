import GodelQ.Turing

/-! 负控制：“真理观察者”接受恰好全部永不完成的过程，它可靠，但不可枚举。若硬把它当成可枚举的
观察者，漏点定理就会给出矛盾：它的漏点集是空集，而空集可枚举。这里缺少 `re` 的证明，Lean 必须拒绝。
图灵路线因此确实用到了“可枚举”这一条：去掉它，结论不成立（真理观察者没有漏点）。 -/

open GodelQ in
theorem wrong_turing_with_truth_observer : False :=
  NeverObserver.misses_not_re
    { accepts := fun e => ¬ Done e
      re := by simp
      sound := fun _ h => h }
    (empty_re.of_eq fun e => by simp [NeverObserver.Misses])
