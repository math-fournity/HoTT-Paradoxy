# P37：原普通去点 M 与当前强域模型的任务忠实性复资格化

**任务：** `P37-P1-WEAK-PUNCTURE-FIDELITY-REQUALIFICATION-001`

**状态：** `EXACT_COVERAGE_BY_EXISTING_C283_C290_C307_C308 / ORIGINAL_WEAK_M_NOT_UNCONDITIONALLY_MODELED_BY_STRONG_SOURCE / SPEC_REFINEMENT_NOT_JUSTIFIED_BY_ORIGINAL_TEXT / P38_REAL_ORIGIN_EVENT_BRIDGE_DISCOVERY_SELECTED / NO_HOTT_DEFECT_OR_ACTUAL_K_CLAIM`

## 1. 固定原 M 与当前形式模型

用户的原始圆环表述把 M 说成“圆上拿掉一点后的样子”，并把它同普通 N、来源、端点、允许复原方式和
同一过程历史一起考虑；它没有指定一个实数 apartness witness。ABX 的当前任务设计也明确指出，
`Σ x:C, x≠p` 只能描述给定 p 以后的剩余点，不能单独承载完整来源史。

P37 因而固定三个不同对象：

| 名称 | 当前精确形式 | 角色 |
|---|---|---|
| `M_weak` | `PuncturedRealCircle = Σ p:RealCircle. p ≠ east` | 原普通“圆减指定点”的最小静态形式 |
| `M_strong` | `StrongPuncture = Σ p:RealCircle. apart(xCoord p,1)` | 当前 `mRich` 实际采用的强域 |
| `N` | `OpenRealInterval` | 当前开区间 carrier |

P37 问的不是“这些对象哪个真实”，而是：当前代码中关于 `M_strong ≃ N`、闭图和过程的结果，能否无条件地
作为关于原 `M_weak` 的结果交付。

## 2. 已有资产已经覆盖的精确关系

本波次进行本地/历史资产侦察后判为 `EXACT_COVERAGE_BY_EXISTING_C283_C290_C307_C308`；不新建代码、不重跑
既有 kernel proof。

| 义务 | 已有直接证据 | 结论 |
|---|---|---|
| 弱、强对象的定义 | `PuncturedRealCircle`、`StrongPuncture`、`forgetStrong` | 两个输入不是同一个定义；强域到弱域有显式 forgetful map |
| 弱→强的条件 | C-283：`Lift = ∀p, Weak p → Strong p`；same-point refinement 与 `Lift` 对齐 | 没有静默 point replacement |
| 强域到开区间 | C-285/C-288/C-290：`StrongPuncture` 到 `Real` 再到 `OpenRealInterval` 的明确结果 | 强域 result 已有相称范围证据 |
| 弱域到开区间 | C-290、C-308：weak path/homeomorphism 是 `Lift` 或等价的明确 real principle 的函数参数 | 已有的是**条件构造**，不是无条件 weak-domain delivery |
| 原过程的弱终态覆盖 | `NativeMotionComplete.weakFinalCoverageIffLift` | 对这一个固定 `WeakFinalCoverage` 合同，弱域覆盖与 `Lift` 互相蕴含 |
| 历史/来源边 | P36 与 `NativeSourceContract` | source 是 supplied strong `mRich`；没有历史 event witness |

因此没有待补的“弱/强关系基础定理”：它们已经在当前固定 source/run 中被处理并明确携带条件。

## 3. P37 的任务忠实性裁决

### 3.1 可以忠实交付什么

可以交付的是下列范围准确的陈述：

1. 当前模型精确构造了强域 `M_strong` 与 `N` 的指定同胚/等价、闭图和过程控制；
2. 对原弱域 `M_weak`，代码给出以 `Lift` 或 `RealNonzeroApartness` 为输入的保持点 refinement、
   path/homeomorphism 与某些 final-coverage contracts；
3. 对已定义的 `WeakFinalCoverage`，存在 `WeakFinalCoverage ↔ Lift` 的机器证明。

### 3.2 当前不能无条件交付什么

当前资产**没有提供**一个无参数的 `M_weak ≃ N`、无参数的原 weak final coverage，或一个把
`M_weak` 自动改写成 `mRich` 的函数。它们提供的正向构造都明确接收 `Lift` 或等价的原则。

这句话不是“已证明任何无条件弱同胚都不可能”，也不是“`Lift` 必然非现实”。它只报告当前 formalization
的参数与范围：把强域结论称作原弱 M 的无条件结果，会发生 `SPEC_SUBSTITUTION_DRIFT`。

### 3.3 与原圆环目标的关系

这项重资格化削弱而非加强“已经击落 HoTT”的说法。当前 P1 强域控制显示来源/端点/过程信息能被表示，
弱域则显示某些希望的 completion/coverage 需要额外明确输入。两者都还没有一个实际 HoTT 规则或消费者
把弱 `H/U` 当作原 `Done_s`；故 P2/P3/P4 的门槛完全不变。

## 4. P38：真实来源事件桥的有界发现

P38 不把“加一个字段”当作答案。它先审计现有 `OriginDirectedDiagram`、`Input + CurveData + Denotes/Satisfies`、
`RealCircle/east/PuncturedRealCircle` 与 `mRich` 是否已经共同给出一个能满足下列合同的真实 source-event bridge：

| 字段 | P38 要求 |
|---|---|
| Input | 完整圆、指定 east、弱去点 source 和/或其强细化 |
| Operation | 从完整圆及点到去点 source 的明确数学 operation，而不是仅 carrier 命名 |
| Observation | operation 与 closed diagram、端点和当前 `mRich` 的可追踪关系 |
| Done | source relation 保持并能被过程合同消费 |
| 正控制 | 若既有 asset 已含全部字段，判 `EXACT_COVERAGE`，不另造 record |
| 最强反解释 | 若只有静态 subtype、供应的 source 与有限 label 控制，记录精确缺 field；不得把缺 field 本身说成 HoTT 不能表达或理论错误 |

P38 是 P1 独立对象理论任务。它不会重开 P3，除非找到版本固定的实际 K；也不会把历史 provenance 直接转换成现实判词。

## 5. 波次反思

1. **新增事实：** 当前 P1 result 的 exact domain 已被重述为 `M_strong`；原 `M_weak` 的相关正向构造显式携带 `Lift`。
2. **改变的判词：** P34/P35 的 `mRich` controls 不再可被称作原普通 M 的无条件形式化。
3. **合同一致性：** 原 M 的普通去点含义、N、端点和过程没有改；改变的是对现有 source 所覆盖范围的诚实分层。
4. **正控制与反解释：** C-308 的 conditional weak consumer 与 `weakFinalCoverageIffLift` 是正控制；它们防止把“目前没有无条件项”误写成不可能性定理。
5. **重复检查：** C-283–C-290/C-307–C-308 已精确覆盖本波次，不重跑或复造同义形式化。
6. **分支资格：** P1 获得 P38 event-bridge discovery；P2仍关闭，P3无新 K，P4无触发。
7. **停止理由：** 当前 weak/strong comparison 的分母已完整覆盖；继续只会重复已有条件性结论。

### 波次坐标

- **最终目标连接：** P1 / `R_min` 的 source-input fidelity，防止原 M 被强域替代。
- **实际价值：** 将“圆上拿掉一点”拆成弱静态去点、强计算性细化和来源事件，使后续理论审计不能混用三者。
- **裁决：** `CLOSE_WITH_SCOPE / SWITCH_BRANCH_TO_P38_REAL_ORIGIN_EVENT_BRIDGE_DISCOVERY`。

## 6. 禁止外推

- P37 不证明强域与弱域无条件不等价，也不证明任意 weak-domain homeomorphism 必须使用 `Lift`。
- P37 不判断 `Lift`、real apartness、LEM 或相关原则的现实地位。
- P37 不构成传统拓扑学或 HoTT 的矛盾、实际 K、引擎问题或现实非现实性悖论。
