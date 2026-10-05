# MSS phase-space state set：参数时间顺序的表示控制

> **package ID：** `MP-ZFC-MSS-PHASE-ORDER-CONTROL-001`
> **claim IDs：** `C-377`、`C-378`
> **身份：** `SOURCE_MOTIVATED_REPRESENTATION_CONTROL / NOT_A_BARE_ZFC_VERDICT`。

## 一手来源与精确问题

在 da Costa--Sant'Anna, *The Mathematical Role of Time and Space-Time in
Classical Physics*，PDF p.8 / printed p.8，作者先说 prediction refers to future
and time，随后把 MSS classical mechanics 的目标表述为 physical-state description：
由 `s_p(t), f(p,q,t), g_p(t)` 给出的 phase-space points；同页说 phase space does
not refer to time parameter `t`。

本包不把这段话解释为“物理预测已经失败”。它只做一个必要的表示检查：如果一个
parameterized trajectory 被投影为“访问过哪些 state”的 set/range，是否还足以决定
开始和结束的顺序？

## 形式规格

| 源概念 | Lean control |
|---|---|
| time-parameterized phase trajectory | `TemporalTrace := Bool → Bool` |
| phase-space state set/range | `RangeView := Bool → Bool`，用 characteristic function 表示 visited-state set |
| order-sensitive observation | `OrderedForward trace := trace false = false ∧ trace true = true` |
| source-level positive control | `temporalView = identity` |
| source-level negative control | `rangeView` forgets which stage supplied each visited state |

`forwardTrace` and `reverseTrace` visit the same Boolean states but in opposite order.

## Machine claims

- **C-377:** `temporalView` determines `OrderedForward`; keeping the parameterized
  trace preserves this fixed order observation.
- **C-378:** `rangeView` does not determine `OrderedForward`; the same range occurs
  for forward and reversed traces with opposite ordered-endpoint verdicts.

All selected theorems are Lean 4.34.1 core checks and report no axioms.

## What this control does and does not establish

It establishes a precise fact about the explicitly defined finite projection. It does
not establish that:

1. the paper's MSS phase-space phrase implements this exact range projection;
2. a phase-space curve never carries orientation or parameter recovery data;
3. a physical prediction, a Zeno task, a circle restoration, or full `OriginDone`
   is equal to `OrderedForward`;
4. ZFC, MSS, N, or mathematical practice fails a bridge obligation.

The source-to-spec fidelity table and C0 classification live in
`audit/20261005-ZFC-META-SUBTHEORY-ADEQUACY-C0R8-MSS-PHASE-ORDER-SOURCE-TO-SPEC-CONTROL.md`.
