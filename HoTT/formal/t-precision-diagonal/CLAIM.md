# T-DIAG-001：条件性自编码接受边界

> **Proof package：** `MP-T-PRECISION-TDIAG-001`。
>
> **Claim：** `C-368`。
>
> **状态：** `T_DIAG_LOGICAL_KERNEL_MACHINE_PROVED_WITH_SCOPE`。

## 精确命题

在 Lean core 的任意 `Code : Type` 上，固定：

```text
step : Code → Code
d : Code
Accept : Code → Prop
OriginDone : Code → Prop

step d = d
OriginDone (step d) ↔ ¬ Accept d
Accept d → OriginDone (step d)
```

机器目标是：

```text
¬ Accept d
```

该结论只证明一个有显式前提的 acceptance-reflection boundary。它不说理论本身推出 `False`；只有另有来源支付的 total acceptance、completeness 或实际 consumer contract，才可以提出更强的哥德尔式问题。

## 控制

- `bridgeMissingControl`：self-code 和 diagonal contract 存在，`Accept d` 为真，而 `OriginDone (step d)` 为假；因此 bridge 不存在。
- `bridgePaidControl`：bridge 与 diagonal contract 共存，且 `Accept d` 为假；主结论给出相同的拒绝。
- `WrongAcceptanceDiagonal.lean`：故意为第一个控制伪造 bridge，Lean 应拒绝。

## 来源边界

Foundation 的 generic Gödel theorem 提供 code/quote/substitution/diagonal 的真实技术基线；`set.mm` 提供真实 ZFC proof acceptance interface。二者当前没有共同支付研究发起人关心的 `OriginDone`、保真 `ρ`、internal-provability adequacy 或 actual diagonal。详见 `audit/20261005-T-PRECISION-TDIAG-001-SOURCE-DENOMINATOR.md`。

## 禁止外推

`C-368` 不证明：

- bare ZFC、`set.mm` 或任何具体证明器不一致；
- bare ZFC 满足 Foundation 的 arithmetic incompleteness 前提；
- 芝诺、圆环或 fixed HoTT H0 已经是 `d`；
- `Accept` 已经等于任何现实过程的完成；
- 想法 T 已整体得证。
