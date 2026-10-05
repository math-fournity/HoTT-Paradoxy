# C5D：completion classification bifurcation 的来源—内核控制

> **身份：** `C5_SOURCE_TO_SPEC_BIFURCATION / EXISTING_KERNEL_CONTROL_REUSED / NOT_A_CORE_VERDICT`。
>
> **TaskCard：** [C5D](ZFC-META-SUBTHEORY-ADEQUACY-001-C5D-TASKCARD.md)。
>
> **machine evidence:** `C-369` / [20261005-MP-ZFC-META-SUBTHEORY-ADEQUACY-001-04](../HoTT/verification/runs/20261005-MP-ZFC-META-SUBTHEORY-ADEQUACY-001-04/RUN.json)。
>
> **判词：** `CLASSIFICATION_UNDERDETERMINED_WITH_SCOPE / C5D_LOCAL_LEAF_CLOSED / F_A2_REOPENED_FOR_ACTUAL_POLICY_INGRESS`。

## 1. 固定来源事实

同一 IEP page同时说：

1. Standard Solution处理/解决 Achilles和Dichotomy，并用连续统、实分析、有限距离／时间描述physical motion；
2. “必须有final step / final sub-path”是错误的要求。

第一句提供 `applicationClaim` 和可能的 `claimsOriginalResolution` 入口；第二句提供相对 C2C finite-stage `OriginDone` 的明确completion-contract difference。它们都是真实来源材料，但二者之间是否意味着“IEP仍声称已经满足**用户**的原任务”，不是页面自己用 C2C predicate 作出的判定。

## 2. C-369 已经机器检查的两支

| fixed reading | `ApplicationCase` | kernel verdict | source-to-spec边界 |
|---|---|---|---|
| `resolution-reading` | `applicationUnpaid`：application/original-resolution/requires-bridge为真，bridge和switch为假。 | `application_unpaid_is_failure`。 | 只有当IEP的“resolution”被来源/用户裁定为C2C original-resolution时可实例化。 |
| `task-switch-reading` | `taskSwitchControl`：application为真，original-resolution为假，explicit switch为真。 | `task_switch_control_is_not_failure`。 | 只有当IEP的final-step rejection被裁定为对C2C Q的explicit task switch时可实例化。 |

两条定理都已由Lean 4.34.1 core接受。它们严谨地证明了**分类一旦给定**时的后果；不会从网页用词自动推出哪种分类是真的。

## 3. C5D 的机器结论

```text
same visible source facts + different completion-classification input
→ different ApplicationAdequacy verdict branch.
```

这不是“ZFC内有矛盾”的数学结论。它是一个精确的 source-to-spec 限制：在没有额外的 `OriginDone` 对齐、source policy或用户裁定时，C-369不能诚实地从这份来源自动选出failure或defense。

## 4. 反控制

- `applicationUnpaid`和`taskSwitchControl`均真实存在于同一C-369 proof package；它们不是本轮新造的相反结论；
- C4C已排除 continuous endpoint与finite-stage Done的同一化；
- 如出现一手来源明确说“即使没有final natural stage，仍已满足C2C finite-stage OriginDone”，或明确说“我们只是解决另一个任务”，本卡立即可被推翻为唯一source classification。

## 5. 自动后继

F-A2恢复为 `LIVE / ACTUAL_POLICY_CLASSIFICATION_UNPAID`。C0R2/C0R3的F-B source cards继续保留，但当前最高判别动作回到C0：寻找能够支付 actual policy classification 的来源，或在用户固定 `OriginDone` 后冻结其解释。C0C2保持 `PARKED_PENDING_C5D`，然后可作为F-C ingress恢复。
