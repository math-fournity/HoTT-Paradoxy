# C5A：ApplicationAdequacy 的来源范围合同

> **身份：** `C5_ADEQUACY_CONTRACT / SOURCE_BACKED_APPLICATION_POLICY / NOT_A_ZFC_AXIOM`。
>
> **TaskCard：** [C5A](ZFC-META-SUBTHEORY-ADEQUACY-001-C5A-TASKCARD.md)。
>
> **判词：** `APPLICATION_ADEQUACY_CONTRACT_FIXED_WITH_SCOPE / ELIGIBLE_FOR_C6_CONDITIONAL_KERNEL_TARGET`。

## 1. 来源到合同的编译

| contract ingredient | source support | 编译边界 |
|---|---|---|
| `P` makes a physical-target claim | IEP Standard Solution的 runner/path/motion resolution language。 | 不把它等同于 bare ZFC object-language derivation。 |
| model-to-target application needs a relation | SEP Scientific Representation将数学模型适用于 physical target视为独立适切性问题。 | 不假装 SEP 给出单一形式化 bridge schema。 |
| mathematical foundation supports internal mathematics | SEP Set Theory / IEP Foundations / Mizar sources。 | 不把 internal derivability变成 physical adequacy。 |
| task revision is a legitimate different resolution | Norton strict/revised completion analysis。 | 必须明确声明，不能事后暗改 Q。 |

这些来源共同支持下列有限 policy，而非任何更强的形而上断言：

```text
RequiresBridge(P, Q):
  P explicitly uses a mathematical model to support a completion claim
  about an external/physical target Q.

SatisfiesApplicationAdequacy(P, Q):
  BridgePaid(P, Q)
  OR ExplicitTaskSwitch(P, Q) ∧ ¬ ClaimsOriginalResolution(P, Q).

ApplicationAdequacyFailure(P, Q):
  RequiresBridge(P, Q)
  ∧ ClaimsOriginalResolution(P, Q)
  ∧ ¬ BridgePaid(P, Q)
  ∧ ¬ ExplicitTaskSwitch(P, Q).
```

## 2. 被固定的 actual instantiation

```text
P          = IEP Standard Solution application
Q          = IEP physical runner/course target
Model      = standard real-analysis continuous trajectory model
M/S proxy  = TG/MML rich continuous model fragment
```

当前来源审计给：

```text
RequiresBridge                    = SOURCE-SUPPORTED (application is physical)
ClaimsOriginalResolution           = SOURCE-SUPPORTED AS IEP application language,
                                      but scope must remain the IEP Standard Solution
BridgePaid                         = SOURCE-TO-SPEC UNPAID in current denominator
ExplicitTaskSwitch                 = Norton control exists, but is not automatically
                                      identical to IEP's every physical claim
```

所以这一事实集合尚不直接交付 `ApplicationAdequacyFailure`：`ClaimsOriginalResolution` 与 `ExplicitTaskSwitch` 的同一任务关系仍需在 C6 fixture里显式分支和测试。它已经足以让 C6 建立 **两种可区分的 source-certified inputs**：

1. application-claim / unpaid bridge branch；
2. explicit-revised-task branch。

## 3. C6 的形式规格

形式化不得把网页本身变成 Lean proposition。应定义一个来源卡形状：

```text
structure ApplicationCase where
  applicationClaim        : Prop
  claimsOriginalResolution : Prop
  bridgePaid              : Prop
  explicitTaskSwitch      : Prop
  requiresBridge          : Prop
```

然后机器证明三个条件命题：

```text
Failure:
  applicationClaim ∧ claimsOriginalResolution ∧ requiresBridge
  ∧ ¬ bridgePaid ∧ ¬ explicitTaskSwitch
  → ApplicationAdequacyFailure

PaidBridgeControl:
  bridgePaid → ¬ ApplicationAdequacyFailure

TaskSwitchControl:
  explicitTaskSwitch → ¬ ApplicationAdequacyFailure
  -- under the contract’s requirement that original resolution is not claimed
```

每个 actual source classification 是 audit card 的输入，不是 Lean 从网页推出的事实。C6 的 `CLAIM.md` 必须逐字段列出这个界线。

## 4. 禁止外推

该 contract 不允许称：

- `ZFC ⊢ False`；
- ZFC 缺少表达时间／轨迹的能力；
- 所有 real-analysis application 都失败；
- Norton 已经反驳 IEP；
- 当前 C4 source gap是数学 `¬Bridge` theorem。

它只建立一个源自实际 application / representation distinction 的、可被 explicit bridge或explicit task switch反驳的 adequacy criterion。
