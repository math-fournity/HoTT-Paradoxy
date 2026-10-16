<!-- governance-shard-index:v2
logical_id: PATTERN_P_DYNAMIC_DAG_ORCHESTRATION
mode: topical
shard_root: 模式P动态DAG调度
last_shard: 模式P动态DAG调度/005 - 原初理念对照、自审与偏差处置.md
append_target: -
soft_line_target: 300
-->

> ⚠️ 逻辑文档索引：全文 = 本索引 + 下方 5 个分片；缺一片即未完成，按表顺序读取。

# 模式 P 动态 DAG 调度

> **身份：** `TASK_SCOPED_ORCHESTRATION_SOP / CURRENT_P_DAG_OWNER / NOT_A_MATHEMATICAL_RESULT`。
>
> **目的：** 本 SOP 让 Master 以条件驱动的 DAG 调度 P1、P2、P3、来源核对、反控制与 Battle 节点。它保留三把刀各自的发现惯性，也让分歧变成可回源检验的研究材料；它不把多代理一致、长解释或节点数量升级为 ZFC、HoTT 或任何数学理论的结论。

## 开工前的理念入口

新开或恢复 P-DAG、准备修改 P1/P2/P3 的职责、提出新刀或改变成功定义时，先读 [刀具系统理念](<刀具系统理念.md>) 的完整逻辑文档。它让 Master 先回答“这次节点在保护哪一项原初发现动作”，再冻结 TaskCard；它不替代本 SOP 的 NodeCard、来源、权限、trajectory 或同一任务证据。需要把原初讨论与实际运行逐段相对照时，再按 005 的条件进入 full origin audit。

用户若在 `/goal` 中引用 `P-FORGE-SOP`，或要求连续锻造、新刀出生、全历史自审／对照和 Power Set 防御审查，先完整读 [P-FORGE-SOP](<模式P刀具持续锻造SOP.md>)。它协调本 SOP、三刀、full audit 与 Git 写回，要求每个节点以 `QConvergenceLink` 说明其怎样让固定Q卡生成、收紧、桥接、淘汰、会合或免于误报；新增的 `PowerSetDefenseLedger` 让任何“超越 Power Set 的罗素防御”候选先面对具体来源 guard；它不替代本 SOP 的逐节点授权。用户若明确引用 `P-FORGE-ATOMIC-AUDIT-SOP`，还须完整读 [模式 P 原子锻打全量审计 SOP](<模式P原子锻打全量审计SOP.md>)：它先分开审计卡、粗自然单元和实际运行分母，再进行逐单位历史重放；在 A0--A3 审计中不得因该引用启动新的理论 worker。

当外部候选 worktree、文献调查或来源综合被拿来改变 P-FORGE 的任何判断时，先完成 [路线级文献回流审计 SOP](<P-FORGE路线级文献回流审计SOP.md>) 的 B0--B3：candidate-only I0/I1不能生成TaskCard，I2/I3须经CURRENT_EVIDENCE，只有I4才可成为新的ForgeIntent入口。该门不会把文献调用变成一般worker授权。

## 适用范围

本文件仅服务于模式 P 的共同锻造：当前是 ZFC Power Set 线与将来的 HoTT 盲重放。用户 2026-10-02 已明确允许 Master 按节点需要启动 Terra / Max 代理，也明确允许某些节点阅读项目 `dev`／`main`／其它分支或联网，而另一些节点必须保持盲态。每一个节点仍须由 Master 给出精确输入、权限、验收、停止和递归禁止；这不是无限代理授权。

<!-- governance-shard-table:start -->
| Shard | 文件 | 语义范围 | 状态 |
|---|---|---|---|
| 001 | [任务卡、角色与节点合同](<模式P动态DAG调度/001 - 任务卡、角色与节点合同.md>) | 当前任务范围、Master/worker 职责、TaskCard、NodeCard、`QConvergenceLink`、输出与权限不变量 | current |
| 002 | [动态展开、访问等级与冻结接力](<模式P动态DAG调度/002 - 动态展开、访问等级与冻结接力.md>) | DAG 初始骨架、触发式扩展、盲态/来源/项目/网络访问和并行边界 | current |
| 003 | [Battle、裁决与收据](<模式P动态DAG调度/003 - Battle、裁决与收据.md>) | 分歧触发、互相质询、Master 参与和裁决、证据优先级、停止与写回 | current |
| 004 | [运行引擎、验证与治理影响](<模式P动态DAG调度/004 - 运行引擎、验证与治理影响.md>) | App Server/CLI 运行选择、启动回执与终态 TrajectoryReceipt、当前资格边界、验证计划和 C01–C10 影响表 | current |
| 005 | [原初理念对照、自审与偏差处置](<模式P动态DAG调度/005 - 原初理念对照、自审与偏差处置.md>) | 每个自然锻造单元的系统自审、P/Q共同涌现、原初讨论的完整复盘、偏差分类、纠偏与 Git 审计链 | current |
<!-- governance-shard-table:end -->

## 总体不变量

1. DAG 的边表示**证据依赖**，不是谁的语言更有说服力；
2. P1、P2、P3 可并行，但任何下游会合只消费同一冻结 `T/u/F/C/Q/I/O/Done` 卡；
3. Master 可以提出候选或质询，却不能以自身意见跳过独立来源核对；
4. 各 worker 只读、无递归、无 Git/current-owner 写权；Master 是唯一 current-truth writer；
5. 网络、项目历史、其它分支与先前答案是否可见，逐 NodeCard 决定并留收据；
6. Battle 有界，不能用反复互相提示代替新增 source、控制或 Master 裁决；
7. `ZFC_Q_LOCATED` 仍须三刀在同一任务上会合，且不等于 ZFC 不一致、数学定理或现实哲学判词。
8. 每一 P-FORGE 节点必须有可证伪的 `QConvergenceLink`；没有Q状态变化或固定卡防误报作用的工具复杂化是 `TOOL_ONLY_DRIFT`，不计作共同锻造推进。
