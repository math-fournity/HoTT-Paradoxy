# ZFC 作为 Meta Theory、极限理论作为 Sub Theory：完成观察力的形式审计

> **身份：** `CONTRIBUTOR_CANDIDATE / META_SUBTHEORY_COMPLETION_AUDIT / NOT_A_BARE_ZFC_THEOREM`。
>
> **用户问题：** 若 ZFC 是承载极限理论的 Meta Theory，为什么它没有识别极限理论在芝诺／圆环过程上的完成边界？这一问题的原文保存在 `dev-notes/0110` 与用户的 Q/P/A/B 论证中。

## 1. 被形式化的最小责任

本审计不把“Meta Theory”理解成一个全知的现实语义裁判。它只固定一项较弱、可检验的责任：

```text
Sub Theory 给出 formalDone(state)
Meta Theory 接受该 formal completion
Meta Theory 若把接受的结果交付为 originDone(state)
    则必须交出 formalDone → originDone 的 statewise bridge。
```

这里的 `originDone` 是用户所说的原过程完成，不是“某个等价对象存在”“某个极限已经定义”或“某个模型有终点”的同义词。

## 2. 机器模型

[MetaSubtheoryAudit.lean](../HoTT/formal/zfc-observation-boundary/MetaSubtheoryAudit.lean) 定义：

| 概念 | Lean 对象 | 作用 |
|---|---|---|
| 原过程 | `ProcessTask` | 记录输入、`step`、`formalDone` 与 `originDone`。 |
| 子理论 | `Subtheory` | 对一个过程任务提供形式完成谓词。 |
| 元理论 | `MetaTheory` | 观察状态并接受某些观察结果。 |
| Q | `MetaCanAuditOriginDone` | 某个观察谓词能否对每个状态判定 origin Done。 |
| 强 P | `MetaPromotesAcceptedAsOrigin` | 元理论是否把每个已接受结果都升格为 origin Done。 |

这与用户的叙述相接：`lacksQ` 不是 ZFC 没有任何时间对象，而是这一个 meta observation 接口无法从它所保留的信息判断 origin completion。

## 3. 已机器检查的结论

1. **promotion 必须支付 bridge。**

   `meta_promotion_pays_subtheory_bridge` 证明：元理论如果接受 formal completion，又将每个被接受结果称作 origin completion，那么它已经承担 `formalDone → originDone` 的 bridge。

2. **一个未付 completion witness 足以阻止强 promotion。**

   `unpaid_subtheory_completion_blocks_meta_promotion` 证明：若某状态 `formalDone` 成立、`originDone` 不成立，且 meta 接受 formal completion，则强 promotion 不可能成立。

3. **粗观察会缺少 Q。**

   `meta_observation_collision_blocks_origin_audit` 证明：若 meta observation 将一个 origin-complete 状态和一个 origin-incomplete 状态合并，它无法从该 observation 审计 origin Done。

4. **不是所有 Meta/Sub 关系都失败。**

   `bridgeAwareMeta`/`paidSubtheory` 是正控制：subtheory formalDone 与 originDone 一致，meta 保留区分观察；机器证明它既能 audit，又能支付 bridge。

5. **错误强 promotion 被拒绝。**

   [WrongMetaSubtheoryAudit.lean](../HoTT/formal/zfc-observation-boundary/WrongMetaSubtheoryAudit.lean) 声称 coarse meta 能把所有 accepted formal results 升格为 origin completion。Lean 在 unresolved state 拒绝该证明；收据为 `20261004-MP-ZFC-META-SUBTHEORY-AUDIT-NEG-001-02`。

## 4. 与 ZFC、芝诺、圆环和 HoTT 的关系

该模型不证明“ZFC 自身必然错误”。它证明的是一个可移植的元理论审计规则：

```text
只要某个 ZFC-supported meta/subtheory 使用实践
  接受 formalDone
  并以此宣布 originDone
而其可用观察不能区分同样 formalDone 下的不同 originDone，
它就需要一个明确 bridge；否则该强 promotion 不成立。
```

芝诺／圆环方向必须先把实际 `originDone` 固定为同一过程合同；HoTT 方向必须先给出 actual policy scope，而不能把 `QuestioningDelay` 与芝诺过程当成同一任务。已有 U3/U4 结论正是这一反控制：直接 same-Q transport 当前不成立。

## 5. 当前判词

```text
META_SUBTHEORY_COMPLETION_OBSERVATION_BOUNDARY_FORMALIZED
ACTUAL_ZFC_META_POLICY_NOT_YET_SOURCE_MAPPED
ACTUAL_ZENO_CIRCLE_HOTT_POLICY_SCOPE_NOT_YET_ESTABLISHED
NO_BARE_ZFC_INCONSISTENCY_CLAIM
```

这项形式化使用户的“ZFC 理论精度不够”获得一个更精确的候选读法：并非说 ZFC 没有表达时间的能力，而是说它的某个**接受并交付子理论完成结果的接口**，若不带 origin bridge，就没有足够的观察力把形式完成与原过程完成区别开。

## 6. 证据

- 正向 run：[RUN.json](../HoTT/verification/runs/20261004-MP-ZFC-META-SUBTHEORY-AUDIT-001-02/RUN.json)，Lean 4.34.1 exit 0，十个打印 theorem 均无额外公理。
- 负向 run：[RUN.json](../HoTT/verification/runs/20261004-MP-ZFC-META-SUBTHEORY-AUDIT-NEG-001-02/RUN.json)，Lean exit 1，预期错误 `Tactic \`assumption\` failed`，`outcome_matches_expectation=true`。
- `...-001/NEG-001-01` 被保留为 capture helper 的历史 `RUNNER_OR_EVIDENCE_FAILURE`：Lean 已拒绝错命题，但旧 helper 只查 stderr、没有识别 stdout 诊断；`-02` 修复为双流检查。

## 7. 下一条必须支付的事实

下一步不再是构造更多 toy meta theories，而是找到或排除一个版本固定的实际 ZFC-supported consumer：它必须明确接受一个 limit/completion output，并把它交付为用户所固定的芝诺／圆环 origin Done。若没有这个 consumer，模型只能证明责任形状，不能指控实际 ZFC 已实施该错误 promotion。
