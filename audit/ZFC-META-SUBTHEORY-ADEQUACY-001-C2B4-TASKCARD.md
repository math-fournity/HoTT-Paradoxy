# CoreAdequacyTaskCard — C2B4：set.mm `geoihalfsum` 的 dense-Q/`FormalDone` 保真

> **状态：** `LOCAL_LEAF_CLOSED / SOURCE_TO_SPEC_FIDELITY / NOT_A_CORE_VERDICT`。
>
> **父合同：** C1B4；冻结 fixed `set.mm@160ebb…`，C2C/C3C/C4C、C-361/C-370/C-371及IEP source。

## 1. 问题

```text
Does the fixed object-level theorem geoihalfsum faithfully instantiate the
mathematical dense half-process / FormalDone side of C2C, without importing
the physical runner, finite-stage OriginDone, or actual Standard-Solution P?
```

## 2. 判别字段

| field | 必须核对 |
|---|---|
| sequence | index domain and terms `1 / 2^k`; relationship to C-361 partial sums. |
| FormalDone | set.mm infinite sum / convergence versus C-361 Tendsto. |
| finite stages | whether exact source represents partial sums but does not state a finite endpoint. |
| physical/quantized Q | must remain absent unless source actually supplies it. |

## 3. 停止与后继

若数学字段保真，记录`Q_MATH_FIDELITY_WITH_SCOPE`并自动转C3B4；若只词汇相似或索引/term不对应，关闭 route并回C0。无论如何不把 `geoihalfsum`当作 IEP promotion或bare-ZFC verdict。

**实际结论。** [C2B4 fidelity card](ZFC-META-SUBTHEORY-ADEQUACY-001-C2B4-SETMM-GEOHALFSUM-DENSE-Q-FIDELITY.md)确认 `df-sum`把上整数序列的sum定义为partial sums的limit，`geoihalfsum`精确给出从 `k=1`的半程级数和为1；它可与 C-361 的`1-(1/2)^n`通过标准index shift同形对照。它不在自身 theorem中支付有限阶段不抵达或physical/quantized `OriginDone`，故为`Q_MATH_FIDELITY_PARTIAL_WITH_SCOPE`；C3B4现在只审actual P。
