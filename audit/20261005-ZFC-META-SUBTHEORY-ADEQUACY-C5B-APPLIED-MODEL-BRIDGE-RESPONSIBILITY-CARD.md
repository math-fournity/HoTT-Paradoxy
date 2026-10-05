# C5B：应用模型的表征责任与 bare ZFC 的基础责任分层

> **身份：** `CORE_ADEQUACY_TASK_CARD / C5_SOURCE_ALLOCATION_AUDIT / APPLIED_MODEL_BRIDGE_CRITERION_SOURCE_ESTABLISHED / ZFC_DIRECT_DUTY_NOT_ESTABLISHED`。
>
> **父方案：** [ZFC-META-SUBTHEORY-ADEQUACY-SOP](../dev-docs/ZFC元理论子理论充分性最终闭环SOP.md)。
>
> **前序：** [C5A foundation adequacy source card](20261005-ZFC-META-SUBTHEORY-ADEQUACY-C5A-FOUNDATION-ADEQUACY-SOURCE-CARD.md)。
>
> **冻结来源：** [C5B snapshot manifest](../sources/external/zfc-meta-subtheory-c5b-20261005/README.md)。

## 1. C5B 的问题

C5A 已表明：set-theoretic foundation 的 faithful-representation criterion 只直接覆盖 mathematics 内部的 mathematically relevant features。C5B 检验 IEP Standard Solution 的 physical runner promotion 是否有另一类来源责任，从而回答：

```text
当 P 把 continuous mathematical model 用于 physical runner Q 时，
谁必须说明 FormalDone 到 OriginDone 的适用性？
bare ZFC / S 本身，还是 P 所构成的 applied representational model？
```

## 2. 来源给出的责任分层

SEP *Scientific Representation* 把下列内容列为一个数学化科学模型的独立问题：model 的 target、accuracy standard、misrepresentation 的可能性，以及 mathematics 如何 applied to the physical world。它明确把最后一项称为 Applicability of Mathematics Condition。

SEP *Models in Science* 再给出对本卡决定性的区分：

```text
logical model        = 结构使一个 formal theory 的句子为真；
representational model = model represents a real target system。
```

两者可同时成立，但不能相互推出。该来源还说明，interpretative model 是 mathematics/theory 到 real-world target 的中介；构造它需要 materials、approximations 与 setup 的详细知识，理论本身并不“像自动售货机一样”产出这种模型。

而 IEP Zeno 的 Standard Solution 正是后一种 application claim：它不只陈述一个 series theorem，而是把 path/time/speed 解释为 physical continuum，并由此说 runner arrives / paradox resolved。

由三份来源共同形成的最小分层是：

```text
M  (ZFC foundation)         : mathematical surrogate / proof arena
S  (real analysis mechanics): formal / logical model resources
P  (Standard Solution)      : applied representational model of Q

Bridge(Q,S) is a condition of P's target-accuracy/applicability,
not a condition supplied merely by M or by S's formal truth.
```

## 3. 对原核心问题的精确影响

这一步既不是替 Standard Solution 付款，也不是把责任从研究中抹掉。

### 已获得的来源性准则

若 P 用 S 来代表 physical runner Q，则 P 需要回答的至少包括：

```text
target(Q)                 : P 到底代表哪一个 runner/process task；
accuracy( P , Q )         : 哪些输入、操作、观察、完成条件必须相符；
applicability(S,Q)        : 为什么该数学 apparatus 可以用于该 physical target；
misrepresentation control : 哪种差异会使 P 的 promotion 失准。
```

这正是我们的 `Bridge` 字段在 application 层的来源化版本。C3A 已经显示：strict last-action Done 不是 IEP Standard Solution 保留的完成条件；C5B 现在说明，这类差异应被审计为 **representational/application adequacy**，而不能用“有一个逻辑模型／有一个 ZFC formalization”自动消失。

### 尚未获得的 ZFC 归责

SEP 也使下面的推论失效：

```text
S 是 ZFC-founded logical model
∧ P uses S for a physical target
∧ Bridge is unpaid
⇒ bare ZFC itself failed to perform a required bridge check.
```

前两项不能推出最后一项。来源给出的原因不是“bridge 不重要”，而是 **logical-model status 与 representational-model status 是不同的关系**；P 的 applied interpretation 需要额外的契约、模型构造和 target accuracy。当前来源没有说 bare ZFC 的公理系统承诺代替 P 完成这项工作。

## 4. source-to-spec fidelity table

| 来源字段 | 形式规格字段 | 已支付 | 尚未支付 |
|---|---|---|---|
| SEP Scientific Representation：数学化模型需要 target、accuracy、misrepresentation、Applicability of Mathematics Condition。 | `AppliedRep P Q`、`Accuracy P Q`、`Applicability S Q` | bridge 是有来源身份的 application obligation。 | IEP P 已逐字段支付这些条件。 |
| SEP Models：logical model 与 representational model 必须区分。 | `LogicalModel(S)` vs `Represents(P,Q)` | `LogicalModel(S)` 不能独自推出 `Represents(P,Q)`。 | 对 IEP P 的 exact model-target map。 |
| SEP Models：interpretative models 中介 theory 与 real-world target，理论不自行生成模型。 | `InterpretiveData(P)` | application bridge 的额外数据责任不由 theory-only contract 消除。 | bare ZFC 是否有额外、专属的 semantic enforcement rule。 |
| IEP Zeno：physical continuum / point-events / finite speed / resolution。 | `ActualPromotion P` | P 是 application-side promotion，非纯几何级数 theorem。 | strict OriginDone 的 preservation。 |
| C5A Maddy/SEP set-theory criterion。 | `FoundationFaithfulMath M` | 数学 surrogate 的 feature-sensitive requirement。 | 将 physical Q 的 completion 自动归入该集合。 |

## 5. C5B 判词

```text
APPLIED_MODEL_BRIDGE_CRITERION_SOURCE_ESTABLISHED
LOGICAL_MODEL_AND_REPRESENTATIONAL_MODEL_SOURCE_DISTINGUISHED
APPLICATION_BRIDGE_OWNER_IS_NOT_AUTOMATICALLY_BARE_ZFC
IEP_EXACT_TARGET_ACCURACY_AND_STRICT_BRIDGE_UNPAID
CORE_ADEQUACY_FAILURE_NOT_ESTABLISHED
CORE_ADEQUACY_DEFENSE_NOT_YET_MACHINE_PROVED
```

最重要的修正是归因分层：如果 strict completion 与 Standard Solution 的 revised completion 确实不同，来源支持把它称为 P 的 target/accuracy/applied-model 问题；它还**不支持**直接称为 bare ZFC 的对象语言错误或 bare ZFC 必须承担却没有承担的责任。

## 6. 控制与最强反证

- **Bridge-paid control：** IEP 或同源 authority 若固定同一 physical target 后证明 `FormalDone ↔ strict OriginDone`，此卡的 application gap 被支付。
- **Actual-representational-model control：** 若 IEP Standard Solution 或其明确理论消费者列出 target、accuracy 和 preservation map，且覆盖 strict Done，则 P 的责任可实付；不能因它由 ZFC 支撑而免除此检查。
- **Foundation-enforcement control：** 若一个 ZFC/set-theoretic foundational source 明确规定，任何 such physical application must be checked by the foundation itself，并将 IEP P 纳入，那么 direct M-duty 可以重新进入 C5。
- **No-overreach control：** P 尚未支付 bridge 不推出 P 是无表示、数学无效或 ZFC 有矛盾；SEP 明确允许 misrepresentation 仍是 representation。

## 7. successor scan

`C5B` 将 C5 的问题从“无来源的抽象责问”推进为可分别审计的两层责任，但仍缺 IEP P 自身的完整 target-accuracy contract。

下一项唯一最小行动是：

```text
C5C-STANDARD-SOLUTION-APPLIED-TASK-CONTRACT

在 IEP Standard Solution 与其明确引用／同层权威来源中，
固定一个版本的 runner target、continuous model、
accepted observations 和 Done condition；逐项比较：
  (a) source 是否只采用 revised completion；
  (b) source 是否声称仍是 strict original task；
  (c) source 是否给出 model→target accuracy / applicability payment；
  (d) 若没有，缺口是实际 P 的 application contract，
      而不是 bare ZFC 的未证明 defect。

只在 (a)–(d) 与 M 的 foundation role 被同一来源明确接合时，
才允许重开 direct-M adequacy failure route。
```

`reopen_if`：发现一份版本固定、同层来源把 IEP-like standard solution 的 formal model、runner’s exact task contract 和 ZFC foundation 的 mandatory validation responsibility 明确合在一起。
