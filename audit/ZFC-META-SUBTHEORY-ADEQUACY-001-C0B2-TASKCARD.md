# CoreAdequacyTaskCard — C0B2：独立 Isabelle/ZF 连续统子理论盘点

> **状态：** `LOCAL_LEAF_CLOSED / INDEPENDENT_FORMALIZATION_INVENTORY / NOT_A_CORE_VERDICT`。
>
> **父合同：** `C0B`；由 [C6A successor scan](ZFC-META-SUBTHEORY-ADEQUACY-001-C6A-SUCCESSOR-SCAN.md) 自动选择。

## 1. 问题

Mizar/TG 已给出一条 ZFC-founded extension 的模型链。C0B2 以独立系统岛检验：官方 Isabelle/ZF current distribution 是否存在版本固定、可定位的

```text
ZF/ZFC foundation → real numbers / sequences / limits / continuous trajectory
```

链。它只影响 M/S candidate universe，不把 Isabelle checker acceptance混成 physical completion。

## 2. 准入字段

| 字段 | 要求 |
|---|---|
| `M` | Isabelle/ZF 的 exact version、理论身份与 Choice边界。 |
| `S` | 至少一条实际 real/sequence/limit/continuity theorem chain，不能只出现 ordinal or natural-number `Limit`。 |
| version | official current documentation/source locator，记录日期及 commit/release若有。 |
| falsifier | current library只含 ZF core/ordinal-limit而无可承接 IEP continuum S；或理论变体不含所需 Choice/real construction。 |
| forbidden inference | 不将未找到写成全局不存在；不将 theorem checker说成 bridge/P。 |

## 3. 局部停止

若命中，创建独立 C1B2 card；若未命中，记录 `NO_ADMISSIBLE_CONTINUUM_CHAIN_IN_THIS_LIBRARY_VERSION`、保留 exact denominator和 successor scan，再转 C0E1。任何结果均不改变 C6A 的已有证明范围或停止 Goal。

**实际结论。** [C0B2 result](ZFC-META-SUBTHEORY-ADEQUACY-001-C0B2-ISABELLE-ZF-CONTINUUM-INVENTORY.md) 在 frozen Isabelle2025-2 FOL/ZF session内没有发现可承接 S；当前 actual-defense 后继见 [successor scan](ZFC-META-SUBTHEORY-ADEQUACY-001-C0B2-SUCCESSOR-SCAN.md)。
