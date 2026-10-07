import GodelQ.EffectiveTheory
/-! 负控制 3：不可枚举的“真理论”封闭于 P 而不矛盾；不能把它当作有效理论去套魔鬼交易。
这里缺少 `re_never` 的证明，Lean 必须拒绝。 -/
open GodelQ in
theorem wrong_bargain_without_effectiveness : False :=
  EffectiveTheory.devils_bargain
    { provesHalts := truthTheory.provesHalts
      provesNever := truthTheory.provesNever
      provesNotYet := truthTheory.provesNotYet
      re_never := by simp [truthTheory]
      sigma1_complete := truthTheory.sigma1_complete
      delta0_complete := truthTheory.delta0_complete
      consistent := truthTheory.consistent }
    truthTheory.omega
