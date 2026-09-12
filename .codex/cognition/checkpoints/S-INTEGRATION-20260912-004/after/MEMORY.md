# 当前工作记忆

> Owner：顶层综合 repo 的 `AGENTS.md` 与 `.codex/cognition/PROTOCOL.md`。本文件只记录当前状态，不复制 `核心认知.md` 或历史长文。

## 当前状态（2026-09-12）

- 顶层 `/Volumes/D/HoTT_AI_HANDOFF_20260911` 已初始化为新 Git repo；来源基线提交为 `7ba0088`，当前交接波次由 `S-INTEGRATION-20260912-004` 封存。用户明确授权“顶层作为新 repo、写方案并执行”，因此本 repo 内的本次提交已获授权。
- 已保存实施方案 `实施方案-三AI历史整合与核心认知治理.md`、治理影响分类 `audit/governance-impact.md`、顶层 `.gitignore`、原始 handoff 目录、`理解章节/`、从 `/Volumes/D/ALL-Markdown/HoTT/` 收录的 `HoTT/`、LocalGPT/WebGPT/Gemini 原始来源副本和 `sources/SOURCE_MANIFEST.json`。
- `/Volumes/D/ALL-Markdown/aistudio-docs/` 没有恢复。`HoTT_is_GONE_COMPLETE.md` 已保存为历史 AI 产物；它可能是替代性摘要，但“覆盖原目录全部关键内容”仍是 `NOT_PROVEN`。
- cognition runtime 当前状态为 STATE revision 4 / latest session `S-INTEGRATION-20260912-004`；该状态只表示交接 checkpoint 已持久化，不表示数学或模型理解已认证。
- `核心认知.md` 当前 generation 为 `core-cognition-generation-1`，由三份用户提问提取文件作 primary、Codex 父线程和并行提取作 supplemental。当前 manifest：125 条提取消息，92 条进入核心，903 个连续 `KC-000001`—`KC-000903` 原文单元；纯素数并行消息只进入处置账本，不进入核心正文。核心验证脚本当前 PASS；每个 KC 在 session 001/002 均有逐编号回评文件。

## 已确认的历史来源事实

- LocalGPT：Codex HoTT-2 主提取 10 条用户消息、34 条 visible assistant；父线程与主文件合计 38 turns/41 条真实用户消息的关系必须保留。父 trajectory 原始 SHA-256 为 `23dcdb6e862f3333f0ac9d5e9f8daed55f93ccbadab6ed3e8fad21ddb60094a0`，HoTT-2 main 为 `2e0fef446f5eb58d7c843fc9e8cd852834e5c771ec68c589e737a457a2489f51`；原始文件只在 `private-audit/`，不公开提交。
- WebGPT：导出提取 56 Prompt、55 Response、111 UI sections；`sources/webgpt/workspace-snapshot/` 是其工作目录快照。其治理框架的双 Skill、LOAD_SET、STATE、checkpoint 和 exchange 规范已原样快照保存，当前本地版本必须用顶层相对路径改造。
- Gemini：用户提取 22 条；模型可见普通文本 24 条，另有 21 thought、17 executableCode、17 codeExecutionResult、2 inlineFile、1 Drive 文档引用。两个 inlineFile 是实际可解码文本代码，不得标为 empty；Drive 正文缺失必须标为附件正文不可得。

## 当前仍开放 / 未完成

1. **历史响应与工具全量账本**：已生成 `audit/ai-response-ledger.jsonl`、`audit/tool-event-ledger.jsonl`、`audit/work-product-ledger.jsonl`、`audit/claim-evidence-ledger.jsonl`，可见回答、工具调用/结果、工作产物和理解章节主张均有行级定位；仍需人工完成关键 response→artifact/Git 的语义映射，不能声称数学主张已认证。
2. **理解章节博士论文级更新**：已新增 C0 当前审计层并为 B/A 旧章节加历史状态边界；旧的 13/38、约 173/171 等冲突已被 C0 明确降级，但 A/B 每个重要历史主张仍需逐句回连直接证据，不能把当前 C0 当作最终论文。
4. **Checkpoint 运行事实**：session 003 的第一次尝试因依赖 review_required 被正确拒绝，第二次提交成功；session 004 用同一 runtime 对齐 MEMORY/RESUME/LESSONS，当前 transaction/lock 已清理，before/after/result receipts 保留。
3. **WebGPT 与 LocalGPT 的 Git/产物对应**：WebGPT 快照和 LocalGPT ALL-Markdown/trajectory 已进入 work-product 与 response/tool ledger；逐条语义因果映射、关键文件 diff 和 commit body 复核仍开放。
4. **aistudio-docs 覆盖**：旧 `hott_discussion_corpus.py validate` 依赖已移走目录而失败；此失败应作为真实边界保存。`HoTT_is_GONE_COMPLETE.md` 的替代覆盖关系不能仅凭文件存在或 AI 自述升级为已证明。
5. **当前数学研究**：本轮是交接/治理工程，不等同于 R040 或新的数学突破。除非用户另行要求，当前不把历史候选的 `review_required` 变成已证实定理。

## 下一最小可验结果

在新 Session 中先全文加载 core，沿 `A-UNDERSTANDING-RECONCILIATION-001` 逐章做 sentence→source→response/tool→artifact/code→Git/run 的语义映射，并在不改变历史原文的前提下原位更新对应 owner；同时保持 `A-AISTUDIO-COVERAGE-001` 与 `A-HISTORICAL-MATH-CLAIMS-001` 的 review_required 状态。
