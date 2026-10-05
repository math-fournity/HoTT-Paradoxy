# C1D：IEP Standard Solution 中的 ZFC—standard analysis actual M→S foundation card

> **身份：** `C1_ACTUAL_FOUNDATION_TO_SUBTHEORY_SOURCE_CARD / SOURCE_SUPPORTED_WITH_SCOPE / NOT_A_CORE_VERDICT`。
>
> **TaskCard：** [C1D](ZFC-META-SUBTHEORY-ADEQUACY-001-C1D-TASKCARD.md)。
>
> **source：** IEP [*Zeno’s Paradoxes*](https://iep.utm.edu/zenos-paradoxes/)，2026-10-05读取，本次view行100–126、147–184。
>
> **判词：** `M_ZFC_STANDARD_ANALYSIS_FOUNDATION_SOURCE_SUPPORTED / C1D_LOCAL_LEAF_CLOSED`。

## 1. 来源字段

IEP在其Standard Solution的历史／基础段落明确说：

- standard analysis以Zermelo–Fraenkel set theory作为其严谨基础的发展环境；
- 多数观点认为加入Choice的ZFC为real analysis和其他数学领域提供适当foundation，并间接解决Zeno；
- Standard Solution使用standard calculus与Zermelo–Fraenkel set theory，且将real-analysis concepts应用于motion paradoxes。

因此本项目当前actual source contract可以固定：

```text
M_actual = IEP所说的ZFC / ZFC-with-Choice foundation context
S_actual = standard real analysis + calculus + linear continuum model
```

这比 C1A Mizar/TG 或 C1B4 set.mm更直接地对应 IEP 自己的 Standard Solution discourse。那些formalizations仍是对象层可重放控制，不是IEP的historical consumer。

## 2. 支付范围

`M_actual → S_actual` 已由来源支付；没有由此支付：

```text
S_actual → user/C2C OriginDone
P_actual 的 user-Q classification
BridgePaid
bare-ZFC internal Adequacy duty
```

基础关系能够说明ZFC在该数学框架中扮演什么角色，不能让来源语句自己变成 ZFC 公式或物理过程的 theorem。

## 3. 后继

下一条核心链已具备actual M、S、C2C Q、C3C P、C4C Bridge audit与C5E policy adjudication的输入。C6D只可机器化这些已标明身份的字段后果，不得把本卡扩大为`ZFC ⊢`任何 physical-completion claim。
