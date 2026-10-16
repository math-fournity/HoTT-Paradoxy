# P35：`CurveRun` 对 presentation-fiber 过程合同的覆盖审计

**任务：** `P35-P1-FIBERWISE-TRACE-COVERAGE-001`

**状态：** `EXACT_COVERAGE_WITH_SCOPE / NO_NEW_WRAPPER_OR_KERNEL_CLAIM / P36_PROVENANCE_ORIGIN_COVERAGE_GATE_SELECTED / NO_HOTT_DEFECT_OR_ACTUAL_K_CLAIM`

## 1. 问题、范围与不变的任务合同

P35 不尝试再造一个名为 `PresentationRun` 的记录。它只检验 P34 固定的两个
`PresentationFiber OpenRealInterval` 成员，是否已经能够与既有的连续过程合同逐项配对。
根路径是：

```text
G0 → P1 → P6/P7/P19 → P33 → P34 → P35
```

这里的原 `X` 仍是“圆去点、开区间呈现、两端闭合/复原”的过程。为避免换题，P35 只使用下列窄合同：

| 项 | P35 固定内容 | 不能替代为 |
|---|---|---|
| Input | `f,g : PresentationFiber OpenRealInterval`，本例为 `nInOpenFiber` 与 `transportedMInOpenFiber` | 任意两个裸类型或一般路径 |
| Operation | `CurveRun (pr1 f) (pr1 g)` 的连续切片族 | 有限 ambient-homeomorphism trace |
| Observation | `closedAt`、`agreesInterior`、slice homeomorphism、起末 closed image，以及 P34 的 `EndCoincidence` | 仅 `Bare` 相等 |
| Done_P35 | `CurveRun.final`：末态 closed diagram 等于给定 target presentation 的 closed image | `Success`、`Satisfies` 或现实物理复原 |

这个 `Done_P35` 是 P35 只为“fiberwise trace / endpoint completion”定义的完成标准。它不是
`NativeSourceContract.Satisfies`，也不是原用户全部的来源、历史、操作和现实完成标准。

## 2. 学术和本地资产侦察

**公开搜索：** `NOT_SEARCHED_WITH_REASON`。本波次的问题不是命名一个外部数学结构，也不是确认某个变化中的论文或库版本；它是对固定版本、本地 `CurveRun` 的字段与 P34 固定合同逐项比较。外部文献不能改变这些源码中是否已经有这些字段。P34 已将 Moore path、directed space 与 structured-cospan 类材料记录为 `NEARBY_NOT_SAME_TASK`，本波次不重复该分母。

**本地资产判词：**

| 资产 | 与 P35 的关系 | 判词 |
|---|---|---|
| `PresentationFiber.agda` | 给出两个指定 fiber 成员、其相同 `Bare` carrier 及 endpoint-closure 分离 | `EXACT_INPUT_COVERAGE` |
| `NativeTaskIntegration.agda` | `CurveRun` 已具有所需的连续、slice、内点、initial/final 与空间界字段；`actualCurveRun : CurveRun nRich mRich` 已有原生收据 | `EXACT_OPERATION_OBSERVATION_DONE_COVERAGE` |
| `NativeRichCurve.agda` | `fullTransportPath : mRich = transportedRich` 使 P35 的 target specialization 成为既有依赖类型运输，而非新操作 | `EXACT_TARGET_SPECIALIZATION_COVERAGE` |
| `NativeSourceContract.agda` | 固定 `Satisfies`、`Done`、`Run` 与 re-expression 的另一种合同，并证明 bare check 不足 | `BOUNDARY_CONTROL_NOT_MERGED` |
| `NativeCurveTask.agda` | `Success` 是有限 ambient-homeomorphism trace，且与 `CurveRun` 在同一对象对上不同 | `STRONG_COUNTEREXPLANATION` |
| C-325 `OriginDirectedDiagram` | 是有限静态 label 对照，不能替换实际曲线过程 | `NEARBY_ONLY` |

## 3. 字段逐项对照

`NativeTaskIntegration.CurveRun` 的字段已经覆盖 P35 所声明的所有过程字段：

| P35 义务 | 现有字段或事实 | 覆盖结论 |
|---|---|---|
| 指定 source / target presentation | `nInOpenFiber`、`transportedMInOpenFiber`，其第一投影分别为 `nRich`、`transportedRich` | fiber membership 由 P34 已给出 |
| 连续过程 | `CurveRun.closedAt` 与 `jointlyContinuous` | 已覆盖 |
| 开区间与闭参数的相容 | `CurveRun.at`、`agreesInterior` | 已覆盖 |
| 每个时刻的可逆 slice | `slice`、`sliceIsActualMap` | 已覆盖 |
| 初态与末态 | `initial`、`final` | 已覆盖 |
| 有界控制 | `spaceBound` | 已覆盖 |
| 实例 | `actualCurveRun : CurveRun nRich mRich` | 已有 C-320 kernel receipt |
| P34 target 的对齐 | `fullTransportPath : mRich = transportedRich`；对 `CurveRun nRich` 沿该 path 作既有类型运输 | 已有理论操作，不需新 record |

最后一行不是新增定理：它只说明 `CurveRun` 的 target 参数本来就是 `RichCurve` 的依赖位置，而
`NativeRichCurve` 已提供该 target 的 path。若另写

```text
PresentationRun f g := CurveRun (pr1 f) (pr1 g)
```

或只为该 path 写一行 `tr`，将只把现有 Input membership 和现有 operation record 捆绑成新名字；它不会增加新的观察量、完成条件、理论承诺或可判别事实。因此 P35 按工作合同判为 `EXACT_COVERAGE_WITH_SCOPE`，并且**不新增 wrapper、Agda module、kernel run 或 claim row**。

## 4. 不能混同的两个完成合同

P35 的覆盖裁决并不把所有“完成”压成一个词：

1. `CurveRun.final` 是连续曲线过程的末态图等于目标 `RichCurve` 的 closed image；它是 P35 的 `Done_P35`。
2. `NativeCurveTask.Success` 是有限 `AmbientStep` trace。C-320 已证明它在 `(nRich,mRich)` 处不能由 `CurveRun` 统一恢复，也不与它等价。
3. `NativeSourceContract.Done` 与 `Satisfies` 是 source re-expression 和闭图 denotation 合同；它说明 bare carrier 检查不足，却不把来源历史或物理恢复装进 `CurveRun`。

所以这里没有 `P ∧ ¬P`，没有 HoTT 规则把一个完成合同自动当作另一个，也没有 proof assistant 的接受或拒绝异常。P35 只是确认：对它自己预先声明的 fiberwise continuous-process 合同，现有项目代码已覆盖。

## 5. 波次反思、全树比较与后继

1. **新增事实：** P35 没有新增数学事实；它定位到 P34 与 C-320 的 exact composition，排除了“再造 record”这一重复劳动。
2. **判词变化：** P1 的静态 fiber→过程连接在声明的窄 `Done_P35` 下从 `OPEN` 变为 `EXACT_COVERAGE_WITH_SCOPE`。完整来源—操作—复原理论仍开放。
3. **合同一致性：** `X`、carrier、过程观察和 target 未变；P35 明确没有把 `CurveRun.final` 偷换成 `Success` 或 `Satisfies`。
4. **正控制与反解释：** `actualCurveRun` 是正控制；`noCurveAmbientEquivalence`、`noUniformCurveToAmbient` 和 `bareCheckIsInsufficient` 防止把三种合同混同。
5. **重复检查：** 若创建 wrapper，将只是同义重包装；本报告停止于已有源码和 C-320/P34 收据。
6. **分支资格：** P2 仍由 P33 关闭，P3 无新 K，P4 无 semantic trigger；P1 尚有“这个 source 是否以 circle-minus-point 的 origin operation 被明确保存”的未闭合边。
7. **停止理由：** 继续 P35 不会改变 Input、Operation、Observation 或 Done；故在此停止。

### 波次坐标

- **最终目标连接：** P1 / `R_min` 的 operation—completion 子边。
- **实际价值：** 把 P34 的 presentation separation 与既有 P21 continuous-process evidence 接上，同时拒绝把这条接线误报为 HoTT 失配。
- **裁决：** `CLOSE_WITH_SCOPE / SWITCH_BRANCH_TO_P36_PROVENANCE_ORIGIN_COVERAGE_GATE`。

### P36 的最小候选卡

`P36-P1-PROVENANCE-ORIGIN-COVERAGE-001` 不先造“来源历史”新 record。它首先审计既有
`StrongPuncture`、`PunctureApartness`、`NativeRealCircleQualification`、`NativeRichCurve` 与
`NativeSourceContract` 是否已经对原 `X` 保存了下列字段：

| 字段 | P36 固定要求 |
|---|---|
| Input | 一个圆对象及被去掉的指定点，或其在当前 formalization 中的精确等价输入 |
| Operation | 明确的 puncture / re-expression operation |
| Observation | 该 operation 与 source `RichCurve`、closed image、端点关系的对应 |
| Done | source 的确来自该 puncture，而不是仅与开区间同胚或裸等价 |
| 正控制 | 既有 `StrongPuncture` 已完整给出这些字段时，判 `EXACT_COVERAGE` 并停止 |
| 最强反解释 | 若当前对象只命名 source carrier 而未给 operation/provenance witness，才有资格精确提出一个缺字段 |

P36 的负结果不会停止 active goal；它只会触发另一个不同分母的 successor discovery。它不会重开 P3，除非一个版本固定的实际 K 出现。

## 6. 禁止外推

- P35 的 exact coverage 只针对本报告定义的 fiberwise continuous-process contract。
- 它不证明 P34 加上 `CurveRun` 已给出完整 `R_origin`、物理复原或用户全部的现实同一性判词。
- 它不证明 HoTT 规则、univalence、同胚、库消费者或 proof assistant 有错误。
- 它不发现实际 `K_theory`、`K_app` 或 `K_engine`。
