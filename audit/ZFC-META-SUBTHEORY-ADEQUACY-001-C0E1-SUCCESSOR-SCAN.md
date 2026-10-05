# C0E1 后继扫描：SameQ_H0 最小审计

> **身份：** `SUCCESSOR_SCAN / CORE_GOAL_ACTIVE / NOT_A_COMPLETION_RECORD`。
>
> **前叶：** [C0E1 defense audit](ZFC-META-SUBTHEORY-ADEQUACY-001-C0E1-ACTUAL-DEFENSE-AND-BRIDGE-SOURCE.md)。
>
> **结果：** `C0E1_LOCAL_LEAF_CLOSED / C0D1_SELECTED / TOTAL_GATE_UNSATISFIED`。

## 1. 为什么现在轮到 H0，而不能直接合并它

C6A 已把 `h0MissingSameQ` 作为正控制：没有 SameQ，H0 不能加强当前 application verdict。C0E1 给出 strict/revised source defense，使“字面上都说完成”更加不能充当 SameQ 证据。

因此下一高判别工作不是再找一般 HoTT 模型，而是对已有 fixed H0与当前 Q 做一次**最小逐字段检验**：

```text
object / input / operation / observation / OriginDone / theory layer / source policy.
```

若有一项不能支付，就登记 `SameQ_H0_UNPAID` 并将 H0 从核心 verdict永久排除；若存在 source-supported mapping，才允许进入更强 cross-theory consequence。

## 2. 自动选择：`C0D1-H0-SAMEQ-MINIMUM-AUDIT`

它只消费 main 已固定 H0 evidence和本轮 Q cards；不重跑 HoTT，除非发现来源身份变更。无论结果都不替 current ZFC application theorem补出未付 bridge，也不停止 Goal。
