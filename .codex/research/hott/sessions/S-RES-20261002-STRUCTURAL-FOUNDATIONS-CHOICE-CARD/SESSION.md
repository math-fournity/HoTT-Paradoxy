# S-RES-20261002-STRUCTURAL-FOUNDATIONS-CHOICE-CARD

> **身份：** `RESEARCH_GENERATION / T2 / BOUNDED_SOURCE_CARD / THREE_CONSUMER_DEFENSE / NO_NEW_GOAL`  
> **日期：** 2026-10-02  
> **触发：** 研究发起人授权“推进这个方向”，所指为此前历史 Gemini/ZFC 审计中留下的表示独立性、规范选择与自然性方向；随后纠正“菲尔兹奖入口”为可选来源，而非硬门。

## 1. 任务描述与完成标准

**研究对象：** Lawvere 的 Elementary Theory of the Category of Sets（ETCS）及其中“同构不变结构 + Choice”的组合；它是结构主义集合基础的一个精确候选，不把“所有范畴论”当成单一对象。

**本轮要判断的问题：** 历史 Gemini 的“同构证明改变对象”错误被剔除后，是否仍能在结构主义基础里提出一个保持同一任务的候选：结构输入只给出对象的同构类型／mere existence，后续却需要一个具体且自然的选择或运输。

**成功标准：**

1. 固定理论版本、基础资格与原典来源；
2. 区分普通选择任务与自然选择任务，避免把后者暗中当成前者；
3. 用项目现有的无标签二元素机器结果作为控制，而不把它误称为 ETCS 定理；
4. 给出 `E / T→T′ / X_i / P / O / Done / C+ / C−` 的首张卡，并判断其是否达到 UR；
5. 将用户关于菲尔兹入口的纠正写回唯一 current owners。

**本轮不做：** 不新建 Goal、不改 `STATE.json`、不新增数学证明、不重跑既有证明、不把 ETCS 或 ZFC 说成不一致、不声称所有结构主义消费者均无问题。

## 2. 研究前提与来源

| 层 | 本轮消费的证据 | 可支持范围 |
|---|---|---|
| 用户范围 | `rulings.md` 2026-10-02 两项裁定；KC-000003/004/016/048–054 | 理论级靶、过程与同一任务要求；菲尔兹为可选来源；不构成数学定理。 |
| 原典 | F. W. Lawvere, *An Elementary Theory of the Category of Sets*（1964；2005 长版重印） | ETCS 的基础定位、同构不变表述、Choice 公理与族选择形式。 |
| 项目形式化控制 | `HoTT/formal/truncation-no-recovery/NoCanonicalPoint.agda`；`MP-NOCANONICAL-001` 保存收据 | 固定 Cubical Agda 中无标签二元素呈现无统一选点、保留标签有正控制；不等于 ETCS 定理。 |
| 既有消费者审计 | `audit/natural-consumer审计-20260912.md` | Cubical v0.9 + S2–S5 固定集合内没有 E6 consumer；不能外推到所有 ETCS／范畴论使用。 |
| 真实消费者原典 | David Mumford, *Picard Groups of Moduli Problems*（1965，扫描件第 33–34、37 页目检） | 模问题中 universal family 的失败、automorphism-free 正控制、“definite model”选择与具体映射要求；是标准回答控制，不是 UR 命中。 |
| 真实消费者源码 | mathlib4 `8e30cac82f69c18f6cbe88799bdc3ebd74cc592d` 的 `Mathlib/CategoryTheory/Iso.lean` | `IsIso` 的存在性 inverse、`Classical.choose`、inverse 唯一性与 `map_inv`；unique-witness control，不是非唯一代表选择。 |
| 真实消费者源码 | 同一 mathlib4 commit 的 `Mathlib/CategoryTheory/Skeletal.lean` | 同构类 quotient、非计算 representative、具体 iso 与 natural isomorphism；nonunique representative control。 |
| 历史 AI 输入 | 外部 Aistudio ZFC 同构叙事与其在路线图中的来源审计 | “Identity Scar”是负控制，不能作为理论证据。 |

## 3. 首张候选卡与当前裁决

```text
ID / 身份：FND-STRUCT-005 / USER_AUTHORIZED_SOURCE_CARD / DRAFT_CANDIDATE
理论 T：ETCS（冻结为 Lawvere 的 categorical set theory；Choice 是否纳入须显式写出）
基础资格：Lawvere 明确作为集合论基础提出；对象按同构不变结构／泛性质理解。
可选来源入口：Lawvere 原典；菲尔兹关联不构成门。
收益 E：避免成员编码负担，以结构性映射与同构不变量组织对象；Choice 允许构造选择／quasi-inverse。
初步转换 T→T′：从有具体标签、呈现或选择史的对象，转为仅有结构性／同构不变信息的对象；Choice 仍可断言某个选择存在，但不提供自然性。
普通任务 X_any：为每个非空纤维给出某个选择。
被加强任务 X_nat：同一输出还必须对所有同构／自同构兼容。
过程 P：二元素对象到终对象的映射，加上交换自同构；比较任意选择与自然选择。
观察 O：自然选择将被交换强制成不动点；带标签接口存在正选择。
完成 Done：X_any 的完成是有某选择；X_nat 的完成是有所有呈现兼容的选择。
正控制 C+：保留具体 `A ≃ Bool` 标签，已有 `labeledChoice`。
标准回答 C−：ETCS Choice 只承诺 X_any，不承诺 X_nat；要求自然性已经变更 Done。
当前判词：G0_SOURCE_SUPPORTED；G2 有种子；G3/G4 尚未通过；STRUCTURAL_CHOICE_BOUNDARY / NOT_UR_YET / DEPRIORITIZED_WITH_SCOPE。
```

**当前研究判断：** `X_nat` 的失败不能被当作 ETCS 使 `X_any` 失败。此前 Gemini “Identity Scar”的错误正是没有写出这一 Done 的变更。故本轮收获是一个严格的候选筛选边界，而非一个新的非现实性悖论。

## 4. 第一个真实消费者控制：Mumford 1965

Mumford 的原始扫描件第 33 页明确记录：非奇异曲线的 universal family 并不存在；限制到没有自同构的曲线后才存在 universal family。第 34 页又把“若研究一个 definite model 的不变量，要选哪一个模型”列为问题；第 37 页明确说有非平凡自同构时必须指定具体映射。这是一条完整的结构性分类 → 具体代表族／模型选择的消费者链。

它没有把 coarse classification 说成已完成 universal family；相反，保留了失败并在自同构消失的子类给出正控制。故判词为 `REAL_CONSUMER_CONTROL / DEFENSE_WORKS_WITH_EXPLICIT_PAYMENT`。它使本轮候选更严格，而不构成 ETCS 或模理论的非现实性结论。

## 5. 第二个真实消费者控制：mathlib4 `IsIso`

固定 mathlib4 commit 的源码把 `IsIso f` 定义为 inverse 存在的 Prop，并用 `Classical.choose` 实现 noncomputable `inv f`。但 inverse 是唯一的，随后 `map_inv` 以唯一性保证函子映射与 inverse 相容。此处不存在“从同构类中任意挑一个代表却声称自然”的动作；它是 `UNIQUE_WITNESS_DEFENSE`。

这使下一步搜索条件更精确：候选输出必须是**非唯一**的具体点、代表或标记，而不是唯一可由结构恢复的 inverse。

## 6. 第三个真实消费者控制：mathlib4 skeleton

`Skeleton C` 用对象同构类的 quotient 构造 skeletal category，并在 `fromSkeleton`、`toSkeletonFunctor`、`skeletonEquivalence` 等定义上显式写 `noncomputable`。`Quotient.out`／`Nonempty.some` 取得代表和具体 iso；unit/counit 与 `toSkeletonFunctorCompMapSkeletonIso` 保留相干。因此它处理的正是非唯一代表选择，却没有声称该选择是无代价的定义性相等或可计算自然选择。

判词为 `NONCOMPUTABLE_COHERENT_REPRESENTATIVE_DEFENSE`。下一来源不应只“使用 quotient 或 representative”，而必须在未标记这些支付的情况下把它们当作免费完成。

## 7. 后续有界动作与重开条件

下一步只在找到一个真实、版本固定的 ETCS／结构主义／范畴论消费者时开启。该消费者必须同时：

1. 只接受同构不变或 mere 输入；
2. 实际要求具体、自然或相干的输出；
3. 没有把标签、顺序、Choice、标记或相干数据作为显式输入；
4. 仍声称完成原来的同一任务。

若消费者显式要求这些额外数据，或将任务降为任意选择，则记录 `DEFENSE_WORKS / REPRESENTATION_BOUNDARY`，不再把它报作 ETCS 的 UR。

## 8. 有界结案

`STRUCT-001` 固定了三个真实消费者：Mumford 模空间、mathlib4 `IsIso`、mathlib4 `Skeleton C`。三个例子分别显式支付自同构、唯一性或非计算＋相干成本；都不把结构性输入免费升级为自然代表交付。因此该候选在固定分母内降为 `DEPRIORITIZED_WITH_SCOPE / REUSABLE_CONTROL`。

这不是“所有 ETCS／范畴论／结构主义数学都没有问题”的结论。重开条件仍是发现一个版本固定的 E6 消费者：它有非唯一输出、未声明支付、保持同一任务，并在正控制中能因补足数据而完成。

## 9. 交叉审视与写回

- **核心认知：** 本轮遵循“基础理论靶 + 针对性过程”，不把“理论没有时间”或“证明历史改变对象”当成取靶替代；没有新用户原文，故不改 core。
- **方向／结果：** 此为 post-HoTT 候选来源卡，不修改 HoTT 的 `STATE`、方向追踪、全景视野或既有 Goal7。
- **持久 owner：** 用户的入口纠正写入 `rulings.md`；F-025 原位更新；候选卡与其证据边界写入 `dev-docs/菲尔兹奖后续理论级目标路线图/`。
- **数学状态：** 无新数学主张、无新 proof source、无新 kernel run；既有 `MP-NOCANONICAL-001` 按其原始 scope 使用。
