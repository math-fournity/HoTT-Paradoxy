# C-371：共同规范化的 dense—quantized 有限阶段完成谓词不等价

> **proof ID：** `MP-ZFC-DENSE-QUANTIZED-CONTRACT-001`
>
> **状态：** `FORMAL_CHECKED_WITH_SCOPE / SYMBOLIC_COMPLETION_CONTRACT_CONTROL`。

`NormalizedCompletionContract.lean` 固定一个共同的 remainder state space：`dyadic n` 表示非零的 `2⁻ⁿ` 余量，`zero` 表示精确到达。它证明：

```text
dense 0 = quantized 0
dense 1 = quantized 1
dense 2 = quantized 2
dense 3 = quantized 3
∀ n, dense n ≠ zero
quantized 4 = zero
¬ ∀ n, DenseFiniteStageDone n ↔ QuantizedFiniteStageDone n
```

## source-to-spec fidelity

| 研究字段 | 形式字段 | 范围 |
|---|---|---|
| C-361 dense geometric control | `denseRemaining n = dyadic n` | 符号化其非零 dyadic stage，不能取代 C-361 的 Mathlib real-analysis proof。 |
| C-370 quantized finite control | `quantizedRemaining 0..3 = dyadic 0..3`、此后 `zero` | 共同比较模型；不声称导入、复用或等同 C-370 的源代码。 |
| user/C2C finite-stage Done | `remainder = zero` | 一个明确的完成谓词，不是物理时间或 IEP 的实际定义。 |
| C4C contract difference | `finite_stage_done_not_pointwise_equivalent` | 只防止把两个 fixed control的有限阶段Done悄悄视为同一谓词。 |

## controls and prohibited extrapolation

- 正控制：两个模型初态与前三个 normalized half stages 一致；quantized 在第4步完成；
- 负控制：`WrongUniformFiniteStageDone.lean` 伪造 dense stage-4 done，必须被内核拒绝；
- 不证明真实时空量子化、任何 ZFC theorem／defect、IEP 来源事实、连续端点不存在，或 user Q 与 IEP Q 同一。
