# P-DAG-ZFC-019–022：all-subobjects site、冻结 consumer relay 与当前 source gap

> **身份：** `POST_HOTT_REPLAY_ZFC_DISCOVERY_CALIBRATION / FORMAL_MODEL_BOUNDARY / NOT_A_ZFC_Q_OR_INCONSISTENCY_RESULT`。

## 1. H019：P1 看见明显 site，却拒绝直接形成问题

H019 的 blind input 没有“Power Set”名称、历史候选或实际 consumer。Terra/Max 在 90.416 秒自然终态（0 tool/file/approval；private liveness `RUNNING → STILL_RUNNING@61.514 → TERMINAL`；wire SHA-256 `983bf6b5660ff009f51d91663a3ed7f9f7131c1ca6841ed9ab58988709757dc8`）。它选到规则“对每个 a 交出所有子对象 B(a)”并立即识别：

```text
formation task B(a): DISCOVERY_DIRECT_RULE_ANSWER
terminal: NO_MODEL_RECALL_CANDIDATE / DIRECT_PAYMENT_ONLY
```

这是一项 P1 正确控制。它说明模型可定位明显 formation interface，也说明“形成 B(a)”本身已由规则支付，不能伪造为剩余 Q。

## 2. H020：无冻结 parent 的 source mapping 不作为验证

H020 在 Mathlib ZFSet card上自然终态、E0–E7完备、0 tool/file/approval，然而其 prompt没有携带 H019 的 parent 字段；worker合法地把候选换成了泛化 `f`。它因此不能验证 H019，也不能反驳旧的 `powerset → funs` source trace。

这一事件是 `EXECUTION_SPEC_INCOMPLETE`：source P1 validation prompt 必须冻结父节点 `T/u/F/Q?`，验证者只能补、拒绝或收窄，不能重选。该修复已进入 010、P-DAG SOP 和 H022 NodeCard。H020 的有限结论只是：裸摘录本身没有自明的正义务，不能写为 ZFC 的数学或哲学结论。

## 3. H021/H022：冻结 formal-model card 的有效判词

H021 固定如下 model-layer source card：

```text
T     = Mathlib ZFSet model @ v4.16.0/a6276f4… (not standard ZFC)
u     = powerset (prod x y)
F     = powerset
C     = funs x y := sep (IsFunc x y) u
I/O  = x,y,f,u → funs x y
Done  = mem_funs: f ∈ funs x y ↔ IsFunc x y f
Q     = UNSET
```

H022 was a fresh source-match validation that was explicitly forbidden to replace those fields. It ran 113.963 seconds with `RUNNING → STILL_RUNNING@61.371 → TERMINAL`, 0 tools/files/approvals, E0–E7 complete, and a 633-event direct-wire trajectory. Its public reasoning distinguishes:

- `f ∈ powerset(prod x y) ↔ f ⊆ prod x y` is already an F-level membership translation, so not an independent L6 Q;
- `IsFunc x y f` and `f ∈ funs x y` are ordinary classification queries; false produces a legitimate false result, so L7 fails;
- the card contains no existential/function-construction action or source-level Done that positively requires a new fact.

The valid outcome is therefore:

```text
QUALIFYING_FORMAL_MODEL_CONSUMER_WITH_SCOPE
NO_DISTINCT_Q / Q_UNSET
NO_COMMON_Q / NOT_ZFC_Q_LOCATED
```

It is stronger than a keyword search but sharply limited to this Mathlib model/API excerpt. It does not say that standard ZFC has no relevant consumer, that all mathematical use of powersets is harmless, or that the user’s time/process hypothesis is false.

## 4. Why no P2/P3 node follows H022

P2 and P3 have not been skipped. The DAG contract says they run after a validated P1 card carries a candidate Q that survives L6/L7. H022’s parent has `Q_UNSET`; launching P2/P3 would force a language feedback or lifecycle story onto a card that has no P1 obligation. The next admissible action is a new version-fixed **standard-ZFC or actual-use source** whose consumer provides:

1. an input/output/Done contract at one declared layer;
2. a positive obligation involving the all-subobjects object, beyond membership classification;
3. source facts allowing P2/P3 to test the same `u/F/C/Q/I/O/Done` card.

Until such a source is frozen, `ZFC_SITE_SELECTED` is the strongest location status and `ZFC_Q_LOCATED` remains blocked.

