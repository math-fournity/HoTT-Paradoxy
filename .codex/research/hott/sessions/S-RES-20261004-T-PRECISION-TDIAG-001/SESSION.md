# S-RES-20261004-T-PRECISION-TDIAG-001

> **Role:** `RESEARCH_GENERATION`.
>
> **Tier:** `T3` — 新增 C-368 的机器证明、运行收据、矩阵和 proof-version registry。
>
> **Parent:** `T-PRECISION-DIAGONAL-SOP` continuous execution.

## 本单元

`T-DIAG-001` 先冻结“self-code、diagonal completion contract、Accept→OriginDone bridge”的条件性逻辑核，再读取 Foundation generic Gödel source、`set.mm` proof-acceptance source 与 G0 mapping-gap evidence，最后用 Lean 4.34.1 core 证明 C-368 并运行伪造 bridge 的负控制。

## 结论范围

`C-368` 是有明确前提的逻辑边界：paid bridge 使 self-code 不可被接受；bridge 缺失时 self-coding 可与 acceptance 共存。当前 source 只支付 generic Gödel技术与 proof acceptance，未支付 parent `OriginDone`、ρ、internal-provability adequacy 或 actual diagonal。因此本单元状态为 `T_DIAG_LOGICAL_KERNEL_MACHINE_PROVED_WITH_SCOPE / ACTUAL_PARENT_BRIDGE_UNPAID_WITH_SCOPE`，下一单元为 T-Meta same-task / bridge-payment 裁决。

## 直接证据

- `audit/20261005-T-PRECISION-TDIAG-001-ACCEPTANCE-DIAGONAL-CARD.md`
- `audit/20261005-T-PRECISION-TDIAG-001-SOURCE-DENOMINATOR.md`
- `HoTT/formal/t-precision-diagonal/`
- `HoTT/verification/runs/20261004-MP-T-PRECISION-TDIAG-001-02/`
- `HoTT/verification/runs/20261004-MP-T-PRECISION-TDIAG-NEG-001-01/`

## 不能外推

没有 bare ZFC 不一致性、不完备性、时间维度缺失、实际 set.mm Gödelization、芝诺／圆环／H0 同一任务或想法 T 总证明的结论。
