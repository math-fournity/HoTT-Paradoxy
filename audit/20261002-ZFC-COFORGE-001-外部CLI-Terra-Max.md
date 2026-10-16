# ZFC-COFORGE-001：联合三刀无泄漏映射盲测

> **身份：** `EXTERNAL_CLI_BEHAVIOR_PROBE / ZFC_CO_FORGING_DIAGNOSTIC / NOT_A_ZFC_RESULT`。
>
> **结论：** `ZFC_SITE_SELECTED_ONLY / JOINT_PROMPT_P1_DRIFT / NO_COMMON_Q`。联合 prompt 未定位 ZFC Q；它暴露了共同锻造协议中 P2/P3 约束污染 P1 独立选靶的缺口。

## 运行身份

| 字段 | 记录 |
|---|---|
| CLI | `codex-cli 0.157.0` |
| 工作根 | `/tmp/pattern-p-zfc-coforge-001` |
| 模型请求 / effort | `gpt-5.6-terra` / `max` |
| sandbox / approval | `read-only` / `never` |
| session | `01a0fce9-bb7a-7723-9a12-44f0390c4abd` |
| prompt | 中性 ZFC card + P1/P2/P3 同时要求；禁止项目、网络、历史答案和名称 |

## 输出

代理选择 bounded separation instance，而不是此前 P1 单独盲测所选择的 Power Set。其 P1 卡中 `u` 是有界子集，`F` 是 schema-level bounded separation，`Q` 是外部 formula predicate；P2 正确拒绝 formula binder／representation／reentry；P3 正确拒绝 lifecycle。最终为 `ZFC_SITE_SELECTED_ONLY`。

## Master 判词

本次未产生 `ZFC_Q_LOCATED`，但产生了决定性方法证据：将 P2/P3 条件预先放入与 P1 同一提示时，P1 的选靶会被“哪个候选更容易填 P2/P3 字段”反向牵引，导致从 Power Set 漂到 bounded separation。这破坏了三把刀各自的惯性。

下一协议必须三阶段：

1. P1 先在独立无泄漏 session 中选择并冻结 `u/F/C`；
2. P2/P3 仅消费该冻结 P1 卡和同一 source card，不得重选候选；
3. Master 比较是否在同一 Q/Done 会合。

这次输出本身不能支持 bounded separation 是更好的 ZFC 靶，也不能支持 ZFC 有问题。
