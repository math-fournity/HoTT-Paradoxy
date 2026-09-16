# HoTT 不可停机悖论机器统观的完备性审计

> Evaluation：`NONTERMINATION-OVERVIEW-COMPLETENESS-AUDIT-001`  
> 审计日期：2026-09-14  
> 审计对象：`machine-overview/` 当前工作树实现与不可停机—不完备性路线图  
> 总判词：`ARCHITECTURALLY_COMPLETE_RESEARCH_PROTOCOL / RELATIVELY_COMPLETE_IN_FROZEN_FINITE_SLICES / GLOBAL_DISCOVERY_COMPLETENESS_NOT_ESTABLISHED / EXACT_HOTT_AND_REALITY_BRIDGES_OPEN`  
> Git 状态：`LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED`

## 1. 问题不能只用一个“完备/不完备”回答

“机器统观是否完备”至少包含六个不同量词。若不先拆开，有限文法中的穷举、研究流程的完整、HoTT 理论空间的覆盖和对所有悖论的决定能力会被混为一谈。

| 层级 | 精确问题 | 当前结论 |
|---|---|---|
| `COMP-1` 流程结构完备性 | 一个候选是否经历来源资格化、规格冻结、生成、执行、缩减、形式核验、对应审查、重放和索引？ | `ACHIEVED_FOR_STRICT_V2_CASE_CHAIN` |
| `COMP-2` 冻结文法枚举完备性 | 对某个固定 TaskSpec、固定有限/有界文法，生成器是否遍历文法声明的全部良类型候选？ | `MACHINE_PROVED_FOR_PF-CUBICAL-CANDIDATE-COVERAGE-001; OPERATIONALLY_ACHIEVED_FOR_REGISTERED_COMPLETE_RUNS` |
| `COMP-3` 冻结资料分母完备性 | 对一个预先固定的源码/论文集合，是否逐项检查了声明的观察维度？ | `ACHIEVED_ONLY_FOR_NAMED_DENOMINATORS` |
| `COMP-4` 候选类归约完备性 | 每个相关 HoTT 非现实性候选是否都能保持任务、观察量和现实对应地归约到当前文法中的某个代表？ | `NOT_ESTABLISHED` |
| `COMP-5` HoTT 专属机制链完备性 | 是否已从某个精确 HoTT 规则，经对象语言编码、不可完成定理和自然消费者，一直连接到现实任务差异？ | `NOT_ESTABLISHED` |
| `COMP-6` 全局发现/否定完备性 | 机器是否总能找到任意存在的 HoTT 悖论，或在不存在时停机并给出否定证书？ | `NOT_ESTABLISHED_AND_NOT_A_REALISTIC_TOTAL_ALGORITHM_TARGET` |

因此，当前系统可以称为**研究协议在结构上的完整实现，并在若干冻结有限切片内具有相对枚举完备性**。它不能称为“对 HoTT 全理论空间已经完备”，也不能因一次搜索没有命中就推出 HoTT 没有非现实性悖论。

## 2. 哪些意义下已经完备，以及为什么

### 2.1 一条候选的证据生命周期已经闭合

严格 v2 链已经把以下阶段连成同一条可重放路径：

```text
来源与工具链资格化
  → TaskSpec / grammar / profile 冻结
  → 文法内良类型候选枚举
  → 任务保持缩减
  → 原生 Cubical Agda 核验与正负控制
  → 逐字节重放
  → 现实对应分类
  → 报告与可重建索引
```

这是一种**流程结构完备性**：一个结果不能只凭超时、AI 叙述、单次编译或孤立证明进入结论层。`selftest` 当前 94/94，`validate` 报告 16 个 case revisions、39 个 runs、18 个 correspondence reviews 和 0 errors。这里的“完整”只量化这条证据生命周期，不量化整个 HoTT 的所有可能项和解释。

### 2.2 声明文法内的搜索可以给出真正的相对完备性

若一个 case 同时固定：

1. 构造子集合；
2. 类型规则；
3. 深度、大小或参数的有限界；
4. 候选等价/规范化规则；
5. TaskSpec 的消费者、输入和观察量；

则生成器可以机械遍历该域内全部良类型候选，并用独立顺序扰动、候选集合哈希和消融复核结果。L1 校准就是这种意义的实例：7 个 delay 原子、399 个良类型上下文、4,788 次 pair-context 检查、916 个分离，缩减为 50 个不同见证；打乱枚举顺序不改变见证集合，移除 `deadline` 构造后对应族消失。

这里的完备性是一个带分母的命题：

```text
∀ c ∈ Candidates(TaskSpec, Grammar, Bound), search visits c.
```

它不是：

```text
∀ c ∈ all possible HoTT terms, interpretations and real-world correspondences,
search decides whether c is a paradox.
```

`PF-CUBICAL-CANDIDATE-COVERAGE-001` 已把这一层第一次提升为当前 repo 的机器定理。对每个 `n`，它定义精确的 `Raw n` 文法：`never`、`now false`、`now true` 和最多 `n` 层的 `laterR`。Cubical Agda 证明：

```text
(r : Raw n) → r ∈ allRaw n
```

同一包还证明 `normalize : Raw n → Delay Bool` 保持 convergence 与每个 deadline observation，`reduceCandidate` 保持 horizon、expected observation 与实际 observation，并且每个 reduced candidate 都出现在 `canonicalSpace`。因此这里不仅有 Python 枚举计数，也有“枚举覆盖 + 任务保持归约”的内核证书。

这个包仍只是 `COMP-2` 的一个小型 witness。它的 consumer 固定为 deadline，文法不含任意 dependent term、HIT eliminator、proof search 或现实语义；它没有证明全体目标候选类到该文法的 `COMP-4` 归约。

### 2.3 不可停机线已经覆盖了从观察到定理的主要证据等级

当前路线把容易混淆的层级分开，并已经为其中多层建立实例：

| 层级 | 已有实例 | 当前证据 |
|---|---|---|
| 有限观察窗内未完成 | Agda reflection/termination probes；Coq-HoTT typeclass search probes | 原始运行、控制、重放；不外推为数学发散 |
| 固定程序的数学发散 | `PF-CUBICAL-MACHINE-HALTING-001` | 对一个固定循环程序证明任意有限步仍运行，并推出不存在有限停机见证 |
| 可枚举 proof/refutation 部分分类 | `PF-CUBICAL-GODEL-PROOF-SEARCH-CLASSIFIER-001` | 自然数证明码逐阶段检查；成功与正/反证明双向对应；允许永不返回 |
| 对角构造出的分类器发散 | `PF-CUBICAL-SYNTHETIC-INCOMPLETENESS-001` | 在显式 `Universal θ` 下，对任一 self-return separator 构造发散 index |
| 条件性独立句/本质不完备 | 同一 Cubical 包；作者 Coq 实现 | 在有效分类器、strong separation、extension 等精确前提下得到 independent sentence |
| Robinson `Q` 算术实例 | 作者 Coq 源 `cd7d849…` | 两次干净原生构建与关键定理资格化通过；仍显式依赖 Peirce、CTQ、包含 `Qeq`、可枚举性和一致性 |
| 精确 HoTT calculus 实例 | 无 | `OPEN` |
| 现实相对非现实性实例 | 无 | `OPEN` |

这说明系统的证据阶梯已经完整到足以阻止“某进程没有及时返回，所以 HoTT 有悖论”这类越级推断。它也准确定位了尚未完成的数学节点，而不只是列出更多工具。

### 2.4 六条研究线已有可执行薄路径

M3 已让 L1–L6 每条主线至少具有 TaskSpec、搜索、原生核验、控制、重放、对应审查和报告。它提供的是**研究活动覆盖**：主要假说不再只有文字标题。L2/L4/L6 仍多为校准或已知机制，M2 的一般高阶合成、M4 的独立留出评估和 M5 的主线状态投影仍未完成，因此“横向路径已贯通”不能改写为“每条路径都已充分探索”。

## 3. 为什么不存在一个诚实的全局总判定式完备性

本研究把通用程序、证明枚举和自指引入候选空间后，搜索对象已经能够表达一般部分计算。Turing 停机不可判定、Rice 型语义性质不可判定和 Gödel 型不完备性的学术结果共同限制了这样一个目标：要求一个总会停机的算法，对每个任意程序化 HoTT 候选都判断其是否最终完成、是否具有某个非平凡语义性质、是否存在独立命题，并在“没有候选”时给出全局否定证书。

这不是当前实现偶然缺少算力，而是方案必须尊重的元理论边界。当前 repo 尚未把这一整段限制重新形式化为“机器统观自身的不可能性定理”，所以本段身份是 `SOURCE_GROUNDED_DESIGN_CONSTRAINT`，来源由路线图中的 Turing、Rice、Kirst–Peters 和已原生重放的作者 Coq 实现承担；它不冒充本项目新增的机器定理。

正确的机器目标因此应当是：

- 对有限或有界语法切片给出穷举证书；
- 对无限可枚举空间使用公平交错搜索，使每个有限编码候选最终得到有限计算配额；
- 对“停机”保存有限见证；
- 对“发散”要求归纳不变量、共归纳证明、不可分离性或经机器核验的归约，不能只靠 timeout；
- 对仍无证书的候选保持 `UNRESOLVED`；
- 对全局否定只在已有覆盖/归约定理限定的类中作出。

这是一种**证书完备、过程公平、结论有界**的研究系统，而不是一个假定能绕过不可判定性的万能裁决器。

## 4. 当前最关键的缺口不是“再跑更多程序”

### 4.1 缺少候选规范形/归约覆盖定理

目前每个 grammar 的完整枚举只能证明该 grammar 内的结果。要把它提升到一个有数学意义的候选类，需要固定候选类 `P`、当前文法代表类 `G` 与归约 `R : P → G`，并证明：

1. `R` 对每个 `P` 中候选都有定义；
2. `R` 保持良类型性与使用的 HoTT calculus；
3. `R` 保持同一任务、同一输入、同一消费者和同一观察量；
4. `R` 保持或反映所研究的完成性断裂；
5. `R` 保持现实对应所需信息，而不是在缩减时把现实任务删除；
6. `G` 的枚举器在声明界内无遗漏。

没有这组定理，机器只能说“在这个声明空间中完整搜索过”，不能说“所有相关候选都已经被代表”。

### 4.2 缺少精确 HoTT 对象理论实例

当前 Cubical Gödel 基础设施已有公式/证明编码、总 proof checker、证明枚举和抽象 incompleteness core；作者 Coq 源又展示了如何通过 Robinson `Q`、`Σ₁` completeness、μ-recursive computation 与 strong separation 完成算术实例。仍须为一个固定 HoTT calculus 建立：

1. 有限 syntax 与 judgment/proof code；
2. substitution、typing 和 conversion 的机器化关系；
3. proof relation 的可枚举性；
4. 一个可解释 Robinson `Q` 或等强算术片段的内部/外部表示；
5. exact strong separation/representability；
6. 一致性前提、模型或相对一致性假设的准确位置；
7. inner HoTT、outer 2LTT、MetaRocq/Agda meta layer 与外部 kernel 的层级划分。

完成这些义务后，才能得到“这个精确 HoTT calculus 受到某个 Gödel 型边界约束”。即使如此，该结果首先仍是一般有效形式系统边界；还要回答 HoTT 的哪一项抽象使现实任务发生了新增完成义务。

### 4.3 缺少现实对应的保真映射

用户所说的“非现实性”比一般不完备性多一个关系命题。至少要给出：

```text
现实过程 W
理论表示 T(W)
同一输入 I
同一可观察量 O
现实完成条件 Cw
理论完成条件 Ct
抽象步骤 A 对 Cw/Ct 的影响
```

只有证明 `A` 恢复、预先保留或新增了何种完成义务，并排除纯实现策略、纯资源成本和任意错误配置，才达到现实相对候选。当前 correspondence review 已强制提问这些项目，但它是结构化审查器，不是现实语义定理证明器。

## 5. 怎样把“相对完备”进一步变成可证明主张

下一阶段应为一个足够小但真正含 HoTT 结构的 calculus 冻结 `CompletenessEnvelope`：

| 要素 | 必须固定或证明的内容 |
|---|---|
| `Calculus` | universe、Π/Σ、identity/path、univalence/HIT/截断及计算规则的精确子集 |
| `CandidateClass` | 所研究的方向 A/B/Gödel 候选之语法与语义边界 |
| `Observation` | 归约、证明检查、证明搜索、对象运行或现实事件的哪一层完成性 |
| `Enumerator` | 有界穷举或无限公平枚举；覆盖、无重复/等价处理与终止性质 |
| `Reducer` | 候选到机器 grammar 的规范形映射及性质保持定理 |
| `Verifier` | 核验器相对于 calculus 的 soundness；若声称 rejection 完备，还要 completeness |
| `DivergenceOracle` | 只接受不变量、共归纳证明、不可分离性或归约证书；timeout 只是观察材料 |
| `RealityMap` | 同任务、输入、观察量和完成标准的可审计对应 |
| `Denominator` | 源码、论文、版本、排除项与变更策略 |
| `Holdout` | 由独立来源给出的任务/consumer，用来测量设计者过拟合 |

若上述 envelope 有机器证明，并且存在 `P → G` 的覆盖归约，那么可以诚实声明：

> 对这个精确 calculus、CandidateClass、Observation、现实对应规则与资源界，系统的候选覆盖和结论证书是相对完备的。

该句仍不会升级为“对所有 HoTT、所有未来扩展和所有现实解释完备”。

## 6. 当前判决

1. **方案作为系统化研究方法，已经接近结构完备，且第一条完整链路真实运行。** 它覆盖来源、候选、执行、形式证明、因果缩减、现实对应、文献校准、重放和证据生命周期。
2. **部分结果具有严格的相对完备性。** `PF-CUBICAL-CANDIDATE-COVERAGE-001` 已为一个固定 deadline TaskSpec 证明 bounded grammar enumeration、normalization semantics 与 reduced-space coverage；量词仍必须写成“固定 TaskSpec + 固定 grammar + 固定 bound/denominator 之内”。
3. **基于不可停机代码的全局 HoTT 悖论查找尚不完备。** R1 固定程序发散已完成；通用机器/不可判定归约 R2、精确 HoTT calculus、strong representability、候选归约覆盖和现实桥梁仍是开放义务。
4. **“总能找到，找不到就证明不存在”的全局算法不是应追求的验收标准。** 合理标准是公平枚举、证书驱动、对声明切片的覆盖证明，以及对 unresolved 的忠实保留。
5. **所以，当前最有价值的深化不是增加一次超时，而是证明一个候选类到搜索文法的保真归约，并把作者 Coq 的算术实例义务移植到一个精确 HoTT/2LTT 对象理论。**

## 7. 可复核证据

```bash
python3 machine-overview/mo.py selftest
python3 machine-overview/mo.py validate

python3 machine-overview/coq_synthetic_incompleteness.py verify \
  --receipt machine-overview/evaluations/COQ-SYNTHETIC-INCOMPLETENESS-REPLAY-001/BUILD-RECEIPT.json \
  --rerun-qualification

python3 -m unittest machine-overview/tests/test_cubical_godel_infrastructure.py
python3 -m unittest machine-overview/tests/test_coq_synthetic_incompleteness.py
```

本次实际结果：`selftest` 94/94；`validate` VALID、0 errors；Cubical candidate coverage 专项 4/4；Cubical Gödel/incompleteness 专项 6/6；作者 Coq replay 专项 4/4；Coq verifier 为 `COQ_SYNTHETIC_INCOMPLETENESS_REPLAY_VALID`，资格化重放为 `EXACT_EXIT_STDOUT_STDERR_MATCH`。九个当前 Cubical formal-package receipts 均通过；新 coverage 包为 `EXACT_INDEX_SNAPSHOT_MATCH` 和 `EXACT_EXIT_STDOUT_STDERR_MATCH`。
