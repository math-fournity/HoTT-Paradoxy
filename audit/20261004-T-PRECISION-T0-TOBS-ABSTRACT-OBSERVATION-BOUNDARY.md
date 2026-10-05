# T-PRECISION T0：抽象观察边界的冻结卡

> **ID：** T-OBS-001 / T0-OBSERVATION-BOUNDARY-CARD。
>
> **状态：** T0_COMPLETE / SOURCE_ADMISSION_PASS / C-367_MACHINE_PROVED_WITH_SCOPE。
>
> **所属方案：** T-PRECISION-DIAGONAL-SOP 的 T0 与 T-OBS。
>
> **目的：** 在任何 ZFC、HoTT、完成接口或哥德尔式归因之前，冻结“任务相对观察精度”最小可形式化单元；随后才核对来源与开源证明代码，并用 Lean core 检查这个单元的精确命题。

## 1. 选择理由

本单元选择 T-OBS，而不选择 T-DIAG 或 T-ZFC：

- 当前 canonical dev 的 GODEL-Q-REFLECTION-SOP 已有一条尚未提交的 G0 来源分母工作；它属于 T-DIAG 的实际接口候选，不能被本单元重写、抢占或当成 current truth。
- C-364 已经证明一个**固定**两世界 completion-contract control 的 non-factorization；它是 T-OBS 的校准实例，不是 T-OBS 的一般定理。
- T-OBS-001 只证明一个普通依赖类型论中的函数／命题因子化事实。它为想法 T 给出精确语言，不能单独归因任何实际理论。

## 2. 冻结对象

| 字段 | 冻结值 |
|---|---|
| 证明理论 | Lean 4.34.1 core dependent type theory；无 Mathlib、无 ZFC syntax、无 HoTT-specific rule |
| 原任务域 | W : Type，任意状态／过程／任务表示域 |
| 粗观察 | π : W → O，O : Type |
| 任务判词 | D : W → Prop |
| 碰撞见证 | x y : W，π x = π y，D x，¬ D y |
| 目标结论 | 不存在仅由 π w 决定 D w 的 decoder：不存在 δ : O → Prop 使全域 D w ↔ δ (π w) |
| 明确正控制 | π = id 时令 δ = D，则 D 可因子化；或在 Bool 例中保留 bit 时可决定 D |
| 明确负控制 | 在 Bool 例中把 true 与 false 都压到 Unit.unit，却假称存在 decoder；Lean 应在 True ↔ False 义务处拒绝 |

## 3. 候选命题

~~~text
T-OBS-001:
  若粗观察 π 把两个任务状态 x,y 映为相同输出，
  而 D 在 x 成立、在 y 不成立，
  则不存在一个只读取 π 输出的全域 decoder δ 决定 D。
~~~

它是“D 不经 π 因子化”的精确形式。它不说 W 是现实世界、π 是任何具体理论的全部观察，也不说 D 是唯一的完成谓词。

## 4. 反证与防漂移条件

| 条件 | 若发生，必须怎样判定 |
|---|---|
| 找不到 x,y 的同投影异判词见证 | 本候选在该冻结接口上失败，不能说观察不充分 |
| D 本来就经 π 因子化 | 记录 INTERFACE_PRECISION_DEFENSE_WITH_SCOPE |
| 通过把 D 换成与原过程无关的新谓词才得到碰撞 | 判 DIFFERENT_TASK_CONTROL_TRIGGERED |
| 富接口或显式 code 恢复 D | 这是一项正控制，证明结论是接口相对的 |
| 只构造有限 Bool 例却外推任何理论 | 判 FINITE_CONTROL_ONLY |
| 用该命题归因 bare ZFC、HoTT 或现实过程 | 禁止；需要 T-ZFC/T-Meta 的独立来源与保真支付 |

## 5. 来源与代码核验计划

本卡冻结后才允许进入以下来源分母：

1. **一手数学来源：** 核验“函数经商／观察映射因子化，需要在纤维上保持相应判词”的标准 universal-property 表述；来源文本只能支持该一般数学背景，不能支持本项目的 T、Q 或现实归因。
2. **开源证明代码：** 核验 Lean core 的 Function／Iff 基础能力与 Mathlib 中的 quotient/factorization 接口，确认本项目源码使用的只是更小的自包含 fragment。
3. **项目控制：** C-364 的 Determines 定义、两世界碰撞和 rich-view 正控制；它是实例对照，不是本定理的证明来源。

## 6. 可交付边界

本卡在冻结时是 CANDIDATE_FORMAL_SPECIFICATION。当前已完成 kernel 运行、负控制、运行收据、claim matrix 与 selected proof-registry evidence closure；版本提交之前仍是 LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED。可交付的是：

> 在 Lean core 的精确函数／命题接口中，存在碰撞见证时，D 不可只经该接口全域决定。

它不交付“理论抽象必然导致悖论”、bare ZFC 缺陷、哥德尔不完备性、HoTT 非现实性或任何现实时间结论。

## 7. 执行结果

| 项 | 结果 |
|---|---|
| 正向定理 | MP-T-PRECISION-TOBS-001 / C-367，primary run 20261004-MP-T-PRECISION-TOBS-001-06，Lean 4.34.1 core accepted |
| 公理检查 | 五个 selected theorem 的 stdout 均报告 does not depend on any axioms |
| 正控制 | identity/rich observation 确实决定同一 predicate |
| 负控制 | 20261004-MP-T-PRECISION-TOBS-NEG-001-02 在 False ↔ True 义务处被 Lean 拒绝 |
| 运行核验 | verify_formal_proof_run exact rerun PASS_WITH_SCOPE；selected proof-version evidence closure PASS |
| 下一边界 | 这只完成 T-OBS 的一个抽象单位；T-DIAG 仍需要真实 Accept_T、有效编码、diag、ρ 和 bridge；T-ZFC 尚未启动 |

## 8. 核心认知 curation 决定

CORE_CURATION_DEFERRED_WITH_EXPLICIT_TRIGGER：两轮用户原文已经有 hash-pinned primary snapshot 和完整配对记录，足以作为本轮 T0 的来源输入；将它们升级成新的 core generation 会改变全项目四件套、STATE/current_core 与随后的逐 KC 审计分母，属于独立的 T3 curation transaction。

本轮不手工追加核心认知，也不把 AI 的 C-367 定理、方案分层或来源解释入核。重开条件是研究发起人明确要求把这两条用户原文纳入下一 core generation，或后续 T 单元必须以它们作为所有四件套的 current core 输入；届时必须以 core-cognition curation manager 创建新 generation、transition receipt 与相称审计。
