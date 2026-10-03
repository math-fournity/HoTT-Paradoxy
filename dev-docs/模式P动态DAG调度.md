<!-- governance-shard-index:v2
logical_id: PATTERN_P_DYNAMIC_DAG_ORCHESTRATION
mode: topical
shard_root: 模式P动态DAG调度
last_shard: 模式P动态DAG调度/005 - 原初理念对照、自审与偏差处置.md
append_target: -
soft_line_target: 300
-->

> ⚠️ 逻辑文档索引：全文 = 本索引 + 下方 5 个分片；缺一片即未完成，按表顺序读取。

# 模式 P 刀具锻造与理念自审 SOP

> **正式名称：** `模式 P 刀具锻造与理念自审 SOP`。
>
> **旧称与定位：** “模式 P 动态 DAG 调度”是本 SOP 的旧标题与调度方式，不是另一份 SOP。后续 `/goal` 使用正式名称并引用本 canonical 路径。
>
> **身份：** `TASK_SCOPED_ORCHESTRATION_SOP / CURRENT_P_DAG_OWNER / NOT_A_MATHEMATICAL_RESULT`。
>
> **目的：** 本 SOP 让 Master 依照稳定的刀具理念，以条件驱动的 DAG 调度 P1、P2、P3、来源核对、反控制与 Battle 节点；每个自然单元都将实际工作与原初理念系统对照。它保留三把刀各自的发现惯性，也让分歧变成可回源检验的研究材料；它不把多代理一致、长解释或节点数量升级为 ZFC、HoTT 或任何数学理论的结论。

## 每次 `/goal` 的固定开工次序

新 `/goal`、恢复中的 `/goal`、压缩恢复或更换工作分支时，先完整读取[`刀具系统理念`](刀具系统理念.md)索引及其全部分片，然后完整读取本 SOP 索引与其全部分片，再核对 current Goal、项目任务角色、`MEMORY`／`STATE` 和相关 source/evidence。理念索引必须参与当前任务判断，不能只记录“曾经读过”或由历史审计摘要替代。完成该加载和 source-first 复述后，才冻结本轮 TaskCard。

后续 `/goal` 可直接写：**“执行《模式 P 刀具锻造与理念自审 SOP》”**，并引用路径 `dev-docs/模式P动态DAG调度.md`。

## 适用范围

本文件仅服务于模式 P 的共同锻造：当前是 ZFC Power Set 线与将来的 HoTT 盲重放。用户 2026-10-02 已明确允许 Master 按节点需要启动 Terra / Max 代理，也明确允许某些节点阅读项目 `dev`／`main`／其它分支或联网，而另一些节点必须保持盲态。每一个节点仍须由 Master 给出精确输入、权限、验收、停止和递归禁止；这不是无限代理授权。

<!-- governance-shard-table:start -->
| Shard | 文件 | 语义范围 | 状态 |
|---|---|---|---|
| 001 | [任务卡、角色与节点合同](<模式P动态DAG调度/001 - 任务卡、角色与节点合同.md>) | 当前任务范围、Master/worker 职责、TaskCard、NodeCard、输出与权限不变量 | current |
| 002 | [动态展开、访问等级与冻结接力](<模式P动态DAG调度/002 - 动态展开、访问等级与冻结接力.md>) | DAG 初始骨架、触发式扩展、盲态/来源/项目/网络访问和并行边界 | current |
| 003 | [Battle、裁决与收据](<模式P动态DAG调度/003 - Battle、裁决与收据.md>) | 分歧触发、互相质询、Master 参与和裁决、证据优先级、停止与写回 | current |
| 004 | [运行引擎、验证与治理影响](<模式P动态DAG调度/004 - 运行引擎、验证与治理影响.md>) | App Server/CLI 运行选择、启动回执与终态 TrajectoryReceipt、当前资格边界、验证计划和 C01–C10 影响表 | current |
| 005 | [原初理念对照、自审与偏差处置](<模式P动态DAG调度/005 - 原初理念对照、自审与偏差处置.md>) | 读取理念 owner；每个自然锻造单元的系统自审、原初讨论的完整复盘、偏差分类、纠偏与 Git 审计链 | current |
<!-- governance-shard-table:end -->

每次 `/goal` 还须先加载[刀具系统理念](<刀具系统理念.md>)的索引与全部分片；它是本 SOP 的理念输入 owner，不是本 SOP 的新增 shard。

## 总体不变量

1. DAG 的边表示**证据依赖**，不是谁的语言更有说服力；
2. P1、P2、P3 可并行，但任何下游会合只消费同一冻结 `T/u/F/C/Q/I/O/Done` 卡；
3. Master 可以提出候选或质询，却不能以自身意见跳过独立来源核对；
4. 各 worker 只读、无递归、无 Git/current-owner 写权；Master 是唯一 current-truth writer；
5. 网络、项目历史、其它分支与先前答案是否可见，逐 NodeCard 决定并留收据；
6. Battle 有界，不能用反复互相提示代替新增 source、控制或 Master 裁决；
7. `ZFC_Q_LOCATED` 仍须三刀在同一任务上会合，且不等于 ZFC 不一致、数学定理或现实哲学判词。
