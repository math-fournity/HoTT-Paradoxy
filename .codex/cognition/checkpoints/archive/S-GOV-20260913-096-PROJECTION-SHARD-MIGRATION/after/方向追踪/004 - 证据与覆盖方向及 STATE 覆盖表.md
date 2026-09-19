<!-- governance-shard:v2
logical_id: DIRECTION
shard_id: 004
index: ../方向追踪.md
-->

# 证据与覆盖方向及 STATE 覆盖表

| direction_id | 方向 | 来源 | 当前状态 | 核心关联（初始主题级） | 已有结果 | 下一判别动作 | 证据入口 |
|---|---|---|---|---|---|---|---|
| `DIR-E-LOCAL-HISTORY-COVERAGE` | LocalGPT 38-turn lineage、ALL-Markdown、trajectory、Git 和工作产物的完整可审计性 | 顶层交接工程 | `SUPPORTING_DIRECTION` | `CORE_UNRELATED/GOVERNANCE_RULING` | `OUT-TOP-LEDGERS` | 完成 response→tool→artifact/code→Git 的语义映射，保留 dirty/缺源边界 | `audit/`；`sources/SOURCE_MANIFEST.json`；`private-audit/` |
| `DIR-E-WEB-HISTORY-COVERAGE` | WebGPT 56 Prompt/55 Response/111 UI sections 到 workspace records/artifacts/Git 的映射 | 顶层交接工程 | `SUPPORTING_DIRECTION` | `CORE_UNRELATED/GOVERNANCE_RULING` | `OUT-TOP-LEDGERS` | 将 WebGPT record IDs 与 integrated direction/result 双向对齐 | `audit/`；`workspace/.codex/research/hott/STATE.json`；`workspace/git log` |
| `DIR-G-UNDERSTANDING-RECONCILIATION` | 两个理解章节的逐文件语义融合和当前 canonical 路由 | 用户当前要求、顶层计划 | `SUPPORTING_DIRECTION` | `CORE_UNRELATED/GOVERNANCE_RULING` | `OUT-UNDERSTANDING-MERGE`（设计） | 当前 29/24 inventory 已逐文件处置；继续按 2,396 条历史 claim 的用户选择范围做直接语义/数学复核；C4 为新增顶层 current synthesis，不改写历史 claim 分母 | `理解章节/`；`AI对话录/理解章节/`；`audit/understanding-chapter-merge-manifest.json` |

## 4. WebGPT `STATE` 全记录覆盖表

这张表是“全部记录身份被纳入综合审计”的机械分母；逐项 source mapping 已由 `audit/cross-source-reconciliation.json` 完成，句级语义裁决仍按条目状态显式保留。

| STATE 前缀 | 数量 | 在本投影中的处理 | 主要去向 |
|---|---:|---|---|
| `P-*` | 10 | 每条建立一个或一个对应 integrated direction；结果链接见 `全景视野.md` | 方向/结果 |
| `U-*` | 4 | 用户方向/工作要求，先与 core/rulings 对照，不当作 AI 结果 | 用户方向/方向 |
| `Q-*` | 4 | 治理未知或来源缺口，保留 `UNKNOWN`/`REVIEW_REQUIRED` | 证据/未知 |
| `R-*` | 1 | 历史恢复记录，不直接进入当前数学主线 | 历史结果 |
| `A-*` | 3 | 附件/来源审计身份，连接附带结果 | 证据/结果 |
| `C-*` | 10 | candidate/claim 结果，保留 paper/native/novelty 分层 | 结果 |
| `D-*` | 13 | Gemini 往来和同行意见，保留转述/未发送/收到状态 | 证据/结果 |
| `S-*` | 41 | Session 过程记录，作为结果的时间/依赖证据，不独立制造新方向 | session/结果 |
| `V-*` | 5 | 验证或有限模型结果，保留 `NOT_RUN`/范围 | 结果/证据 |
| **合计** | **91** | **无记录静默删除；仍需句子级语义映射** | `STATE.json` |

