# CoreAdequacyTaskCard — C0R3：F-B object-level sources后候选前沿重评

> **状态：** `LOCAL_LEAF_CLOSED / CANDIDATE_FRONTIER_RECONCILIATION / NOT_A_CORE_VERDICT`。
>
> **父合同：** C3B4 successor scan；输入为Mizar、Isabelle/ZF、Foundation、set.mm、Rocq ZFC的固定source cards，以及F-C候选来源。

## 1. 问题

```text
After separating object-level M→S evidence from actual P/Bridge evidence,
which candidate family can still change the core M/S/Q/P/Bridge/Adequacy
verdict, and what exact new payment must it supply?
```

## 2. 纠错字段

`C0B5` 的Rocq source ingress在本卡写入前已经发生。它是来源发现动作，不是研究结论；本卡必须如实登记 `TASKCARD_ORDER_EXECUTION_DEVIATION`，以C0B5的独立source evidence为准，并恢复“先TaskCard、后source action”的顺序。

## 3. 判别标准

- 单有新的 object-level real/limit theorem，不能让F-B继续live；
- 新候选必须有希望支付actual `P`、`Bridge`或foundation-facing `Adequacy`之一；
- 若F-B的版本固定分母完成，记录其reopen conditions，转F-C；
- 不以当前没有bare interface的事实作为Goal完成理由。

**实际结论。** [C0R3 reconciliation](ZFC-META-SUBTHEORY-ADEQUACY-001-C0R3-FB-FC-CANDIDATE-FRONTIER.md)将F-B冻结为五条可审source lane：Mizar、Isabelle/ZF、Foundation、set.mm、Rocq ZFC。前两种正S中均无actual P，后三种无admissible S；F-B在这一分母中已耗尽。F-C仍有一条可检验的“scientifically applicable mathematics in set-theoretic framework”来源入口，但C0C2在C5D完成前保持PARKED_READY；F-A2的actual-policy classification优先。C0B5的TaskCard顺序偏差已登记并修复。
