# C1B4：set.mm 的 M→S 基础关系与 `geoihalfsum` 依赖卡

> **身份：** `C1_FOUNDATION_TO_SUBTHEORY_SOURCE_REPLAY / OBJECT_LEVEL_ONLY / NOT_A_CORE_VERDICT`。
>
> **TaskCard：** [C1B4](ZFC-META-SUBTHEORY-ADEQUACY-001-C1B4-TASKCARD.md)。
>
> **source replay：** [20261005-SOURCE-REPLAY-SETMM-GEO-LIMIT-001](../HoTT/verification/runs/20261005-SOURCE-REPLAY-SETMM-GEO-LIMIT-001/RUN.json)。
>
> **判词：** `C1B4_ZF_SUBTHEORY_TO_OBJECT_LEVEL_GEOMETRIC_S_SOURCE_REPLAYED_WITH_SCOPE / ACTUAL_PROMOTION_UNPAID / C1B4_LOCAL_LEAF_CLOSED`。

## 1. M 的精确范围

fixed `set.mm@160ebb…`自身把其主要 set-theory section标为 ZF，并在稍后 `ax-ac`处说明加入Choice为ZFC。C1B4不把整个数据库粗暴称为“一个单一 ZFC theorem”；它采用较窄的、足够的 M：

```text
M_ZF = fixed set.mm 的 ZF object-theory part
M_ZFC = any extension of this fixed ZF part with ax-ac
```

在本轮 exact replay中，`SHOW TRACE_BACK geoihalfsum / AXIOMS`列出的set-theoretic labels包含 `ax-rep`、`ax-pow`、`ax-un`、`ax-inf2`等ZF-side infrastructure；完整显示的trace不列`ax-ac`。这支持一个有限的 source fact：该 fixed theorem可作为 ZF-side theorem，而 ZF本身当然可嵌入常规 ZFC foundation context。

它**不**宣称已经给出每一个 source label到教材 ZF axiom schema的独立 metatheory proof，也不把“trace未列ax-ac”扩大为任何不同 set.mm 版本或任何分析 theorem的一般性质。

## 2. S 的精确范围

```text
S_setmm = { df-seq, df-rlim, df-sum, geoihalfsum }
```

其中 `geoihalfsum` 的对象层式子是：

```text
sum_ k e. NN (1 / (2 ^ k)) = 1.
```

本轮 verifier先验证固定数据库全部47,917条`$p` proofs，随后对该 theorem输出完整 `$a` traceback。因此这是版本固定的、已实际核验的 object-level geometric-series S；不是单纯网页上的 theorem catalog，也不是 proof verifier 对一个外部过程的 acceptance。

## 3. 仍然没有 P 或 Bridge

IEP current page把 ZF(C)、real analysis和 Standard Solution并列，但本次网页检索对 `Metamath` / `Mizar` / `formalization`没有命中。这个负结果只说明该固定 IEP page不把 `set.mm` 作为其 application consumer。它不证明数学共同体从未以别的形式使用类似formalization。

所以本卡支付的唯一核心箭头是：

```text
M_ZF (hence admissible in a ZFC-founded context) → S_setmm (object-level series/limit theorem)
```

`S_setmm → Q_physical`、`P`、`Bridge`和`Adequacy`仍为空。它们不能由同一个级数公式或全库 proof verification补上。

## 4. 自动后继

进入 **C2B4：set.mm `geoihalfsum` 与 C2C dense process的 source-to-spec fidelity**。该卡必须处理索引约定、partial-sum limit、finite-stage non-arrival、continuous endpoint正控制之间的准确关系。若只得到数学形状类比，必须记录为 `Q_MATH_ONLY`，随后 C3B4审实际 promotion route。
