# C6 entry admission review：现有 IEP/Norton/Maddy/SEP 合同能否释放核心机器证明

> **身份：** `CORE_ADEQUACY_C6_ADMISSION_AUDIT / NO_SURROGATE_UPGRADE / NOT_A_MACHINE_PROOF`。
>
> **父方案：** [ZFC-META-SUBTHEORY-ADEQUACY-SOP](../dev-docs/ZFC元理论子理论充分性最终闭环SOP.md) §C6。
>
> **输入：** C1A–C1D、C5A–C5F、C-359/C-361/C-362/C-364的既有范围控制。

## 1. 要判断的不是“能不能再写一个 Lean 文件”

C6 只在一个 actual `M/S/Q/P/Bridge/Adequacy` contract 已固定时允许启动。否则，一个新的有限 `CompletionWorld` 只会重做 C-362/C-364，违反本方案禁止 surrogate closure 的规则。

## 2. 现有来源合同逐字段准入

| 字段 | 当前来源状态 | 是否足以进入 core C6 | 理由 |
|---|---|---:|---|
| `M` | IEP/SEP/Maddy 说明 ZFC-with-Choice / set theory 的数学基础角色。 | 部分 | foundation role 已固定；没有 matching object-language source/proof context。 |
| `S` | IEP 说 standard real analysis/calculus；Mizar/Isar给出不被 IEP P 消费的 formal components。 | 否 | actual P 没有指向一个 exact version-fixed theorem/formalization。 |
| `Q` | IEP runner；Norton 给 strict/revised completion readings。 | 部分 | source的 target/readings明确，但 strict Q不是唯一历史解释。 |
| `FormalDone` | IEP finite-time/revised resolution language；Mizar exact geometric component。 | 否 | 没有 same-source theorem identity与 P consumption。 |
| `P` | IEP/Norton application-level resolution。 | 是，限 revised task | strict-Q promotion 已被 C5C拒绝。 |
| `Bridge` | Norton 明示 task switch。 | 是，作为 defense control | 它付款的是 `ExplicitTaskSwitch`，不是 `BridgePaid`。 |
| `Adequacy` | C5A–C5E给 mathematical representation、application accuracy和 foundation-role scope split。 | 否 | 没有来源把 bare ZFC 指定为该 physical bridge 的 required checker。 |
| H0 consequence | existing H0 theorem/controls。 | 否 | `SameQ_H0` / `UniformJudgment` 未支付。 |

## 3. C6 准入判词

```text
C6_CORE_SOURCE_TO_SPEC_ADMISSION = NOT_RELEASED
REUSABLE_MACHINE_CONTROLS = C359_C361_C362_C364_ONLY
STRICT_Q_ROUTE = EXPLICIT_TASK_SWITCH_DEFENSE
M_S_THEOREM_IDENTITY_AND_ADEQUACY_DUTY = UNPAID
```

这不是“没有机器证明工作可做”。C-359 已机器证明用户的条件性 `ZFC-1` 逻辑骨架；C-361/C-362/C-364 已机器证明相应 completion/observation controls。它说的是：把它们改名成 `CORE_ADEQUACY_FAILURE` 或 `CORE_ADEQUACY_DEFENSE` 仍会缺 source-to-spec 箭头。

## 4. 准入反控制

- 若把 IEP 的 generic standard analysis 直接编码成一个新 Lean theorem，Lean run只能证明该编码；它不会使 IEP P 真正消费 Mizar/Isar theorem。
- 若把 `ExplicitTaskSwitch` 写成类型构造，得到的仍是 C-362 同类逻辑后果，不能凭此表示 bare ZFC承担或免除物理语义责任。
- C5E 的 `ProcessCompletionAudit` 现已作为独立 `ZFC+Q_norm` 规范包（C-370–C-374）完成 Lean core 检查：它精确规定 paid bridge、explicit task switch与missing bridge的判词。它仍是**用户规范前提**，不是来源已指定的 bare-ZFC role；故不改变当前 C6 的未准入状态。

## 5. successor

核心任务继续 active。下一个有效选择只能是：

```text
C0-SUCCESSOR-RESELECTION-003

在 F-A / F-C 中寻找一个实际来源，能分别改变：
  A. standard continuum application 是否真的保持 strict task；
  C. set-theoretic foundation 是否明确承担 physical-process bridge audit。

若两者都不能取得，必须以 version-fixed source denominator记录其外部不可支付条件，
并将“user normative ProcessCompletionAudit extension”与“bare ZFC现有职责”
明确拆为两个正式研究对象；不能直接完成本 Goal。
```
