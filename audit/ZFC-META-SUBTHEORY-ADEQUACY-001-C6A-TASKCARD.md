# CoreAdequacyTaskCard — C6A：ApplicationAdequacy 的来源认证条件内核证明

> **状态：** `LOCAL_LEAF_CLOSED / KERNEL_PROOF_ACCEPTED / CANDIDATE_CORE_VERDICT_WITH_SCOPE`。
>
> **父合同：** `C6`；规范输入为 [C5A contract](ZFC-META-SUBTHEORY-ADEQUACY-001-C5A-APPLICATION-ADEQUACY-CONTRACT.md)。

## 1. 要交付的精确命题

新的 Lean core package 必须证明：在显式的、来源认证的 `ApplicationCase` 分类中，若实际 application claim 宣称 original physical resolution、要求 bridge、而 bridge未付且无 explicit task switch，则该 case 满足 `ApplicationAdequacyFailure`。

```text
ApplicationClaim ∧ ClaimsOriginalResolution ∧ RequiresBridge
∧ ¬ BridgePaid ∧ ¬ ExplicitTaskSwitch
→ ApplicationAdequacyFailure
```

这是 **固定 application contract 的条件性逻辑结论**。它不是 ZFC 对象语言定理；网页／来源分类是 Lean 输入之外的 audit evidence。

## 2. 必须机器检查的 controls

| fixture | 预期 |
|---|---|
| `applicationUnpaid` | failure 成立。 |
| `bridgePaidControl` | failure 不成立。 |
| `taskSwitchControl` | failure 不成立。 |
| `modelOnlyControl` | failure 不成立。 |
| `h0MissingSameQ` | H0 不可进入核心 theorem premise。 |
| negative source | 伪造 `bridgePaidControl` 的 failure 必须被 Lean 拒绝。 |

## 3. 预注册的证据边界

`C-369` 若通过，最多可写为：`FORMAL_CHECKED_WITH_SCOPE / SOURCE_CERTIFIED_APPLICATION_ADEQUACY_CONTRACT`。不得写为 bare ZFC inconsistency、ZFC没有时间、所有标准解法失败、或 HoTT同Q异判。总 Goal仍需 C0 family remainder、独立 controls和最终 Gate。

**实际结果。** fixed Lean 4.34.1 core primary run `20261005-MP-ZFC-META-SUBTHEORY-ADEQUACY-001-04` 接受，负控制保留为 `NEG-001`。详见 C6A result 与 successor scan；这完成一份 source-certified conditional contract 的内核证明，不完成总 Goal。
