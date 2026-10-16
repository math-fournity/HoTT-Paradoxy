import GodelQ.ProvabilityLogic
/-! 负控制 4：在一致的 HBL 模型里，一致性陈述不可证（Gödel II 的结论成立）；
试图证明它必须失败。 -/
open GodelQ in
theorem wrong_consistency_provable : trivialBoxModel.Pr trivialBoxModel.con := by
  simp [trivialBoxModel, HBLTheory.con]
