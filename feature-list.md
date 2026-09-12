# Feature / 当前需求状态

本文件是当前 feature 状态 owner；历史来源中的“已完成”不自动改变这里的状态。

| ID | 需求 | 当前状态 | 证据/下一步 |
|---|---|---|---|
| F-001 | 顶层目录成为综合 Git repo，保留原嵌套来源边界 | IMPLEMENTED | `git log`、`.gitignore`、`audit/governance-impact.md` |
| F-002 | 保存 LocalGPT、WebGPT、Gemini 来源快照和 provenance | IMPLEMENTED_WITH_SCOPE | `sources/SOURCE_MANIFEST.json`；私有 trajectory 仅在 ignored `private-audit/` |
| F-003 | 三份用户提问原文按时间组成连续编号 `核心认知.md` | VERIFIED_WITH_SCOPE | `核心认知.manifest.json`、`scripts/audit/verify_core_cognition.py`；generation-1 |
| F-004 | 记录所有可见 AI response、tool event、work product、claim-evidence | VERIFIED_WITH_SCOPE | 四类主 ledger + WebGPT/Gemini 专项 ledger 已生成；关键语义映射仍待人工复核 |
| F-005 | 建立顶层 `.codex` 本地治理：启动按 `核心认知.md`→`方向追踪.md`→`全景视野.md` 的三件套全文加载、动态状态、三方交叉审视、结束逐 KC 回评、可恢复 checkpoint | IMPLEMENTED_PENDING_FRESH | `.codex/` 骨架、三件套、runtime plan、三方 validator、session audit；真实 fresh/压缩恢复行为和模型理解仍未认证 |
| F-006 | 以审计结果更新 `理解章节/`，达到交接/博士论文级而非摘要级 | IN_PROGRESS | 已新增 C0 和历史边界层；逐句 source→AI→artifact/Git/run 的 owner 修订仍待下一波 |
| F-007 | 不恢复用户移走的 `aistudio-docs`，明确替代材料覆盖是否可证明 | VERIFIED_BOUNDARY | 缺源 validator 失败；coverage 仍 `NOT_PROVEN` |
| F-008 | 未来每个工作单元按核心认知逐编号评估方向 | IMPLEMENTED_PENDING_FRESH | `.codex/cognition/PROTOCOL.md`、三件套交叉合同、session `CORE_COGNITION_AUDIT.md` |
| F-009 | 以 `方向追踪.md` 和 `全景视野.md` 统筹两个 GPT 的历史方向/成果，并与 `核心认知.md` 交叉决定更新归属；不把 AI 结果写入用户原文 | INITIAL_PROJECTION_PENDING_SEMANTIC_RECONCILIATION | `方向追踪.md`、`全景视野.md`、`治理框架对比审计与核心认知增补评估-20260912.md`；WebGPT 91 条 record 和 LocalGPT 全谱系逐条语义映射仍开放 |
