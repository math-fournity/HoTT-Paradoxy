# P-DAG-ZFC-SOURCE-023/024：relative-powerset 边界控制

> **身份：** `PRIMARY_SOURCE_CONTROL / MODEL_RELATIVE_BOUNDARY / NOT_A_STANDARD_ZFC_Q_RESULT`。

## H023 的预启动失败

H023的 source prompt 将 required marker 写成`BEGIN FROZEN PRIMARY SOURCE CARD`，因此在认证借用和模型采样前被source-match profile拒绝。它无模型输出、thread、turn、wire或理论判词；[失败收据](20261002-P-DAG-ZFC-SOURCE-023-PREFLIGHT-FAIL.md)保留原字节。H024只将 marker 改为正确的`BEGIN FROZEN SOURCE CARD`，不改 source/task 内容。

## H024 的来源范围与外部节点证据

source是 Isabelle2013-1 的 `ZF-Constructible/Relative.thy`，其页面明确位于`M_trivial`的相对模型语境。H024 source-match prompt gate通过；`gpt-5.6-terra/max`以`approval=never`自然终态，73.188秒、302 words、0 tool/file/approval。private liveness记录`RUNNING → STILL_RUNNING@61.311 → TERMINAL`；wire为230,854 bytes、SHA-256 `027fb6447ef70db737187a92aa24b5990abf99bcf0dcb632149ef8b68af29b79`。trajectory为620 events、一个terminal turn、0 tool/result/approval；L1–L5仍按有限source保留`NOT_TESTED/NOT_OBSERVED/REQUIRES_*`边界。

## P1 判词

该 source card给出：

```text
power_ax(M) = ∀x[M]. ∃z[M]. powerset(M,x,z)
powerset(M,x,Pow(x))
powerset(M,x,y) ∧ M(y) ⇒ y ⊆ Pow(x)
```

并明确说明不能证明 `M` 中的 internal powerset 包含 external real powerset。外部 Terra/Max MatchTrace 正确得到：

```text
relative-model / one-direction powerset correctness: SOURCE_SUPPORTED
same-layer internal consumer with I/O/Done: NOT_SUPPLIED
positive Q surviving L6/L7: NOT_SUPPLIED
standard-ZFC Q: NOT_ESTABLISHED
```

关键原因是 `Pow(x)` 在这里是模型外比较项或证明见证；它不是 M 内部的 downstream consumer。内部 y 到 external `Pow(x)`的一向包含不等于内部 y 与外部幂集相等。这个源可以作为“模型内外差异必须标层”的正控制，不能用作ZFC说了所有外部子集、因而已产生悖论的证据。

## 当前 source-search 停止条件

H019–H024 已有四类不同卡：

| 卡 | P1 结果 | 为什么不能升级 |
|---|---|---|
| 脱敏 all-subobjects formation | `DIRECT_PAYMENT_ONLY` | formation 已直接给出对象。 |
| Mathlib ZFSet `funs` API | `Q_UNSET` | API分类条件可正常 false，缺 positive Done。 |
| Cantor / proof-system / formula card | proof/formula scoped | 无同层 semantic/actual-use consumer，或只有受 guard 的语言链。 |
| Isabelle relative powerset | model-relative boundary | internal/external comparison不是内部 consumer任务。 |

这个有界分母内没有可交给 P2/P3 的 Q。下一轮必须由一个新的、版本固定的 standard-ZFC 或实际数学使用 source 提供同层 consumer与positive obligation；继续改写已有四张卡不会提高结论等级。

