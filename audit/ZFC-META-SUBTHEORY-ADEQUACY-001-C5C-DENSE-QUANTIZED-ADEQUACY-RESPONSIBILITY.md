# C5C：稠密—量化 completion-contract difference 的基础充分性责任审计

> **身份：** `C5_ADEQUACY_RESPONSIBILITY_AUDIT / SOURCE_LAYERED / NOT_A_CORE_VERDICT`。
>
> **TaskCard：** [C5C](ZFC-META-SUBTHEORY-ADEQUACY-001-C5C-TASKCARD.md)。
>
> **来源范围：** IEP [*Zeno’s Paradoxes*](https://iep.utm.edu/zenos-paradoxes/)；SEP [*Scientific Representation*](https://plato.stanford.edu/entries/scientific-representation/)（2026-10-05的 substantive revision）；SEP [*Set Theory*](https://plato.stanford.edu/entries/set-theory/)；IEP [*Foundations of Mathematics*](https://iep.utm.edu/fomath/)；C0C1、C4C、C5A 与 C-369。
>
> **判词：** `COMPLETION_CONTRACT_DIVERGENCE_SOURCE_SUPPORTED / TASK_SWITCH_VS_ORIGINAL_RESOLUTION_CLASSIFICATION_UNRESOLVED / APPLICATION_ADEQUACY_CRITERION_SUPPORTED_WITH_SCOPE / BARE_ZFC_ADEQUACY_DUTY_UNPAID_WITH_SCOPE / C5C_LOCAL_LEAF_CLOSED`。

## 1. 三层责任不能合并

| 层 | 当前来源实际支持 | 当前来源没有支持 |
|---|---|---|
| `M` 作为数学基础 | SEP *Set Theory* 说明集合论语言可形式化数学对象、概念和论证，并在该意义上成为数学基础（本次页行15–16、144–154）。 | bare ZFC因此必须对每个物理运动任务的完成契约作内部裁决。 |
| application / representation | SEP *Scientific Representation* 把模型到 target 的 representation、surrogative reasoning、accuracy和数学对物理世界的适用性列为独立问题（行45–49、62–71、76–88）。 | 存在唯一、无争议、由ZFC公理直接给出的 bridge。 |
| current Standard Solution | IEP 用continuous model解决语言，同时明说 user/C2C式 final-step requirement不被接受。 | 它已经证明 finite-stage `OriginDone` 或把这项判断归为bare ZFC的semantic duty。 |

IEP *Foundations of Mathematics* 也明确基础一词可以只指形式框架，也可以附带哲学／认识论要求，而标准没有单一共识（本次页行74–85、197–205）。这阻止我们把“基础应当足够精确”未经说明地改写成 ZFC 的既有对象语言公理。

## 2. C4C 的 source facts不足以自行选择 C-369 的哪一支

C4C已经固定两条同时为真的来源事实：IEP用 Standard Solution 的语言称其为 Achilles/Dichotomy 的 resolution，同时又把“必须有 final step”列为错误的要求。相对 user/C2C 的 finite-natural-stage Done，这给出的是**completion-contract difference**；它尚未单独裁定“IEP是否仍声称解决用户原任务”。

因此必须保留两种、不可偷换的 `ApplicationCase` 读法：

```text
resolution-reading:
  applicationClaim = true
  claimsOriginalResolution = true
  explicitTaskSwitch = false
  -- 读“resolution”是在用户Q上的宣称；若无bridge，C-369 failure branch适用。

task-switch-reading:
  applicationClaim = true
  claimsOriginalResolution = false
  explicitTaskSwitch = true
  -- 读“final step is mistaken”是明确改写C2C Done；C-369 TaskSwitchControl适用。
```

IEP文本支持两个字段各自的来源句，却没有给出一条元规则说明如何把它们相对于用户的 `OriginDone` 合并为唯一 classification。故这一步的正确状态是 `TASK_SWITCH_VS_ORIGINAL_RESOLUTION_CLASSIFICATION_UNRESOLVED`，而不是“task switch已经自动为bare ZFC辩护”。C-369仍可分别机器检查两种已明示case的逻辑后果；它不替来源做分类。

## 3. 什么仍然没有支付

本分母中没有一个版本固定的 bare-ZFC-facing source 给出：

```text
Observe_Q / Reject_Q / BridgePaid_Q / AdequacyLift_Q
```

其中 `Q` 是用户要求的有限阶段、最小粒度 `OriginDone`。SEP的 representation discussion支持“模型到物理 target的适切性是一个须说明的问题”；它不把这个一般哲学条件指定为 ZFC 的 internal rule。SEP/IEP关于集合论基础的材料支持它是数学的形式／解释性基础，但没有把 C2C的 physical motion contract放进其 actual acceptance interface。

所以本叶得出的不是“ZFC已经通过审查”或“ZFC已经失败”，而是：

```text
within this source denominator:
  completion-contract divergence is source-supported;
  task-switch vs original-resolution requires an extra Q-policy adjudication;
  an actual bare-ZFC adequacy interface for user Q is not source-paid.
```

## 4. 控制和禁止外推

- **Task-switch / original-resolution双读控制：** C4C的来源事实可以进入 C-369 两个不同case，但不得在没有 `OriginDone` 同一任务裁定时替它选一支；
- **unpaid-bridge control：** C4A/C6A保留IEP physical application的一条不同、未形式支付的 bridge route；
- **representation control：** SEP允许误表征的可能，防止“数学模型存在”被写成其 target自动成立；
- **禁止外推：** 不说 ZFC不能表示离散过程、不说现实量子化已证、不说 IEP错误、不说所有Standard Solution都只是换题、不说bare ZFC的理论精度已被证明充分或不足。

## 5. 自动后继

进入 **C5D：source classification bifurcation 的形式规格与机器控制**。它必须把 resolution-reading与task-switch-reading写成相同source facts下、不同`OriginDone`读法的两个显式case，分别调用C-369逻辑，证明没有完成合同裁定就不能机器地从来源文本选出唯一adequacy verdict。C0R2及其F-B branch可以保留为独立候选来源工作，但不得再称F-A2已经在C5层关闭。
