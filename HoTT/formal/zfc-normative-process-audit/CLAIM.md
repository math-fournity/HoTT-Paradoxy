# `MP-ZFC-NORMATIVE-PROCESS-AUDIT-001`：形式命题与范围

> **Claims:** `C-370`–`C-374`。
>
> **Scope:** 对用户显式提出的 `ZFC+Q_norm` process-completion audit 进行 Lean core 形式化；不是 bare ZFC 语法、模型、一致性或社区实践的形式化。

## Source-to-spec fidelity

| 来源／规范字段 | Lean 字段 | 范围 |
|---|---|---|
| 用户的 MetaTheory 应审查 SubTheory process bridge | `CompletionContract` / `audit` | 外加的用户规范，而非 ZFC 公理。 |
| C5A–C5E 的 foundation/application role split | `BridgeStatus` 的 `paid` / `explicitTaskSwitch` / `missing` | 规范对来源状态作分类；不宣称来源本身由 Lean 证明。 |
| Norton strict/revised source classification | `nortonContract` | source-bound input：revised completion、strict origin和 explicit switch。 |
| C5F / process observation positive control | `bridgeRequired` outcome 的规范动机 | 不把 hybrid Zeno 与 Norton/IEP task同一化。 |

## Kernel-checked claims

1. **C-370:** `audit_original_resolved_is_sound`：只有 `paid` bridge 分支才会返回 `originalResolved`，因此该 verdict 蕴含 `originDone`。
2. **C-371:** `audit_explicit_switch_is_revised`、`audit_explicit_switch_is_not_original` 与 `audit_norton_contract_reports_task_switch`：明确 task switch 被输出为 `revisedResolved`，并且不能被输出为 original resolution。
3. **C-372:** `audit_missing_bridge_requires_payment`、`audit_missing_bridge_is_not_original` 与 `audit_missing_bridge_control_requires_payment`：无 payment 时输出 `bridgeRequired`，并且不能被输出为 original resolution。
4. **C-373:** `audit_paid_bridge_control_resolves_original` 与 `paid_bridge_control_origin_done`：真实 bridge 的正控制可得到 original verdict及其 origin conclusion。
5. **C-374:** `audit_missing_bridge_control_does_not_resolve_original`：formal Done alone不能让本规范输出 original resolution。

## 禁止外推

- 不证明 bare ZFC 已经实现或缺失 `audit`；
- 不证明 IEP/Norton/SEP/Maddy 的历史文本；
- 不证明标准连续统模型、混合系统或 HoTT 的实际物理适用性；
- 不证明 ZFC 不一致，或用户 A/B 的 `SameFullQ` 前提；
- 不替代 C6 actual source-to-spec admission。
