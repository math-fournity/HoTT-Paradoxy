# HMZ-008：R-HIGHER 与 Set/ZF 语义来源分母

> **身份：** `SUCCESSOR_SOURCE_RUN / FROZEN_DENOMINATOR / DENOMINATOR_COMPLETE_WITH_SCOPE / MODEL_SEMANTIC_AND_ASSUMPTION_CONTROLS / NO_ZFC_Q_CLAIM`。

## 研究问题

HoTT Book 的 `R-HIGHER` 说 higher inductive types（HITs）提供基本同伦空间和构造的直接逻辑描述，不能被 classical
set-theoretic foundations **directly** 捕获。Set/ZF 的 HIT 语义文献究竟表明：ZFC-side 是否在同一 formation/consumer/Done
任务上留下了模式 P 的未付张力，还是它们建立的是已支付的 model-semantic task？

## 冻结分母

| ID | 类 | 来源 | 状态 | 作用 |
|---|---|---|---|---|
| `HMZ-S-001` | A | HoTT Book 2013（HMZ-001 复用）。 | `REUSED_R_SOURCE` | `R-HIGHER` 的 “directly” 原文与 HIT 动机。 |
| `HMZ-S-024` | B, C, D | Lumsdaine & Shulman, *Semantics of higher inductive types*, arXiv:1705.07088v2, 2019。 | `READ_RELEVANT_LOCATORS` | model category / local universes / strict stability 语义构造的 obligations。 |
| `HMZ-S-025` | C, D, E | Andrew W. Swan, *A class of higher inductive types in Zermelo-Fraenkel set theory*, arXiv:2005.14240v2, 2021。 | `READ_RELEVANT_LOCATORS` | ZF 中 image-preserving QW-types；ZF 不足以构造的另一类 QW-type；Choice/cardinality假设边界。 |

### 冻结范围

本 run 考察“直接 type-theoretic formation”与“Set/ZF semantic model/initial algebra”之间的任务边界，不考察所有 HIT、
所有 ZFC 语义、HIT 统一 syntax 或 Power Set 的独立 P-FORGE 站位。

## 结果摘要

```text
some HITs/QW-types in Set/ZF: SOURCE-SUPPORTED
some QW-type not provably present in ZF: SOURCE-SUPPORTED, but not a ZFC claim
semantic model construction: explicit stability/cardinality/choice obligations
same direct formation/consumer/Done as HoTT rule: NOT ESTABLISHED
P2/P3 same-object reentry: NOT SUPPLIED
P-qualified ZFC Q: NO
```

详见 [SOURCE-CATALOG](SOURCE-CATALOG.md)、[R-CARDS](R-CARDS.md)、[Z-CARDS](Z-CARDS.md)、[Q-CARDS](Q-CARDS.md)、[CONSUMER-CONTROLS](CONSUMER-CONTROLS.md)、[COVERAGE](COVERAGE.md) 与 [FINDINGS](FINDINGS.md)。
