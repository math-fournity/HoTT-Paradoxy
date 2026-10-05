# C0R9：ZFC extension 中 hybrid operational time 的比较控制

> **身份：** `PRIMARY_SOURCE_SCREEN / COMPARATIVE_EXTENSION_CONTROL / BARE_ZFC_SUBTRACTION_UNPAID`。
> **任务卡：** [C0 successor reselection 009](20261005-ZFC-META-SUBTHEORY-ADEQUACY-C0-SUCCESSOR-RESELECTION-009-TASKCARD.md)。
> **source snapshot：** [Benveniste et al. 2012](../sources/external/zfc-meta-subtheory-c0r9-hybrid-nonstandard-20261005/README.md)。

## 1. 这个来源为什么有判别力

这不是另一篇泛泛说“时间重要”的哲学文字。作者把混合系统模型的可执行语义问题明确拆成：

```text
continuous ODE evolution + discrete events / zero-crossings
→ simulation engines may give non-reproducible or non-deterministic outcomes
→ static semantic map must coexist with discrete computation and adaptive run-time discretization
→ introduce a non-standard time base with infinitesimal steps, predecessor/successor, discrete order
→ obtain an operational / constructive / Kahn semantics that can accept or reject programs.
```

这正是研究发起人关注的“没有时间维度的静态表达”与“实际执行必须有时序”的真实工程版本。

## 2. `M/S/Q/P/Bridge/Adequacy` source card

| field | source payment | status |
|---|---|---|
| `M` | Robinson non-standard analysis described as adding three axioms to basic ZFC | `ZFC_EXTENSION_EXPLICIT / NOT_BARE_ZFC` |
| `S` | SimpleHybrid / hybrid systems modelers with ODEs, discrete events and zero-crossings | `PAID` |
| `Q` | construct a statically definable operational semantics usable for executable simulation, including Zeno / cascaded zero-crossing cases | `SOURCE_TASK_SUPPORTED` |
| `FormalDone` | non-standard semantics on `T={n∂}`; explicit predecessor/successor; constructive and Kahn semantics | `SOURCE_DEFINED_FORMAL_SEMANTICS` |
| `P` | source says this gives a firm basis for accepting/rejecting programs and sound compilation/simulation-engine semantics | `SOURCE_STATED_PROMOTION_WITHIN_HYBRID_LANGUAGE` |
| `Bridge` | source provides a semantics-to-program-execution argument within SimpleHybrid; physical-model-to-reality completion is not proved | `LANGUAGE_SEMANTICS_BRIDGE_ONLY` |
| `Adequacy` | concern belongs to the authors’ hybrid-systems semantic design, not an asserted bare-ZFC foundation duty | `LOCAL_TO_EXTENSION_AND_LANGUAGE` |

## 3. Relation to the C0R8 controls

The comparison sharpens rather than replaces C-375–C-378:

| C0R8 control | Benveniste source relation |
|---|---|
| graph domain can recover an endpoint | source builds a richer time base with explicit predecessor/successor; it does not treat a bare state set as sufficient for execution. |
| parameter order can be lost under range projection | source makes order operational through `t•`, `•t`, clocks, transitions and zero-crossing handling. |
| operation consumer remains source-specific | source supplies a concrete consumer: compilation / simulation / program acceptance, yet its task is not Zeno’s runner or the user’s circle. |

This makes the paper a **positive construction control** for the research program: a richer formal framework can expose and manage time/order obligations that a simpler representation leaves opaque.

## 4. What it does not show

1. It does not prove that bare ZFC is unable to formulate the same construction, or that a model of non-standard analysis cannot exist in a ZFC metatheory.
2. It does not establish `ZFC → P` for any Standard Solution to Zeno.
3. Its `Q` concerns hybrid-language execution and program acceptance, not the user’s fixed `OriginDone` for motion or circle restoration.
4. It does not create a SameQ bridge to H0.

Therefore the correct C0 label is:

```text
ZFC_EXTENSION_TEMPORAL_OPERATIONAL_SEMANTICS_POSITIVE_CONTROL
BARE_ZFC_THEORY_PRECISION_COMPARISON_NOT_YET_PAID
```

## 5. Consequence for C0R9

The paper validates a source-backed requirement for any next candidate:

```text
do not ask only whether M can encode a time variable;
ask whether M/S provides a semantic bridge that supplies
  ordered instants, next-step/causality structure, and a program/task acceptance criterion.
```

The next eligible bare-ZFC source must still demonstrate the **subtraction** part: which one of these
obligations is missing, unobserved or silently bypassed when the extension-level semantics is not present.
