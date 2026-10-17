# russell-archaeology：罗素「解决」考古的形式化面（CG001-C-432…C-435）

「ZFC 解决了罗素悖论」——当初的形式化证明是什么？工作假说（QUESTION 状态）：
不存在；Zermelo 1908 做的是公理删除/准入层拒绝。本包把该叙事拆成四条可机器
检查的分层命题，作为 `docs/罗素解决考古/` 步骤 4 三栏对照表的形式化底座。

| 编号 | 定理 | 层 | 内容 |
|---|---|---|---|
| CG001-C-432 | `noRussellSet` | 对角层 | `¬∃ R, ∀ x, x ∈ R ↔ x ∉ x`——纯逻辑，零集合论公理 |
| CG001-C-433 | `sep_russell_not_mem` | 分离层 | 分离式成员刻画 ⇒ `R_A ∉ A`——非矛盾，准入层拒绝 |
| CG001-C-434 | `foundation_irrefl` | 正则层 | 正则 + 单元素集 ⇒ `∀ x, x ∉ x`——准入禁止 |
| CG001-C-435 | `unboundedComprehensionFalse` | 负控制 | 无界概括（命题形态）⇒ `False`——爆炸的充分条件 |

- 主入口：`GodelQ/Russell/Qualification.lean`（四核合取 `qual_russell_arch` +
  公理审计；四核与合取经 `#print axioms` **不依赖任何公理**）。
- 负控制：`GodelQ/Negative/WrongSepContradiction.lean`（照搬无界层对角结尾到
  分离层，预期被 Lean 拒绝：`h.mpr hne` 期望 `R ∈ A ∧ R ∉ R`）。
- 编译（开发，不进收据）：
  `python3 .claude/goals/CG-007-formalization-completion/tools/devbuild_ns.py HoTT/formal/claude-cg001/russell-archaeology GodelQ/Russell/Basic.lean GodelQ/Russell/Sep.lean GodelQ/Russell/Foundation.lean GodelQ/Russell/Unbounded.lean GodelQ/Russell/Qualification.lean`
- 证据与运行：`HoTT/CLAIM_EVIDENCE_MATRIX.md`、`HoTT/verification/runs/`、
  `形式化追踪/`（正式收据按 F-011 五步门禁出）。
- 详细命题表与禁止外推：`CLAIM.md`。