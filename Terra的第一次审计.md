<!-- governance-shard-index:v2
logical_id: TERRA-FIRST-AUDIT
mode: topical
shard_root: Terra的第一次审计
last_shard: Terra的第一次审计/006 - 审计主张、未知与后续准入.md
append_target: -
soft_line_target: 300
-->

# Terra的第一次审计 — 索引

> ⚠️ 逻辑文档索引：全文 = 本索引 + 下方 6 个分片；缺一片即未完成，按表顺序读取；300 行只是软目标，不是上限。
>
> 文档身份：`AUDIT_GRADE_EVIDENCE_REPORT`；报告 ID：`TERRA-MF-AUDIT-20260919-v1`；状态：`PREIMPLEMENTATION_AUDIT_COMPLETE_WITH_BLOCKERS`。

本报告审计未来 `MATH-FOURNITY` 公开结果包的数学命题忠实性、已保存机器证明、证据关系、可移植重放资格与发布准入边界。它只陈述已由具体源码、run 收据、验证器、Git 或本次可复现检查支持的结论；不把用户—AI 讨论过程、未跟踪并行资产、理论哲学动机或未证的现实对应提升为数学定理。

它不是未来公开仓库的内容。公开包仍必须只交付最终结果、精确形式命题、必要最终控制、范围、许可证和开放问题；本报告只作为当前综合项目的内部审计证据。

<!-- governance-shard-table:start -->
| Shard | 文件 | 语义范围 | 状态 |
|---|---|---|---|
| 001 | [审计任务、快照与证据方法](<Terra的第一次审计/001 - 审计任务、快照与证据方法.md>) | 授权、范围、版本快照、证据等级、并发边界与可复核方法 | current |
| 002 | [十个候选公开证据单位逐项审计](<Terra的第一次审计/002 - 十个候选公开证据单位逐项审计.md>) | R01–R10 的精确命题、源码、run、范围与公开分类 | current |
| 003 | [命题忠实性与研究目的审计](<Terra的第一次审计/003 - 命题忠实性与研究目的审计.md>) | 形式命题、自然语言读法、HoTT 特有性、现实桥梁与禁止外推 | current |
| 004 | [机器证明、收据与版本闭合审计](<Terra的第一次审计/004 - 机器证明、收据与版本闭合审计.md>) | 内核重放、R07 控制、manifest、全局 closure 与治理 verifier 缺口 | current |
| 005 | [公开包准入、范围与修复路线](<Terra的第一次审计/005 - 公开包准入、范围与修复路线.md>) | P0–P4 的适用结论、范围分母、目标仓库状态与不得越阶条件 | current |
| 006 | [审计主张、未知与后续准入](<Terra的第一次审计/006 - 审计主张、未知与后续准入.md>) | claim–evidence 映射、反证条件、残余未知与下一授权边界 | current |
<!-- governance-shard-table:end -->

## 即时判词

- 九个正向候选公开单位的主 run 已在固定本机 Cubical Agda 环境中重新核对为 `PASS_WITH_SCOPE`；此事实只证明各自精确形式命题。
- R07 是 `EXPECTED_NEGATIVE_CONTROL` 族，不是对象层否定定理，更不是 HoTT 不一致性证明。
- 现有 source 项目的 `verify_proof_version_closure.py` 报 `CURRENT_MATRIX_NOT_APPEND_ONLY_SUCCESSOR`，数学交付治理 verifier 报 `.codex/AGENTS.md` marker 漂移；因此“整包机器证明已经版本闭合”不能成立。
- `MATH-FOURNITY` 尚未有 release manifest、portable replay、clean-environment receipt 或 CI receipt，不能开始 P1 导出、P2 staging 或其后的公开构建动作。
- 本报告不改变 `HoTT/CLAIM_EVIDENCE_MATRIX.md` 的数学状态、不替代原始 run 收据，也不授权目标仓库写入、commit、push 或公开发布。
