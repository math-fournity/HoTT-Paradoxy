# P2-FORGE-001：外部 Codex CLI 分类盲测

> **身份：** `EXTERNAL_CLI_BEHAVIOR_PROBE / P2_FIXTURE_VALIDATION / NOT_A_MATHEMATICAL_RESULT`。
>
> **结论：** `P2_FIXTURE_CLASSIFICATION_PASS_WITH_SCOPE`。外部 Terra / Max 请求实例按冻结预期区分 P2-F-001、F-002、F-003；此结果只支持该 prompt、模型请求、夹具和运行面的行为范围。

## 运行身份

| 字段 | 记录 |
|---|---|
| CLI | `codex-cli 0.157.0` |
| 工作根 | `/tmp/pattern-p-forge-p2-f1`，独立 scratch directory |
| 模型请求 | `gpt-5.6-terra` |
| reasoning effort | `max` |
| sandbox | `read-only` |
| approval | `never` |
| session | `01a0fca3-9498-71f0-b8d6-255b9a65648b` |
| prompt | `PROMPT.md`；禁止项目历史、外部文件、网络、命令和历史名称 |
| Host output | CLI 启动横幅实际显示 model、provider、sandbox 与 reasoning effort；输出保存在 scratch 的 `RESULT.md`。 |

第一次命令因全局 CLI 参数位置错误而在模型启动前退出；第二次使用正确的全局 `--no-daemon`、`-m`、`model_reasoning_effort`、sandbox 与 approval 参数完成。该工具错误不改变 fixture，也不产生模型结果。

## 冻结夹具与输出

| Fixture | 冻结预期 | Terra / Max 输出 | Master 判词 |
|---|---|---|---|
| P2-F-001 | 无限制 formation、全域双向 bridge、合法 reentry、负极性 → `q↔¬q` | `MATCHED / FINITE_SPECIFICATION_CONFLICT_CANDIDATE`，要求 theory-specific logic oracle | PASS |
| P2-F-002 | bridge 仅在 `a` 内成立，未证 `u∈a` → guard 阻断 | `GUARD_BLOCKED`，拒绝把 formation 推成 reentry 合法 | PASS |
| P2-F-003 | 正极性自代 → `q↔q` | `MATCHED / NONCONFLICTING_OR_UNDECIDED_FEEDBACK` | PASS |

代理还准确保留了两个边界：`↔` 与 `¬` 的含义需由理论实际逻辑固定；有界环境可能另有未提供的 closure／reentry rule，故不能把 fixture 的 guard 结果外推为一般定理。

## 结论边界

本次验证了 P2/v0 的**分类夹具**：代理能稳定遵守 bridge 域、合法回代、极性和 logic oracle 的分层。它未验证 P2 对 HoTT、ZFC 或任何实际理论的匹配能力，也没有机器证明、来源核验或数学结论。
