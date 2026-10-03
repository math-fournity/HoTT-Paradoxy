# HMZ-003：形式化、存在与可交付的来源分母

> **身份：** `CLOSED_SOURCE_RUN_WITH_SCOPE / FROZEN_DENOMINATOR / EXISTENCE-DELIVERY-INTERFACE_RECONSTRUCTED`。

## 问题

本 run 检查 HoTT/UF 的“计算／形式化”动机是否在 ZFC 的实际形式化中暴露出一个更窄的候选：

```text
ZFC source says ∃ object
  → does a same-layer consumer treat that object as already delivered,
    executable, or legitimate before the relevant formation/payment is present?
```

这不是把“有公理”或“没有归约”自动称为问题。对象、formation、consumer、I/O、Done 和 P1/P2/P3 均须来源支持。

## 冻结来源

| ID | 类别 | 来源 | 状态 | 作用 |
|---|---|---|---|---|
| `HMZ-S-016` | A, E | Daniel R. Grayson, *An Introduction to Univalent Foundations for Mathematicians*, 2018. | `READ_RELEVANT_LOCATORS` | 类型、归约计算、axiom与有效方法的区分。 |
| `HMZ-S-017` | A, E | Egbert Rijke & Bas Spitters, *Homotopy Type Theory and the Formalization of Mathematics*, 2016. | `READ_RELEVANT_LOCATORS` | set-theoretic encoding、weak type discipline、proof assistant computation 与 practical foundations。 |
| `HMZ-S-018` | B, E | *The HoTT Library: A Formalization of HoTT in Coq*, 2017. | `READ_RELEVANT_LOCATORS` | HoTT formalization 的实际 universe/axiom/computation constraints。 |
| `HMZ-S-011` | C, D | Isabelle/ZF 2021, reused from HMZ-001. | `REUSED_SAME_VERSION` | named ZF constants, existential axioms, derived syntax, `Inf`, `Pow`, `Replace`, `The`. |
| `HMZ-S-010` | C, D, E | Shulman 2008, reused from HMZ-001. | `REUSED_SAME_VERSION` | ZFC/NBG/meta-language and explicit Choice payments. |

## Result at source scope

```text
bare ZF existential axiom ≠ automatic executable delivery
practical formalization may add constants/derived rules = explicit payment
HoTT formalization itself may use axioms that block computation = control
P-qualified Q = not found
```

The detailed cards below keep the `Inf` naming case open only as a source-level formation/payment control; it does
not supply P2/P3 reentry or a reality-relative candidate.
