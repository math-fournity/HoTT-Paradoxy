# C3A：FOTG 几何级数候选的 promotion 与 Bridge 审计

> **身份：** `CORE_ADEQUACY_TASK_CARD / C3_C4_SOURCE_AUDIT / COMPONENT_PROMOTION_ESTABLISHED / FULL_PROMOTION_UNPAID`。
>
> **前序：** [C2A task-fidelity card](20261005-ZFC-META-SUBTHEORY-ADEQUACY-C2A-FOTG-GEOMETRIC-TASK-FIDELITY-CARD.md)。

## 1. P 在来源中实际是什么

IEP 的 Standard Solution 不是只说“存在一个极限”。它作出下列复合断言：

1. runner 的 path、time 与 motion 被建模为 linear continuum／point-events；runner 以 positive finite speed 运行；
2. (1/2+1/4+1/8+cdots) 的 partial sums 趋近有限值；Dichotomy 的几何级数和为 1；
3. Achilles 的 geometric subpaths 和为 finite distance，runner 在 constant speed 下可以完成；
4. no-last-step intuition 被 Standard Solution 拒绝。

因此，来源中确有一个 promotion，但它的输入不是 Mizar `Sum` alone，而是：

```text
P_IEP = continuum/path/time/speed model
        ∧ geometric-series calculation
        ⇒ standard-solution resolution / arrival language
```

Mizar `SERIES_1` 只支付这个合取中的第二项。它没有 runner、path、time、speed、point-event 或 arrival predicate。故它与 IEP 的 P 有真实的**数学组件交集**，却不是 `P_IEP` 的 complete formalization。

## 2. Bridge 的实际来源判词

既有 Norton source card冻结：严格完成把“有一个最后 action”列为条件；revised completion 只要求每一个自然数编号 action 完成；其解法是删除前一条件。IEP 的 Dichotomy 段也明确回答“trips need last steps?”为否。

因此在目前固定的 strict Q reading 下：

```text
P_component                 = SOURCE_ESTABLISHED
P_full_from_Mizar_theorem   = SOURCE_UNPAID
Bridge(formal/revised, strict-origin) = SOURCE_REFUTED_FOR_THIS_READING
```

这不是“连续时间端点不可能到达”的结论。C‑361 的 Lean/Mathlib translation control 本轮 `--rerun` 通过，证明：

```text
s_n = 1 - 2^{-n}  → 1
¬ ∃ n : Nat, s_n = 1
```

同时它给出 closed real-time interval 的 endpoint arrival 正控制。C‑362 的 Lean core source-contract control亦本轮重放通过：在来源认证的 revised completion 中，没有 strict last-action completion，也没有 bridge。二者只验证固定规格的逻辑后果，不能替来源本身发言。

## 3. C3A/C4 判词

```text
IEP_COMPOSITE_PROMOTION_SOURCE_ESTABLISHED
MIZAR_COMPONENT_TO_FULL_PROMOTION_GAP
STRICT_BRIDGE_EXPLICITLY_UNPAID_FOR_FIXED_Q
CONTINUOUS_ENDPOINT_NEGATION_REJECTED_BY_POSITIVE_CONTROL
ADEQUACY_NOT_YET_SOURCED
NOT_CORE_MACHINE_PROVED
```

这张卡排除了两种相反的过度读法：

- 不能说“只有级数，所以 IEP 没有任何 promotion”；它有 composite source promotion。
- 不能说“Mizar 级数 theorem 已经证明 runner 的原任务完成”；full Q 与 bridge没有进入该 theorem。

## 4. successor scan

F-B 的 Mizar/FOTG leaf已把 source evidence推进到 component level，并在 strict Q reading 上显示 task switch。它仍没有 `Adequacy`：为什么一个基础框架 (M) 应当要求 source application 为 full-Q promotion 支付 bridge。

下一项最小行动为 `C5A-FOUNDATION-ADEQUACY-SOURCE`：只寻找版本固定的集合论／数学基础来源，明确它对“解释、保真、模型、应用、语义”承担何种责任；逐项判断其是否真的要求 process-completion bridge，而不是把研究者的规范偏好写成 ZFC 公理。若无 payment，记录 source scope并转下一个候选族；不得将无来源沉默直接写成 ZFC failure。
