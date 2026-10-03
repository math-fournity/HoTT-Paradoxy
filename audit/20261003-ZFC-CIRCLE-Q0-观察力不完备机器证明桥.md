# ZFC-CIRCLE-Q0：观察力不完备的机器证明桥

> **身份：** `CONTRIBUTOR_CANDIDATE_NOT_CURRENT / FORMAL_LOGICAL_CORE + DIRECT_REAL_ANALYSIS + REPLAYED_CONCRETE_GEOMETRY_CONTROL / NOT_A_FORMALIZATION_OF_ZFC_OR_FINAL_ZFC_VERDICT`。

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
| `observation_collision_implies_completion_observation_incomplete` | 将“观察力对给定Done问题不完备”严格定义为`¬ CompletionObservable observe done`；Done异值碰撞蕴含该相对不完备性。 | 把“观察力不完备”从口号变成带`observe/done`参数的判据。 |
| `completion_bridge_delivers_origin_done` | 只有把`formalDone → originDone`作为显式`CompletionBridge`输入，才可将同一state的formal Done运输为origin Done。 | 正控制：缺桥不能由同一个词“完成”补出；有桥时运输确实可做。 |
| `completion_equivalence_supplies_bridge` | `CompletionEquivalent`要求在同一state domain上逐点`formalDone ↔ originDone`，它才可推出forward bridge。 | H093需要的“同一任务身份”可被写成精确证明义务。 |
| `no_formal_completion_only_classifier` | 具体的`continuousEndpoint`与`sequentialNoLastAction`都取`formalCompletion=1`，却有相反`strongDone`；故formal completion alone不能判定strong Done。 | 最小的 O2/O3 反例结构。 |
| `enriched_observation_decides_strong_done` | 加入terminal-event布尔观察后，具体fixture的strong Done可被判定。 | 正控制：不完整来自忘却，补回明确数据即可改变结果。 |

保存的当前源码运行收据是[20261003-MP-ZFC-OBSERVATION-BOUNDARY-001-02](../HoTT/verification/runs/20261003-MP-ZFC-OBSERVATION-BOUNDARY-001-02/RUN.json)。内核接受、退出码0、stderr为空；四个`#print axioms`输出均为“不依赖任何axioms”。精确命题、非目标和解释边界见[CLAIM.md](../HoTT/formal/zfc-observation-boundary/CLAIM.md)。

该证明的严格范围是：`observe`碰撞加上Done差异时的不可因子化；fixture是研究语义模型。它不证明 ZFC 实际存在这个碰撞，也不证明某一真实极限来源作出了未付 LiftClaim。

## 3. 几何级数的实分析机器对照

新的[GeometricCompletion.lean](../HoTT/formal/zfc-observation-boundary/GeometricCompletion.lean)不再只用抽象的二元
fixture，而是对最接近芝诺二分法的实数序列运行 Lean/Mathlib：

```text
s(n) = 1 − (1/2)^n
```

| 已机器检查的命题 | 精确内容 | 研究上排除的混淆 |
|---|---|---|
| `zenoPartialSum_strictly_below_one` | 对任意自然数`n`，`s(n) < 1`。 | 不能把任一有限阶段误说成已达端点。 |
| `zenoPartialSum_never_reaches_one` | 对任意`n`，`s(n) ≠ 1`。 | 收紧为明确的有限阶段否定。 |
| `zenoPartialSum_tendsto_one` | `s`在实数通常拓扑中趋于`1`。 | 没有否定通常极限定理。 |
| `zeno_limit_outcome_without_finite_stage_endpoint` | `hasLimitOutcome ∧ ¬ hasFiniteStageEndpoint`。 | 同一数学对象可同时满足“极限结果成立”与“没有有限编号阶段到端点”。 |
| `zeno_limit_outcome_does_not_imply_finite_stage_endpoint` | `¬ (hasLimitOutcome → hasFiniteStageEndpoint)`。 | 直接拒绝把这两个已命名的命题当作无条件蕴含。 |
| `zeno_limit_outcome_done_not_equiv_final_stage_done` | `¬ (limitOutcomeDone ↔ finalStageDone)`。 | 对“把无最后阶段的条件换成极限结果”给出严格的非等价控制。 |
| `closed_continuous_time_has_endpoint_arrival` | 闭实数时间区间内有terminal parameter，轨迹在该参数取目标值。 | 正控制：有限阶段定理并未否定连续端点模型可以有到达。 |

保存的运行收据是[20261003-MP-ZFC-GEOMETRIC-COMPLETION-001-01](../HoTT/verification/runs/20261003-MP-ZFC-GEOMETRIC-COMPLETION-001-01/RUN.json)。它由固定的 Lean 4.34.1 与本机锁定的 Mathlib 构建接受，退出码为0、stderr为空；Lean 明示其依赖`propext`、`Classical.choice`、`Quot.sound`。因此它是**带已声明经典／Mathlib依赖的实分析证明**，不能描述成无公理 core 证明。完整命题与非目标见[GeometricCompletion-CLAIM.md](../HoTT/formal/zfc-observation-boundary/GeometricCompletion-CLAIM.md)。

这个结果精确支持一件事：标准实分析的`Tendsto`结论，与“某个有限自然数阶段达到端点”是两件可分开的数学陈述。它不替任何现实过程预设哪个才是唯一合法的`Done`，也不把“无有限阶段”偷换成“在某个连续时间端点绝不完成”。那个额外的过程判词正是需要被来源和同一任务桥检验的部分。

H091已经找到一份实际来源，IEP *Zeno’s Paradoxes*，明示 Standard Solution 对“旅行是否需要最后一步”回答“不需要”，并把拒绝该直觉列为采用 Standard Solution 的代价。新的第七条定理使这一来源的最小形式控制可检查：若把`finalStageDone`改称为`limitOutcomeDone`，二者在本几何模型中并不等价。因此来源可以**透明地改写／替换**完成条件，却不能仅凭名称把两种条件证明为同一。该控制仍不证明它的连续时间模型无法完成；它只禁止把“明示替换”误报为“已保持原条件”。

第八条是反向的正控制：在独立定义的闭实数时间区间中，`terminalTime = 1`确实属于时间域，`continuousTrajectory terminalTime = 1`被Lean接受。这正是一个来源若要支付连续端点模型桥可以给出的数学部分。它也划清了结论边界：本项目并不从“无自然数最后阶段”推出“连续端点不可能到达”；真正待问的是来源是否把这个模型到达与**同一个原过程**的`Done_origin`明示连接。

## 4. 已有的实连续几何机器控制

项目已有一个更接近圆环的 Lean/mathlib 控制；本轮已对当前源码重新运行，而非只引用历史收据：

| 证据 | 已形式化的内容 | 与新逻辑核的关系 |
|---|---|---|
| `C-275` / `MP-ASTRA-STRUCTURED-CURVE-001` | `nPresentation/mPresentation`各有开参数嵌入、闭参数连续completion和内点一致；两者的`BareCarrier`存在具体 Homeomorph，但不存在将`BoundaryCoincident`从任意`BareEquivalent`自动运输的通用规则。 | `BareCarrier`是粗观察，boundary coincidence是被忘却的completion观察。 |
| `C-276` | 让ambient、parameters和completion一起运输时，`PresentationEquivalence`存在并保持boundary coincidence。 | 丰富观察／显式bridge的正控制。 |
| `C-277` | 指定整数坐标边界观察精确对应，且坐标交换下仍可显式运输。 | 不是所有丰富结构都不可运输；关键是保留正确字段。 |

源码中的关键定理是[StructuredCurve.lean](../HoTT/formal/astra-real-geometry/StructuredCurve.lean:76)的`no_bare_coincidence_transport`；当前矩阵行[C-275–C-277](../HoTT/CLAIM_EVIDENCE_MATRIX.md:1164)记录既有主张索引。本轮对同一当前源码的新运行收据是[20260920-MP-ASTRA-STRUCTURED-CURVE-001-03](../HoTT/verification/runs/20260920-MP-ASTRA-STRUCTURED-CURVE-001-03/RUN.json)：Lean 4.34.0 在锁定的真实拓扑依赖下退出码0、stderr为空，并逐项打印了`propext`、`Classical.choice`、`Quot.sound`依赖。它复核的是这份几何控制本身，不把它升级为物理运动或 ZFC 的证明。

由此得到两层相互校验：

```text
抽象逻辑层：同一 observation + 不同 strongDone ⇒ 不能仅凭 observation 判定 Done
连续几何层：BareEquivalent + 不同 BoundaryCoincident ⇒ bare carrier不能自动运输completion性质
```

## 5. 对“观察力不完备”的精确推进

现在有三层不同的、可分开审计的结论：

1. **实分析层已证明：** 对指定几何级数，极限端点成立而无有限阶段端点成立；二者不能以文字压成同一数学谓词。
2. **观察接口层已证明：** 若某一接口把强Done不同的状态压成相同观察，强Done不能只经该接口判定；加入真正所需字段的正控制会改变结论。
3. **ZFC元理论层仍待证明：** 必须给出实际的ZFC／标准极限消费者、其输入输出和完成标准，证明它只使用了粗观察，又把`Done_formal`抬升为原过程的`Done_origin`，并且没有同一任务的桥。

### 把“时间维度”变成可证伪术语

这里的“时间维度”不应被理解为 ZFC 词表中少了一个叫`Time`的符号。对一个固定过程任务，它应被理解为：理论实际保留的观察能否区分**对原完成条件有差异的历史／阶段结构**。Lean 中的精确版本已经叫作`CompletionObservable observe done`：存在一个只看`observe`输出的判定，能对每个过程状态给出同一个`done`答案。

所以，把研究发起人的候选判词压缩成可反驳的条件句，是：

```text
若存在一个实际的 ZFC → 极限理论接口 I 和一个固定的原过程 P，
I 把 Done_origin 不同的过程历史压成同一数学观察，
而来源仍用 I 的结果交付 P 已完成，且没有给出保持 Done_origin 的桥，
则 I 对 P 的完成观察不充分。
```

这不是“ZFC 形式不一致”的定义，也不是“ZFC无法表达时间”。它是一项关于某个实际`I/P/LiftClaim`组合的可证伪归因。反例也很明确：若来源保留了足以判定`Done_origin`的过程字段，或给出一个验证过的`Done_formal ⇒ Done_origin`桥，或者明说自己改了原`Done`，这个组合就不能承担候选判词。

因此机器证明支持如下**限定条件句**：

> 在一个明确的忘却／粗观察接口中，若强完成性质没有因子化通过该接口，那么只看粗观察的理论结论不够判断强完成；保留并运输相应的过程／端点字段会改变结论。

它们尚未证明下列更强命题：

- ZFC 的全部实数／极限框架存在同样的忘却接口；
- 标准极限理论的任何一条定理必然把强 Done 丢掉；
- 某个实际来源已经无付款地从`Done_formal`跳到`Done_origin`；
- ZFC 形式不一致或所有 HoTT 模型失效。

这也校正了“ZFC 没有时间维度”的粗说法。这里已形式化的有限索引、极限和端点都可被精确讨论；目前可检验的候选不是`O1`完全不能表示顺序或阶段，而是某个实际的`O2`形式结果是否被**没有充分过程观察的情况下**当成`O3`过程完成。把责任最终指向 ZFC，需要完成第3层的来源与桥证明，不能由第1、2层自动推出。

这些未完成事项正是 Q0/Q1 的来源卡要补的`LiftClaim / Payment / same-task`义务。机器证明没有取代它们，反而给了一个可复用的判别准则：只要未来来源宣称“形式完成已经就是过程完成”，就必须给出令`strongDone`因子化通过其所用 observation 的桥；否则它的主张处于本定理所描述的失败形状。

## 6. 下一步与停止

H083与H084已经完成第一轮实际来源分母：

1. SEP *Supertasks*有实际completion LiftClaim，却显式区分最终动作与每一步完成；
2. Le Blanc明确将数学极限到实际无限重复的推断称为subjunctive leap；
3. H085 的 HoTT 模型控制说明：一个模型／相对一致性来源可以完成其自身的元理论任务，而不因此完成另一个 H0 过程契约；故 H0→Z0 不能自动转移。
4. Norton、SEP adequacy与连续端点模型继续分别提供Done替换、数学—物理边界和正控制。
5. H086以隔离的 Terra/Max 复核本报告自身的形式范围：它确认两组Lean定理只支持相对的completion-observation边界，且仍缺一个实际 ZFC interface、同一过程桥、独立`Done_origin`与真实观察碰撞；因此本报告不能自行把Q0升级为 ZFC 判词。

因此下一步不应继续重复“极限不等于过程”的一般文本。只有两类新证据值得开启下一卡：

```text
A. 某来源把强 Done 与 formal completion 同一化，却没有明确 payment；
B. 某 ZFC/集合论元理论来源把模型、语义或一致性提升为 HoTT 的 H0_process 已完成，且没有 B_H。
```

本报告及新 Lean proof/run是贡献者交付，尚未进入canonical `dev` current owner或claim matrix。接受时必须从当时`dev` HEAD重审其输入哈希、范围与既有Q0/Q1卡，不能因本报告存在就提高 ZFC 候选等级。

## 7. 新的 Zeno—HoTT 同一 Q 条件定理

研究发起人进一步提出：若同一个 ZFC 的特性`Q`在芝诺上被判“已经解决”、在 HoTT 上却被判不合理，那么ZFC是否在同一个Q上产生了悖论？

[MetaObservationConsistency.lean](../HoTT/formal/zfc-observation-boundary/MetaObservationConsistency.lean)现已将这个问题机器化。它把`QProfile`显式拆成O1–O5、bridge payment和原任务保持；并证明：若两个站点的**完整**QProfile相同，而一个被判`originalResolved`、另一个被判`bridgeRequired`，则不存在Q-uniform的基础观察政策。若一个需要bridge的站点却被称为原任务已经解决而bridge未支付，则它违反形式化的O3–O5充分性政策。

这不是“ZFC推出False”的定理。它证明的是一个更贴近本研究的条件句：同一完整Q上的异判与一套声称统一的O3–O5完成观察不能共存。相反，若两站点只共享粗特征而payment／任务保持不同，判词可以不同；源码也有这个正控制。因此当前工作要证明的是完整QProfile映射，不能用“都和完成有关”替代。

最新收据是[20261003-MP-ZFC-META-OBSERVATION-CONSISTENCY-001-02](../HoTT/verification/runs/20261003-MP-ZFC-META-OBSERVATION-CONSISTENCY-001-02/RUN.json)，所有七个选定定理无公理。H094的独立映射当前判`PROFILE_MATCH_NOT_YET_PROVED`：IEP接近`revisedResolved`，QuestioningDelay的现实解释是bridge，故尚不能直接把条件定理提升为实际ZFC实例。
