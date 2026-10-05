# CoreAdequacyTaskCard — C4D：共同规范化的 dense—quantized completion divergence 控制

> **状态：** `LOCAL_LEAF_CLOSED / FORMAL_CONTROL / NOT_A_CORE_VERDICT`。
>
> **父合同：** C4C；该 unit只形式化已固定的数学控制，不形式化 IEP 网页、物理时空或 bare ZFC。

## 1. 形式目标

以一个共同的 symbolic normalized remainder state space 表示半程过程：

```text
dense n      = dyadic(n)             -- represents nonzero 2⁻ⁿ remainder
quantized 0  = dyadic(0)
quantized 1  = dyadic(1)
quantized 2  = dyadic(2)
quantized 3  = dyadic(3)
quantized n  = zero for n ≥ 4
```

证明：两者从共同规范化初态开始、前三个 half stages一致；dense finite-stage Done 永不成立；quantized stage-four Done成立；因此不能把二者的 finite-stage completion predicate 当作逐点相同。

## 2. 保真与控制

- `dyadic(n)`是 `2⁻ⁿ` 的符号表示；实际实数 dense side仍由 C-361拥有；
- quantized half-step具体八单位实现仍由 C-370拥有；本单元检验二者比较所需的共同 `Done` shape，不宣称源码互相导入；
- expected rejection control必须伪造 dense stage-four completion，并在 `dyadic 4 ≠ zero`处被内核拒绝；
- `ContinuousEndpoint` 不进入本定理；C-361的闭区间 endpoint正控制必须仍可并存。

## 3. 局部停止和后继

若 kernel接受正控制且拒绝伪造Done，则写回 C-371、run、matrix和C4D结果；它仅完成两个 fixed control的共同合同。随后 C5C 才可审计 IEP／M对已明示的完成合同差异是否具有adequacy responsibility。

**实际结论。** C-371由 Lean 4.34.1 core接受，并通过 dense stage-four Done伪造的 expected rejection control。它只证明共同规范化的两个**控制模型**在 finite-stage Done 上不逐点等价；C-361的实数极限和C-370的八单位递归仍各自保有自己的数学范围。后继是 C5C，审计actual Standard Solution的explicit completion-contract difference是否触发基础充分性责任。
