<!-- governance-shard-index:v2
logical_id: P_FORGE_PQ_WARGAME_AUDIT
mode: sequential
shard_root: 20261003-P-FORGE-PQ-WARGAME
last_shard: 20261003-P-FORGE-PQ-WARGAME/004 - R02 真实来源对发现能力的消费.md
append_target: 20261003-P-FORGE-PQ-WARGAME/004 - R02 真实来源对发现能力的消费.md
soft_line_target: 300
-->

> ⚠️ 逻辑文档索引：全文 = 本索引 + 下方 4 个分片；缺一片即未完成，按表顺序读取。

# P-FORGE：P/Q共同锻造逐轮兵棋审计

> **身份：** `USER_REQUESTED_STEPWISE_METHOD_AUDIT / AUDIT_CAMPAIGN_ACTIVE / NOT_A_MATHEMATICAL_RESULT`。
>
> **审计问题：** 每一轮锻造是否实际让理论 X 的 Q 生成、收紧、桥接、淘汰或会合，或者仅改善了工具外观？每一轮都按当时可见材料重放，再以当前 `P/Q_CO_FORGING` 不变量作反事实推演；不以终局知识倒灌当时的判词。

<!-- governance-shard-table:start -->
| Shard | 文件 | 范围 | 状态 |
|---|---|---|---|
| 001 | [审计合同、轮次分母与兵棋规则](<20261003-P-FORGE-PQ-WARGAME/001 - 审计合同、轮次分母与兵棋规则.md>) | 范围、轮次地图、共同卡、证据纪律、逐步写回规则 | current |
| 002 | [R00 原初目标与锻造起点](<20261003-P-FORGE-PQ-WARGAME/002 - R00 原初目标与锻造起点.md>) | P 出现前的原初目标、P/Q关系与第一轮锻造的起点 | complete |
| 003 | [R01 第一轮夹具与发现能力](<20261003-P-FORGE-PQ-WARGAME/003 - R01 第一轮夹具与发现能力.md>) | P1/P2/P3初始夹具、外部分类与其对Q发现能力的作用 | complete; `Q_CAPABILITY_CALIBRATION` repaired |
| 004 | [R02 真实来源对发现能力的消费](<20261003-P-FORGE-PQ-WARGAME/004 - R02 真实来源对发现能力的消费.md>) | Delay、CFTT、Climber实际来源是否消费R01校准能力 | complete; Target/Candidate/Control-Q repaired |
<!-- governance-shard-table:end -->
