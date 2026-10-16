# C-370：固定量化 half-step 过程的有限完成

> **proof ID：** `MP-ZFC-DENSE-QUANTIZED-MOTION-001`
> **状态：** `FORMAL_CHECKED_WITH_SCOPE / FINITE_QUANTIZED_CONTROL`。
> **primary run：** `20261005-MP-ZFC-DENSE-QUANTIZED-MOTION-001-02`。

`quantizedRun` 从八个最小单位开始，以 floor-half rule递归，内核将检查：

```text
run 0 = 8; run 1 = 4; run 2 = 2; run 3 = 1; run 4 = 0;
¬ (run 3 = 0); ∃ n, run n = 0.
```

## 与用户原任务的保真边界

| 用户／模型字段 | 本包对象 | 边界 |
|---|---|---|
| 最小运动尺度 | `Nat` unit | finite control，不是物理测量。 |
| 每次取剩余一半 | `quantizedHalf` | 最后一个 unit不能继续分成非零半单位。 |
| 完成 | `remaining = 0` | 只在固定 lattice task。 |
| 稠密对照 | C-361 的 `2⁻ⁿ > 0` | 另一个已证 package，不是本文件的 object theorem。 |

禁止外推：不证明实际时空离散、ZFC错误、极限理论错误，或所有离散规则都会有限完成。
