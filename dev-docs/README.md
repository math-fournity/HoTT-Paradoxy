# 未定过程与设计工作区

这里保存尚未成为当前真值的调查方案、迁移草案、实验计划和审计过程。正式需求写根 `feature-list.md`，用户原意写 `rulings.md`，稳定设计写 `docs/`，当前状态写 `MEMORY.md`；不要把本目录的草案直接当成已实现或已验证。

当前主方案：[`实施方案-三AI历史整合与核心认知治理.md`](../实施方案-三AI历史整合与核心认知治理.md)。

- [T-PRECISION-DIAGONAL-SOP：理论精度、观察边界与哥德尔式自反方案](理论精度与哥德尔式自反方案.md)：研究发起人于 2026-10-04 要求把“理论维度缺失／观察力不完备／理论精度”作为想法 T 的上位研究程序，并完整保存紧邻两轮哥德尔式元／元元讨论。方案分为 T-OBS 相对观察精度、T-DIAG 自编码完成接口和 T-ZFC 实例化；跨 Session 的恢复入口为 `认知闭包/T-PRECISION-DIAGONAL-001.md`。当前严格处于 `PLAN_READY_NOT_EXECUTING`：它不自动恢复已暂停的 ZFC-H0 总证明 Goal，也不把 T、条件性观察边界或既有控制包写成 bare ZFC 缺陷定理。

- [GODEL-ZFC-CONVERGENCE-SOP：哥德尔式 ZFC 理论精度收敛闭环](哥德尔式ZFC理论精度收敛闭环SOP.md)：研究发起人要求未来 `/goal` 不再把一个来源、模型、compiler、局部形式化或 scoped negative 当作整条哥德尔—ZFC 路线的停止点。本 SOP 在不复制 T-PRECISION、R3–R4 和 ZFC-H0 M0–M5 的真值职责前提下，拥有它们之间的连续推进、successor、总完成状态机和跨 Session 恢复；对应闭包为 `认知闭包/GODEL-ZFC-CONVERGENCE-001.md`。稳定启动名是 `GODEL-ZFC-CONVERGENCE-SOP`；当前为 `GOAL_PREPARED_NOT_AUTOSTARTED`，不因文档存在自行恢复研究。

- [H0-Z0-FOUNDATION-ADEQUACY-SOP：从 main HoTT H0 反投影 ZFC 的基础验收](H0-Z0基础验收反投影SOP.md)：当前下一主线。它以 main 的 fixed Cubical HoTT H0 为 B，审计集合论模型／一致性／基础资格来源是否覆盖同一理论变体、是否有 H0Map、以及是否把 Done_meta 无支付地提升为理论／过程 adequacy。它把 C-364 保留为校准控制，禁止再用普通芝诺 application source 代替 main H0。

- [ZFC-H0-FINAL-PROOF-CLOSURE-SOP：ZFC 的 Q/P/A/B 总形式化与机器证明闭环](ZFC-H0最终形式化与机器证明闭环SOP.md)：总任务的执行合同。它把 H0→Z0 的来源停止改回一个局部事件，统一管理 fixed H0 semantic transport、A 侧真实过程、P/Q 的 bare-ZFC-facing 接口、SameFullQ 和最终结论；每一工作单元必须支付 M0–M5 的一个明确义务，不能用新的条件 fixture 冒充最终证明。

- [Goal任务项目治理化与全局复用方案](Goal任务项目治理化与全局复用方案-20260923.md)：本轮root/Skills/最高指示角色化接入、A/B Goal6单体闭包、全局两核心增量及C01–C10/验收边界。新提示词见[治理化入口](../第三轮机器统观/README.md)。

- [机器统观的多层次语义覆盖与格化组织方案](机器统观的多层次语义覆盖与格化组织方案-20260923.md)：保留形成时的候选设计与历史执行状态；不作当前选题模板。A/B闭包与提示词见[第三轮入口](../第三轮机器统观/README.md)。

- [第三轮机器统观多尺度覆盖改进工作方案](第三轮机器统观多尺度覆盖改进工作方案-20260923.md)：本轮直接实施的递归语义单元、关系、上下往返、粒度反事实与独立结案改进；操作合同在Goal5，实际证据见[再次自审](../audit/第三轮机器统观多尺度覆盖再次自审-20260923.md)。

- [菲尔兹奖后续理论级目标路线图](菲尔兹奖后续理论级目标路线图.md)：F-025/F-026 的未来选靶路线图。它区分基础理论靶标、可选的菲尔兹或其它原典入口、针对性过程、控制和证据；ZFC 及其它罗素之后理论先按第 007 片的罗素模式 P 重新资格化，H1–H9 只是机制线索。2026-10-03，研究发起人选择`FND-CONTINUUM-004`作候选资格化入口；其`ZFC-CIRCLE-Q0`卡冻结在[该审计](../audit/20261003-ZFC-CIRCLE-Q0-连续统完成与圆环复原候选卡.md)，仍不是Goal、STATE candidate或数学结论。Cohen/ZF(C) 与 ETCS 的结构—选择线仍未被选定。

- [模式 P 的三把刀：P1、P2、P3](模式P三把刀.md)：P1 的理论位置定位、P2 的计算—逻辑翻译、P3 的构造状态／准入次序，各自的打造惯性、正负控制、停止条件和持续横向比较；它们是研究工具草案，不是任何理论已有问题的结论。

- [刀具系统理念](刀具系统理念.md)：从罗素的计算—存在—自指张力到 P1/P2/P3 的不同惯性，说明案例怎样校准、发现怎样进入来源验证、为何“锻刀”与 ZFC Q 的定位共同推进，以及新刀何时才有出生资格。P-DAG 新开、恢复或改刀职责时先从这里恢复工作意识；原始用户来源和逐段运行证据仍分别由 sources/rulings 和 full origin audit 拥有。

- [P-FORGE-SOP：模式 P 刀具持续锻造、新刀具出生与全历史自审](模式P刀具持续锻造SOP.md)：用户可在后续 `/goal` 直接引用的总操作合同。它把持续打磨、Tool-BirthCard、理念—实作自审、全历史分母、`PowerSetDefenseLedger`、`CAL-0`至`CAL-4`校准、来源层与Power Set station审查，以及把每一锻绑定到Q的生成／收紧／桥接／淘汰／会合的`QConvergenceLink`串成一条流程；新增的`SourceBackflowGate`要求外部候选文献先经EvidenceEnvelope、R/Z/Q路线和I0--I4分流，只有I4才能提出ForgeIntent。每一细节仍路由到已有的三刀、P-DAG 与审计 owner。

- [P-FORGE-ATOMIC-AUDIT-SOP：模式 P 原子锻打全量审计](模式P原子锻打全量审计SOP.md)：对“锻刀＝发现 Q”的历史过程做逐原子、来源受限的兵棋审计。它将审计卡、粗自然单元、H 节点、non-H session/run、无 ID 执行和 Master 决策分开，先冻结精确分母，再逐卡重放、去重、写回与提交；不能用 R00--R14 的宏观综合代替实际锻打的全量审计。未来 `/goal` 可直接引用稳定名 `P-FORGE-ATOMIC-AUDIT-SOP`；该 SOP 不会自行恢复已暂停的 Goal 或启动新理论节点。

- [P-FORGE-LITERATURE-BACKFLOW-AUDIT-SOP：模式 P 路线级文献回流审计](P-FORGE路线级文献回流审计SOP.md)：将 HoTT 创建动机反投影 ZFC 的候选文献，按 R_i→Z_i→Q_i 与 H0→Z0→Q0 的路线卡回流既有 P-FORGE 审计。它固定 LiteratureEvidenceEnvelope、16 个 RB 维度、payment/route/layer/同一任务控制、I0--I4 选择性影响分流和 B0--B5 checklist；候选 worktree 未整合时只可产生候选性路线卡。未来 `/goal` 可直接引用稳定名 `P-FORGE-LITERATURE-BACKFLOW-AUDIT-SOP`，从 B0 证据冻结开始，不自动集成、启动 worker 或宣称 ZFC Q。

- [ZFC-Q-ACTUAL-INSTANCE-FORMALIZATION-SOP：ZFC 实际同 Q 实例化与机器证明](ZFC实际同Q实例化与机器证明SOP.md)：将 `ZFC-CIRCLE-Q0/Q1` 与 `ZFC-HOTT-Q2` 从条件性 bridge／QUniform fixture 推向版本固定的实际 Q 实例化，或给出有界的同 Q 不成立／来源政策不足结论。它分开原过程 Done、连续统模型 Done、来源级 acceptance policy、Cubical Agda 的固定 HoTT Q、Lean consequence 和跨证明器对应；未来 `/goal` 可直接引用稳定名 `ZFC-Q-ACTUAL-INSTANCE-FORMALIZATION-SOP`，首项为 A0 闭包与候选证据冻结，不自动集成候选 worktree、启动 worker、联网或宣称 ZFC 矛盾。

- [BARE-ZFC-Q-PRECISION-SOP：bare ZFC 的 Q 理论精度形式化](BareZFC理论精度Q形式化SOP.md)：研究发起人 2026-10-04 澄清后的上位路线。它将“bare ZFC 的理论精度不够”写成接口相对、可证伪的 Q 观察合同：固定 ZFC-facing interface、过程合同、投影、FormalDone、OriginDone、bridge/payment、来源 owner 和正反控制。当前执行已完成 P0/P1/P3 来源绑定及 C-364 的接口相对机器控制，结论为 `SOURCE_APPLICATION_INTERFACE_CONTROL_COMPLETE / BARE_SEMANTIC_INTERFACE_UNDERDETERMINED_WITH_SCOPE`；它继承而不重命名 C-359–C-363、ERCF/ZCore 的通用边界，不能把结果偷换成 ZFC 不可表示时间或对象语言矛盾。

- [模式 P 动态 DAG 调度](模式P动态DAG调度.md)：当前 P1/P2/P3 共同锻造的 Master 调度 SOP 与项目内 Skill。它把 worker 的盲态、来源、项目分支、网络、Battle、Master 裁决、App Server/CLI 运行资格和证据收据分成按节点决定的合同；只在用户 2026-10-02 的任务限定授权下使用。
