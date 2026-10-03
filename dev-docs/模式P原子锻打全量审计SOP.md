<!-- governance-shard-index:v2
logical_id: PATTERN_P_FORGE_ATOMIC_AUDIT_SOP
mode: topical
shard_root: 模式P原子锻打全量审计SOP
last_shard: 模式P原子锻打全量审计SOP/003 - 顺序执行、写回与完成判据.md
append_target: -
soft_line_target: 300
-->

> ⚠️ 逻辑文档索引：全文 = 本索引 + 下方 3 个分片；缺一片即未完成，按表顺序读取。

# P-FORGE-ATOMIC-AUDIT-SOP：模式 P 原子锻打全量审计 SOP

> **身份：** `TASK_SCOPED_ATOMIC_AUDIT_SOP / P_Q_CO_FORGING_AUDIT_CONTRACT / NOT_A_MATHEMATICAL_RESULT`。
>
> **稳定引用名：** `P-FORGE-ATOMIC-AUDIT-SOP`。

## 用途、起点与边界

本 SOP 把“锻刀与发现 ZFC 的 Q 是同一个共同涌现过程”落实为一次可复算的历史审计：逐个实际锻打单位回到其当时的
来源、输入、运行、产物和方法状态，判断它对 P/Q 收敛实际作了什么贡献。它不把 P1/P2/P3 的元层记录与 Q 的发现
拆成两项交付，也不允许用一次总综合替代逐单位的兵棋推演。

它解决已发现的范围错误：`R00--R14` 的 15 张审计卡、其中的 13 个粗粒度自然单元，和全历史实际执行的原子单位
不是同一分母。当前 [P-FORGE 原子锻打账本](<../audit/20261003-P-FORGE-ATOMIC-LEDGER.md>) 已登记 `H001--H075`，
并保留 non-H 执行族的去重待办；它是本 SOP 的分母 owner，不是数学结论。

本 SOP 只标准化历史审计。它不自动恢复暂停的 `/goal`、不启动新理论 worker 或网络节点、不改变 `STATE`、不创建新刀，
也不把审计结论升级为 ZFC、HoTT 或任何数学理论的矛盾结论。未来需要新 ForgeIntent 或 NodeCard 时，仍回到
[`P-FORGE-SOP`](<模式P刀具持续锻造SOP.md>) 与 [模式 P 动态 DAG 调度](<模式P动态DAG调度.md>)。

<!-- governance-shard-table:start -->
| Shard | 文件 | 语义范围 | 状态 |
|---|---|---|---|
| 001 | [分母、范围与原子身份](<模式P原子锻打全量审计SOP/001 - 分母、范围与原子身份.md>) | 原子单位定义、计数层级、去重、分母冻结和 A0 门 | current |
| 002 | [AtomicAuditCard与证据重放](<模式P原子锻打全量审计SOP/002 - AtomicAuditCard与证据重放.md>) | 单卡字段、当时态重放、trajectory、P/Q 判词、反事实与财富 | current |
| 003 | [顺序执行、写回与完成判据](<模式P原子锻打全量审计SOP/003 - 顺序执行、写回与完成判据.md>) | A0--A3 顺序、逐卡 Git 谱系、验证、停止和 `/goal` 启动句 | current |
<!-- governance-shard-table:end -->
