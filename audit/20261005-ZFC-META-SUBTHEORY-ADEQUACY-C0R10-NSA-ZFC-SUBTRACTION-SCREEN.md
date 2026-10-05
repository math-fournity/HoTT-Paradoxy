# C0R10：非标准时间的 bare-ZFC subtraction screen

> **身份：** `PRIMARY_SOURCE_SCREEN / REPRESENTABILITY_POSITIVE_CONTROL / OPERATIONAL_DUTY_UNPAID`。
> **任务卡：** [C0 successor reselection 010](20261005-ZFC-META-SUBTHEORY-ADEQUACY-C0-SUCCESSOR-RESELECTION-010-TASKCARD.md)。
> **source snapshot：** [Kanovei--Lyubetskii 2007](../sources/external/zfc-meta-subtheory-c0r10-kanovei-lyubetskii-2007-20261005/README.md)。

## 1. 要排除的过强推理

Benveniste et al. 使用 `ZFC + non-standard-analysis axioms` 的时间结构，不能推出：

```text
bare ZFC cannot define / construct / interpret a suitable non-standard time structure.
```

这正是 C0R10 的 subtraction question。它必须区分“base theory不够强”与“base theory
可以建立模型，但某个物理或执行语义没有把它作为自己的 native bridge”。

## 2. Kanovei--Lyubetskii 的实际支付

Theorem 1.16 在 source 中给出两条相关结果：

1. **provably in ZFC**，可得到带 `st` predicate 的 `*V`，它满足 BST，并以 elementary
   embedding扩张标准 universe `V`；
2. BST 对 `st`-conservative extension意义下与 ZFC 相连，source还陈述 equiconsistency。

它还解释了：非标准 extension使用额外的 standardness relation，`st` 不属于原来只有
membership的语言；在扩展的 `st-∈` language里才可以表达 Transfer、Boundedness等原则。

## 3. 对 C0R9 的精确裁决

| C0R9 requirement | result |
|---|---|
| bare ZFC cannot construct the extension | **rejected within this source scope**：source states a ZFC proof of the relevant extension structure. |
| extended language has additional observational vocabulary | **supported**：`st` predicate and BST principles are explicit added structure. |
| this gives the Benveniste hybrid operational semantics | **not paid**：no SimpleHybrid, execution engine, zero-crossing or program-acceptance source bridge. |
| bare ZFC must natively require that operational bridge | **not paid**：metatheoretic construction is not an adequacy policy. |
| user’s Zeno/circle `OriginDone` is paid | **not paid**. |

The proper verdict is:

```text
ZFC_NONSTANDARD_REPRESENTABILITY = SOURCE_SUPPORTED_WITH_SCOPE
ADDED_STANDARDNESS_INTERFACE = SOURCE_SUPPORTED
HYBRID_OPERATIONAL_CONSUMER_TRANSPORT = UNPAID
BARE_ZFC_OPERATIONAL_OBSERVATION_DUTY = UNPAID
```

## 4. What this changes in the ZFC question

This is evidence against a crude claim that ZFC is unable to host time-sensitive structures. It
does **not** settle the user’s theory-precision question. The remaining candidate is narrower:

> A theory may be strong enough to build a richer observational universe, while its ordinary
> application contract neither selects that universe nor requires the bridge from its formal result
> to the original operational task.

That sentence is a C0 research hypothesis, not a theorem of ZFC or a source-reported physical fact.

## 5. Successor

The next source question is no longer “can ZFC represent a discrete/dense time base?” It is:

```text
Can an actual ZFC-founded physical or computational consumer be shown to use a standard
continuum formal result while declining, omitting or failing to pay the temporal-operation bridge
that the non-standard/operational comparison makes explicit?
```

Until a source pays that shared task contract, C0R9/C0R10 are comparative controls, not C1--C6 admission.
