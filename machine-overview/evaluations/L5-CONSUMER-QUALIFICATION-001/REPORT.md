# L5 消费者资格化：从“会检查证明”到“同层自我可靠性”的四分审计

状态：`IMPLEMENTED_AND_REPLAYED_LOCALLY / NO_QUALIFIED_CONSUMER_IN_FROZEN_SET / ERCF3_STILL_GATED / NOT_A_HOTT_BUG`

本工作单元解决 M3/L5 原案例留下的核心歧义。原案例机器核验了一个标准布尔对角边界：若同一类型 `A` 能精确表示它的全部 `A → Bool` 谓词，则把否定谓词送回该表示会产生布尔否定的不动点。这个结果没有固定对象语言、真实 proof checker、证明搜索范围、真值范围或实际系统的自我可靠性承诺，因此不能回答“HoTT 的真实消费者在哪里”。

本轮把此前混在一起的四种能力拆成四个独立 TaskSpec，并在它们之外建立 Q1–Q6 固定来源审计：

1. 检查一份已经给出的证明；
2. 在显式燃料内搜索并检查一个证明；
3. 在显式有限片段内判定真值；
4. 同一层同时拥有反射、Löb 闭包和对该反射的内部认证。

前三种能力即使全部存在，也不能自动升级成第四种。

## 1. 冻结与来源范围

- adapter/source freeze：`ADAPTER-FREEZE.json`
- freeze SHA-256：`00b7fdb2bfa6da513acf40652a5ef048cc0d99e7b9bb6df0b5b5132b25731664`
- source scope：`SCOPE.json`
- semantic decisions：`DECISIONS.json`
- audit run：`runs/20260913-L5-CONSUMER-AUDIT-001/RUN.json`
- deterministic digest：`63a533a1374c54812bc75dcfba09fe7f8a85f135cf12e3c024aeff1e2be63e03`
- 5 个固定 source system、9 份固定原件、49 个证据锚点；全部锚点回读成功。

来源集合有意覆盖一个实际 Cubical Agda host、一个最强自引用工程近邻、两种学术界内部化路径，以及本项目自己的 ERCF-3：

| source | 固定身份 | 与 HoTT 的关系 |
|---|---|---|
| Agda reflection | 官方 2.8.0 文档 | Cubical Agda 的实际 host `TC` 接口 |
| MetaRocq | 9.1 branch @ `c8cd4605…` | 非 HoTT 的强比较对象：verified checker、quotation、self-erasure |
| 2LTT | arXiv:1705.03307v5 | inner theory 明确为 HoTT，元理论在 outer theory |
| NBE in type theory | arXiv:1612.02462v4 | 用 QIIT metalanguage 内部化 normalization/definitional equality |
| local ERCF-3 | 当前固定 Agda 模块 | 已有 Fml、Hilbert derivation、修复编码与对角实例；反射仍 open |

这是一个有界 primary-source set，不是全学术界的穷尽性检索。

## 2. Q1–Q6 判据

一个“消费者命中”必须在**同一个固定接口**里同时满足：

| ID | 判据 |
|---|---|
| Q1 | 固定真实系统、版本和公开接口 |
| Q2 | 对象域实际含相关 code/proof，而非只有名称或类比 |
| Q3 | proof predicate/checker 与所声明片段的真实接受关系相连 |
| Q4 | reflection/soundness 的范围、假设和 trust base 精确 |
| Q5 | 自应用留在同一声明层，没有悄悄转交 outer theory 或 host primitive |
| Q6 | 来源真实承诺总的同层自我可靠性；不能用给定证明检查、有限搜索、局部真值或相对规范正确性替代 |

机器只验证来源字节、证据锚点、source roster、Q1–Q6 完整性和由这些判断导出的 all-pass 结果。每一格的语义判词仍是直接读源后的显式人工/AI 审查，不由关键词自动决定。

## 3. 来源判定

| source | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | 结论 |
|---|---|---|---|---|---|---|---|
| Agda reflection 2.8.0 | PASS | PASS | PASS | FAIL | PARTIAL | FAIL | `TC` 提供真实 `checkType/quoteTC/unquoteTC`，但这是 host checker primitive，不是对象层对 kernel 的自证 |
| MetaRocq 9.1 | PASS | PARTIAL | PASS | PARTIAL | PARTIAL | FAIL | 最强近邻；raw quotation/cojoin 与 self-erasure 已有，typed quotation 仍在开发，safe checker 依赖 strong-normalization postulate |
| 2LTT v5 | PASS | PARTIAL | N/A | PASS | FAIL | FAIL | 元理论能力明确由 outer theory 承担；它展示分层支付装置，而非 inner HoTT 同层自证 |
| NBE-in-TT v4 | PASS | PASS | PARTIAL | PASS | FAIL | FAIL | normalization/definitional equality 在 QIIT metalanguage 中完成；不是全真或系统自身可靠性的同层裁决 |
| local ERCF-3 | PASS | PASS | PARTIAL | FAIL | PARTIAL | FAIL | 编码和对角实例已准备；proof-predicate representability、reflection、fixed point 和真实 consumer 仍开放 |

机械判词：`NO_QUALIFIED_CONSUMER_IN_FROZEN_SET`，命中数 `0/5`。

### 最强近邻为什么重要

MetaRocq 的 Quotation 文档明确把 `cojoin : □T → □□T` 作为 public-facing construction，并说预期的 lax monoidal semicomonad 足以证明 Löb 定理。它同时明确区分：

- `□T := Ast.term` 已实现；
- 带有 typing derivation 的 `□T := { t : Ast.term & Σ ;;; [] |- t : T }` 仍在开发；
- safe checker 的 correct/complete 是相对 PCUIC specification；
- fuel-free checker 依赖 well-typed PCUIC reduction 的 strong-normalization postulate；
- `self_erasure.v` 的确把 erasure 用在 `typecheck_program` 自身上。

因此，学术界并非没有走到自应用和 Löb 门口。最强真实工程恰好把缺口公开写在 typed quotation、归一化假设和相对规范边界上。这个近邻为 HoTT 搜索提供了具体接口清单，却没有提供 Q6。

## 4. 四个机器任务

四个 grammar 都在 freeze 之后创建；每个搜索都在声明深度内完整、规则次序置换同集、关键规则移除后目标为零。四次 native run 都得到 `verify / controls / negative-control / replay = 0 / 0 / 42(expected) / 0`，且 replay 为 `EXACT_EXIT_STDOUT_STDERR_MATCH`。

| task | checks / witnesses | 最小合成项 | native 解释 |
|---|---:|---|---|
| `MS-TASK-L5-GIVEN-PROOF-CHECK-001` | 20 / 1 | `L5.checkGivenProof (L5.givenK)` | 一份已给出的 K derivation 被检查；错误地当作 bottom proof 被内核拒绝 |
| `MS-TASK-L5-BOUNDED-PROOF-SEARCH-001` | 26 / 1 | `Target.bounded L5.searchAtOne (L5.searchSoundAtOne L5.searchAtOne)` | one-fuel 搜索的执行结果与 derivation 一并交付；zero-fuel success 被拒绝 |
| `MS-TASK-L5-FINITE-TRUTH-DECISION-001` | 6 / 1 | `L5.truthDecision` | 只决定 closed `BFml`；把 false literal 当 true 被拒绝 |
| `MS-TASK-L5-LOB-SELF-CERTIFICATION-001` | 33 / 1 | `reflect ⊥ (lob ⊥ (certify ⊥))` | 条件目标把 reflection、Löb rule、internal certification 的联合后果具体化；删掉 certification 后原生负控制拒绝 |

原生目标与生成 proof/controls/falsify 都保存在各自 verify run 下。它们是 machine-overview exploration receipts，没有进入 `HoTT/CLAIM_EVIDENCE_MATRIX.md`，因此本报告不把这些条件性构造重新包装成当前项目已经登记的数学结论。

## 5. 与 ERCF-3 的关系

本轮没有填造一个虚假的 proof predicate。它把现有 ERCF-3 的剩余责任重新排成一条可核查链：

```text
Fml / derivation / repaired coding / diagonal substitution
  → proof-predicate representability
  → typed quotation or equivalent Box correspondence
  → Löb/diagonal closure with exact assumptions
  → reflection/soundness scope
  → internal certification of that reflection
  → one real fixed HoTT consumer that promises the joint package
```

本项目当前只完整拥有第一行左侧的语法、编码和对角替换基础。旧 `ProvRepresentability.agda` 提供的是表示骨架/公理模式；`ReflectionSketch.agda` 明确把 reflection 留作 named obligation。新 Löb target 说明：如果最后三项被压成同一层的联合接口，bottom 是机器可见的终点；source audit 又说明当前没有来源把这组联合接口交付给 HoTT 使用者。

所以 ERCF-3 继续是 `GATED`。本轮把门禁从“缺一个自然 consumer”细化成了可逐接口搜寻的 Q2/Q4/Q5/Q6，而没有把通用 Gödel/Löb 边界冒充 HoTT 独有现象。

## 6. 时间、时序与理论经济

这个 L5 构造讨论的是**验证责任的时序**，不是芝诺意义上的时间、时空、运动稠密性。真实系统把工作安排为：先有对象代码或证明，之后由 checker 检查；checker 的正确性由一份规范、元理论或 trust base 承担；需要更强元结论时进入 outer theory 或 metalanguage。

理论经济的危险点，是把这些阶段和层级压缩成一个看似自足的 `Box`：同一个机制既产生证明、又解释证明、又认证“这种解释可靠”。`certify ⊥ → lob ⊥ → reflect ⊥` 把这种责任回环显示为三步可见链条。它是用户所说“自馈结构”的一个精确候选形状，但只有真实 HoTT consumer 同时提供三项，才能从通用边界升级为 HoTT 的现实相对现象。

这项结果不替代时间结构线。L3 仍负责连续/非连续、Path/dimension 与运动/事件结构；L5 负责对象—元对象—验证者之间的时序和层级。二者保持分工，避免“时序”吞掉“时间”。

## 7. 本轮对机器统观效果的实际提升

机器统观现在可以机械阻止一种过去反复发生的错误：

```text
能检查一份证明
  ≠ 能找到未知证明
  ≠ 能判定一个有限片段以外的真值
  ≠ 能在同一层总地证明自身可靠
```

这比旧 L5 的一个抽象 section 反例更接近真实系统，因为它同时拥有：固定对象语法、独立 capability tasks、原生正负控制、实际系统 source matrix、最强近邻和明确的 missing conjunction。它仍未达到最终目标，因为“HoTT 自身非现实性实例”要求最后一个现实消费者桥梁；当前结果准确地告诉后续搜索应当寻找哪组接口，而不是再枚举无消费者的抽象对角式。

## 8. 下一最小可验工作

下一工作单元应是 `HOTT-QUOTATION-BRIDGE-001`：

1. 在一个固定 HoTT 变体中选定候选 `Box`（优先比较 Cubical Agda reflection 的 host `TC` 与 2LTT 的 outer layer）；
2. 给出 `quote/cojoin`、typed quotation、proof-predicate correspondence 的逐项类型；
3. 尝试原生构造或反驳 Löb 所需的闭包；
4. 单独固定 reflection 和 internal-certification 的来源，禁止把 host kernel soundness 偷渡进对象层；
5. 再跑 Q1–Q6。Q5 失败则记录分层防御；Q6 失败则记录没有消费者；只有六项同源通过才允许进入 HoTT-specific paradox candidate。

这个路径直接消费 MetaRocq 近邻和 2LTT 防御，不再重复 generic diagonal，也不要求先实现完整 Gödel 不完备性。

## 9. 证据边界

- 当前结论是固定来源集合的消费者资格审计与四个本地 machine-overview run 的事实，不是全局“没有消费者”定理。
- MetaRocq 是非 HoTT 比较系统；它的近邻价值不能直接转写成 HoTT 缺陷。
- 2LTT 与 NBE 的摘要/接口足以定位分层，但本轮没有重放它们的完整形式化。
- 所有新资产仍在独立 worktree，未提交、未合并、未 tag、未 push；主工作树未被修改。
- 第一次新增单测失败来自测试把 JSON 确定性排序误当成语义顺序；改为集合比较后通过。该失败不涉及搜索、原生证明或消费者判词。

