# C3B4 后继扫描：F-B/F-C 的可支付字段重排

> **身份：** `SUCCESSOR_SCAN / CORE_GOAL_ACTIVE / C0_RECONCILIATION`。
>
> **前叶：** [C3B4 actual promotion audit](ZFC-META-SUBTHEORY-ADEQUACY-001-C3B4-IEP-TO-SETMM-PROMOTION-AUDIT.md)。
>
> **结果：** `C3B4_LOCAL_LEAF_CLOSED / C0R3_SELECTED / TOTAL_GATE_UNSATISFIED`。

## 触发条件

F-B现在已有两个不同的数学对象层正例（Mizar、set.mm）和两个固定负 inventory（Isabelle/ZF、Foundation），但两个正例都未支付actual P。继续寻找同形“实数／极限库”不会改变core verdict。

## 自动选择：`C0R3-CANDIDATE-FRONTIER-AFTER-OBJECT-LEVEL-S`

从C0 manifest逐项问：哪个未耗尽 family可能支付 `P`、`Bridge`或actual `Adequacy`，而不是再支付M→S？

- 若是F-C，必须冻结一个实际foundation-facing semantic acceptance source；
- 若是F-B，必须是formalization与Standard-Solution application同源或有明确consumer；
- 若现有冻结候选都不具这种潜力，登记 `CANDIDATE_UNIVERSE_NEEDS_SOURCE_INGRESS`，并按SOP决定如何有界扩展，不以“没有更多库”结束Goal。
