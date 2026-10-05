# C0R11：标准实数时间与 operational-time repair 的同一弹跳球任务候选

> **身份：** `PRIMARY_SOURCE_SCREEN / SHARED_SIMULATION_TASK_CANDIDATE / BARE_ZFC_LINK_UNPAID`。
> **任务卡：** [C0 successor reselection 011](20261005-ZFC-META-SUBTHEORY-ADEQUACY-C0-SUCCESSOR-RESELECTION-011-TASKCARD.md)。
> **source snapshot：** [Bliudze--Furic 2014](../sources/external/zfc-meta-subtheory-c0r11-bliudze-furic-2014-20261005/README.md)。

## 1. 同一任务为何首次有资格被认真讨论

论文不是把一个抽象的数学极限和另一个无关的计算例子并列。它在同一 Modelica
bouncing-ball program 上，连续讨论：

```text
input/model    = the fixed initial equations, ODEs and bounce reset rule
S_std          = physical time based on standard reals R
observation    = whether the model can move forward / whether simulator still executes its semantics
Zeno event     = infinitely many flights converge to a finite time (normalised as t=1)
S_op           = a non-standard operational semantics, then standardisation to signals
```

这构成 `SameModelAndConsumerCandidate`，比“两个领域都谈 time”强得多。

## 2. 字段卡

| field | source payment | evidence status |
|---|---|---|
| `M_std` | standard reals as physical time model | `SOURCE_STATED_MODEL_ASSUMPTION` |
| `S_std` | Modelica bouncing ball with ODEs, reset and geometrically decreasing bounce times | `PAID` |
| `Q` | run/simulate the model while remaining within its alleged semantics, including past the Zeno point | `SOURCE_TASK_SUPPORTED` |
| `FormalDone_std` | finite limit of the flight-duration series | `SOURCE_DERIVED` |
| `OriginDone_std` | not merely a limit: source says moving forward past the Zeno limit is blocked; a simulator that nevertheless runs is outside alleged semantics | `SOURCE_TASK_CONTRACT_SUPPORTED` |
| `S_op` | non-standard-time operational semantics and standardisation of output signals | `SOURCE_DEFINED_REPAIR` |
| `Bridge_op` | source says standardisation yields signals zero after `t≥1`, and explains behavior beyond the Zeno point inside the repair semantics | `SOURCE_LOCAL_BRIDGE_SUPPORTED` |
| `M_bare_ZFC` | not named as the operational source theory | `UNPAID` |
| `Adequacy_bare_ZFC` | no claim that bare ZFC must select or check this bridge | `UNPAID` |

## 3. What the source establishes

Within its own modelling-language task, the source supports this narrower contrast:

```text
finite-time limit under standard real-time model
  does not itself yield executable semantic continuation;

an enriched operational-time model
  can define and standardise a continuation.
```

This is a genuine source-level instance of the distinction between a mathematical limit result and a
completed operational semantic task. It is also a direct positive control that a refined time interface
can change what the theory can responsibly say about continuation.

## 4. Controls that prevent overstatement

1. The source calls the ball model a behavioural abstraction. It does not establish that physical reality
   obeys exactly its idealised reset rule.
2. The repair uses a non-standard model of time. It does not establish that bare ZFC's ordinary language
   cannot formulate a corresponding construction.
3. Kanovei--Lyubetskii 2007 gives a source-level ZFC construction of non-standard extension structures;
   this blocks an inference from “uses non-standard time” to “ZFC cannot represent it.”
4. The paper's simulation-semantic `OriginDone` is not automatically the user’s runner, circle, or HoTT
   completion task.

## 5. Current C0 classification

```text
SHARED_MODEL_AND_EXECUTION_CONSUMER = SOURCE_SUPPORTED
STANDARD_LIMIT_TO_OPERATIONAL_CONTINUATION_BRIDGE = SOURCE_REJECTED_OR_UNPAID
OPERATIONAL_REPAIR_AND_LOCAL_STANDARDISATION = SOURCE_SUPPORTED
BARE_ZFC_FOUNDATION_LINK = UNPAID
SAME_Q_WITH_USER_ZENO_OR_CIRCLE = NOT_YET_PAID
C1_TO_C6_CORE_ADMISSION = NOT_RELEASED
```

## 6. Exact next proof obligation

This card creates a more precise candidate for future formalization than the earlier generic controls:

```text
FormalDone_std: finite Zeno-time limit for the fixed bouncing-ball abstraction.
OriginDone_exec: a source-defined executable continuation that remains within the model's semantics.
RepairBridge: non-standard operational semantics + standardisation gives a valid continuation.
```

Before formalizing it as any bare-ZFC statement, a source must still connect `M_std` or `M_bare_ZFC`
to an actual foundation acceptance/adequacy policy. Otherwise the correct result remains a hybrid-system
semantic comparison, not a ZFC verdict.
