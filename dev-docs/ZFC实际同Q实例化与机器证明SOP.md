<!-- governance-shard-index:v2
logical_id: ZFC_Q_ACTUAL_INSTANCE_FORMALIZATION_SOP
mode: topical
shard_root: ZFC实际同Q实例化与机器证明SOP
last_shard: ZFC实际同Q实例化与机器证明SOP/003 - 执行检查表、停止与自审.md
append_target: -
soft_line_target: 300
-->

> ⚠️ 逻辑文档索引：全文 = 本索引 + 下方 3 个分片；缺一片即未完成，按表顺序读取。

# ZFC-Q-ACTUAL-INSTANCE-FORMALIZATION-SOP：ZFC 实际同 Q 实例化与机器证明 SOP

> **身份：** `TASK_SCOPED_ACTUAL_Q_FORMALIZATION_AND_PROOF_SOP / P_Q_CO_FORGING_EXTENSION / NOT_A_PREDECLARED_ZFC_INCONSISTENCY`。
>
> **稳定引用名：** `ZFC-Q-ACTUAL-INSTANCE-FORMALIZATION-SOP`。
>
> **当前准备状态：** `PLAN_READY / ACTUAL_Q_INSTANCE_NOT_YET_FORMALIZED / NO_ZFC_POLICY_CONFLICT_CLAIM`。

## 目标

把目前已机器检查的条件性结论

```text
same full QProfile + opposite judgments → ¬ QUniform
```

推进为对**实际、版本固定的**圆环／芝诺过程、ZFC 支撑的标准连续统解法、固定 HoTT `QuestioningDelay` Q 与来源级基础验收政策的可审计实例化；或者以同等严格度证明它们不能构成同一个完整 Q。它不预设哪一种结果会成立。

本 SOP 继承 `P-FORGE-SOP`、`P-FORGE-LITERATURE-BACKFLOW-AUDIT-SOP`、`ZFC-CIRCLE-Q0/Q1` 与 `ZFC-HOTT-Q2` 的 owner，不创建第二套 current state、第二套 P1/P2/P3 或自动的数学判词。

## 逻辑全文分片

<!-- governance-shard-table:start -->
| Shard | 文件 | 语义范围 | 状态 |
|---|---|---|---|
| 001 | [任务身份与实际Q合同](<ZFC实际同Q实例化与机器证明SOP/001 - 任务身份与实际Q合同.md>) | TaskDescriptor、实际 Q 的数据合同、层级与证据状态、成功／拒绝边界 | current |
| 002 | [来源绑定与跨证明器机器化](<ZFC实际同Q实例化与机器证明SOP/002 - 来源绑定与跨证明器机器化.md>) | 候选来源回流、Zeno/continuum/HoTT/policy绑定、Lean–Cubical Agda 证明架构与控制 | current |
| 003 | [执行检查表、停止与自审](<ZFC实际同Q实例化与机器证明SOP/003 - 执行检查表、停止与自审.md>) | 阶段清单、P/Q共同锻造、验证、写回、停止／重开和 `/goal` 启动词 | current |
<!-- governance-shard-table:end -->

## 直接调用

```text
按照SOP=ZFC-Q-ACTUAL-INSTANCE-FORMALIZATION-SOP，继续推进，直至无法推进。
```

该调用先重建本 SOP 指定的输入闭包和候选分支证据冻结；不自动集成 candidate worktree、启动 worker／网络、修改数学 STATE、tag、push 或宣称 ZFC 有形式矛盾。
