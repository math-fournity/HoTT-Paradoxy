<!-- governance-shard-index:v2
logical_id: P_FORGE_PARENT_RECONCILIATION
mode: sequential
shard_root: 20261003-P-FORGE-PARENT-RECONCILIATION
last_shard: 20261003-P-FORGE-PARENT-RECONCILIATION/002 - R02 真实来源对发现能力的消费.md
append_target: 20261003-P-FORGE-PARENT-RECONCILIATION/002 - R02 真实来源对发现能力的消费.md
soft_line_target: 300
-->

> ⚠️ 逻辑文档索引：全文 = 本索引 + 下方 2 个分片；缺一片即未完成，按表顺序读取。后续 R03--R13 只有在其原始汇总和全部已归属原子卡都被逐项比较后才加入表，缺一父级即不能进入 A3 综合。

# P-FORGE 父级回接审计

> **身份：** `A2_PARENT_RECONCILIATION / SOURCE_LIMITED_PARENT_COMPARISON / NOT_A_MATHEMATICAL_RESULT`。
>
> **当前状态：** `A2_ACTIVE / PARENT_CARDS=2/13 / PARENT_REMAINDER=11 / A3_NOT_STARTED`。

本逻辑文档将 128 张已封存的原子卡回接到原始 `R01--R13` 粗单元。`R00`、`R14`、`R15`是目标／最终综合／分母冻结的历史上下文，不替代这13个父级的逐项回接。每张父卡只给出：原汇总主张、成员分母、原子证据所支持的范围、被修正或撤回的部分、P/Q影响、财富与重开条件。

<!-- governance-shard-table:start -->
| Shard | 父级 | 原子成员 | 父级判词 |
|---|---|---|---|
| 001 | [R01 第一轮夹具与发现能力](<20261003-P-FORGE-PARENT-RECONCILIATION/001 - R01 第一轮夹具与发现能力.md>) | `N32,N06,N07,N08,N09` | `SUPPORTED_BY_COMPLETED_CHILDREN_WITH_SCOPE` |
| 002 | [R02 真实来源对发现能力的消费](<20261003-P-FORGE-PARENT-RECONCILIATION/002 - R02 真实来源对发现能力的消费.md>) | `N14,N15,N16,N17,N18,N19` | `SUPPORTED_BY_COMPLETED_CHILDREN` |
<!-- governance-shard-table:end -->
