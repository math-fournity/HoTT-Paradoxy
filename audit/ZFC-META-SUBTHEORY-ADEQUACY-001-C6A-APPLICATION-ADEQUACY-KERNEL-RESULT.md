# C6A：ApplicationAdequacy contract 的内核结果

> **身份：** `C6_MACHINE_PROOF_RESULT / CANDIDATE_CONDITIONAL_VERDICT / NOT_TOTAL_GOAL_COMPLETION`。
>
> **proof / claim：** `MP-ZFC-META-SUBTHEORY-ADEQUACY-001` / `C-369`。
>
> **primary run：** `HoTT/verification/runs/20261005-MP-ZFC-META-SUBTHEORY-ADEQUACY-001-04/`。

## 1. 已由 Lean 4.34.1 core 接受的内容

`ApplicationAdequacy.lean` 以显式 `ApplicationCase` 字段证明：

```text
applicationClaim ∧ claimsOriginalResolution ∧ requiresBridge
∧ ¬ bridgePaid ∧ ¬ explicitTaskSwitch
→ ApplicationAdequacyFailure.
```

同一次内核运行还证明：

- 已支付 bridge 的 `bridgePaidControl` 不满足 failure；
- 明确 task switch 的 `taskSwitchControl` 不满足 failure；
- 只有数学模型端点、没有 physical application claim 的 `modelOnlyControl` 不满足 failure；
- 未提供 `SameQ_H0` 的 H0 control不可进入本 theorem premise。

运行 stdout 对这九条 selected theorem 都报告“不依赖任何 axioms”。负控制 `WrongPaidBridgeFailure.lean` 以 exit 1 被拒绝，错误位于试图居住 paid-bridge case 的 failure predicate。

## 2. 来源到规格、而非来源到内核的边界

| 层 | 已完成 | 仍不是内核定理 |
|---|---|---|
| source audit | C1A–C5A 把 TG/MML、IEP、Norton、SEP 的作用和范围逐项定位。 | 网页文字的历史／哲学真值。 |
| formal specification | `ApplicationCase` 与 C5A contract把 application P、bridge、task switch显式化。 | bare ZFC 的公式或模型。 |
| kernel | 给定这些字段的逻辑 consequence及四控制。 | “ZFC 本身已被证明失败／无时间／不一致”。 |

故 C6A 产物准确身份是：

```text
CANDIDATE_APPLICATION_ADEQUACY_FAILURE_MACHINE_PROVED_WITH_SCOPE
```

它为当前 source-certified application contract给出一份可重放的 conditional verdict，不能替代 SOP 004 的全候选族总完成门。

## 3. 对下一阶段的作用

这个结果做了两件以前没有完成的事：

1. 它把“model completion被拿去谈physical completion，需要什么”从散文变成有 source-to-spec table、有正反控制、可由内核复核的有限 contract。
2. 它同时证明此 contract不把所有连续数学都判错：模型内端点、已付 bridge、公开改题都走不同路径。

尚未完成的不是“再把这个 theorem重跑一次”，而是 C0 candidate universe 的其余 family、独立 formalization/defense sources、以及能否把 current source classifications升级成满足 SOP 总门的 actual core verdict。
