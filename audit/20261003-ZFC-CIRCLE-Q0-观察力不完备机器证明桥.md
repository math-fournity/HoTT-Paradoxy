# ZFC-CIRCLE-Q0：观察力不完备的机器证明桥

> **身份：** `CONTRIBUTOR_CANDIDATE_NOT_CURRENT / FORMAL_LOGICAL_CORE + REUSED_CONCRETE_GEOMETRY_CONTROL / NOT_A_FORMALIZATION_OF_ZFC_OR_FINAL_ZFC_VERDICT`。

## 1. 要证明的最小逻辑核

研究发起人的候选终局语言是“ZFC 在时间维度上的理论观察力不完备”。这个句子不能直接被写成 Lean 定理，因为它混合了：ZFC 的对象语言、实分析、一个过程模型、来源的 LiftClaim、以及现实／完成解释。

先分离一个可以机器证明的核：

```text
若 observe 把两个过程状态压成同一 formal observation，
但 strongDone 对这两个状态给出相反答案，
则不存在一个仅依赖 observe 的全域 strongDone 判定谓词。
```

这精确表达 `O2 → O3` 不自动成立：数学／形式完成的观察若忘去了过程完成所需的数据，就不能独自判断强 Done。它是条件性信息论／逻辑结论，不是假称“每个极限都忘记过程”。

## 2. 新的 Lean 4 机器证明

[ObservationBoundary.lean](../HoTT/formal/zfc-observation-boundary/ObservationBoundary.lean) 以 Lean 4.34.1 core kernel 证明三个命题：

| 定理 | 精确内容 | 对 Q0 的作用 |
|---|---|---|
| `no_done_classifier_of_observation_collision` | 任意`observe`若合并一个Done与一个非Done状态，任何只依赖`observe`的谓词均不能正确判定所有状态的`done`。 | 一般逻辑核。 |
| `no_formal_completion_only_classifier` | 具体的`continuousEndpoint`与`sequentialNoLastAction`都取`formalCompletion=1`，却有相反`strongDone`；故formal completion alone不能判定strong Done。 | 最小的 O2/O3 反例结构。 |
| `enriched_observation_decides_strong_done` | 加入terminal-event布尔观察后，具体fixture的strong Done可被判定。 | 正控制：不完整来自忘却，补回明确数据即可改变结果。 |

保存的运行收据是[20261003-MP-ZFC-OBSERVATION-BOUNDARY-001-01](../HoTT/verification/runs/20261003-MP-ZFC-OBSERVATION-BOUNDARY-001-01/RUN.json)。内核接受、退出码0、stderr为空；三个`#print axioms`输出均为“不依赖任何axioms”。精确命题、非目标和解释边界见[CLAIM.md](../HoTT/formal/zfc-observation-boundary/CLAIM.md)。

该证明的严格范围是：`observe`碰撞加上Done差异时的不可因子化；fixture是研究语义模型。它不证明 ZFC 实际存在这个碰撞，也不证明某一真实极限来源作出了未付 LiftClaim。

## 3. 已有的实连续几何机器控制

项目已有一个更接近圆环的 Lean/mathlib 控制：

| 证据 | 已形式化的内容 | 与新逻辑核的关系 |
|---|---|---|
| `C-275` / `MP-ASTRA-STRUCTURED-CURVE-001` | `nPresentation/mPresentation`各有开参数嵌入、闭参数连续completion和内点一致；两者的`BareCarrier`存在具体 Homeomorph，但不存在将`BoundaryCoincident`从任意`BareEquivalent`自动运输的通用规则。 | `BareCarrier`是粗观察，boundary coincidence是被忘却的completion观察。 |
| `C-276` | 让ambient、parameters和completion一起运输时，`PresentationEquivalence`存在并保持boundary coincidence。 | 丰富观察／显式bridge的正控制。 |
| `C-277` | 指定整数坐标边界观察精确对应，且坐标交换下仍可显式运输。 | 不是所有丰富结构都不可运输；关键是保留正确字段。 |

源码中的关键定理是[StructuredCurve.lean](../HoTT/formal/astra-real-geometry/StructuredCurve.lean:76)的`no_bare_coincidence_transport`；当前矩阵行[C-275–C-277](../HoTT/CLAIM_EVIDENCE_MATRIX.md:1164)与保存的运行收据`20260920-MP-ASTRA-STRUCTURED-CURVE-001-02`拥有其既有范围。

由此得到两层相互校验：

```text
抽象逻辑层：同一 observation + 不同 strongDone ⇒ 不能仅凭 observation 判定 Done
连续几何层：BareEquivalent + 不同 BoundaryCoincident ⇒ bare carrier不能自动运输completion性质
```

## 4. 对“观察力不完备”的精确推进

这些内核证明支持如下**限定结论**：

> 在一个明确的忘却／粗观察接口中，若强完成性质没有因子化通过该接口，那么只看粗观察的理论结论不够判断强完成；保留并运输相应的过程／端点字段会改变结论。

它们尚未证明下列更强命题：

- ZFC 的全部实数／极限框架存在同样的忘却接口；
- 标准极限理论的任何一条定理必然把强 Done 丢掉；
- 某个实际来源已经无付款地从`Done_formal`跳到`Done_origin`；
- ZFC 形式不一致或所有 HoTT 模型失效。

这些未完成事项正是 Q0/Q1 的来源卡要补的`LiftClaim / Payment / same-task`义务。机器证明没有取代它们，反而给了一个可复用的判别准则：只要未来来源宣称“形式完成已经就是过程完成”，就必须给出令`strongDone`因子化通过其所用 observation 的桥；否则它的主张处于本定理所描述的失败形状。

## 5. 下一步与停止

H083与H084已经完成第一轮实际来源分母：

1. SEP *Supertasks*有实际completion LiftClaim，却显式区分最终动作与每一步完成；
2. Le Blanc明确将数学极限到实际无限重复的推断称为subjunctive leap；
3. Norton、SEP adequacy与连续端点模型继续分别提供Done替换、数学—物理边界和正控制。

因此下一步不应继续重复“极限不等于过程”的一般文本。只有两类新证据值得开启下一卡：

```text
A. 某来源把强 Done 与 formal completion 同一化，却没有明确 payment；
B. 某 ZFC/集合论元理论来源把模型、语义或一致性提升为 HoTT 的 H0_process 已完成，且没有 B_H。
```

本报告及新 Lean proof/run是贡献者交付，尚未进入canonical `dev` current owner或claim matrix。接受时必须从当时`dev` HEAD重审其输入哈希、范围与既有Q0/Q1卡，不能因本报告存在就提高 ZFC 候选等级。
