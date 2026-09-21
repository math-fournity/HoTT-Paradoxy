# P27：对象反射／quotation 消费者的异类发现

**任务：** `P27-REFLECTION-CONSUMER-DISCOVERY-2026-001`

**状态：** `SUCCESSOR_SELECTED / CFTT_STAGED_QUOTATION_SPLICE_AND_UNSTAGING_CONSUMER_CANDIDATE / LOCAL_DISCOVERY_UNREVIEWED_ASSET_UPGRADED_TO_VERSION_PINNED_CANDIDATE / P28_NOT_STARTED / NO_NEW_HOTT_DEFECT_CLAIM`

## 1. 为什么需要新分母

P24、P25、P26 依次审计了三种不同情况：局部 Agda proof-predicate 脉冲、Lean-hosted MLTT syntax/model、Cubical Agda native intrinsic syntax。它们都没有给出对象可证明性—reflection—global self-validation 的完整实际消费者。继续在任何一个已冻结版本中搜索同义关键词不会改变最终链。

P27 因此把检索目标改为 **实际 quotation/splicing/evaluation 的消费者**，同时要求它有版本固定的源码或 artifact。这里的“reflection”仍须分层：对象 code、host metaprogramming、two-level staging、proof predicate 与自身真理验证并不相同。

## 2. 公开与本地侦察结果

### 本地历史资产

项目的 2026-09-14 文献分母已经登记 DOI `10.1145/3674648`：*Closure-Free Functional Programming in a Two-Level Type Theory*，candidate key `doi:10.1145/3674648`，状态为 `DISCOVERY_UNREVIEWED`，triage reason 仅为 `hott:two-level type theory`。这不是既有完整审计或可复用结论；它避免了把 P28 错写成从零发现。

### 新的公开来源核验

ICFP 2024 论文说明 CFTT 将一阶 object theory 与依赖型 meta theory 分开，并且有 Agda code supplement；它的 unstaging 是对 particular presheaf model 中 syntax 的 evaluation，论文讨论 quotation/splicing、generativity，以及 object operations 在 Agda embedding 中以 postulated operations 表示。[论文](https://andraskovacs.github.io/pdfs/2ltt_icfp24.pdf)，[ACM 页面](https://doi.org/10.1145/3674648)。作者维护的 [`AndrasKovacs/staged`](https://github.com/AndrasKovacs/staged) README 也明确标为 ICFP 2024 code supplement。

它原本在 P27 的“2025–2026”启发性时间窗之外（2024），但以**已登记而未审的本地 asset**重新进入。这个 out-of-envelope admission 有具体理由：它具备 P24–P26 都没有的 actual quote/splice/unstaging operation 与可进入源码的 code supplement。它不改变四分支顺序或任何旧判词，只改变本次 successor 的 source denominator。

## 3. P28 候选卡

| 字段 | 冻结内容 |
|---|---|
| Candidate | `P28-CFTT-STAGED-QUOTATION-SPLICE-UNSTAGING-CORPUS-001` |
| Source | `https://github.com/AndrasKovacs/staged.git`，P27 观测 `main`/`HEAD` = `9c4e2017669086e2f77df5014f1c215a5a7e07a3`；ICFP 2024 DOI `10.1145/3674648`。 |
| Input | CFTT 的 object/meta stages、quotation/splicing、unstaging semantics、Agda code supplement 与其 generativity boundary。 |
| Operation | 固定 source tree 后追踪 quote/splice/unstage 的具体定义、object-code representation、postulates、host reflection、运行/模型路径与实际 consumer。 |
| Observation | 是否把 object code 当作可任意 introspect 的自身证明对象；是否有 object provability predicate/reflection/global self-soundness，或是否明确维持分层/generativity。 |
| Done | 产生版本固定的 P28 consumer audit；若 CFTT 只体现分层 staging，记录为 defense/boundary，并选择下一个不同 consumer。 |
| 正控制 | CFTT 有明确 quote/splice/evaluation operation 与 Agda supplement，而非泛泛的元理论论文。 |
| 最强反解释 | 它是 2LTT/staging 而不等于 HoTT；如果操作全部留在 meta level，不能称为 HoTT 自身自验证。 |
| 停止 | 不将 quote/splice 的存在升级为 P24 S3–S6；固定源码未出现该链即结束分母。 |

## 4. 波次价值与反思

P27 是 P2/ERCF3 的 **successor discovery**，不是又一轮结论性扫描。它的最终价值在于补上前面三种审计未覆盖的 operation axis：实际 staged quotation、splicing 和 unstaging。无论 P28 的结果是“明确层级防线”还是发现某个新的 object consumer，都会改变我们对“理论是否把静态语法当成过程性强完成”的证据结构。

1. **新增事实：** 本地 `DISCOVERY_UNREVIEWED` CFTT 条目、论文的实际 operations、source supplement URL 和 remote commit 已定位。
2. **判词影响：** P26 的 `CLOSE_WITH_SCOPE` 保留；P27 不声称已有同层 self-validation。
3. **任务忠实性：** P28 将固定 Input/Operation/Observation/Done，特别分开 staged code 和 proof predicate。
4. **重复控制：** P24 Coquand BRA、P25 HoTTLean、P26 TTasQIIRT、已审 P3 consumers 均明确排除；CFTT 是现有但未审的近题资产。
5. **继续裁决：** `SWITCH_BRANCH` 到 P28；它的 source、操作和观察量均不同于前述分母。
6. **不延续的条件：** 若 P28 只重现元层—对象层分离，不再围绕同一 CFTT 增加关键词；改为另一个不同的 consumer/source 分母。

## 5. 证据边界

P27 只做选择和固定。它没有 clone、构建或审读 CFTT code supplement；也没有把该论文的 staged semantics 当作 HoTT 的内在 reflection、原圆环 K、现实任务失配或缺陷证据。

## 6. 可复核入口

- 机器可核的本地/公开定位：[`P27-REFLECTION-CONSUMER-SOURCE-FREEZE.json`](P27-REFLECTION-CONSUMER-SOURCE-FREEZE.json)。
- 选择验证器：[`verify_p27_reflection_consumer_discovery.py`](verify_p27_reflection_consumer_discovery.py)。
