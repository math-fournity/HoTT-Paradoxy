<!-- governance-shard-index:v2
logical_id: PATTERN_P_CONTINUOUS_FORGE_SOP
mode: topical
shard_root: 模式P刀具持续锻造SOP
last_shard: 模式P刀具持续锻造SOP/002 - 文献来源回流门与系统影响.md
append_target: -
soft_line_target: 300
-->

> ⚠️ 逻辑文档索引：全文 = 本索引 + 下方 2 个分片；缺一片即未完成，按表顺序读取。

# P-FORGE-SOP：模式 P 刀具持续锻造、新刀具出生与全历史自审

> **身份：** `TASK_SCOPED_CONTINUOUS_FORGING_SOP / USER_DIRECTED_PROCESS_CONTRACT / NOT_A_MATHEMATICAL_RESULT`。
>
> **稳定引用名：** `P-FORGE-SOP`。后续 `/goal` 可直接说“按 P-FORGE-SOP 对 <冻结理论卡／新花纹／Power Set 来源>继续”，或指定其中的阶段。对已经发生的锻打作逐原子全量审计时，改用其专门子合同 [P-FORGE-ATOMIC-AUDIT-SOP](<模式P原子锻打全量审计SOP.md>)。

## 用途与边界

本 SOP 把持续打磨 P1/P2/P3、审查新刀具、核对原初理念与实际锻造、让固定候选的 Q 生成／收紧／桥接／淘汰／会合、处理 Power Set 的已知防御、保存 Git 谱系，连成一条可执行的工作链。它路由到各现有 owner，不复制它们的字段或证据。

它不自动创建 Goal、启动 worker、联网、修改数学 STATE、给出数学结论或授予新的权限。每个理论节点仍遵循 P-DAG 的 TaskCard／NodeCard、当前用户授权与来源边界。粗粒度的自然单元自审不能声称已经覆盖实际运行分母；后者由 `P-FORGE-ATOMIC-AUDIT-SOP` 的 A0--A3 处理。

<!-- governance-shard-table:start -->
| Shard | 文件 | 语义范围 | 状态 |
|---|---|---|---|
| 001 | [操作合同、检查维度与幂集防御账本](<模式P刀具持续锻造SOP/001 - 操作合同、检查维度与幂集防御账本.md>) | 代码块逐项覆盖、阶段流程、`QConvergenceLink`、检查维度、`PowerSetDefenseLedger`、写回与 Git 合同、可引用启动句 | current |
| 002 | [文献来源回流门与系统影响](<模式P刀具持续锻造SOP/002 - 文献来源回流门与系统影响.md>) | 外部候选来源的 EvidenceEnvelope、I0--I4 分流、ForgeIntent 准入、三刀和站位影响 | current |
<!-- governance-shard-table:end -->
