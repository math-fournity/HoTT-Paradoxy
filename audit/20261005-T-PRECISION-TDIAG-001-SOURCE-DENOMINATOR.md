# T-DIAG-001：来源分母与接口角色裁决

> **对应候选：** [T-DIAG-001 acceptance-diagonal card](20261005-T-PRECISION-TDIAG-001-ACCEPTANCE-DIAGONAL-CARD.md)。
>
> **状态：** `SOURCE_ADMISSION_PASS_FOR_LOGICAL_KERNEL / ACTUAL_PARENT_BRIDGE_UNPAID_WITH_SCOPE`。
>
> **范围：** 说明哥德尔技术与 `set.mm` proof acceptance 各自承担什么；不证明它们共同构成 bare-ZFC completion interface。

## 1. 冻结来源

| ID | 来源与版本 | 当前读取到的事实 | 对 T-DIAG-001 的作用 | 不能支付 |
|---|---|---|---|---|
| `SRC-TDIAG-FOUNDATION-001` | [Foundation `First.lean` at `f3972f4`](https://github.com/FormalizedFormalLogic/Foundation/blob/f3972f4204fc61e1b736ed843415894c83f35508/Foundation/FirstOrder/Incompleteness/First.lean)；本地 exact replay `20261004-SOURCE-REPLAY-FOUNDATION-GODEL-001` | 该源码的 `incomplete` 明确以 `ArithmeticTheory`、递归可枚举 predicate、quote、substitution、`π = δ/[⌜δ⌝]`及 soundness 为前提；本地运行复现 generic theorem，但带 `propext`、`Classical.choice`、`Quot.sound`。 | 校准 T-DIAG 的 `Code / quote / substitute / diagonal` 不可以被口头自指替代。 | bare ZFC 或 `set.mm` 满足这些前提；任何 parent `OriginDone` 或 bridge。 |
| `SRC-TDIAG-SETMM-002` | [`set.mm` README at `160ebb63`](https://github.com/metamath/set.mm/blob/160ebb63ec17ff00a809520a420c92914a424622/README.md)；G0 audit、官方 verifier replay | `set.mm` 是使用 classical logic 与 ZFC 的 formal proof database；每项变更经独立 verifier 复核。 | 为一个真实 `Code / Check / Accept` proof-acceptance interface 提供来源资格。 | 它没有将 proof acceptance 定义为芝诺、圆环或 H0 的原过程完成。 |
| `SRC-TDIAG-FOUNDATION-GAP-003` | `20261004-SOURCE-REPLAY-FOUNDATION-ZFC-GODEL-GAP-001` 与 [mapping-gap audit](20261004-GODEL-Q-REFLECTION-G2-FOUNDATION-ZFC-GODEL-MAPPING-GAP.md) | 同一 Foundation source 中 `ZermeloFraenkelChoice : SetTheory` 不能直接作为 generic theorem 所需的 `ArithmeticTheory`；Lean 预期拒绝这个直接应用。 | 防止把“ZFC source 和 generic Gödel theorem 出现在同一代码树”误当作 target-specific diagonal payment。 | 不证明不存在任何未来 arithmetization 或 interpretation。 |
| `SRC-TDIAG-COMPLETION-004` | C-362/C-363 的来源合同与 machine controls | 已固定的 revised completion 可以与 strict original completion 分离，且 bridge 需要额外支付。 | 为 `Accept → OriginDone` 是独立义务提供项目内的 completion-control 校准。 | `set.mm` interface 与这两个过程是同一任务。 |

## 2. 来源裁决

哥德尔 source 说明的，是怎样让一个**已经具备**算术化、表示性、替换和相称 soundness 的理论遇到自己的 provability interface。`set.mm` source 说明的，是一个真实的 ZFC proof-verification consumer 如何接受一个 proof database。两者各自真实，但当前来源没有把它们与研究发起人关心的过程完成合成一个接口。

因此，T-DIAG-001 可以且应当机器化一个**条件性逻辑核**：若 `fixed`、`diagonalContract` 和 `bridge` 同时给出，则接受该 self-coded instance 不可能。它不能把这三项条件中的 `bridge` 写成已经由 `set.mm`、bare ZFC、芝诺、圆环或 H0 支付。

## 3. 反控制与实际后果

`set.mm` 的 README 把其工作明确限定在 formal proofs 的验证；这正是它作为 `Accept` 候选的力量，也正是它不能自动承担 `OriginDone` 的原因。Foundation mapping-gap control 则表明：generic theorem 的可运行 source 也不能越过具体理论映射的支付。

故当前来源 verdict 为：

```text
TDIAG_LOGICAL_KERNEL_SOURCE_ADMITTED
ACTUAL_SETMM_ACCEPTANCE_INTERFACE_SOURCE_CERTIFIED
ACTUAL_PARENT_ORIGINDONE_BRIDGE_UNPAID_WITH_SCOPE
NO_BARE_ZFC_INCOMPLETENESS_OR_INCONSISTENCY_CLAIM
```

新 package 必须把这个 verdict 写进 `CLAIM.md` 与 run receipt 的 non-goals；若 Lean 正面证明了逻辑核，也只能证明带显式前提的反射边界。
