# C5A 后继扫描：C6 source-certified conditional kernel target

> **身份：** `SUCCESSOR_SCAN / CORE_GOAL_ACTIVE / FORMALIZATION_RELEASE`。
>
> **前叶：** [C5A application adequacy contract](ZFC-META-SUBTHEORY-ADEQUACY-001-C5A-APPLICATION-ADEQUACY-CONTRACT.md)。
>
> **结果：** `C5A_LOCAL_LEAF_CLOSED / C6A_SELECTED / FINAL_CORE_VERDICT_NOT_PROVED`。

## 1. C6 已具备的输入

现在已固定：

```text
M/S      = TG/MML rich mathematical model proxy
Q        = IEP physical runner/course target (source-bounded)
FormalDone = model endpoint / trajectory result
P        = IEP Standard Solution application claim
Bridge   = model-to-physical completion relation, source-to-spec unpaid
Adequacy = ApplicationAdequacy, source-backed but non-ZFC-internal
```

需要 machine check 的不是“ZFC 事实”本身，而是固定 source classifications 与 contract共同推出的 adequacy verdict，并验证控制不会被一并误判。

## 2. C6A fixture set

| fixture | expected kernel verdict | source role |
|---|---|---|
| `ApplicationUnpaid` | `ApplicationAdequacyFailure` | IEP physical P + source-to-spec bridge gap，范围受 source audit限制。 |
| `BridgePaidControl` | not failure | completion-preserving bridge exists. |
| `TaskSwitchControl` | not failure | explicit revised task and no original-resolution claim. |
| `ModelOnlyControl` | not failure | mathematical endpoint without physical application P. |
| `H0Control` | H0 absent SameQ cannot enter theorem premise. | prevents false cross-theory transfer. |

## 3. 自动选择：`C6A-APPLICATION-ADEQUACY-KERNEL-PROOF`

建立 source-to-spec fidelity table、Lean core package、`CLAIM.md`、保存 run、claim-matrix行和负控制。若 kernel拒绝或形式规格发现缺字段，关闭该 proof route并回 C4/C5补 contract，不得结束 Goal；若通过，只完成这个 actual-candidate core verdict，C0 remainder仍要求继续。
