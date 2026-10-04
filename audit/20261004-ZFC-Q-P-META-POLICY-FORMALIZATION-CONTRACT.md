# ZFC-Q-P：时间观察力、数学幻觉与政策张力的形式化合同

> **身份：** `CONTRIBUTOR_CANDIDATE_NOT_CURRENT / USER_HYPOTHESIS_FORMALIZATION / META_POLICY_NOT_ZFC_OBJECT_THEORY`。

## 1. 用户提出的链条

本轮用户提出：若 ZFC 缺少一种关于时间／过程完成的理论观察力 Q，则该缺口可能允许数学共同体采用 P；P 让共同体获得想要的 A（极限理论解决芝诺／圆环的判断），同时导向不想要的 B（HoTT 的罗素计算内核显出的不合理）。用户将实际采用 P 的共同体实践称为 `ZFC-1 = ZFC + A = ZFC + P`，并希望经由反证式回溯从 B 找到 P。

该链条包含三个不同层次，必须分开：

| 层 | 本轮形式对象 | 不能自动推出 |
|---|---|---|
| 对象理论 | `baseZFC` 的抽象占位符 | 实际 ZFC 的不一致或定理。 |
| 社区政策 | P 的许可、采纳、A/P 互推和 P→B 的显式规则 | 数学共同体真的实行这些规则。 |
| 现实／计算解释 | P 的计算／现实 bridge 是否存在 | P 实际不可计算或反现实。 |

## 2. 冻结的最小逻辑合同

```text
Q-missing      = community lacks a specified observation capacity
Q-missing → permitted(P)
permitted(P) → community adopts P in its operational extension
P ↔ A          = explicit policy-level equivalence, not syntactic identity
P → B          = explicit policy-level consequence
P → A ∧ B      = conjunction produced by the policy
```

`ZFC-1 = ZFC + A = ZFC + P` 因此在 Lean 中必须读作：在固定的 A↔P policy rules 下，`baseZFC+A` 与 `baseZFC+P` 的**可导后果相同**。它不是“实际 ZFC 的公理集合逐字相等”。

本轮补上的完整政策链是：

```text
Q-missing + absence-permits-P + adoption(P)
    ⇒ P in the operational extension
    ⇒ A ∧ B
    ⇒ (wanted A ∧ unwanted B) = normative tension
```

如果另有一条正式真理约束排除 B，或证明 A/B 在同一政策中形式不相容，才可从这条链推出 `False`。空基理论的负控制也确保 A/P 的互推循环不会无中生有地产生 P；模型中的 P 必须是显式加入的政策声明。

## 3. B 的两种可能身份

1. **规范性张力：** 共同体想要 A、却不想要 B。Lean 可无额外数学假设地表达这一政策冲突。
2. **对象层矛盾：** 需要额外证明 A 与 B 在同一形式系统内不相容，才可以推出 `False`。

当前材料只允许把 B 定为第一种候选。把“不想要 B”直接写成 `ZFC ⊢ False` 将是层级跳跃。

## 4. 形式化与来源义务的连接

当前 [MP-ZFC-META-OBSERVATION-CONSISTENCY-001](../HoTT/formal/zfc-observation-boundary/MetaObservationConsistency-CLAIM.md) 已经给出另一条条件性定理：相同完整 QProfile 且相反 completion judgment 会破坏一项拟议的 O3–O5 政策一致性。前一轮 U6 已证明直接 Zeno↔QuestioningDelay 映射不满足 `sameQ`。

本轮新模型不推翻该控制。它回答另一个问题：如果未来有实际来源填入 Q/P/A/B，那么“共同体选择 P 而同时出现 A、B”该怎样在不偷换 ZFC 对象理论的前提下精确表达。

## 5. 成功／反证条件

| 需要的事实 | 达成后能做什么 | 缺失时的正确状态 |
|---|---|---|
| Q 的一手定义及 ZFC／共同体缺失证据 | 把 `hasObservationQ` 从占位符替换为来源概念 | `Q_CANDIDATE_ONLY` |
| P 的精确规则和采纳来源 | 把 `permitted/adopts` 变成来源卡 | `P_NOT_SOURCE_MAPPED` |
| A 与 P 的实际等价／互推证据 | 检验 `ZFC+A` 和 `ZFC+P` 的实际 policy equivalence | `A_P_EQUIVALENCE_UNPROVED` |
| P 到 B 的保真同任务链 | 检验用户的“想要 A 也得到 B”机制 | `P_TO_B_UNPROVED` |
| A 与 B 的形式不相容 | 才可能讨论对象层 `False` | `NORMATIVE_TENSION_ONLY` |
