# HMZ-014：Separation schema、统一算符与受限 truth 的预检

> **身份：** `SOURCE_PREFLIGHT / EXISTING_R_CONSTRUCT_MACHINE_ROUTE / SCHEMA_OPERATOR_CONTROL / ADMISSION_REJECTED_WITH_SCOPE / NOT_A_FULL_DENOMINATOR_RUN`。

## 预检问题

`ZFC-H9` 的精确探针是：ZFC 对每个已固定公式给出 Separation instance，是否会被理论或真实消费者升级为一个对象语言内部、对任意公式代码 \(p\) 与集合 \(a\) 都正确的统一算符 `Build(p,a)`？若有，是否会迫使整个 \(V\) 的 truth/satisfaction 被当作已交付，从而接近罗素模式 P 的存在性、再入或预支使用结构？

本预检将这个探针与两种来源对照：Voevodsky 的 type-system derivation operations，及 Koepke–Koerwien 对编码、schema、受限结构 satisfaction 和递归 truth 的明确构造。它不把“ZFC schema 没有统一 Build”直接写成 ZFC 缺陷；恰恰要检查该边界是否是来源明示的 payment/guard。

## 冻结来源

| ID | 类 | 来源 | 原件／身份 | 作用 |
|---|---|---|---|---|
| `HMZ-S-012` | A/B | Vladimir Voevodsky, *Univalent Foundations and Set Theory*, 2013. | [HMZ-002 原件](../20261003-HMZ-002-voevodsky-set-theory/originals/HMZ-S-012-Voevodsky-2013-Univalent-Foundations-and-Set-Theory.pdf)，SHA-256 `bf2e5e71f00503d0d9297ceada068ee698bf0d1fcc2b14496d6b462927aecbeb`. | Slides 7–11：type-system derivation rules作为固定 operations/equations及其 B-system model。 |
| `HMZ-S-010` | C/E | Michael Shulman, *Set Theory for Category Theory*, 2008. | [HMZ-001 原件](../20261003-HMZ-001-primary-motives/originals/HMZ-S-010-Shulman-2008-Set-Theory-for-Category-Theory.pdf)，SHA-256 `3f1e2d9f9a7a026ab54cd982cfad8742c9c38e9696cb60b52e18dfaa90298012`. | PDF p. 15 footnote 9 / derived lines 740–760：公式代码、all-axioms truth与NBG/MK class-forming boundary。 |
| `HMZ-S-029` | C/D/E | Peter Koepke and Martin Koerwien, *Ordinal computations*, *Mathematical Structures in Computer Science* 16 (2006), 1–18, DOI `10.1017/S0960129506005615`. | `originals/HMZ-S-029-Koepke-Koerwien-2006-Ordinal-Computation.pdf`; SHA-256 `e9a0765407ff214d1017ae48a4bab810845e590c9117f0fcacd633cd3f7fc151`. | pp. 1, 6–7, 16–17：formula coding, SO schemas, structured satisfaction, ordinal-machine truth T and reflection. |

## Source-supported comparison

```text
ZFC-H9 desired Build:
  one object-language builder correct for arbitrary formula codes and arbitrary
  set inputs, with a whole-V truth consequence.

Shulman control:
  individual axioms/schema instances are not a single all-axioms theorem;
  Gödel coding and class quantification are needed in the stronger setting
  discussed there.

Koepke–Koerwien control:
  formula codes, an explicit LT language, a specified set-sized ordinal
  structure, assignments, a recursive truth T and a reflection ordinal θ are
  all supplied. Their T is not a bare-ZFC whole-V evaluator.

Voevodsky comparison:
  derivation rules also form a fixed formal system of operations/equations;
  this source does not claim a uniform evaluator for every formula code.
```

## Preflight disposition

```text
new HoTT primary motive: NO
existing R-CONSTRUCT / R-MACHINE comparison: SOURCE-REPORTED
ZFC schema → unified internal Build: NOT A SOURCE COMMITMENT
restricted code/truth consumer: SOURCE-REPORTED WITH EXPLICIT LANGUAGE,
  STRUCTURE, RECURSION AND REFLECTION PAYMENTS
P1 native u/F/C for proposed whole-V Build: FAIL
P2/P3 same-object reentry or pending admission: NOT SUPPLIED
P4 unbounded self-reference: NOT SUPPLIED; source recursion is restricted and
  structurally staged
P5 preemptive use: NOT SUPPLIED
H0→Z0: NOT FORMED
SUCCESSOR RUN: ADMISSION_REJECTED_WITH_SCOPE
```

This preserves H9 as an open source-admission class only for a consumer that actually claims the forbidden whole-V `Build` contract or that conceals the coding/structure/reflection payment. The sources inspected here instead expose those conditions.
