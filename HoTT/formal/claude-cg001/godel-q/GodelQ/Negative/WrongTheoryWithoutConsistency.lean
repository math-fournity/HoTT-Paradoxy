import GodelQ.EffectiveTheory
/-! 负控制 2：不一致的理论（什么都证明）不是 `EffectiveTheory`：一致性字段无法提供，
因而魔鬼交易不能被它“反驳”。Lean 必须拒绝。 -/
open GodelQ in
def wrongInconsistentTheory : EffectiveTheory where
  provesHalts _ := True
  provesNever _ := True
  provesNotYet _ _ := True
  re_never := ComputablePred.to_re (Computable.computablePred
    ((Computable.const true).of_eq fun _ => by simp))
  sigma1_complete _ _ := trivial
  delta0_complete _ _ _ := trivial
  consistent _ _ _ := by trivial
