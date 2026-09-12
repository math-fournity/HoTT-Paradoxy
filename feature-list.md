# Feature / 当前需求状态

本文件是当前 feature 状态 owner；历史来源中的“已完成”不自动改变这里的状态。

| ID | 需求 | 当前状态 | 证据/下一步 |
|---|---|---|---|
| F-001 | 顶层目录成为综合 Git repo，保留原嵌套来源边界 | IMPLEMENTED | `git log`、`.gitignore`、`audit/governance-impact.md` |
| F-002 | 保存 LocalGPT、WebGPT、Gemini 来源快照和 provenance | IMPLEMENTED_WITH_SCOPE | `sources/SOURCE_MANIFEST.json`；私有 trajectory 仅在 ignored `private-audit/` |
| F-003 | 三份用户提问原文按时间组成连续编号 `核心认知.md` | VERIFIED_WITH_SCOPE | `核心认知.manifest.json`、`scripts/audit/verify_core_cognition.py`；generation-1 |
| F-004 | 记录所有可见 AI response、tool event、work product、claim-evidence | VERIFIED_WITH_SCOPE | 四类主 ledger + WebGPT/Gemini 专项 ledger 已生成；关键语义映射仍待人工复核 |
| F-005 | 建立顶层 `.codex` 本地治理：启动全文 core、动态状态、结束逐 KC 回评、可恢复 checkpoint | VERIFIED_WITH_SCOPE | `.codex/` 骨架、runtime plan、55-doc load set、session 001/002 逐 KC audit；数学理解不由工具认证 |
| F-006 | 以审计结果更新 `理解章节/`，达到交接/博士论文级而非摘要级 | IN_PROGRESS | 已新增 C0 和历史边界层；逐句 source→AI→artifact/Git/run 的 owner 修订仍待下一波 |
| F-007 | 不恢复用户移走的 `aistudio-docs`，明确替代材料覆盖是否可证明 | VERIFIED_BOUNDARY | 缺源 validator 失败；coverage 仍 `NOT_PROVEN` |
| F-008 | 未来每个工作单元按核心认知逐编号评估方向 | DESIGNED | `.codex/cognition/PROTOCOL.md`、session `CORE_COGNITION_AUDIT.md` 合同 |
