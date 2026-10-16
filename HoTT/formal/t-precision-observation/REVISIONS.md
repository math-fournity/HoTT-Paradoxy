# MP-T-PRECISION-TOBS-001 修订记录

| Run | 状态 | 发生了什么 | 处置 |
|---|---|---|---|
| 20261004-MP-T-PRECISION-TOBS-001-01 | positive accepted | ObservationPrecision.lean 由 Lean 4.34.1 core 接受，五个 selected theorem 的 axiom report 均为 no axioms | 保留历史 run；最终 primary 由 -06 的最小且稳定 source manifest 固定 |
| 20261004-MP-T-PRECISION-TOBS-NEG-001-01 | setup classification failure | WrongObservationPrecision.lean 实际被 Lean 拒绝，诊断写在 stdout 而不是 stderr；初版 capture 只检查 stderr，故错误标为 EXPECTED_REJECTION_NOT_CONFIRMED | 保留失败收据；修复 capture 使其检查 stdout 与 stderr 合并诊断 |
| 20261004-MP-T-PRECISION-TOBS-NEG-001-02 | expected rejection confirmed | 修复后重跑，Lean 在 False ↔ True 义务处拒绝 | 作为当前负控制 |
| 20261004-MP-T-PRECISION-TOBS-001-03 | accepted but provisional index | source run 被接受；随后发现 C-366 的 duplicate matrix row 使全局 closure validator 不能选择任何 proof | 保留收据；不作为 primary |
| 20261004-MP-T-PRECISION-TOBS-001-04 | accepted but provisional index | duplicate C-366 已修复，但 matrix evidence row 仍指向旧 -03，因而 verifier 缺少 -04 identity | 保留收据；不作为 primary |
| 20261004-MP-T-PRECISION-TOBS-001-05 | accepted but contextual-manifest drift | source denominator and T0 card were initially listed as kernel inputs, then received their required final status update | preserve run; final manifest removes mutable contextual cards |
| 20261004-MP-T-PRECISION-TOBS-001-06 | final primary accepted | final source manifest contains only proof source, claim, package README, toolchain and capture procedure; matrix row and registry primary are aligned before recapture; exact rerun and selected evidence closure PASS | current primary run |

第一条 negative run 不改变数学命题；它只说明 capture 程序错误地假定 Lean 的 diagnostics 必然写到 stderr。不得把它说成 decoder 被 kernel 接受或数学反例。
