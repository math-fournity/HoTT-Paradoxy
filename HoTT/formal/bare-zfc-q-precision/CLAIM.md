# bare ZFC Q 理论精度：形式命题、来源依赖与禁止外推

> **证明包：** `MP-BARE-ZFC-Q-PRECISION-001`。
>
> **Claim：** `C-364`。
>
> **身份：** `INTERFACE_RELATIVE_FORMAL_CONTROL / SOURCE_BOUND_APPLICATION_VIEW / NOT_A_FORMALIZATION_OF_BARE_ZFC`。

## 1. 被形式化的精确命题

该包固定两个 `CompletionWorld`：

```text
strictOriginal : FormalDone = true, OriginDone = false
revisedTask    : FormalDone = true, OriginDone = true
```

它们都投影到同一个粗 `StandardResolutionView.resolved`。令

```text
Determines(project, OriginDone)
  := ∃ decode, ∀ world, OriginDone(world) ↔ decode(project(world)).
```

Lean 4 core 证明：

1. `¬ Determines standardResolutionView OriginDone`；
2. `¬ CompletionBridgePaid`，其中后者是全域的
   `∀ world, FormalDone world → OriginDone world`；
3. 加入完整 completion-contract tag 的 `richCompletionView` 能决定
   `OriginDone`；
4. 一个显式的有限 code 也能决定 `OriginDone`。

因此，已证的是一个**固定接口的观察精度边界**：若接口把这两种世界都交付成同一“resolved”结果，它不能单独回答原过程 completion 是否成立；补入具体 contract 数据后，观察恢复。

## 2. 来源绑定

外部来源事实不由 Lean 证明，它们由
[P0/P1/P3 source card](../../../audit/20261004-BARE-ZFC-Q-PRECISION-P0-P3-来源接口与完成合同.md)
及其冻结的 [H095 NodeCard](../../../audit/20261004-P-DAG-SOURCE-095-BARE-ZFC-Q-PRECISION-NODECARD.md) 持有：

- SEP：ZFC 是仅以 equality 和 membership 为非逻辑核心的一阶公理系统，同时集合可表示数学对象；
- IEP：把带 Choice 的 ZF 支撑的标准实分析放在标准芝诺解答／基础的语境；
- Norton：明示从含 first/last-action 条件的严格 completion 转到不要求该条件的 revised completion；
- H095：这只冻结了一个 ZFC-supported standard-solution **application** interface，不能把研究者给出的投影写成 bare ZFC 的语义接口。

## 3. C-364 的精确范围

`C-364` 可以说：

> 在本包固定的两世界 source-contract control 中，粗标准解答视图对 `OriginDone` 没有足够观察精度；一份明确携带 contract 或 code 的富接口有足够精度。

它不可以说：

- `ZFC ⊢ False`，或 bare ZFC 不一致；
- bare ZFC 不能表达时间、数列、步骤、程序或 process contract；
- 所有标准实分析、所有 Zeno 解答或所有数学实践都遗漏 Q；
- IEP／Norton 已经证明 `FormalDone → OriginDone` 失败于每个原过程；
- 这个有限 source-contract control 与固定 HoTT Q 已经是同一个完整 Q。

所谓 bare-ZFC 的理论精度问题因而得到一个更准确的阶段性判词：**bare language/representation 与 source policy 的实际语义接口仍需分开；当前来源足以绑定 application-level contract，但不足以把 `C-364` 升格为 bare-ZFC 的全域定理。**
