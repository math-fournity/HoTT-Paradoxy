# CoreAdequacyTaskCard — C4C：稠密—量化同一任务与完成合同

> **状态：** `LOCAL_LEAF_CLOSED / SAME_TASK_AND_COMPLETION_AUDIT / NOT_A_CORE_VERDICT`。
>
> **父合同：** C3C；source范围固定为用户原始稠密—量化 motion Q、IEP *Zeno’s Paradoxes*、C-361与C-370 controls。

## 1. 问题

```text
Does IEP's dense Standard Solution solve the same completion task as the
user-origin finite-stage/quantized Q, or does its explicit rejection of a
final step define a different completion contract?
```

必须逐项比较：对象、输入、操作、观察、`OriginDone`。不允许将“都谈 runner / endpoint / completion”当作 SameQ 的证据。

## 2. 候选规格与反控制

| contract | tentative Done | 必须核对的来源责任 |
|---|---|---|
| user/C2C Q | 一个最小粒度过程在某个有限自然数阶段 `remaining = 0`。 | 这是用户研究输入和 C-370 finite control，非物理测量定理。 |
| IEP Standard Solution Q | continuous runner/path以有限正速度完成；final step不被要求。 | 需要核对它是否明确排除 user Done，或仍声称它已满足。 |
| C-361 model control | continuous closed-time endpoint exists/attains target。 | 不应被误当成 finite-stage completion。 |

**最强反证。** 一手来源若给出一个保留最小单位、有限自然数阶段零余量的过程，并证明它与连续 Standard Solution 的输入、操作、观察和 Done 完全等价，则 SameQ 可进入 C5C；否则必须准确记录哪一字段未支付。

## 3. 局部停止与后继

若完成字段对照后发现 explicit completion-contract difference，记录其 source scope，运行 successor scan到 C5C。若发现真正同一任务 bridge，C5C改审该 bridge 和 M 的 responsibility。任何结果不得以 C-370 或同一任务不成立直接宣布 bare ZFC failure/defense。

**实际结论。** [C4C audit](ZFC-META-SUBTHEORY-ADEQUACY-001-C4C-DENSE-QUANTIZED-SAME-TASK-AUDIT.md)逐字段拒绝当前分母下的 SameQ：IEP以连续运动/端点与“没有最后一步”组织 Standard Solution，C2C以有限自然数阶段余量为零组织用户的受控量化契约；IEP未声称后者已经成立。这个差异不是 bare ZFC defense，而是 `EXPLICIT_COMPLETION_CONTRACT_DIVERGENCE_WITH_SCOPE`。下一叶 C4D 将这种 finite-stage predicate 差异与共同规范化起点写成受控 Lean theorem，再进入 C5C 的 foundation-adequacy审计。
