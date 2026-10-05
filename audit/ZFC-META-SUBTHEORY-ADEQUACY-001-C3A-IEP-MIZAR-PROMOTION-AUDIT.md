# C3A：IEP/Mizar exact promotion P 的来源审计

> **身份：** `C3_PROMOTION_CARD / EXACT_PAIR_REJECTED_WITH_SCOPE / NOT_A_CORE_VERDICT`。
>
> **TaskCard：** [C3A](ZFC-META-SUBTHEORY-ADEQUACY-001-C3A-TASKCARD.md)。
>
> **判词：** `P_MATH_DEFINITIONAL_ADMISSION_SOURCE_SUPPORTED / P_MIZAR_TO_PHYSICAL_Q_UNPAID / P_STRICT_ORIGINAL_REFUTED_BY_EXPLICIT_REVISION / C3A_LOCAL_LEAF_CLOSED`。

## 1. 分开三个容易被同名“解答”吞掉的 P

| 名称 | 来源所做的事 | 与 C1A/C2A 的关系 | 判定 |
|---|---|---|---|
| `P_math` | IEP 说明无限级数的和以 partial sums 接近有限值来定义；Norton 也指出这是一项现代数学附加定义。 | MML `Partial_Sums` / `summable` / `Sum` 正是这个数学操作的 version-fixed formal analogue。 | `SOURCE_SUPPORTED_AS_DEFINITIONAL_ADMISSION`。 |
| `P_motion` | IEP Standard Solution 说 runner path 是 physical continuum、以有限正速度完成；并把微积分、classical mechanics、real time/position 放入模型。 | `SERIES_1` 不定义 runner、path、time、speed、derivative 或 physical model。IEP 没有引用 Mizar。 | `UNPAID_FOR_THIS_EXACT_M/S_PAIR`。 |
| `P_original_strict` | Norton 的完成分析明确把“包括最后动作”的条件删去，改成“做完所有动作”。 | C-362 的 source-certified control正是此 strict/revised distinction。 | `SOURCE_REFUTED_AS_A_BRIDGE`，限于该 strict reading。 |

## 2. 为什么 `P_math` 不是核心 promotion

`P_math` 合法地规定了一个**数学词项**“infinite sum”如何取值。它将 MML 的 `FormalDone` 与 IEP 的 `Q_math` 接起来，却不包含下列字段：

```text
the runner's physical state,
the operation of running a path,
the complete physical time model,
or the original task's Done predicate.
```

所以它最多给出：

```text
FormalDone(SERIES_1) → Done_math(series)
```

而不是 SOP 所需的：

```text
FormalDone(SERIES_1) → OriginDone(physical Q).
```

这不是以“来源没提 Mizar”为由否定标准实分析；它是对本轮**版本固定 Mizar fragment**所能承载的对象、操作、观察和完成条件作范围判断。

## 3. 实际反 promotion control

Norton 当前页给出极强的同来源反控制：

- 第 226–233 行：partial-sum 条件作为无限和定义具有额外现代数学假定的身份；
- 第 259–276 行：严格完成含“最后动作”，缩减完成删除它，原来的不可能性结论因此不再推出；
- 第 282–286 行：每个编号动作有相应时间。

这不是“Norton 已经判定 IEP 或 ZFC 错误”。它说明在此来源分母内，能够称为 `revisedResolved` 的东西不能被悄悄写成已付的 `StrictCompletion` bridge。

IEP 自身也把 Standard Solution 的物理适切性保留为可争论问题：其第 98、100–104、125–130 行分别谈到 real analysis 对真实时间、空间、具体现实的争议、概念修订和 standard solution 的多种哲学立场。故本卡不从 IEP “resolution” 一词直接推导 `OriginDone`。

## 4. C3A leaf verdict

```text
actual P for Mizar SERIES_1 → physical original Q  = NOT_SOURCE_PAID
actual P for Mizar SERIES_1 → mathematical series  = SOURCE-SUPPORTED DEFINITION
strict bridge in Norton contract                    = SOURCE-REFUTED / task revision
```

这排除了一个具体错误路径：把一个形式化几何级数定理连同 IEP 的“标准解法”标签一起称作 bare ZFC 已经完成 physical Q 的 machine-proof evidence。它没有排除更丰富的 ZFC-founded continuous-model formalization，也没有排除另一个来源会提供 physical bridge 或 adequacy policy。

因此这不是 C4/C5/C6 的负结论，而是 **exact Mizar-series promotion route 的本地关闭**。
