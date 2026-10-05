# C0B1：TG/MML 中更丰富连续模型子理论的来源盘点

> **身份：** `C0B_SOURCE_INVENTORY / RICH_S_CANDIDATE / NOT_A_PHYSICAL_OR_COMPLETION_VERDICT`。
>
> **TaskCard：** [C0B1](ZFC-META-SUBTHEORY-ADEQUACY-001-C0B1-TASKCARD.md)。
>
> **判词：** `MML_RICH_CONTINUOUS_MODEL_FRAGMENT_SOURCE_SUPPORTED / PHYSICAL_INTERPRETATION_UNPAID / C0B1_LOCAL_LEAF_CLOSED`。

## 1. 冻结的 M 与三个 S 入口

全部下列条目属于 C1A 固定的 Mizar 8.1.15 / MML 5.94.1493 current distribution，因此共享 TG 的来源级基础关系；本卡不把它们的 checker status重放成本机 run。

| MML article | source locator | 覆盖的数学字段 | 没有覆盖的字段 |
|---|---|---|---|
| [NFCONT_4](https://mizar.uwb.edu.pl/version/current/html/nfcont_4.html) | `PartFunc of REAL,(REAL n)`；`is_continuous_in` 的 epsilon-delta definition。 | real parameter、real-vector-valued function、连续性。 | 物理时间／空间解释、runner。 |
| [NCFCONT1](https://mizar.uwb.edu.pl/version/current/html/ncfcont1.html) | real/complex normed linear spaces；以收敛 sequence／limit 定义 continuity。 | sequence-limit 与 real/vector function continuity 的连接。 | 速度或具体 path。 |
| [ORDEQ_02](https://mizar.uwb.edu.pl/version/current/html/ordeq_02.html) and [INTEGR26](https://mizar.uwb.edu.pl/version/current/html/integr26.html) | functions from `REAL` into a real Banach space；continuous/differentiable conditions及导数／单边极限关系。 | real-domain trajectory 的函数型、可微性／speed proxy。 | “它是一个正在跑的物体”、有限正速度、原任务完成。 |

这比 C1A 的 `SERIES_1` 明确多付了 IEP 所列的**数学结构**：实时间样式的参数、位置样式的值域、连续性以及导数／速度样式的对象。它是 `S_rich` candidate，而非只包含 geometric sum 的 `S_series`。

## 2. 与 IEP 字段的局部对应

IEP 对 Standard Solution 的数学模型提到 physical continuum、real time/position、continuous position function、derivative as speed（第 68–88 行）。就形式对象而言，可作下列受限对应：

```text
IEP real-time coordinate         ↔ MML REAL domain
IEP position function            ↔ MML PartFunc REAL,(REAL n) / REAL-Banach-space function
IEP continuity                   ↔ NFCONT_4 / NCFCONT1 predicates
IEP derivative/speed calculus    ↔ INTEGR26 / differential-function predicates
```

这使下一个 C2B 能够首次审计一个包含 `time / position / continuity / derivative` 的 **mathematical** S，而非只审计 partial sums。

## 3. 仍未支付的边界

`S_rich` 并不因此得到 IEP 的物理语义。MML source 仍未给：

```text
physical runner identity,
the empirical claim that real parameters are physical instants,
the physical realization of a continuum trajectory,
or OriginDone for the runner's original process.
```

所以本卡只允许：

```text
M → S_rich mathematical-model candidate
```

不允许：

```text
M → physical reality,
S_rich FormalDone → OriginDone,
or an M adequacy judgment.
```

这正是 C0B1 的必要负边界：如果连续函数 source 本身被称为“已经把运动解决”，C3A 的旧错误会换一个更丰富的名字重新出现。

## 4. 叶判词与可证伪性

**通过。** 同一 TG/MML foundation 分母确实有版本固定的 mathematical continuous-model fragment，可进入更丰富的 C2。

**未通过的主张。** 未找到 MML source 把该 fragment解释为 physical motion、支付 completion bridge 或接受 IEP 的 resolution policy。
**重开。** 若 source version、article identity或其 formal fields 被直接推翻，重新盘点；若 C2B 不能使 IEP 与 `S_rich` 保持同一数学模型，关闭 richer-Mizar route，转 C0B2/C0C1。
