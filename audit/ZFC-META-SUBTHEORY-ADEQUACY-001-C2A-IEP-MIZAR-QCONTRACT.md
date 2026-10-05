# C2A：IEP 几何级数与 Mizar `SERIES_1` 的 source-to-spec 对齐

> **身份：** `C2_SOURCE_TO_SPEC_CARD / PARTIAL_Q_FIDELITY / NOT_A_PROMOTION_OR_BRIDGE_PROOF`。
>
> **TaskCard：** [C2A](ZFC-META-SUBTHEORY-ADEQUACY-001-C2A-TASKCARD.md)。
>
> **判词：** `Q_MATH_TO_FORMALDONE_FIDELITY_SUPPORTED_WITH_SCOPE / FULL_Q_MOTION_FIDELITY_UNPAID / DIFFERENT_TASK_CONTROL_PRESENT / C2A_LOCAL_LEAF_CLOSED`。

## 1. 当前一手来源

| source | 版本／定位 | 本卡使用的内容 |
|---|---|---|
| [IEP, *Zeno’s Paradoxes*](https://iep.utm.edu/zenos-paradoxes/) | 2026-10-05 直接读取；第 68–88 行、100–104 行、112–126 行。 | Standard Solution 同时谈 physical continuum、runner path、finite positive speed、real time／position，以及 `1/2+1/4+…` 的 partial sums 趋近有限值。它把 ZFC with Choice／standard real analysis 放在间接解决的基础语境。 |
| [MML `SERIES_1.miz`](https://mizar.uwb.edu.pl/version/current/mml/series_1.miz) | MML 5.94.1493；2025-05-30；61,041 bytes；SHA-256 `b130e347aaebb5ee85fbd5a71698c33ed147ab894d61cf9263bc3e8f2e8d6ef2`。 | `Partial_Sums` recursion；`summable ↔ Partial_Sums` convergent；`Sum = lim Partial_Sums`；Th10 scaling、Th22 geometric partial sums、Th24 geometric summability and sum. |
| [MML `SEQ_2.miz`](https://mizar.uwb.edu.pl/version/current/mml/seq_2.miz) | 当日只读到 version-current 的 convergence/limit definition segment；未把不完整下载冒充完整 source snapshot。 | `convergent` 使用正误差阈值、足够大的所有指数和绝对差的条件；`lim` 被相同条件唯一指定。 |
| [A2 IEP/Norton completion contract](20261004-ZFC-ACTUAL-Q-A2-标准解法来源完成合同.md) | 已冻结来源审计。 | Strict/revised completion 的 distinct-task control。 |

## 2. 逐字段 fidelity table

| 字段 | IEP 的数学子任务 `Q_math` | MML `SERIES_1` 对象 | 结论 |
|---|---|---|---|
| 输入 | `1/2 + 1/4 + 1/8 + …` 的项与有限 partial sums。 | `a GeoSeq`，再取 `a=1/2` 并用 Th10 作常数 `1/2` 缩放。`GeoSeq` 初项为 1，故缩放后是上述项列。 | `SUPPORTED_WITH_SCOPE`。 |
| 有限步骤 | 先加前两个、前三个、……项。 | `Partial_Sums(s).0=s.0`，并按 `n+1` 的新项递推。 | `SUPPORTED_WITH_SCOPE`。 |
| 观察 | partial sums 越来越接近一个有限值。 | `summable` 定义为 `Partial_Sums` convergent；`Sum` 定义为其 limit。 | `SUPPORTED_WITH_SCOPE`。 |
| 数学结果 | 该 infinite series 有有限的和；IEP 在这个语境中以之解释 Standard Solution。 | Th22 给 partial-sum formula；Th24 给 `|a|<1` 时的 summability and sum formula。 | `SUPPORTED_WITH_SCOPE`。 |
| 具体数值 1 | IEP 举 `1/2+1/4+…`。 | Th24 在 `a=1/2` 给未缩放 `GeoSeq` 的和 2；Th10 的缩放使其为 1。 | `PROJECT_SPECIALIZATION_OF_SOURCE_THEOREMS`；尚未作为 Mizar 本机新 theorem 重放。 |

所以，在 **级数—部分和—极限** 这个数学子任务上，MML 是 IEP 所说明的标准实分析操作的一个足够精确、版本固定的 formal specification candidate。它在这个层面不只是“某个实数库存在”。

## 3. 不能携带到完整原任务的字段

IEP 对 Standard Solution 的对象不止级数。它还要求／使用 physical continuum、continuous runner path、positive finite speed、real-number time and position、以及微积分与 classical mechanics。`SERIES_1` 的 source fragment没有给出这些对象、也没有定义：

```text
runner / spatial path / physical time / speed / motion operation /
whether an original process has been completed.
```

因此当前最强的准确映射是：

```text
MML FormalDone  ↔  IEP Q_math 的级数结果
MML FormalDone  ↛  IEP Q_motion 的物理完成
MML FormalDone  ↛  OriginDone
```

第二、三行不是 MML 的反定理；它们是 source-to-spec fidelity 的**未付字段**。把未被 S 表示的运动字段默默删除，再说 S 已解决整个 IEP 原任务，就是本 SOP 要防止的 task switch。

## 4. `DifferentTaskControl`

已有、独立于本卡的两类 control 都阻止了字段混同：

1. `C-361` 的 [ZenoLimitControl.lean](../HoTT/formal/zfc-actual-q-policy/ZenoLimitControl.lean) 机器检查固定部分和趋于 1、任一自然数阶段仍小于 1，并另给闭实数时间区间端点实际到达的正控制。它只说明两种精确形式谓词不同，不能决定 IEP 的物理模型。
2. `C-362` 的 [Norton contract formalization](../HoTT/formal/zfc-actual-q-policy/ZenoSourceCompletionContract.lean) 以 A2 的人工来源分类为输入，证明 revised completion 与 strict last-action completion 之间没有其所假定的 bridge。它不把来源文字变成 Lean theorem。

这两个 control 的共同作用是：即使 `Q_math` 由 MML faithful 地表示，`Q_motion`／`OriginDone` 仍不能自动折叠为它。

## 5. C2A 的范围判词

`C2A` **通过的是有限的数学子任务 fidelity**，并不是完整 Q 的固定：

```text
C2A paid:
  version-fixed M / S / Q_math / FormalDone correspondence

C2A unpaid:
  Q_motion / OriginDone,
  actual P from the Mizar theorem to the IEP resolution,
  Bridge,
  adequacy responsibility.
```

因此 C2A 不产生 `CORE-*` claim、不新建 Lean theorem、不改变 bare ZFC 的结论。其唯一作用是把下一叶收紧：C3 必须审计 IEP 到底是否把这个数学片段作为完成 physical Q 的 promotion，还是公开维持／改写另一个任务。
