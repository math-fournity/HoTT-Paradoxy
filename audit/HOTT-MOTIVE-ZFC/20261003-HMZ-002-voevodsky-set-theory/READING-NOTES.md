# HMZ-002：第一轮阅读笔记（来源重建完成，未形成 Q）

## Source-reported observations

1. **Voevodsky 2011 Göteborg，slides 2–4：** 他说 ZFC 的历史目的不是令数学形式化方便；将其“key practical problem”
   称为 equivalence problem，并说 ZFC 不给区分 equivalence-respecting constructions/properties 的自然办法。
2. **同文 slides 4–5：** UF 的主张是令不尊重 equivalence 的构造在其语言中不可表达；同一 source 同时保留
   ZFC consistency benchmark 与 universal-foundation 目标。
3. **Voevodsky 2013 ASL，slides 17–21：** 更复杂的 type theories 为 practical formalization 而发展，
   但作者要求每项新语言扩张通过相对于 ZFC 的形式 certification。
4. **Voevodsky 2011 Notes：** 其 technical construction 为取得标准 isomorphism 使用 well-orderings；
   这是一项可见的代表／选择支付，而不是“相同即可无代价行动”的证明。
5. **Ahrens & North 2022：** EP 讨论明确说 set-theoretic foundations 中某些表述不随同构保持，例为
   `1 ∈ ℕ`；要建立 EP，需要限制为合适的 properties/structures，并给出 typed-language criterion。

## First candidate distinction

```text
Candidate-Z (source reported):
  ZFC syntax has no native equivalence-respecting / non-respecting partition.

What is still absent:
  A particular ZFC-side construction C, a formation F, a real consumer,
  and a same-task question Q whose answer is forced into P2/P3-type reentry
  or unpaid completion.

Nearest controls:
  Shulman gives explicit NBG/meta-language/global-choice remedies;
  Mumford keeps maps/families explicit; Isabelle/ZF makes formalization and
  derived syntax explicit; Voevodsky's own technical model pays with well-ordering.
```

The present result is `R_SOURCE_REPORTED / Z_RECONSTRUCTION_COMPLETE_WITH_SCOPE / NOT_A_Q`. It must not be reported as
“Voevodsky proved that ZFC has the desired P problem.”
