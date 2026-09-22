# P34：`Bare` 忘却映射的 presentation fiber

**任务：** `P34-P1-ORIGIN-RELATION-DISCOVERY-001`

**状态：** `FORMAL_CHECKED_WITH_SCOPE / SAME_BARE_FIBER_HAS_DISTINCT_PRESENTATIONS / ENDPOINT_CLOSURE_SEPARATES_PRESENTATIONS / P35_FIBERWISE_TRACE_SPEC_SELECTED / NO_HOTT_DEFECT_OR_ACTUAL_K_CLAIM`

## 1. 根目标连接与候选裁决

P34 从 `G0 → P1 → P34` 只减少一个未闭合义务：原 `X` 中“同一裸 carrier 不足以固定来源—闭图—复原 presentation”的差异，能否在**同一后端**构成一个数学对象，而不依赖 P19 的跨后端 minimal label control。

本地侦察确认 P6 已比较带标记、分层、exit-path、cospan、定向和 cohesive structures；继续给它们换名不会增加事实。公开检索中的 Moore paths、directed spaces 与 structured cospans说明参数化过程、方向与边界是已有数学对象，但它们各自不自动给出原 `X` 的全部 source/closure/Done。它们因此是 `NEARBY_NOT_SAME_TASK`，不是 P34 的可直接采用定义。

真正未覆盖的最小对象是 `Bare : RichCurve → Type` 的 strict/dependent fiber。它直接复用既有 `mRich`/`nRich`、`transportedRich`、endpoint closure 和 `CurveRun`，因此没有把原 `X` 替换成一般路径或静态标记空间。

## 2. 形式对象与机器结论

[`PresentationFiber.agda`](../../HoTT/formal/agda-unimath/hott-z/PresentationFiber.agda) 定义：

```text
PresentationFiber A := Σ (r : RichCurve), Bare r = A
```

在固定 `A = OpenRealInterval` 上，代码构造两个 presentation：

```text
transportedMInOpenFiber = (transportedRich , refl)
nInOpenFiber            = (nRich , refl)
```

它们都位于同一 `Bare` fiber，但满足相反的 endpoint/closed-image 情形：

- `transportedFiberClosed : EndCoincidence transportedRich`；
- `nFiberNotClosed : ¬ EndCoincidence nRich`；
- `noOpenFiberPath : ¬ (transportedMInOpenFiber = nInOpenFiber)`。

最后一项由既有 `fullTransportPath : mRich = transportedRich`、`noRichPath : ¬(mRich = nRich)` 和 projection `ap pr1` 得到。它不是“同一类型有矛盾”，而是说一个特定忘却映射的纤维中有不同的结构化 presentation。

固定 agda-unimath/no-erasure 工具链接受该 module，运行收据为 `MP-ASTRA-PRESENTATION-FIBER-001` / `C-326`。直接依赖的 `NativeRichCurve`、`NativeRealCircleQualification` 与 library configuration 均进入 source manifest。

## 3. 对原任务与四分支的精确影响

| 问题 | P34 结果 |
|---|---|
| P1 的 `R_min` | 得到一个清楚的 candidate mathematical relation：保留 `Bare` fiber中的 presentation data，而非只比较裸 carrier。 |
| 原 `X` | fiber成员保留 parametrization/closed diagram；端点闭合提供一个已经机器化的观察量。它仍不是完整 `C,p,M,N,e,trace,Done` 对象。 |
| P2 `K_theory` | 未找到规则把 bare fiber projection当成强 Done。 |
| P3 `K_app` | 未找到实际消费者把 `Bare` 输入升格为原 `Done_s`。 |
| P4 `K_engine` | 无规则—实现差异。 |

因此 C-326 是一个 **P1 对象理论进展**。它反驳的只是“所有同裸 carrier presentation 都自动相同”这种过强命题；它不反驳普通同胚、univalence，或任何 HoTT 理论本身。

## 4. P35 候选：fiberwise trace / completion interface

当前 `PresentationFiber` 记录 static/closed presentation；`NativeTaskIntegration.CurveRun` 已记录 time-indexed continuous operation，但二者尚未以一个同一后端接口联结。P35 只尝试规定最小 `PresentationRun`/fiberwise trace contract：

1. source、target必须是指定 `PresentationFiber` 成员；
2. 复用 `CurveRun` 的 `at`、`closedAt`、initial/final、continuity 与 slice fields；
3. 明确哪一种 endpoint/closed observation被过程保留；
4. 将它与已有 `Success` 区分为不同 operation contract，而非尝试证明其等价；
5. 若现有 `CurveRun` 已完整覆盖这个接口，则报告 `EXACT_COVERAGE` 并停止，不另造同义 record。

P35 服务原 `X` 的 operation/Done 边，而不是回到 P2 reflection 来源或 P3 consumer scan。只有未来存在真实 `K` 消耗这一忘却 projection并宣称完成强任务时，P1 的对象才能进入 P3 失配审计。

## 5. 波次反思与裁决

- **路径：** `G0 → P1 → P6/P7/P19 → P33 coverage closure → P34`。
- **航向检查：** Input 仍是 `mRich/nRich` 的同一原 carrier relation；Operation/Done 未被替换为 generic modal、2LTT 或纯文献话题。
- **替代叶比较：** P3 无新 K、P4 无触发、P2 reflection subline由覆盖关闭；P1 是唯一直接可检查的根边。
- **实际价值：** 新增一个同一后端、kernel-checked fiber object，避免把跨后端最小 label control当作原 X 的完整结构。
- **裁决：** `CLOSE_WITH_SCOPE / SWITCH_BRANCH_TO_P35_FIBERWISE_TRACE_SPEC`。

## 6. 禁止外推

- 这不是完整 `OriginDirectedDiagram`、来源历史或物理复原的形式化。
- 这不证明 HoTT 的同胚/等价规则错误，也不证明实际 `K` 存在。
- 这不将 `CurveRun` 等同于 ambient `Success`，不证明理论/实现错误或现实非现实性悖论。
