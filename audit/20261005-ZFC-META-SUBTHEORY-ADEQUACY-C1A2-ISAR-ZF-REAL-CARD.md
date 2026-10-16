# C1A-2：Isabelle/ZF 实数模型的基础关系卡

> **身份：** `CORE_ADEQUACY_TASK_CARD / C1_SOURCE_WITNESS / SOURCE_REPORTED_FORMAL_THEOREM_UNREPLAYED / NOT_A_CORE_VERDICT`。
>
> **父方案：** `ZFC-META-SUBTHEORY-ADEQUACY-SOP`，C1；前卡：[C1A](20261005-ZFC-META-SUBTHEORY-ADEQUACY-C1A-FOUNDATION-THEOREM-CARD.md)。

## 1. C1A-2 的判别问题

在 C1A 中，IEP 给出了 `ZFC+Choice → standard analysis → Standard Solution` 的应用语言，Mizar 给出了 FOTG 下的具体极限 theorem；二者没有同一基础或定理身份。

C1A-2 只检验：能否在一个版本固定的、明确以 **ZF** 为基础的形式化源里，至少找到 `M → S` 的实数／连续统子理论关系，而不是从 proof checker 或泛泛教材替代它。

## 2. 固定的 Isabelle/ZF witness

| 字段 | 来源支付的内容 | 范围 |
|---|---|---|
| `M_ZF` | IsarMathLib 明说使用 Isabelle 的 ZF logic；GitHub README 将自身称为 Isabelle/ZF 的形式化数学库。 | `SOURCE_REPORTED_FOUNDATION_IDENTITY`；没有在本机重建 ZF heap。 |
| `S_ZF` | `Real_ZF_1.thy` 构造 `RealNumbers / RealAddition / RealMultiplication / OrderOnReals`。 | 固定 commit 与 raw SHA 已保存。 |
| exact theorem identity | `eudoxus_reals_are_reals : IsAmodelOfReals(RealNumbers, RealAddition, RealMultiplication, OrderOnReals)`；该源将其解释为“由整数加法群构造的实数给出 complete ordered field”。 | `SOURCE_REPORTED_FORMAL_THEOREM_UNREPLAYED`。 |
| S 的后续接口 | `Real_ZF_2.thy` 说明这项构造给 ZF world 提供具有所需性质的 real model，并在 complete ordered field 前提下定义 metric/topology、sup/inf。 | 说明 S 有连续统／实分析方向的明确正式接口；不等于已经有指定数列的极限 theorem。 |
| 本地执行 | `command -v isabelle` 与 `command -v Isabelle2025` 均没有结果。 | `LOCAL_REPLAY_UNAVAILABLE`；不写作 kernel replay。 |

## 3. 对 F-053 的精确作用

这一 witness 支付：

```text
M = explicit Isabelle/ZF source context
S = explicit construction of a complete ordered field of reals
M → S = source-reported formal theorem at a fixed Git commit
```

它没有支付：

```text
Q            = Achilles/Dichotomy original task
FormalDone   = a specified sequence reaches a specified endpoint / finite-time arrival
P            = source statement that this theorem resolves Q
Bridge       = FormalDone ↔ OriginDone
Adequacy     = M must check that bridge
```

从 ZF 到 ZFC 的逻辑扩张关系不能在本卡被暗中当作 source-to-spec payment。即使一个 ZF theorem 通常也可在 ZFC 中使用，IEP 并没有指定使用这一套 Eudoxus construction，也没有把 `eudoxus_reals_are_reals` 作为其 Standard Solution 的 theorem。因此它是 `F-B` 的 C1 witness，不能替 `F-A` 填上 exact theorem identity 或 P consumption。

## 4. C1A-2 判词与控制

```text
F_B_C1_ZF_FOUNDATION_TO_COMPLETE_REAL_MODEL_SOURCE_WITNESS
LOCAL_REPLAY_UNAVAILABLE
F_A_P_THEOREM_IDENTITY_UNPAID
Q_FORMALDONE_BRIDGE_ADEQUACY_UNPAID
NOT_CORE_MACHINE_PROVED
```

**正控制：** Mizar FOTG/MML `Th87` 有具体 real-sequence convergence theorem，却因基础 variant 与 Q/P 缺失不能填 core contract。这验证了“找到极限 theorem”本身仍不足。

**负控制：** `Real_ZF_2` 的 complete field locale提供了实数、度量和上确界语言，却没有在本卡读取的固定 source 中支付 runner 的 finite-time conclusion。它验证了“有 real model”不等于“已有 P”。

**最强反证：** 找到同一版本的 Isabelle/ZF 文件或经来源明确链接的 companion source，给出指定 Zeno partial-sum／trajectory theorem，并被 IEP 或等价实际 P 明确消费且支付 Bridge。

## 5. successor scan

`C1A-2` 成功缩小了 M/S 的不确定性，但没有让 C2 合法启动。下一项是：

```text
C1B-SEQ-LIMIT-IDENTITY:
在当前 commit 的 IsarMathLib 或另一版本固定的 ZF/ZFC formalization 中，
寻找指定 real sequence / geometric partial sum / convergence theorem；
把它与 IEP P 的 precise input、FormalDone 与完成合同逐字段比较。
```

若该 source 只有 real-model construction而没有匹配的 sequence theorem，应登记 `THEOREM_IDENTITY_UNPAID` 并转向另一个 `F-B` formalization；不得把“有 complete ordered field”升级成“Zeno 已解决”。
