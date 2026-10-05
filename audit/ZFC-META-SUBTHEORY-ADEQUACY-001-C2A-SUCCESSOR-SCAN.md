# C2A 后继扫描：实际 promotion P 还是公开的 task revision？

> **身份：** `SUCCESSOR_SCAN / CORE_GOAL_ACTIVE / NOT_A_COMPLETION_RECORD`。
>
> **前叶：** [C2A source-to-spec card](ZFC-META-SUBTHEORY-ADEQUACY-001-C2A-IEP-MIZAR-QCONTRACT.md)。
>
> **结果：** `C2A_LOCAL_LEAF_CLOSED / C3A_SELECTED / FINAL_CORE_VERDICT_NOT_PROVED`。

## 1. 当前闭合与仍缺的箭头

现在已经有一个有界链：

```text
TG-founded Mizar M
  → MML SERIES_1 S
  → IEP Q_math / FormalDone
```

但下列箭头仍是开放的，任何一个都能改变总判词：

```text
actual P: FormalDone(Q_math) → "Zeno's original Q is solved" ?
Bridge:   FormalDone(Q_math) → OriginDone(Q_motion) ?
Adequacy: must M inspect/refuse this promotion when the bridge is absent ?
```

## 2. 后继比较

| 后继 | 能改变的总判词字段 | 最小行动 | 选择 |
|---|---|---|---|
| `C3A`：IEP/Mizar promotion audit | `P` 是否真实发生，及它是否是 Mizar theorem 的 consumer。 | 把 IEP 的 “indirectly resolves”／physical-model language 与 C2A 的 `Q_math`、`Q_motion` 分别对照；读 Norton 的 revised-resolution 句作反 promotion control。 | **已选**。 |
| `C4A`：Bridge payment | `BridgePaid` 或 explicit task switch。 | 需要 C3A 先明确 P 的 domain；否则先问什么 bridge 会变成 AI 自造。 | 等 C3A。 |
| `C5A`：Adequacy contract | M 是否承担 bridge audit。 | 需要至少一个确定的 P/bridge candidate；否则会退化为泛泛基础哲学。 | 等 C3A / 并保留 F-C。 |
| `C0B`：第二 M→S formalization | 替换或加强 M/S source denominator。 | 若 C3A 表明 Mizar never reaches application P，直接升为下一项。 | parked with explicit trigger。 |
| `C0E`：defense source | P may be explicit task revision. | Norton is already a control, but C3A must decide whether IEP itself makes the same move. | integrated in C3A。 |

## 3. 自动选择：`C3A-IEP-MIZAR-PROMOTION-AUDIT`

```text
M       = C1A's TG-founded Mizar context
S       = C2A's SERIES_1 geometric-series fragment
Q_math  = C2A's series/partial-sum task
Q_motion = IEP's runner/path/time model
P       = exact IEP resolution wording, if it consumes FormalDone
countercontrol = Norton revised-vs-strict contract
falsifier = IEP explicitly marks the physical claim as a different/revised task,
             or has no theorem-level relation to Mizar S
```

If C3A finds `P` is absent for this exact `M/S` pair, it closes only the Mizar-to-IEP promotion route and automatically selects `C0B` or `C0C`. It cannot close the Goal.
