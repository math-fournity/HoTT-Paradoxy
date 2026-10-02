# P3-FORGE-001：外部 Codex CLI 状态／完成分类盲测

> **身份：** `EXTERNAL_CLI_BEHAVIOR_PROBE / P3_FIXTURE_VALIDATION / NOT_A_MATHEMATICAL_RESULT`。
>
> **结论：** `P3_FIXTURE_CLASSIFICATION_PASS_WITH_SCOPE`。独立 Terra / Max 请求实例按冻结预期区分准入依赖环、有限阶段未完成和带终步的完成控制，并保留操作语义与数学理论之间的边界。

## 运行身份

| 字段 | 记录 |
|---|---|
| CLI | `codex-cli 0.157.0` |
| 工作根 | `/tmp/pattern-p-forge-p3-f1` |
| 模型请求 | `gpt-5.6-terra` |
| reasoning effort | `max` |
| sandbox / approval | `read-only` / `never` |
| session | `01a0fca5-f826-7cd0-9731-09428db42c6d` |
| prompt | `PROMPT.md`；禁读项目历史、网络、命令和历史名称 |

CLI 横幅显示模型、effort、sandbox 与 approval；`RESULT.md` 保存最终输出。

## 冻结夹具与输出

| Fixture | 预期 | Terra / Max 输出 | Master 判词 |
|---|---|---|---|
| P3-A | `BuildDone→NeedEval→OperatorUse→Admitted→BuildDone` | `ADMISSION_ORDER_CYCLE_CANDIDATE`，同时标 `CONSTRUCTION_SEMANTICS_NOT_SUPPLIED` | PASS |
| P3-B | 正值 `r` 仅有 `r→r/2`，Done 当且仅当 `r=0` | `FINITE_STAGES_REMAIN_PENDING` | PASS |
| P3-Bc | 阈值内有 `Final: r→0` | `COMPLETION_CONTROL_PRESENT`，并要求 δ、enabledness 与调度／fairness | PASS |

代理明确拒绝三种越界：从 cycle 推出无模型或全称不可能；从有限阶段未 Done 推出实际运行永不终止；从存在终步推断所有 schedule 都必完成。

## 结论边界

本次只验证 P3 的合成夹具分类能力。它不证明朴素集合论、芝诺、圆环、HoTT 或任何实际理论具有所给状态机；实际理论匹配仍须给每条状态和依赖边提供规则、实现或来源证据。
