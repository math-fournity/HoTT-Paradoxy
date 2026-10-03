# HMZ-005：真实消费者与标准防线

## HMZ-C-010 — 指定 product functor 与 product anafunctor 的契约对照

| 字段 | 普通 product functor | product anafunctor |
|---|---|---|
| 理论层 | Makkai 采用无 AC、无 Foundation 的 constructive Gödel–Bernays class-set theory；这是集合论邻近控制，**不是 ZFC 的对象语言实例**。 | 同左。 |
| `u` | 每对对象 `(A,B)` 的一个**具体选定** product diagram 及其对象值。 | 每对对象的**全部** product diagrams；值只以同构类方式给出。 |
| `F` | “`A` 有 binary products”只给逐对存在；把它升级为全域普通 functor，需要同步选定一个 product。 | 从所有 product diagrams 的类直接构成 anafunctor；不选定单个 product。 |
| `C` | 把 finite-product category 作为 structured-category algebra 的对象，所需 product functor；另有 free structured category 的 universal-property consumer。 | 同一数学背景下的替代构造，但 consumer 接受的是 anafunctor，不是一个 ordinary functor。 |
| 输入／操作／观察 | 输入 `(A,B)`；交付一个特定 `A×B`，并在所有映射上给 functorial action。 | 输入 `(A,B)`；交付一类 possible values／图表以及由 universal property 导出的箭头，观察保持到 isomorphism。 |
| `Done` | 有一个 ordinary functor：每个输入都指定具体值。 | 有一个 saturated product anafunctor：每个输入保留全部同构等价的可能值。 |
| 来源处理 | 作者明说此定义一般需要 AC；它是明示的 payment。 | 作者明说其避免 non-canonical choice，但还必须证明它“enough of the job”；在需要 Cartesian closed 性的更强任务上，文中再次加入 SCSA。 |

## 这为什么不是同一任务的“未付完成”

1. **普通 functor 的 Done 没有被悄悄宣布。** 导言 p. 1 和 §1 p. 10 都把每对对象选一个积的 simultaneous/non-canonical choice 明说为 ordinary product functor 的条件。
2. **替代不是同一输出。** anafunctor 的输出保留所有 product diagrams／可能值到同构，而 ordinary functor 输出每个输入的一个指定值。这是 source-defined interface change，不是同一 `Done` 下的免费恢复。
3. **选择并未被整体抹除。** p. 2 与 §5 pp. 79–81 对 SCSA/SVC 的讨论记录了更强 categorical closure 所需的弱 Choice；这排除“anafunctor 已让所有后续结构无支付”的读法。
4. **没有 P2/P3 的形成再入。** source 中的 product diagrams 已经在 `F` 给定的 existence condition 下被讨论；没有一个自身合法性尚待决定的同一对象被其后的 member/operator/admission consumer 使用。

## 对 HMZ 的处置

```text
CONTROL CLASS: EXPLICIT_CHOICE_PAYMENT + OUTPUT_CONTRACT_CHANGE
Q STATUS: Q-R REJECTED_WITH_SCOPE
P2/P3: NOT SUPPLIED
H0→Z0: ANTI_ANALOGY_CONTROL
```

这个控制保留一个更精确的后续检索式：只有当某个**ZFC 层**的实际消费者声称普通、指定的 object-valued functor／choice output 已由 mere existence 获得，且没有 Choice、标记、代表或 Done 改写时，才值得形成下一张 `Z` 卡。Makkai 本文不满足这项条件。
