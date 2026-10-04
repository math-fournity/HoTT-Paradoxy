# C-366：冻结 Zermelo 模型中的过程轨迹可表示性正控制

> **身份：** `FORMAL_CLAIM_SPECIFICATION / ZFC-H0-FINAL-PROOF-CLOSURE-SOP / M3_POSITIVE_CONTROL`。
>
> **状态：** `KERNEL_ACCEPTED_WITH_SCOPE`；canonical 主运行
> `20261004-MP-ZFC-H0-PROCESS-REPRESENTATION-001-05`，负控制
> `20261004-MP-ZFC-H0-PROCESS-REPRESENTATION-NEG-001-05`。

## 精确命题

在冻结的 [Foundation Lean](https://github.com/FormalizedFormalLogic/Foundation)
commit `f3972f4204fc61e1b736ed843415894c83f35508` 中，对任一满足该库
Zermelo 模型接口的 `V`，令 `Seq trace` 表示具有 ordinal domain 的集合函数图。
`H0ProcessRepresentation.lean` 检查：

1. `Seq trace` 的 domain 是 ordinal；
2. 对每个 `stage ∈ lh trace`，存在唯一 `value` 使得有序对
   `⟨stage, value⟩ₖ ∈ trace`；
3. 这个规范选出的 `nth` value 实际属于该函数图；
4. `Seq` 谓词和 `lh` 函数在该冻结语言中都有一阶集合论的 definability instance。

## 它支付的 M3 义务

这是一项 **可表示性正控制**。它排除下面的过强路线：

```text
bare ZFC 没有原始的时间符号
⇒ bare ZFC / 一个 ZF model 不能表示离散阶段、轨迹或阶段值。
```

它不支付 `C_accept`，不说明任何来源会把 `Seq`／`lh` 当作过程完成的充分观察，
也不证明 `FormalDone → OriginDone`。因此它支持的结论只能是：

```text
ZFC_PROCESS_REPRESENTABILITY_POSITIVE_CONTROL_MACHINE_PROVED_WITH_SCOPE
M3_LANGUAGE_ABSENCE_ROUTE_REJECTED_WITH_SCOPE
M3_ACCEPTANCE_POLICY_STILL_UNPAID
```

## 反控制

`WrongH0ProcessRepresentation.lean` 保留相同模型假设和同一个 in-domain stage，
却试图从一个 sequence graph 构造两个不同值。它应在最后的
`value ≠ value` 义务被 Lean 拒绝。该拒绝检查的是固定库中函数图的唯一值性质，
不能用来论证任何关于连续运动、H0 完整语义、ZFC 一致性或基础充分性的命题。

主运行实际打印五个声明的 axiom 依赖。它们均为 Lean 的
`propext`、`Classical.choice` 与 `Quot.sound`；模型假设
`[V↓[ℒₛₑₜ] ⊧* 𝗭]` 是定理参数，而不是本运行构造的 Zermelo model。

## 禁止外推

- 不构成 ZFC 的对象语言证明、ZFC 模型的完备语义或 ZFC 一致性证明；
- 不构成 fixed Cubical Agda H0 的 full `H0Map`；
- 不构成 bare ZFC 已具有 Q 的完成观察力；
- 不构成 community acceptance policy、`AdequacyLift`、`SameFullQ`、P/A/B 归因或矛盾。
