# C4D：共同规范化的 dense—quantized completion contract 机器控制

> **身份：** `C4_FORMAL_CONTROL / MACHINE_PROVED_WITH_SCOPE / NOT_A_CORE_VERDICT`。
>
> **TaskCard：** [C4D](ZFC-META-SUBTHEORY-ADEQUACY-001-C4D-TASKCARD.md)。
>
> **proof / claim：** `MP-ZFC-DENSE-QUANTIZED-CONTRACT-001` / `C-371`。
>
> **primary run：** [20261005-MP-ZFC-DENSE-QUANTIZED-CONTRACT-001-02](../HoTT/verification/runs/20261005-MP-ZFC-DENSE-QUANTIZED-CONTRACT-001-02/RUN.json)；`-01`保留为旧documentation-pin历史收据，见包内REVISIONS。

## 1. 机器化对象

`NormalizedCompletionContract.lean` 在 Lean 4.34.1 core 中固定：

```text
NormalizedRemainder = zero | dyadic(n)
dense n             = dyadic(n)
quantized 0..3      = dyadic(0)..dyadic(3)
quantized n≥4       = zero
```

这里 `dyadic(n)` 是“非零 `2⁻ⁿ` 余量”的符号表示；真实实数序列仍由 C-361 负责，实际八单位 floor-half递归仍由 C-370负责。

## 2. 已检查的命题

| 形式命题 | 机器结果 | 研究角色 |
|---|---|---|
| 初态和阶段 1–3 一致 | accepted | 防止把两个模型做成完全无关的故事。 |
| `¬∃n, DenseFiniteStageDone n` | accepted | 与 C-361 finite-stage control相容的符号层表达。 |
| `QuantizedFiniteStageDone 4` 且第3步不完成 | accepted | 与 C-370 finite control相容的符号层表达。 |
| `¬∀n, DenseDone n ↔ QuantizedDone n` | accepted | 固定模型的 finite-stage Done不可被逐点同一化。 |
| `DenseFiniteStageDone 4` 的伪造 | rejected, exit 1 | 负控制。 |

primary run对五条选择定理均报告不依赖任何 axioms；run verifier 为 `PASS_WITH_SCOPE`。C-371 的完整 source-to-spec表、禁止外推和负控制位置在[CLAIM.md](../HoTT/formal/zfc-dense-quantized-contract/CLAIM.md)。

## 3. 这一步真正关闭了什么

它关闭的是本项目自身可能犯的一种偷换：把 C-361 的 “continuous model endpoint／limit” 和 C-370 的 “某个有限 natural stage余量为零”叫作同一个 `Done`，随后用名称相同假装 `SameQ`。

它没有证明：

- IEP或数学共同体把二者等同；
- 真实时空采用离散模型；
- ZFC不能表示两种模型；
- IEP的完成合同一定不充分，或 bare ZFC必然有任何对象语言／元理论矛盾。

## 4. 自动后继

进入 **C5C：explicit completion-contract difference 的基础充分性责任**。该卡只可问：在 IEP把最终步骤要求列为错误的现有来源合同中，`M/S/P`是否还声称已经解决用户的 finite-stage Q；若没有，它是 explicit task-switch / contract-difference control。随后必须分开审计 bare-ZFC-facing adequacy duty是否由任何实际来源支付。
