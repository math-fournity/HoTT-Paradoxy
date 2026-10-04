# T-PRECISION-DIAGONAL-001：理论精度与哥德尔式自反启动闭包

> **身份：** AUDIT_CLOSURE / CROSS_SESSION_CAPSULE / PLAN_READY_NOT_EXECUTING。
>
> **稳定方案：** [T-PRECISION-DIAGONAL-SOP](../dev-docs/理论精度与哥德尔式自反方案.md)。
>
> **当前生命周期：** READY / NOT_STARTED / DOES_NOT_RESUME_PAUSED_ZFC_H0_GOAL。

## TaskDescriptor

| 字段 | 当前值 |
|---|---|
| 父结果 | 把“理论维度缺失／观察力不完备／理论精度”从 ZFC 的单点怀疑提升为可检验的想法 T；ZFC 是后续实例而非 T 的定义。 |
| 用户成功标准 | 两轮完整对话被保存；稳定方案名可由 /goal 引用；未来 Session 能恢复 T-OBS、T-DIAG、T-ZFC 的对象、证据、边界与下一动作。 |
| 当前 profile | RESEARCH_PROFILE_PREPARE_ONLY：方案和闭包已经准备，尚未启动 T0 或改变已暂停 Goal。 |
| 主张等级 | USER_RESEARCH_HYPOTHESIS / AI_CANDIDATE_FORMAL_SPECIFICATION / NO_MATHEMATICAL_THEOREM_YET。 |
| canonical source | dev-docs/理论精度与哥德尔式自反方案.md 加四个 shards；用户 primary source 为 sources/prompts/Codex-理论精度与哥德尔式自反两轮用户原文-20261004.md。 |
| 模块关系 | T-PRECISION-DIAGONAL-SOP 是上位程序；已存在的 GODEL-Q-REFLECTION-SOP 是 T-DIAG 的实际 completion-interface 执行模块，不是竞争方案。 |
| 主要风险 | 将“高精度”说成绝对强弱；把观察边界误称为不一致；将手写自指误称为对角化；将元层编码误称为原任务保真；将 C-359/C-364 升格为 T。 |

## 必须激活的来源

1. 方案 001：两轮逐字 user/assistant records，以及 user primary source；
2. 核心认知：KC-000024、KC-000027、KC-000036、KC-000059，及其相关扩展认知；
3. C-364：相对观察／因子化失败的有限控制；
4. C-359：带 SameFullQ、P、B 前提的条件性 policy consequence；
5. GODEL-Q-REFLECTION-SOP 与 CC-20261004-godel-q-reflection：仅当 T-DIAG 被选中时，作为其 G0--G5 执行模块；
6. ZFC-H0-FINAL-PROOF-CLOSURE-SOP：现有 M0–M5 义务与禁止外推；
7. 当前 Feature、MEMORY、rulings、Git HEAD/status。

## 当前已知与未支付项

| 项目 | 状态 | 证据边界 |
|---|---|---|
| T-OBS 的概念骨架 | SPECIFIED_NOT_PROVED | C-364 是有限 calibration，不是一般定理。 |
| T-DIAG 的哥德尔机制 | MODULE_READY_NOT_INSTANTIATED | GODEL-Q-REFLECTION-SOP 已定义 G0--G5 与 GodelizationCard；当前仍没有真实 Accept_ZFC、保真 ρ 或 diag。 |
| T-Meta 的 task bridge | OPEN | OriginDone／SameFullQ 不能由元层代码自动支付。 |
| T-ZFC | NOT_STARTED | C-359、C-364、C-366 仅是 controls。 |
| paused ZFC-H0 Goal | PAUSED | 本 capsule 不授权恢复、提交外部研究或宣布结论。 |

## 恢复算法

1. 先核当前用户是否明确启动 T-PRECISION-DIAGONAL-SOP；若没有，保持本 capsule 为准备材料；
2. 读方案 index + 001–004、user primary source，再读本 capsule；
3. 从 T0–T5 中选择唯一最小单元，冻结其 TaskPrecisionCard；
4. 先写自己的候选、前提、反证和同一任务条件；
5. 再读一手数学来源与开源 formal source，比较理论变体；
6. 只有对象、接口和 proof target 已固定时才写机器证明；
7. 写回本 capsule 的“已知／未支付／下一动作”，并更新 Feature、MEMORY、证据 owner；
8. 若选择 T-DIAG，读取 GODEL-Q-REFLECTION-SOP 和其闭包，复用 G0--G5，不新增平行接口路线；
9. 若 T-ZFC 需要恢复原 Goal，必须由用户明确恢复，不能由本方案隐式解除暂停。

## 失效与重开

本 closure 在下列情形失效并需增量重建：用户重定义 T、选择不同任务域 D、出现实际 Accept_ZFC source、找到可执行 diag/quotation、发现 C-359/C-364 的范围被误读、理论或 proof assistant variant 改变、或当前 worktree/owner 变更。

本 closure 不复制数学结论；它只保证未来工作者知道 T 的问题是什么、哪些条件尚未支付，以及从哪里恢复。两轮用户原文是否进入核心认知 generation 仍由 curation manager 处理；在此之前，它们是已保存的 plan source，不是自动的 core current fact。
