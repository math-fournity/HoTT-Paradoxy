# T-DIAG-001 修订记录

## 2026-10-04 · 初始逻辑核

`AcceptanceDiagonal.lean` 固定一个 self-code、一个 explicit diagonal completion contract 和一个 explicit `Accept → OriginDone` bridge。初始正向 run `20261004-MP-T-PRECISION-TDIAG-001-01` 通过；在 final `CLAIM.md` 状态写回后，primary run `20261004-MP-T-PRECISION-TDIAG-001-02` 逐字重放并冻结 index rows。错误 bridge 控制 `20261004-MP-T-PRECISION-TDIAG-NEG-001-01` 被拒绝。

这里的 `fixed`、`diagonalContract` 与 `Bridge` 都是形式前提，未从 `set.mm`、bare ZFC 或任何过程来源自动推导。下一层来源裁决只判断这些前提在某个实际 target 上是否被支付。
