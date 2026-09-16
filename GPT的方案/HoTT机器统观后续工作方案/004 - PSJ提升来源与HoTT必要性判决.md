<!-- governance-shard:v2
logical_id: GPT-HOTT-MACHINE-OVERVIEW-PLAN
shard_id: 004
index: ../HoTT机器统观后续工作方案.md
-->

# PSJ提升来源与HoTT必要性判决

## 1. 目的

`PSJ-001` 不重做已经闭合的局部数学，而是回答：现有最强结果已经达到一般非因子化、HoTT 相关潜势，还是已经接近现实相对候选？

决定性问题是：

> 哪一个先在任务、哪一个 consumer、哪一条理论规则／论文解释／库 API／应用合同，实际完成了从较弱理论对象到完整过程身份、当前可用能力或现实交付的提升？

## 2. 候选批次

第一批：

1. C-71–C-76：Delay 结果商、`bind`、`race` 与 deadline；
2. C-96–C-99：外延相同函数、成本差异和细化表示正控制。

第二批只在第一批方法有效后展开：

- C-124–C-128：SIP／ua 与签名外观察；
- C-129–C-133：Cauchy modulus；
- C-134–C-148：截断、有限结构接口、无典范选点。

不把 C-59–C-249 全部复制成新表。候选按“理论配置＋抽象变化＋来源任务＋关键障碍”去重。

## 3. 九个独立字段

| 字段 | 问题 |
|---|---|
| `ExactTheoryConstruct` | 哪条 HoTT/Cubical/一般代数规则参与？版本、公理、universe 是什么？ |
| `AbstractionMap` | 哪些状态、顺序、标签、模数、成本或来源被合并／遗忘？ |
| `PromotionSource` | 提升来自理论、论文、库 API、应用接口还是本项目假设？ |
| `TaskIdentity` | input、consumer、observation、completion 是否逐项相同？ |
| `CurrentEvidence` | 哪个 claim/proof/run/source 支持哪一段？ |
| `PositiveControl` | 富表示、显式时序、模态限制或保留数据能否完成同一任务？ |
| `RealityEvidence` | 外部任务、应用合同、运行、测量或来源是什么？ |
| `P0_or_P1_ablation` | comparison calculus 中能否同任务重现？ |
| `HoTTEssentiality` | 哪个 exact HoTT construct 的移除改变判词，保持证据与 generic 解释是什么？ |

第八轮修订明确：消融是取得 essentiality 证据的方法，essentiality 是候选状态；两者不得合并成一个字段。

## 4. P0/P1 消融合同

```text
target_calculus
candidate_construct
comparison_calculus
translation
typing_preservation
equality_preservation
consumer_preservation
observation_preservation
completion_preservation
ablation
verdict
```

comparison calculus 必须具名、固定版本／规则和模型。写“集合论”“ETT”或“非 HoTT”不够。

## 5. 首单元的 comparison pool

PSJ-001A 在开始候选推演前冻结一个最小池：

1. current target calculus；
2. 一个不依赖 HoTT 高阶结构、但能表达同一商／外延函数任务的具名 calculus 或模型；
3. 一个保留 delay/cost/trace 等细化数据的正控制表示。

候选名称只提供搜索起点，不预先指定结论。只有 translation/preservation 闭合后，comparison 才能承担 P0/P1 判词；否则为 `INCONCLUSIVE_TRANSLATION_OR_PRESERVATION_OPEN`。

## 6. PromotionSource 分母

按顺序检查：

1. exact theory rule 或标准演算解释；
2. 论文 theorem/definition/application 文字；
3. 社区库 API、调用者、实例、example；
4. proof assistant／编译器／运行接口的真实承诺；
5. 外部应用合同或任务规范；
6. 用户明确提出的研究解释；
7. 仅为本项目生成的 synthetic translation。

第 7 类必须标 `SYNTHETIC_CALIBRATION_CONSUMER`，不能自授 natural/source-grounded 资格。

搜索使用冻结的 source denominator：渠道、查询式、版本、纳入／排除、先在时点、holdout、结束条件。无命中产生具名范围负结论，不扩大到“没有人会这样提升”。

## 7. 判词

形式层：

```text
P0_GENERIC_REPRODUCED
P1_HOTT_RELATED_NOT_ESSENTIAL
P1_HOTT_ESSENTIAL_WITH_SCOPE
INCONCLUSIVE_TRANSLATION_OR_PRESERVATION_OPEN
```

提升／现实层：

```text
REPRESENTATION_BOUNDARY_CONFIRMED
PROMOTION_SOURCE_FOUND_REALITY_BRIDGE_OPEN
REALITY_RELATIVE_CANDIDATE_READY_FOR_PROOF
CANDIDATE_REJECTED_BY_SAME_TASK_CONTROL
NO_QUALIFIED_PROMOTION_SOURCE_IN_DENOMINATOR
```

## 8. PSJ-001A：Delay/race/deadline

固定：

- Delay 语法和结果等价；
- 商与 `bind` 的下降；
- race/deadline 的 observation；
- theory consumer 与 source consumer；
- 富表示／代表层正控制；
- comparison calculus。

关键不是再证 race 不同余，而是找是否存在先在接口把“结果商”承诺成含竞态／时限的完整过程身份。若接口明确拒绝该操作，判 `DEFENSE_WORKS` 或 `REPRESENTATION_BOUNDARY`。

## 9. PSJ-001B：同函数异时

固定：

- 裸函数相等的 exact rule；
- 程序表示与函数表示的关系；
- source-grounded 资源／期限任务；
- cost/trace observation；
- 细化表示正控制；
- funext 被移除或替换后的 comparison。

关键是查明谁实施“函数相等＝程序完整身份”。funext 只给函数类型内相等；若完整过程提升仅由研究者添加，候选不升 A1。

## 10. 输出与停止

每个候选输出九字段、来源分母、comparison/preservation、正控制、两个层级判词、未决与 reopen 条件。

第一批在两个候选均取得形式判词与提升判词后停止。若任一达到 `REALITY_RELATIVE_CANDIDATE_READY_FOR_PROOF`，立即让位给直达候选链；若都落在 general/boundary，转 ATD/R4X，不在同族反复换故事。

