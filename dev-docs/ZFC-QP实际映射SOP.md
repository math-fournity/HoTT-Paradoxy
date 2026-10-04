# ZFC-QP-ACTUAL-MAPPING-SOP

> **身份：** `CONTRIBUTOR_CANDIDATE_NOT_CURRENT / RESEARCH_EXECUTION_SOP / P_TO_B_SOURCE_MAPPING / NOT_A_ZFC_INCONSISTENCY_CLAIM`。
>
> **目标：** 将 `P = 未验证的完成提升` 从条件性 Lean 结构推进到版本固定的实际来源／同一任务映射；每一步可证伪，并允许由 bridge 正控制、任务切换控制或证据前沿终止。

## 0. 固定定义与层级

```text
P(F, D) = promotionClaim(F, D) ∧ ¬ verifiedBridge(F, D)

F = formal/model completion
D = origin-process Done
Q = 在 F 被提升为 D 前，审查对象、输入、操作、观察、Done 与 bridge 的完成资格观察力
A = 数学共同体／来源所接受的“一个指定 Zeno/circle 任务已解决”判断
B = 用户所定义的 HoTT 侧不合理；只有获得 P→B provenance 才能作为本 SOP 的实际 B
```

本 SOP 的三层不可互换：

| 层 | 本 SOP 允许的结论 |
|---|---|
| 数学／形式层 | 一个极限、轨迹、形式程序或证明命题的精确范围。 |
| 社区政策层 | 某来源是否将 F 提升为 D。 |
| 现实／计算解释层 | P 是否缺计算／现实 bridge，及 B 是否是同一任务的不合理。 |

任何“ZFC 矛盾”必须另有对象语言或正式不相容证明；本 SOP 默认只研究政策和解释层。

## 1. TaskCard

详见 [当前 TaskCard](../audit/20261004-ZFC-QP-ACTUAL-MAPPING-TASKCARD.md)。共同任务不是“芝诺 = HoTT”，而是：

```text
u_assess = 某个来源是否把 F 当作同一 origin-process Done D，且未给 verified bridge？
```

每个案例都必须单独冻结 `T/u/F/C/Q/I/O/Done`。没有被同一来源定义的 `D`，不得以词语相同假装 P 已命中。

## 2. 阶段和最小判别行动

### M0：P 的实际实例格式

为每个候选建立：

```text
Source / TheoryContext / F / D / promotionClaim / verifiedBridge
ProcessState / I/O / Q observation / countercontrol / stop condition
```

只有 `promotionClaim` 和 `¬verifiedBridge` 都有来源级定位，才标 `P_CANDIDATE_SOURCE_MAPPED`。

### M1：芝诺／极限的 A 与 P

读取 IEP、SEP、Bathfield 和必要的一手数学来源，分别回答：

1. A 的“解决”究竟对应 `Done_IEP`、`Done_everyStep`、`Done_finalAction` 还是另一个 Done？
2. F 是极限值、连续模型到达还是二者的合取？
3. 来源是否实际作出 `F ⇒ D` promotionClaim？
4. 是否支付了 source-defined、task-preserving bridge？

**正控制：** 一条闭连续时间轨迹在指定终点取值，能支付该自身模型内的 endpoint Done。

**停止：** 若来源明确改写 D 或支付 bridge，记录 `BRIDGE_PAID_OR_TASK_REVISED_CONTROL`，不得称该卡为 P。

### M2：圆环的 P 候选

从用户原圆环任务和已有离散／实数模型控制，固定：拿走点、展开、逼近、此前 M、复原操作和 Done。不得将“有同胚”“有闭合极限”或“端点距离趋零”直接充作 `D`。

**停止：** 若原 Done 被用户裁定为数学 endpoint 即可，或来源交出 task-preserving bridge，撤回 P 候选；否则保留 `CIRCLE_D_UNRESOLVED`，不以 AI 哲学补填。

### M3：Q 的实际观察责任

不问“ZFC 能否编码时间”，而问来源的完成政策是否实际检查：

```text
same object/input/operation/observation/Done/bridge
```

只有在来源主张 F 已足以交付 D 而遗漏其中至少一项时，才可登记 `Q_OBSERVATION_GAP_CANDIDATE`。纯粹未写某种哲学说明不足以证明缺 Q。

### M4：P 到 HoTT-B 的 provenance

冻结 H0 的精确形式对象、`QuestioningDelay` 的 `Done_formal` 与用户 UR 的 `Done_origin`。要求一条实际来源或同一任务 bridge 显示：同一种 completion promotion P 是如何造成 B。

**反控制：** 若 H0 只是 P 的探测器、而没有来源把 formal status 提升为 `Done_origin`，状态是 `P_TO_B_NOT_ESTABLISHED`，不能制造 PBacktrace。

### M5：交叉裁决与 Lean 实例化

只有 M1–M4 同时满足，才可构造 `ActualPolicyWitness` 并实例化：

```text
A↔P / Q-missing→permission→adoption / PBacktrace / P→B / A⊥B
```

若只得到 A+B 的规范张力，使用 `zfc1_produces_normative_tension`；若有正式不相容，再使用 `object_level_false_requires_formal_incompatibility`。不能跳过 M4 或 M5。

## 3. P-DAG 调度

首轮至多三个独立 source-match 节点：

| 节点 | 任务 | 可见材料 | 预期 |
|---|---|---|---|
| P1/M1 | Zeno source completion map | 冻结 IEP/SEP/Bathfield facts | A/F/D/bridge 分层。 |
| P3/M2 | Circle origin-D map | 用户原文 + 已有控制 | 原 Done 与模型 Done 区分。 |
| P2/P3/M4 | HoTT-B provenance map | QuestioningDelay/H0 boundary | PBacktrace 或明确缺口。 |

Battle 只在同一字段有来源冲突时启动。每个节点必须带 `QConvergenceLink`，标明它如何使 P 实例、Q gap 或 P→B 状态生成、收紧、桥接、淘汰或防误报。

## 4. 合法终局

1. `ACTUAL_UNVERIFIED_COMPLETION_PROMOTION_SOURCE_MAPPED`：某指定案例的 F、D、promotion 和未付 bridge 都被来源定位；不自动表示 ZFC 不一致。
2. `BRIDGE_PAID_OR_TASK_REVISED_CONTROL`：来源支付 bridge 或明确更换 Done，当前 P 候选失败。
3. `P_TO_B_PROVENANCE_NOT_ESTABLISHED`：B 没有同一任务 PBacktrace；只能保留 P 探测器读法。
4. `FORMAL_INCOMPATIBILITY_NOT_ESTABLISHED`：有政策张力但不能称对象层矛盾。
5. `EVIDENCE_FRONTIER_REACHED_WITH_SCOPE`：冻结来源分母内无法完成某字段，记录精确缺口和重开条件。

### 收敛解释

上述终局是**某一来源 lane 的终局**，不是 ZFC 问题查找工作的终局。用户 2026-10-04 已明确指出：芝诺、圆环、罗素计算视角和 main 的 HoTT 分析已经使整个 ZFC 研究进入收尾／收敛阶段。故 M1–M5 的 `EVIDENCE_FRONTIER_REACHED_WITH_SCOPE` 应被读作：宽泛类比、错误 Done 和无 provenance 的路径已被淘汰，下一步只能集中寻找实际完成政策中的 P，不得重新从“ZFC 有什么问题”开始散搜。

### M6：收敛后的实际 P 政策检索

只检索同时含有以下要素的来源：

```text
指定的 formal F
→ 来源实际宣布同一 process Done D
→ 可审计的 promotion rule
→ Q 检查是否存在／遗漏
→ 与 HoTT-B 的可追踪同一任务关系，或明确的反控制
```

M6 的成功不预设发现 ZFC 对象层矛盾。它的目标是定位或排除“数学共同体实际使用的未验证完成提升 P”。任何新来源若只重复极限值、连续模型、H0 的 `never` 或泛泛哲学，不进入 M6 分母。

### M6 的当前收敛判词（2026-10-04）

`SEP Supertasks` 起初被 H103 的窄卡误报为 P 候选；与 H083 的完整来源卡对照后，
它被改为 `SOURCE_TASK_CONTRACT_SPLIT_CONTROL`：该来源明说其 `every-step` 与
`final-action` Done 的区分，不能被写成对用户强原 Done 的未付款提升。

Uttarakhand Open University *Real Analysis* MT(N)-201 §5.1–§5.3 则形成当前 M6
的实际来源候选：它先将 series sum 定义为 partial sums 的极限，再用有限和交付
Achilles catch-up／paradox resolution；在固定相邻段落中，数学定义被支付，
`F -> source-process D` 的保真 bridge 没有被给出。H106 用 SEP 的显式 Done 分叉作为
有界 Battle control，仍判 `P_CANDIDATE_UPHELD`。H104/H105/H106 的 exact Terra/Max
source-match、外部原 PDF identity、trajectory 以及 Lean card/contract controls 应共同读取。

这使 P 的候选位置从“所有极限说法”收敛到一个更窄的可反驳命题：

```text
实际来源将定义性的 formal completion F 交付为 source-process Done D；
是否同一任务、是否有桥、以及 ZFC 是否缺 Q，仍分别需要来源证明。
```

## 5. `/goal` 启动句

```text
按照 SOP=`ZFC-QP-ACTUAL-MAPPING-SOP`，继续将 P＝未验证的完成提升映射到实际 ZFC／数学共同体来源、芝诺／圆环和 HoTT 的同一任务链；逐项完成 Q、P、A、B、PBacktrace 与形式不相容核证，直至本 SOP 终局分类触发。
```
