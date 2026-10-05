# T-PRECISION-DIAGONAL-001：理论精度与哥德尔式自反启动闭包

> **身份：** AUDIT_CLOSURE / CROSS_SESSION_CAPSULE / T0_TOBS_001_COMPLETED_WITH_SCOPE。
>
> **稳定方案：** [T-PRECISION-DIAGONAL-SOP](../dev-docs/理论精度与哥德尔式自反方案.md)。
>
> **当前生命周期：** PLAN_ADOPTED_FOR_CONTINUED_EXECUTION / CONTINUOUS_T_EXECUTION_ACTIVE / T0_COMPLETED / T_OBS_C367_MACHINE_PROVED_WITH_SCOPE / TDIAG_G0_SOURCE_BOUND_WITH_SCOPE / NEXT_UNIT_AUTOMATICALLY_SELECTED_FROM_EVIDENCE_GAP。

## TaskDescriptor

| 字段 | 当前值 |
|---|---|
| 父结果 | 把“理论维度缺失／观察力不完备／理论精度”从 ZFC 的单点怀疑提升为可检验的想法 T；ZFC 是后续实例而非 T 的定义。 |
| 用户成功标准 | 两轮完整对话和后续的方案采纳／闭包续航指令被保存；稳定方案名可由 /goal 引用；未来 Session 能恢复并持续完成 T-OBS、T-DIAG、T-Meta、T-ZFC 的对象、证据、边界与下一动作。原子单元不是总体停机点。 |
| 当前 profile | RESEARCH_PROFILE_GOVERNED：T0 与一个 T-OBS 单元已完成；后续 T-DIAG/T-Meta/T-ZFC 将改变不同的研究决定，必须重新冻结单元，但 active 总体 Goal 下由 Master 自动选择后继。 |
| 主张等级 | USER_RESEARCH_HYPOTHESIS / AI_CANDIDATE_FORMAL_SPECIFICATION / NO_MATHEMATICAL_THEOREM_YET。 |
| canonical source | dev-docs/理论精度与哥德尔式自反方案.md 加四个 shards；用户 primary source 为 sources/prompts/Codex-理论精度与哥德尔式自反两轮用户原文-20261004.md 与 sources/prompts/Codex-T-PRECISION-DIAGONAL-SOP-采纳与闭包续航指令-20261004.md。 |
| 模块关系 | T-PRECISION-DIAGONAL-SOP 是上位程序；已存在的 GODEL-Q-REFLECTION-SOP 是 T-DIAG 的实际 completion-interface 执行模块，不是竞争方案。 |
| 主要风险 | 将“高精度”说成绝对强弱；把观察边界误称为不一致；将手写自指误称为对角化；将元层编码误称为原任务保真；将 C-359/C-364 升格为 T。 |

## 必须激活的来源

1. 方案 001：两轮逐字 user/assistant records，以及 user primary source；
2. 核心认知：KC-000024、KC-000027、KC-000036、KC-000059，及其相关扩展认知；
3. C-364：相对观察／因子化失败的有限控制；
4. C-359：带 SameFullQ、P、B 前提的条件性 policy consequence；
5. GODEL-Q-REFLECTION-SOP 与 CC-20261004-godel-q-reflection：仅当 T-DIAG 被选中时，作为其 G0--G5 执行模块；
6. ZFC-H0-FINAL-PROOF-CLOSURE-SOP：F-050 已有界收尾的 M0–M5 控制、禁止外推与重开条件；
7. 当前 Feature、MEMORY、rulings、Git HEAD/status。

## 当前已知与未支付项

| 项目 | 状态 | 证据边界 |
|---|---|---|
| T-OBS 的概念骨架 | C-367_MACHINE_PROVED_WITH_SCOPE | MP-T-PRECISION-TOBS-001 的 Lean core run 证明 abstract collision-to-no-decoder；C-364 仍是 source-bound finite calibration。 |
| T-DIAG 的哥德尔机制 | G0_SOURCE_BOUND_WITH_SCOPE / PARENT_ROUTE_UNADJUDICATED | GODEL-Q-REFLECTION-SOP 已冻结 set.mm proof-acceptance interface并重放通用哥德尔技术基线；但 parent `OriginDone`、保真 ρ、internal-provability adequacy与 actual diag 仍未支付。 |
| T-Meta 的 task bridge | OPEN | OriginDone／SameFullQ 不能由元层代码自动支付。 |
| T-ZFC | NOT_STARTED | C-359、C-364、C-366 仅是 controls。 |
| F-050 的 ZFC-H0 闭环 | CLOSED_WITH_SCOPE | 本 capsule 不授权重开、提交外部研究或宣布结论。 |

## 恢复算法

1. 若 T-PRECISION 的总体 Goal 处于 active，保留 T0/T-OBS-001 为已完成输入，并自动选择其证据缺口释放的下一 T-DIAG、T-Meta 或 T-ZFC 单元；只有用户明确暂停、取消或替换理论对象时才停止推进；
2. 读方案 index + 001–004、user primary source，再读本 capsule；
3. 从 T1–T5 中选择唯一最小且仍能改变总体结论的后继单元，冻结其 TaskPrecisionCard；T0 已由 T-OBS-001 完成；路由级受限负结论必须先检查是否释放别的后继，不能被当作总体完成；
4. 先写自己的候选、前提、反证和同一任务条件；
5. 再读一手数学来源与开源 formal source，比较理论变体；
6. 只有对象、接口和 proof target 已固定时才写机器证明；
7. 写回本 capsule 的“已知／未支付／下一动作”，并更新 Feature、MEMORY、证据 owner；
8. 若选择 T-DIAG，读取 GODEL-Q-REFLECTION-SOP 和其闭包，复用 G0--G5，不新增平行接口路线；
9. 若 T-ZFC 可能触及 F-050 的范围，先核其明示重开条件和用户授权；不得由本方案隐式推翻 CLOSED_WITH_SCOPE。

## 方案采纳与闭包续航增量（2026-10-04）

研究发起人已明确要求“走这个新的方案”，并要求在多个 Session 与压缩边界之间持续加载和写回相应闭包。此处将该要求落实为恢复合同，而不是将它误写成新的数学支付：

| 续航字段 | 当前合同 |
|---|---|
| 启动名 | `T-PRECISION-DIAGONAL-SOP`。直接调用时必须先读本 closure、方案 index 与全部四片。 |
| 活动层级 | 方案采纳本身没有自动执行后继；但研究发起人已经显式启动总体连续 Goal，因此 T0/T-OBS-001 是输入，G0 是现有 T-DIAG source-bound module，后继必须由 evidence gap 自动选择。 |
| 下一选择 | active 总体 Goal 下，Master 自动冻结唯一的、可判别的 T 单元；若选择 T-DIAG，先复用 GODEL-Q-REFLECTION-SOP 的 G0–G5，而不是重新创建 acceptance-interface 合同。 |
| 强制写回 | 新的用户过程合同、selected interface、T-DIAG/T-Meta/T-ZFC 的支付、失败、控制、来源身份、run 或停止条件分别写回其唯一 owner，并在本 closure 更新“已知／未支付／下一动作／重开条件”。 |
| 禁止越级 | `PLAN_ADOPTED`、C-367、一个来源沉默、一个条件性对角骨架或一个 host-level run 都不证明想法 T、bare ZFC 精度缺陷、actual Q 或 ZFC 对象语言矛盾。 |
| 失效触发 | 用户重定义 T 或选择具体单元；T/M/interface/OriginDone 变化；出现实际 source payment 或反例；proof assistant variant、Git HEAD/worktree owner 变化。触发后重建受影响 slice，再继续。 |

这次增量不要求建立第二份 closure：本文件已是 T 的唯一跨 Session capsule。新的采纳 source 进入其 source set；当前 Feature、MEMORY 与 rulings 各自保持需求、队列和用户裁定的单一职责。

## 失效与重开

本 closure 在下列情形失效并需增量重建：用户重定义 T、选择不同任务域 D、出现实际 Accept_ZFC source、找到可执行 diag/quotation、发现 C-359/C-364/C-367 的范围被误读、理论或 proof assistant variant 改变、或当前 worktree/owner 变更。

本 closure 不复制数学结论；它只保证未来工作者知道 T 的问题是什么、哪些条件尚未支付，以及从哪里恢复。两轮用户原文是否进入核心认知 generation 仍由 curation manager 处理；T0 已作出 CORE_CURATION_DEFERRED_WITH_EXPLICIT_TRIGGER 裁定：它们是已保存的 plan source，不是自动的 core current fact；新的 core generation 必须在研究发起人明确触发后作为独立 transaction 完成。
