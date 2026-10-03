# HMZ-003：消费者与标准支付

## HMZ-C-010 — Isabelle/ZF practical syntax

| 原始层 | 实际支付 |
|---|---|
| Traditional ZF axioms | Existence of empty sets, unions, powersets and related objects. |
| Isabelle/ZF practical layer | Constants `0`, `Inf`, `Pow`, `Union`, `Replace`, `RepFun`, `The`; syntax translations and derived rules. |
| Nonunique infinity | The source explicitly says `Inf` is not uniquely defined, yet names it as a constant to simplify natural-number work. |
| Done discipline | `The` requires unique existence; `Replace` carries its single-valued condition; derived rules state their conditions. |

The contrast is evidence of an explicit implementation/interface choice. It does not establish that the bare
ZFC theory internally runs a construction process or that the named constant is a hidden contradiction.

## HMZ-C-011 — computation versus axiom control

Grayson’s natural-number example distinguishes reduction by inductive definitions from axioms without effective
decision methods. This is a source-supported **contrast of proof/computation roles**. It is not a permission to
call every non-effective axiom a failed construction, because the source retains such axioms as permissible
hypotheses under its stated conditions.

## HMZ-C-012 — HoTT library countercontrol

The HoTT Library source reports that its setting uses axioms for univalence and function extensionality that block
computation in some proofs; cubical technology is described as an improvement. Therefore:

```text
type-theoretic foundation / proof assistant
≠ unconditional computation of every proof term
≠ evidence that ZFC's formalization interface is uniquely defective
```
