# P-DAG-HOTT-DISCOVERY-008：Codex App Server 事后 trajectory 审计

> **身份：** `POST_TERMINAL_TRAJECTORY_AUDIT / PARTIAL_RUNTIME_EVIDENCE / NOT_A_HOTT_RESULT`。
>
> **审计对象：** 已完成的 `P-DAG-HOTT-DISCOVERY-008` 隔离 App Server 节点；本文件不重跑模型，
> 不公开 prompt、assistant 全文或 reasoning，也不改变其已经完成的原典支付判词。

## 1. 审计问题与来源身份

本审计回答的不是“HoTT 候选是否成立”，而是：H008 的受控运行在终态后，是否有足以重建其
thread／turn／item、工具与终态边界的 Host trajectory；其可见 reasoning 到什么程度；哪些 L1–L5
结论仍不能从该轨迹推出。

| 项 | 值 |
|---|---|
| 运行节点 | `P-DAG-HOTT-DISCOVERY-008` |
| thread ID | `01a0fdec-5164-7343-81c0-a3b8fd6e1a9d` |
| turn ID | `01a0fdec-522d-7be3-a868-0df316ac9e17` |
| raw source | 私有双向 App Server wire：`{timestamp,direction,message}` JSONL |
| wire identity | 496 records、185742 bytes、SHA-256 `506da9367912824ccc42700be138971280f73368bbb042e313c69f5cdb00fc9b`；4 outbound／492 inbound |
| persisted rollout | 在本 run root 中未找到 `rollout-*.jsonl` |
| reader | `governance-v3.26.1` shared `session_trajectory.py`；source commit `6b6352f`，实际可执行 mirror commit `4165306` |
| privacy | raw wire、prompt-input、final、stderr与 context extracts 保留在 0700/0600 私有实验目录；本审计只记录 ID、计数、hash、命令和范围 |

因此来源状态为：

```text
PERSISTED_ROLLOUT_UNAVAILABLE /
BIDIRECTIONAL_APP_SERVER_WIRE_AVAILABLE
```

缺少 rollout 不能写成“没有 trajectory”。反过来，wire 不含完整 injected system body，也不能充当
L1 context injection 的替代品。

## 2. 审计方法与可复现收据

先前的 shared reader 将该 wire 全部归为 `unknown`。依据脱敏实际 envelope fixture 完成
`governance-v3.26.1` adapter 后，按下列顺序重审：

1. `catalog --host codex --source <private-wire>` 固定 source、thread、cwd 与字节身份；
2. `tree --host codex --session <thread> --recursive` 重建 session/turn 和 event counts；
3. 仅对 `tool_call`、`tool_result`、`approval_request`作 filtered scan；
4. 执行无 expected body 的 `coverage`，避免把未给出的 context/read source 伪装成 PASS；
5. 将 user/assistant context 分别写入私有 0600 文件，不在此处复制正文。

私有 extract receipt：user context=2 events，SHA-256
`c829c0dcaab2a76d9b36bde43d9ccde438be2ad7ac028a9a71e8e8e5ee5f902a`；assistant context=464 events，SHA-256
`508a6b8d1e3359103ccbf9216e97684eb20cc8c1043faf2571db30c61ddf7880`。两文件 mode 均为 `0600`。

## 3. 可观察运行时间线

tree 对一个 thread 和一个 terminal turn 产生如下计数：

| 事件类别 | 计数 | 可支持的有限事实 |
|---|---:|---|
| `turn_started` / `turn_start_ack` | 1 / 1 | 一个 App Server turn 被接受并开始 |
| `turn_completed` | 1 | 该 turn 以 Host 可见 terminal 状态结束 |
| `assistant_message` / delta | 1 / 455 | Host 输出了一条完成消息及其 transport deltas；不公开正文 |
| `reasoning` summary item / delta | 3 / 6 | Host 提供了可见 summary；不是完整 reasoning |
| `tool_call` / `tool_result` / `approval_request` | 0 / 0 / 0 | 本 wire 没有可解析的此三类事件 |
| `thread_status` / `usage` / other app-server events | 2 / 1 / 9 | lifecycle 与 transport metadata 存在 |

这与 H008 原运行收据的 `command=0, file-change=0, approval-request=0`相容。它不能证明所有可能的
未导出 Host 行为均不存在，不能证明模型没有在训练知识中持有某信息，也不能代替 source validation。

## 4. L1–L5 分层判词

| 层 | 判词 | 证据与边界 |
|---|---|---|
| L1 context injection | `NOT_TESTED` | direct wire 可见 turn input 和 `instructionSources`路径回显，但没有完整 raw system/instruction body 的 exact compare。 |
| L2 selected-read coverage | `NOT_OBSERVED` | filtered scan 观察到0个tool call/result；这不等于“所有文件未读”或任何 target file 的完整性判词。 |
| L3 model recall | `NOT_TESTED` | H008 是一次有界 discovery run；没有独立 fresh recall prompt与对照。 |
| L4 cognition execution | `REQUIRES_SEMANTIC_REVIEW` | event order 和 terminal 可审计，但是否正确消费 D-L5/D-L6b、何种 reasoning 形成候选，不能从 summary或最终文本自动推出。 |
| L5 behavior verdict | `REQUIRES_ACCEPTANCE_EVIDENCE` | NodeCard schema check、output contract与随后 `hlevel-prod` source payment各有范围；它们不合成一般 runtime behavior或 HoTT replay PASS。 |

reasoning 的唯一合法描述是：App Server 导出了若干 **summary** 事件；完整 reasoning 若被加密、红删或未导出，
状态为 `OPAQUE/UNAVAILABLE`。本审计没有尝试从 final text、delta 次数或时序推断它。

## 5. 对 P-DAG 的影响

1. H008 的 `SOURCE_DERIVED_PAYMENT_CONTROL / NO_HOTT_REPLAY_PASS` 保持不变；这次审计没有增加新的
   HoTT 或 ZFC 数学结论。
2. 未来任何在 App Server 终态上做材料性解释的 P 节点，必须在 NodeCard 中预先声明 trajectory policy，
   并在终态后生成同类 `TrajectoryReceipt`。
3. 新 direct App Server wire 若被 reader 标为 `unknown`，应报告
   `TRAJECTORY_PARSER_COVERAGE_GAP`，隔离该节点的行为解释；先以脱敏真实 shape补 fixture、测试、共享 reader
   和 capability记录，再重审。不应拿 terminal output、模型自述或 zero activity block 填补该缺口。

相关证据：[H008 NodeCard](20261002-P-DAG-HOTT-DISCOVERY-008-APPSERVER-NODECARD.md)、
[运行收据](20261002-P-DAG-HOTT-DISCOVERY-008-APPSERVER-Terra-Max.md)、
[原典支付控制](20261002-P-DAG-HOTT-DISCOVERY-008-SOURCE-VALIDATION.md)。
