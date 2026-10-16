# C5C：Standard Solution 的 applied-task contract 与 strict-Q 路线裁决

> **身份：** `CORE_ADEQUACY_TASK_CARD / C5_APPLIED_TASK_CONTRACT / EXPLICIT_TASK_SWITCH_SOURCE_PAYMENT / STRICT_Q_FAILURE_ROUTE_REJECTED_WITH_SCOPE`。
>
> **父方案：** [ZFC-META-SUBTHEORY-ADEQUACY-SOP](../dev-docs/ZFC元理论子理论充分性最终闭环SOP.md)。
>
> **前序：** [C5B applied-model responsibility card](20261005-ZFC-META-SUBTHEORY-ADEQUACY-C5B-APPLIED-MODEL-BRIDGE-RESPONSIBILITY-CARD.md)；历史直接来源卡 [A2](20261004-ZFC-ACTUAL-Q-A2-标准解法来源完成合同.md)。
>
> **冻结来源：** [C5C Norton snapshot](../sources/external/zfc-meta-subtheory-c5c-20261005/README.md)，以及 C5B snapshot 中的 IEP/SEP source。

## 1. C5C 的唯一问题

C5B 已把 mathematical foundation、logical model、applied representational model 分开。现在只检查实际 Standard Solution 有没有把它的 revised completion **冒充**为 fixed strict Q 的同一完成，或是否已经公开 task switch。

```text
Fixed strict Q:
  completion = doing all required actions, including the last action.

Revised Q:
  completion = doing all actions;
  no last action is required for an infinite action sequence.
```

这里的 strict Q 是 Norton 明确讨论的一种 completion reading，用来形成一个严格的 bridge control；它不是对所有 Zeno 解释的唯一原任务合同。

## 2. 实际来源怎样处理 Done

Norton 先将 runner’s concern 读成“完成无限 actions”，再明确说有限 actions 适用的 completion notion 是：doing all actions **including the last one**。在无限 sequence 中，他将这项要求称为不适用，改用 reduced completion，并直说：删除这个 requirement 后，原来的“runner cannot complete the course”结论不再推出。

IEP 的 Standard Solution 同样明确拒绝“trip needs a final step”的直觉；它把 runner’s path/time/speed 作为 physical-continuum model，并说标准解决方案在这种 revised conceptual package 下可说明 finite-time arrival。

因此，对 C5C 固定来源而言，P 的真实形状是：

```text
P_revised : FormalDone(S) → Resolved(Q_revised)

not source-paid:
P_strict  : FormalDone(S) → OriginDone(Q_strict)
```

这不是从 source silence 得出的推测。Norton 公开把 strict condition 删去，并说明删除后此前的 conclusion no longer follows；IEP 公开说 final-step intuition 必须被拒绝。

## 3. 应用模型责任的交叉检查

C5B 的 SEP sources 使这项 source reading 不能被误报为纯词义争论。

- `LogicalModel(S)` 只说明连续数学结构／公式如何成立；
- `AppliedRep(P,Q_revised)` 需要额外说明 target、accuracy 与 mathematics-to-physical-world applicability；
- 当 P 公开把 Done 改为 `Q_revised`，它是一个可以被审计的 **explicit task revision**，而不是对 `Q_strict` 的无说明桥。

所以，针对这个 P 的正确 source verdict 是 `ExplicitTaskSwitch`。这构成 strict-Q failure allegation 的反控制：这里没有一条实际 source 暗中声称 “FormalDone automatically equals strict OriginDone”。

## 4. source-to-spec fidelity table

| 来源字段 | C5C 形式字段 | 已支付 | 不可改写为 |
|---|---|---|---|
| Norton：completion including last action 为 finite-action notion。 | `StrictDone actions` | strict completion contract 已明确。 | 所有正常运动任务都必须采取它。 |
| Norton：infinite actions 没有 last action；delete requirement 后 prior paradoxical conclusion no longer follows。 | `RevisedDone actions`、`ExplicitTaskSwitch StrictDone RevisedDone` | revised contract 与 switch 的来源支付。 | `RevisedDone → StrictDone`。 |
| IEP：Standard Solution 所用 physical continuum / finite speed / calculus，拒绝 final-step intuition。 | `ActualPromotion P_revised` | P 是 application-level resolution language。 | bare ZFC 对 Q_strict 的 object-language judgment。 |
| SEP model sources：logical and representational model distinct; application needs target/accuracy. | `AppliedRep P Q_revised` | target contract 另于 theory-only truth。 | source switch 是 ZFC semantic defect。 |
| Maddy/SEP foundation sources：faithful mathematical representation。 | `FoundationFaithfulMath M` | M 的数学表征角色。 | M 已被来源指定为 Q_strict 的 mandatory bridge checker。 |

## 5. C5C 判词

```text
STANDARD_SOLUTION_REVISED_COMPLETION_CONTRACT_SOURCE_ESTABLISHED
STRICT_TO_REVISED_TASK_SWITCH_SOURCE_EXPLICIT
FORMALDONE_TO_STRICT_ORIGINDONE_NOT_CLAIMED_BY_FIXED_P
APPLIED_MODEL_ACCURACY_REMAINS_AUDITABLE
DIRECT_BARE_ZFC_ADEQUACY_FAILURE_ROUTE_REJECTED_WITH_SCOPE
NOT_CORE_MACHINE_PROVED
```

这个受限拒绝的含义很具体：**不能拿 Norton/IEP 这组来源作为“ZFC 支撑的理论悄悄把 strict original completion 叫作已经完成”的 core failure witness。** 它们自己已经将 completion criterion 改为 revised version。

它没有证明下列任一项：

- Standard Solution 对任何更强的用户圆环任务都 adequate；
- IEP 的 physical application 已完整支付所有 target/accuracy feature；
- bare ZFC 对一切应用模型都充分或无问题；
- 用户的 ZFC theoretical-precision hypothesis 已被否定。

## 6. 控制与最强反证

- **Task-identity control：** 若有同一来源宣称其 revised completion 与 strict contract 完全同一，并给出 preservation proof，则本卡的 `ExplicitTaskSwitch` 读法失效。
- **Alternative-origin control：** 若用户或一手原典固定的 OriginDone 本来就是 `RevisedDone`，则 strict-Q objection 不适用；必须改用该精确 Q 重新做 C2–C5。
- **Actual-payment control：** 若来源将 applied target 的 input/operation/observation/Done 明确交给 model accuracy contract 并支付，则它构成 bridge-paid control，不是 failure evidence。
- **M-level control：** 无论 P 是否 task-switch，都不能仅据此推出 bare ZFC 的语言不表达时间或其对象语言不一致。

## 7. successor scan

本 C5C leaf 关闭的是 **Norton/IEP strict-Q failure route**，不是整个核心目标。C0 manifest 还保有未支付 candidate family：

```text
F-A : 是否存在不同于该 explicit-task-switch source 的 actual
      ZFC-founded continuum application，声称同一 Q 已解决却不说明 bridge；
F-B : 是否存在同一 M/S/P 的 version-fixed formalization，而不只是
      Mizar/Isabelle 与 IEP 的 component juxtaposition；
F-C : 是否存在将 foundation's faithful representation 明确扩展为
      this physical process contract 的 source；
F-D : H0 SameQ control（仍不能自动进入）。
```

下一项最小行动是：

```text
C0-SUCCESSOR-RESELECTION-001

更新 candidate manifest：将 Norton/IEP strict-Q 线登记为
EXPLICIT_TASK_SWITCH_DEFENSE，而不是 active core-failure witness；
对 F-A/F-B/F-C 的 remainder、排除条件和最高判别 successor 做一次
source-first 重选。优先选择能首次形成同一 M/S/Q/P/Adequacy 合同的方向。
```

`reopen_if`：出现一个版本固定 source 明示 `FormalDone → Q_strict`，或证明 strict/revised Done 是同一 task，而非删去 requirement 后的 revised task。
