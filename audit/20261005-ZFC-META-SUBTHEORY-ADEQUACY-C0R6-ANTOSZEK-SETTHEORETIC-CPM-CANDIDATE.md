# C0R6 / F-B：Antoszek 的 set-theoretical CPM 任务忠实性候选

> **身份：** `CORE_ADEQUACY_SOURCE_CANDIDATE / PUBLISHED_SOURCE_INSPECTED / NOT_A_BARE_ZFC_VERDICT`。
>
> **前序任务卡：** [C0 successor reselection 006](20261005-ZFC-META-SUBTHEORY-ADEQUACY-C0-SUCCESSOR-RESELECTION-006-TASKCARD.md)。
>
> **冻结原件：** [Antoszek 2026 snapshot](../sources/external/zfc-meta-subtheory-c0r6-antoszek-20261005/README.md)。

## 1. source 的实际结构

Antoszek 审计 Patrick Suppes 的 classical particle mechanics (CPM) set-theoretical formalization。其对象不是泛泛“连续数学”，而是：

```text
framework F = set-theoretical predicate for CPM
theory T    = F + specific force-law formulas
history H   = temporal development / state history
judgment    = deterministic iff matching present states force matching future states
```

文章批评 Suppes 对整个 framework 的“thoroughly deterministic”判词：该判词的形式推导可以正确，但由于把 framework 和具体 physical theory混在一起，不能给有意义的 determinism verdict。要得到有意义的结论，须固定 force equation、initial conditions和具体 theory。

## 2. 与本项目合同的对应

| 字段 | source 付款 | 边界 |
|---|---|---|
| `M_A` | set-theoretical language / predicate；文章说“only real axioms”是set theory axioms。 | 当前原件未把集合论基础版本固定为ZFC；不能填 bare-ZFC M。 |
| `S_A` | CPM：real time interval、particle set、position `s(p,t)`、velocity、forces、twice differentiability。 | 并非芝诺 runner或极限 theorem。 |
| `Q_A` | determinism：同一时刻的 state是否固定未来 temporal development。 | 不等于`OriginDone_Zeno`。 |
| `FormalDone_A` | Suppes/Montague式 formal determinism theorem/definition。 | source指出formal correctness不能自动支付 meaningful verdict。 |
| `P_A` | “particle mechanics is thoroughly deterministic science”及framework determinism的提升。 | 被 source批评为对错误对象作判词。 |
| `Bridge_A` | theory须含specific force equation；physical theory必须被properly distinguished from framework；任意force的形式模型缺 physical significance。 | 是 task-fidelity/physical-theory bridge，不是 actual Zeno completion bridge。 |
| `Adequacy_A` | source给出 framework→theory 的判断前提，并用Norton’s dome说明具体 theory内的indeterminism。 | 没有把这一责任归给bare ZFC的基础角色。 |

## 3. 对用户研究的有效启发

这篇已发表来源提供一个外部、相对独立的结构性控制：

```text
一个 framework-level 的形式判词即使推导正确，
若没有固定具体 physical theory / force law / histories，
也可能不是对原物理问题的有意义判词。
```

这与本项目反复要求的 `FormalDone`、`P`、`OriginDone` 和 bridge 不能混为一项完全同形。但它证明的是 **CPM framework—theory 的 determinism 诊断**，不证明 ZFC 对芝诺的时间观察力不完备。

## 4. 判词

```text
F_B_SET_THEORETIC_PHYSICAL_FRAMEWORK_TO_THEORY_TASK_FIDELITY_CONTROL
FORMAL_CORRECTNESS_DOES_NOT_ALONE_PAY_MEANINGFUL_PHYSICAL_DETERMINISM_VERDICT
FOUNDATION_VARIANT_ZFC_NOT_YET_FIXED
Q_A_NOT_SAME_AS_ZENO_ORIGINDONE
CORE_C6_NOT_RELEASED
```

## 5. controls 与下一动作

| 控制 | 状态 |
|---|---|
| `Control+` | 具体 force-law theory可得到可审计 determinism/indeterminism verdict；Norton’s dome给 source 的 concrete application。 |
| `Control−` | 只对整个 framework施加判词会引入任意force或物理上无意义的结果；source明确拒绝。 |
| `M-control` | “set-theoretical”不自动是 “ZFC”；须找到 Suppes/Antoszek/source chain中明确的 foundation variant 才可升M字段。 |
| `SameQ-control` | determinism与runner completion不同；不能把 temporal development的相似词汇当成SameQ。 |

下一最小行动：对 Suppes 原始/2002 source 做**版本与基础语言核对**，只问它是否明确选定 ZFC 或可验证的 ZFC-founded base；若不能，则本卡保持 F-B 的高质量不同-M控制，不能进入 core C1。

## 6. 禁止外推

- 不称 Antoszek 的 source 已发现本项目的ZFC悖论；
- 不称 CPM formalization使用set theory就等于ZFC；
- 不把Norton’s dome、determinism或framework/theory distinction偷换成芝诺或圆环；
- 不称 paper的论证为本项目机器证明；
- 不把 source 的successful repair叙述为 framework必然失败或所有数学理论都不忠实。
