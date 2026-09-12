# 当前工作记忆

> Owner：顶层综合 repo 的 `AGENTS.md` 与 `.codex/cognition/PROTOCOL.md`。本文件只记录当前状态，不复制 `核心认知.md` 或历史长文。

## 当前状态（2026-09-12）

- 顶层 `/Volumes/D/HoTT_AI_HANDOFF_20260911` 已初始化为新 Git repo；当前治理 checkpoint 将由 `S-GOV-20260912-010-HISTORY-RECONCILIATION` 封存。
- `核心认知.md` 已从 generation-1 迁移到 `core-cognition-generation-2`：127 条登记消息、94 条含核心单元消息、913 个连续 `KC-*`；generation-1 的 903 个 KC 前缀逐项保持一致。新增输入是用户关于三件套、压缩恢复、跨 GPT 综观和理解章节逐文件融合的原文。
- 三件套当前固定顺序为 `核心认知.md` → `方向追踪.md` → `全景视野.md`；两个 projection 已从有界初始投影升级为“全量 source register + scoped manual review”。这不证明模型上下文实际保有全文。
- `audit/understanding-chapter-merge-manifest.json` 已覆盖顶层 25 文件与 nested 24 文件；顶层 `理解章节/` 是 canonical，nested `/AI对话录/理解章节/` 仍保留为历史源，没有删除。
- `audit/cross-source-reconciliation.json` 已登记 WebGPT 91、LocalGPT response 384、tool event 3,146、work product 16,209、understanding claim 2,396，共 22,226 个来源行；每行有 locator 和方向/结果链接或理由。2,396 条 claim 仍是 `PENDING_DIRECT_SENTENCE_ADJUDICATION`，不把规则匹配写成语义结论。
- `/Volumes/D/ALL-Markdown` 的当前工作树仍 dirty、HEAD `8470721a07f28f842895a67f5fd885ab12c1ee33`；WebGPT workspace snapshot HEAD `26fcecfbfecf6db66a70c1bf3e067159bce3eb6a`、revision 41；二者都没有被本轮修改。

## 当前仍开放 / 未完成

1. `A-UNDERSTANDING-RECONCILIATION-001`：文件级 manifest 已通过，但历史章节的逐句语义等价和数学主张复核仍不认证。
2. `A-AISTUDIO-COVERAGE-001`：不能凭 `HoTT_is_GONE_COMPLETE.md` 文件存在证明已覆盖用户移走的 `aistudio-docs`。
3. `A-HISTORICAL-MATH-CLAIMS-001`：历史数学主张仍按纸笔/有限测试/native/现实桥梁分层，未被本治理 Session 重新证明。
4. `A-HISTORY-LEDGERS-001` 与 `A-CROSS-SOURCE-RECONCILIATION-001`：来源逐行登记完成，但 understanding claim 的直接句级语义裁决和关键 response→artifact/Git 因果仍需人工加深。
5. `Q-CONTEXT`/`Q-FRESH` 等 WebGPT 原始治理未知仍作为历史来源保留；新 Session/压缩恢复的宿主级模型实际消费不能由工具认证。

## 下一最小可验结果

先按固定顺序全文读取 generation-2 三件套，运行 `verify_core_cognition.py`、`verify_three_way_cognition.py`、`verify_understanding_merge.py` 和 `verify_cross_source_reconciliation.py`；随后做 source/hash freshness 与缺件/错序/孤儿的负向演练。数学研究保持暂停，直到用户明确恢复或交接证据链完成。
