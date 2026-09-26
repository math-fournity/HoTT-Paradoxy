<!-- governance-shard:v2
logical_id: hott-paradox-programmatic-exploration-completeness
shard_id: 002
index: ../HOTT-PARADOX-PROGRAMMATIC-EXPLORATION-COMPLETENESS.md
-->

# HoTT构造与程序化激发算子全景

## 一、理论构造分母

| ID | 构造族 | 程序化表示 | 优先观察 |
|---|---|---|---|
| `TC-01` | Π/Σ、dependent elimination、transport | typed AST、substitution、motive generator | 依赖信息丢失、顺序、motive 合法性 |
| `TC-02` | Identity/Path、J、composition/fill | path terms、faces、coherence obligations | Path/判断相等、transport、endpoint observation |
| `TC-03` | Univalence、equivalence、SIP | equivalence codes、ua/transport、structure paths | 外延同一与操作观察恢复 |
| `TC-04` | HIT、set quotient、truncation | constructor/eliminator signatures、truncation levels | mere/chosen、消去限制、coherence |
| `TC-05` | Universes、cumulativity、resizing | universe constraints、codes/El、level solver | 自指层级、large elimination、Girard/Russell 防线 |
| `TC-06` | Modalities、reflective subuniverses、localization | reflector/unit/eliminator、modal predicates | 内外层能力、reflector consumer、固定点 |
| `TC-07` | Guarded/clocked/later/coinduction | clock/tick syntax、later、force、guarded fix | 当前/延后可用、生产性、tick irrelevance |
| `TC-08` | Partiality、general recursion、termination | step-indexed partial elements、machine code、ranking | halting/divergence、quotient、deadline/race |
| `TC-09` | Syntax quotation、reflection、elaboration | quoted AST、reifier/evaluator/substitution | 自观察、对象/元层、normalization feedback |
| `TC-10` | Proof search、typeclass、tactics/macros | rule graph、search strategy、fuel/priority | search completion、loop、proof-check distinction |
| `TC-11` | 2LTT、strict/fibrant、internal metatheory | inner syntax + outer strict equality | HoTT 自编码、substitution、层级合法性 |
| `TC-12` | Directed/cohesive/parametric/cost-aware extensions | directed hom、modalities、relational/cost semantics | 不可逆、因果、资源、时间与表示 |
| `TC-13` | 附加逻辑原则 | LEM、choice、propext、quotient/resizing axioms | 构造性、选择、可计算性与模型范围 |
| `TC-14` | 语义模型 | cubical sets/assemblies、simplicial/realizability models | consistency、independence、Church thesis 域 |

每个 source/version 的存在不等于已经覆盖该构造族。必须固定实际语法、规则和自然 consumer；同名构造在不同框架中分别登记。

## 二、激发算子

| ID | 算子 | 变换 | 典型候选 |
|---|---|---|---|
| `OP-01` | 资格/侧条件擦除 | 删除 clock、universe、truncation、motive、termination、naturality 等条件 | 原规则拒绝、擦除后矛盾/循环；防线定位 |
| `OP-02` | 层级提升 | Path→judgemental、mere→chosen、external→internal、proof exists→solver available | B向能力越级、reflection collision |
| `OP-03` | 量词加强 | pointwise→uniform、每有限步→完成、存在→可计算选择、局部→全局 | 统一完成失败、不可判定/不完备 |
| `OP-04` | 忘却—恢复 | quotient/truncation/extensional equality 忘掉信息，再由 consumer 恢复 | race/deadline、history/cost、选择障碍 |
| `OP-05` | 时序坍缩 | later/tick/step/future proof 变成 current availability | nontermination、production/termination 混淆 |
| `OP-06` | finite→exact | 有限近似、Cauchy evidence、分段路径被提升为 exact limit/arrival | 芝诺/完成性、modulus/choice |
| `OP-07` | 组合闭环 | 单项合法操作组成 cycle、callback、feedback、mutual recursion | 直指循环、consumer re-entry |
| `OP-08` | 自编码/对角 | quote→substitute→evaluate、program index self-application、proof predicate | Gödel/Kleene/Lawvere/Löb |
| `OP-09` | 观察器合成 | 自动生成 transport/deadline/race/eliminator/normalizer/search/application context | 隐藏差异被实际消费 |
| `OP-10` | 跨表示差分 | 等价表示、优化前后、不同 normalization/strategy/kernel | 表示异化、实现差异、性能假象 |
| `OP-11` | 跨模型移植 | 把模型/模态/CT/choice theorem 移入另一 universe 或框架 | 假设域泄漏、模型相对反例 |
| `OP-12` | universe/coherence 压力 | 合成 higher paths、dependent fillers、large eliminations、resizing/self code | 高阶一致性与层级边界 |
| `OP-13` | 资源/完成观察 | 给同一外延值加入期限、在线输出、空间/步骤或业务 continuation | A向新增完成困难 |
| `OP-14` | 反解释生成 | 自动构造保留原任务的富表示、显式事件、guard、clock、modulus 或模型 | 反驳过强 HoTT 缺陷主张 |

## 三、方向 A 的程序候选族

1. `A-DelayCollapse`：结果等价/商化忽略延迟，deadline/race/bind consumer 恢复时序；
2. `A-ContinuousCarrier`：离散完成任务映为 Path/interval/连续 carrier，endpoint apartness 产生 coherence obligation；
3. `A-FiniteExact`：每个有限近似可构造，却要求无给定 modulus/choice 的 exact completion；
4. `A-HistoryErasure`：只保留端点/外延函数，组合 consumer 需要 provenance、因果或成本；
5. `A-GuardErasure`：去掉 later/clock/tick qualification，当前归约或自观察出现冲突；
6. `A-QuotientConsumer`：商/截断合法，但后续操作要求被消去的代表或 witness；
7. `A-CoherenceExplosion`：局部等价/路径组合生成无限/高阶 coherence 义务，检查是逻辑要求还是实现负担；
8. `A-Uniformization`：逐实例可完成被升级为统一算法/统一选择，触发不可判定或选择障碍。

## 四、方向 B 的程序候选族

1. `B-MereToChosen`：mere existence/截断 inhabitance 被交付为 concrete witness；
2. `B-ProofToSolver`：可证明性或给定 proof checking 被交付为 total proof search/theoremhood decision；
3. `B-PathToReduction`：内部 Path 被交付为当前 judgemental computation；
4. `B-ExternalToInternal`：元层 interpreter/kernel knowledge 被交付为对象理论自知；
5. `B-PartialToTotal`：step-indexed/partial classifier 被包装为 total Boolean API；
6. `B-ModelToUniverse`：某模型或 reflective subuniverse 中的能力被推广到任意 HoTT universe；
7. `B-ApproxToExact`：近似/有限检验被交付为 exact/infinite property；
8. `B-EquivalenceToOperational`：structure identity/equivalence 被交付为资源、历史、时序完全可替换。

## 五、Gödel/自指候选族

1. `G-Code`：有限 syntax、decoding、substitution、proof object 与 Nat/bit coding；
2. `G-Enumerator`：proof/refutation 的公平部分分类器；
3. `G-Universal`：universal partial evaluator/EPF 的精确理论或模型域；
4. `G-Separation`：对象语言 strong representation/separation；
5. `G-Diagonal`：self-return/fixed-point sentence 与 classifier divergence；
6. `G-Incompleteness`：一致、可枚举、足够强理论的 independent sentence；
7. `G-Essential`：extension 保持前提并继续不完备；
8. `G-HoTTSyntax`：exact HoTT calculus 的 syntax/judgment/proof code；
9. `G-InnerOuter`：inner HoTT 与 outer 2LTT/meta-kernel 的表达/证明边界；
10. `G-SelfGuarantee`：系统声称自身 consistency/totality/reliability 的 Löb/第二不完备压力。

## 六、时间与时序候选族

- 时间：运动、时空连续性、稠密性、有限/无限路径和现实完成；
- 时序：事件先后、依赖、因果、proof availability、tick/step 和在线交付；
- 交叉：把时间 carrier 理论化是否引入时序义务；把时序外延化是否掩盖现实时间/运动观察。

程序 TaskSpec 必须声明它处理哪一层。`delay/tick/search stage` 不自动证明芝诺式时间问题；continuous/path model 也不自动提供事件 order。

## 七、组合覆盖策略

逐轴薄路径与有理论依赖的pair保留为基础检查，同时从首遍设置结构驱动入口：共同取舍、联合前提、重要接口、参数族和整体任务可直接提出三元或更高阶问题，无需先有低层异常或文献命中。成员、成员组合和更大语义单元可递归重组，不设置固定交互阶数作为完备阈值。

多输入联合不能仅拆成pairwise边，有序过程不能压成无序集合；共享背景即使没有调用边也可形成研究对象。选择必须有类型/来源/任务依据，混合不相容配置不得进入同一组合。covering array和type-directed pruning只支持其实际包络，未选项保留原因、可能影响及重开条件。每单元结果回到父问题，结构驱动与信号驱动均有实际选择记录。OP-14反解释保留在核证阶段，不用它抢先关闭候选生成。
