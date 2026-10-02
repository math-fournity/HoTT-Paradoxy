# P1-FORGE-001：外部 Codex CLI 前提／Done 分类盲测

> **身份：** `EXTERNAL_CLI_BEHAVIOR_PROBE / P1_FIXTURE_VALIDATION / NOT_A_MATHEMATICAL_RESULT`。
>
> **结论：** `P1_POSITION_AND_STOP_DISCIPLINE_PASS_WITH_SCOPE`。独立 Terra / Max 请求实例准确给出芝诺夹具的理论位置与完成合同，也将圆环夹具保留为来源保持的强 Done 规格卡，拒绝把任何一项直接升级为悖论结论。

## 运行身份

| 字段 | 记录 |
|---|---|
| CLI | `codex-cli 0.157.0` |
| 工作根 | `/tmp/pattern-p-forge-p1-f1` |
| 模型请求 | `gpt-5.6-terra` |
| reasoning effort | `max` |
| sandbox / approval | `read-only` / `never` |
| session | `01a0fca9-2ca7-76b2-b5fc-14812da9f046` |
| prompt | `PROMPT.md`；禁止项目历史、网络、命令和历史名称 |

## 输出与 Master 判词

| Fixture | Terra / Max 输出 | Master 判词 |
|---|---|---|
| P1-F-001 芝诺 | 精确正值 halving 中，每个有限步骤仍 `r>0`；阈值＋终步是改变 execution premise 的 control；缺现实同一性、完整 transition relation 与同一任务证据 | PASS |
| P1-F-002 圆环 | 弱 Done（bare N 紧化）与强 Done（来源／边界／operation observations 保持）不同；bare compactification 不能冒充强复原；当前缺 formal relation、admissible repair、origin-preserving equivalence 与可行性证明 | PASS |

代理正确报告两案均 `NOT_READY_FOR_PARADOX_CLAIM`。这不是保守回避：它精确标出了 P1 下一步需要补的 evidence，而没有把紧化、极限或阈值 control 误写为同一任务答案。

## 结论边界

本次验证 P1 fixture 的位置／Done／task-switch 分类能力。芝诺、圆环的用户哲学和现实侧前提仍保持原身份；本次没有证明任何关于极限、时空、拓扑、HoTT 或现实完成性的数学／物理结论。
