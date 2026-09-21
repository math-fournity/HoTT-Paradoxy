# P25：HoTTLean 的 MLTT syntax—typechecker—model 真实消费者审计

**任务：** `P25-HOTTLEAN-MLTT-SYNTAX-SEMANTICS-CORPUS-001`

**状态：** `CLOSE_WITH_SCOPE / ACTUAL_SYNTACTIC_MODEL_CONSUMER_CONFIRMED / NOT_A_SAME_LAYER_GLOBAL_SELF_VALIDATION_CONSUMER_WITHIN_FIXED_COMMIT / DEFENSE_BY_EXPLICIT_HOST_OBJECT_STRATIFICATION_AND_SCOPE / P26_INTRINSIC_QIIRT_CANDIDATE_SELECTED / NO_NEW_HOTT_DEFECT_CLAIM`

**冻结版本：** `sinhp/HoTTLean` `master` = `31133dd5b25226ea897f8aa5e2e43b61392459eb`（commit subject `feat: links to papers`，2026-02-06T10:12:47-05:00）。

## 1. P25 要解决的资格问题

P24 留下的不是“有没有一个叫 typechecker 的程序”，而是更强的问题：一个 HoTT 相关系统是否把对象理论的语法、可证明性或反射链，用作**同一对象层内、全局、健全完备的自身真理验证**。HoTTLean 是 P24 之后选出的真实工程分母，因为公开 README 已同时声明 deep MLTT syntax、认证类型检查器和模型解释。

P25 固定以下合同：

| 项 | 冻结内容 |
|---|---|
| Input | HoTTLean 的 `Expr`/`Wf*` syntax，Frontend 的 Lean→SynthLean translation，NbE typechecker，模型 interpretation 与实际 test scope。 |
| Operation | 按固定 commit 检查对象语言、宿主语言、证明对象、反射/引用、语义 soundness、理论范围与调用链。 |
| Observation | 它是否有对象层 `Prov`/proof-code/quotation/reflection 链，且是否有用户实际消费该链来声称本理论同层的全局自验证。 |
| Done | 给出该工程是强候选、明确防线还是实际强消费者的可复核判词；若不是强消费者，选择一个改变“内在化方式”的后继分母。 |
| 正控制 | 当前 commit 中确有 raw `Expr`、`WfTp`/`WfTm`、`CheckedDef`、`checkTm` 及 `ofType_ofTerm_sound`，而不是只有论文关键词。 |
| 最强反解释 | 深嵌入、host quotation 与对象层 `code` 很容易被误读为自指。P25 逐层区分它们；若实源含有可证明性/自反链，报告必须修正。 |
| 停止 | 若 source 显式把 syntax、checking 或 semantic soundness 保留给 Lean 外层，且没有对象 proof-predicate/reflection consumer，则关闭这个 commit，不从“没有命中”外推到所有 HoTT 系统。 |

## 2. 本地与版本侦察

P25 先查询当前仓库、登记的历史快照、`/Volumes/D` 的相关工作根和 Git 历史。除了 P24 自己写入的引用，没有发现已有 HoTTLean/SynthLean checkout、历史任务或既有审计；因此没有重跑先前资产。随后从公开 GitHub 克隆到临时只读工作目录，checkout 后的 `HEAD` 与 P24 的 remote pin 精确一致，工作树为空。

本报告保存用于复查的 external commit、文件 SHA-256、精确检索分母和临时 checkout 身份；它不把第三方源码复制进当前 repo，也不把 `lake build` 当作本问题的必要条件。P25 是调用链和层级审计，当前版本的源文件直接决定该判断；完整构建会增加环境/依赖事实，却不会把 host-level `Lean.MetaM` 变成 object-level reflection。

## 3. 实际链路：它有何种能力

P25 确认 HoTTLean 是一个实际的 **syntax—checker—model consumer**：

1. `HoTTLean/Syntax/Basic.lean` 定义外部 Lean inductive `Expr`；`Syntax/Typing.lean` 以 Lean `Prop` 值的 `WfCtx`、`WfTp`、`WfTm`、`EqTp`、`EqTm` 指定判断。
2. `Frontend/Translation.lean` 的 `translateAsTp`/`translateAsTm` 在 Lean `MetaM` 中将 Lean expressions 转为 `Q(Expr Lean.Name)`；`Frontend/Commands.lean` 使用这些 host 操作创建 `CheckedAx` 和 `CheckedDef`，后者携带 Lean 中的 `wf_val : ... WfTm ...` 证明。
3. `Typechecker/Synth.lean` 的 `checkTp`、`checkTm`、`synthTm` 是 Lean `MetaM` 中的 `partial def`，并以 quotation 生成 Lean proof terms。它们是认证检查器的真实实现，而不是论文中的假想组件。
4. `Model/Unstructured/Interpretation.lean` 的 `ofType_ofTerm_sound` 是 Lean 中关于 `Interpretation` 与 `Axioms` 的 soundness 定理；它把对象判断解释到外部模型语义。

所以 P25 的正控制成立：HoTTLean 确实把 syntactic construction、checking 和 model reasoning 连通了。CPP 2026 论文也明确把 SynthLean 定位为嵌入 Lean 的 MLTT DSL，并将“内部构造”和“外部模型”组合为双向工作流；论文的 soundness 是关于该解释的宿主证明。[论文](https://voidma.in/assets/papers/2026nawrocki_certifying_proof_assistant_synthetic_mathematics_lean.pdf)

## 4. 为什么它不是 P24 所需的同层自验证消费者

关键不是“有没有 `code` 这个名字”，而是它编码什么、谁构造证明、谁证明 semantic soundness。

| P24 所需桥 | HoTTLean 固定源的对应物 | 判定 |
|---|---|---|
| 对象语法 | `Expr` 是 **Lean 中**的 inductive data type。 | `PRESENT_OUTSIDE_OBJECT_MLTT` |
| 对象判断/局部检查 | `Wf*` 是 Lean `Prop` relations；`checkTp`/`checkTm`/`synthTm` 在 Lean `MetaM` 中。 | `ACTUAL_HOST_CERTIFICATION` |
| 对象自身 quotation | `Expr.code`/`Expr.el` 的注释是“type code”与“type from a code”，即 Tarski universe 的类型编码；Frontend 中的 Qq quotation 是 Lean host quotation。 | `NOT_OBJECT_SYNTAX_QUOTATION` |
| proof predicate / proof-code | 对 `HoTTLean/`、`test/` 与 README 的固定 literal denominator 搜索 `godel`, `provability`, `provable`, `reflection`, `self-reference`, `proof predicate`；未得到相应声明路径。 | `NO_NAMED_P24_PROOF_PREDICATE_WITHIN_LITERAL_DENOMINATOR` |
| semantic soundness | `ofType_ofTerm_sound` 在 Lean 外层，假设 `Interpretation`/`Axioms` 等对象。 | `MODEL_SOUNDNESS_IN_HOST_NOT_OBJECT_SELF_TRUTH` |
| 完整 HoTT 范围 | README 明说当前仅有 Π、Σ、Id、base constants；尚不支持 higher inductive types，模型构造也尚未完成。`test/hott0.lean` 只给 h-set 级 univalence axiom。 | `LIMITED_MLTT_HOTT0_SCOPE` |
| 全局总性 | typechecker/NbE 源码使用 `partial def`；P25 没有运行或证明任何特定不终止，也没有发现“全局总停机”宣称。 | `TOTALITY_NOT_CLAIMED_OR_AUDITED` |

这不是对 HoTTLean 的贬损。它正好展示了一个成熟的分层方案：Lean 负责语法表示、metaprogramming、proof-term certification 和模型 theorem；嵌入的 MLTT 是被检查、被解释的对象理论。该架构避免将“宿主可验证对象理论的片段”误说成“对象理论已在同层验证其全部真理”。

论文还清楚记录了范围选择：其 raw theories 不支持任意方程，原因是这会妨碍复用 Lean elaborator 的可判定 typechecking；其 universe hierarchy 也是有限的，并明确讨论 Gödelian restrictions。这些是明示的工程和元理论边界，不能自动变成 HoTT 缺陷或现实失配。[CPP 论文 §2](https://voidma.in/assets/papers/2026nawrocki_certifying_proof_assistant_synthetic_mathematics_lean.pdf)

## 5. 判词、价值与不延续理由

```text
CLOSE_WITH_SCOPE
/ ACTUAL_SYNTACTIC_MODEL_CONSUMER_CONFIRMED
/ NOT_A_SAME_LAYER_GLOBAL_SELF_VALIDATION_CONSUMER_WITHIN_FIXED_COMMIT
/ DEFENSE_BY_EXPLICIT_HOST_OBJECT_STRATIFICATION_AND_SCOPE
/ P26_INTRINSIC_QIIRT_CANDIDATE_SELECTED
/ NO_NEW_HOTT_DEFECT_CLAIM
```

P25 位于 P2/ERCF3 的“规则—对象理论—消费者”连接段。它比 P24 的局部 Agda 脉冲更接近实际系统，因为有用户可用的 syntax/checker/model 链；但它没有满足 S3–S6 的强反射合同。其价值不是又一次无命中，而是将“缺 consumer”精确改写为：**已有一个真实 consumer，但它以可见的 host/object 分层避免了强同层断言。**

继续同一 HoTTLean commit 没有判别价值：S1、host checking、model soundness、范围与 no-proof-predicate search 都已固定。下一次对同一文件树增加关键词或重跑 build，只会重复 source-level 控制。P26 改变了内在化机制：Cubical Agda 中以 native QIIT/QIIRT 建立 type theory 的 intrinsic syntax；它将测试“对象语法是否真的在同类类型论中表达”而不把这一事实自动当作全局自身真理验证。

## 6. P26 候选卡：native QIIT/QIIRT 的内在 type theory

| 字段 | 冻结内容 |
|---|---|
| Candidate | `P26-TTASQIIRT-INTRINSIC-TYPE-THEORY-CORPUS-001` |
| Public source | CPP 2026 论文 [Can We Formalise Type Theory Intrinsically without Any Compromise?](https://fredriknf.com/papers/tt-qiirt_cpp2026.pdf)，Zenodo artifact [v1](https://zenodo.org/records/17802827)，源代码 `https://github.com/L-TChen/TTasQIIRT.git`，P25 观测 `master`/`HEAD` = `8db08306287333067b2749f95f8ad3ba7a0e14d1`。 |
| Input | Cubical Agda native QIIT/QIIRT intrinsic syntax、standard model、NbE、strictification 与论文明确的 metatheory limitations。 |
| Operation | 固定 commit 后核对 type theory syntax 在何层定义、是否存在 proof predicate/quotation/reflection/global self-soundness consumer，以及 QIIT、transport、strictness、universe 假设如何被承认。 |
| Observation/Done | 判断它是否完成 P24 的 object-layer bridge，或只是完成 intrinsic syntax/metatheory 的较弱阶段；保留 full HoTT、actual K 与现实同任务桥的独立义务。 |
| 正控制 | 论文与 Zenodo 均明确 native QIIT、intrinsic representation、standard model 和 NbE；不是凭语义相似性挑选。 |
| 最强反解释 | 它可能比 HoTTLean 更“内在”，却仍不主张全局 self-verification；P26 必须从源码而不是 abstract 判定。 |
| 停止 | 若该 commit 没有 P24 的 proof-predicate/reflection/global consumer，则以 `INTRINSIC_SYNTAX_NOT_GLOBAL_SELF_VALIDATION` 关闭分母，并生成新的 successor，不声称所有 HoTT 内部化工程都相同。 |

## 7. 反思（Goal 3 §§3–3.2）

1. **新增可定位事实：** 固定 HoTTLean commit 的 actual syntax/checker/model call-chain、host/object boundary、type-code/quotation distinction 和 finite-scope boundary。
2. **判词变化：** P24 的候选从“待查”变成“真实但分层的 consumer”；强 self-verification consumer 仍未在该 commit 建立。
3. **任务忠实性：** P25 未将 `Expr.code`、Lean quotation 或 `ofType_ofTerm_sound` 混作对象证明谓词；Input/Operation/Observation/Done 均在 §1 冻结。
4. **控制：** Deep embedding、certifying checker 和 soundness 是正控制；明确 host `MetaM`、object `Expr` 和 scope 是最强反解释的核查结果。
5. **反重复：** 当前仓库和 `/Volumes/D` 中没有先存 HoTTLean asset；P24 只做 README-level candidate selection，P25 第一次检查 exact code paths。
6. **波次裁决：** P2/ERCF3 保持有效，P3/P4 停放不变；P26 获得资格，因为它改用 native intrinsic QIIRT 机制。
7. **为什么停止：** 固定 commit 的 source contract 已足以否定“same-layer global self-validation”归类；继续同一分母没有新增构造、观察或完成条件。P26 是已命名、版本可冻结的 successor，故 active Goal 继续而本分母关闭。

## 8. 证据与限制

- P25 是固定外部 source tree 的静态/调用链审计；没有构建 HoTTLean，也没有声称其 README、论文或 source 已在本 repo 的 Lean 环境重放。
- P25 的 literal search 不能证明整个工程或未来版本绝无任何相关反射结构；它只支持 `NO_NAMED...WITHIN_LITERAL_DENOMINATOR`。
- `partial def` 的出现只说明 P25 未获得总性证明/运行证据，不能被读成一次实际的不终止或理论错误。
- 既没有找到，也没有构造原圆环的 H/R/K 失配；P25 不改变 ABX 的 `NO_NEW_HOTT_DEFECT_CLAIM` 边界。

## 9. 可复核入口

- 固定 external source identities 和文件哈希：[`P25-HOTTLEAN-SOURCE-FREEZE.json`](P25-HOTTLEAN-SOURCE-FREEZE.json)。
- 本地审计记录的结构/哈希验证：[`verify_p25_hottlean_mltt_syntax_semantics_corpus.py`](verify_p25_hottlean_mltt_syntax_semantics_corpus.py)。
- 一手公开资料：[HoTTLean README at the frozen commit](https://github.com/sinhp/HoTTLean/blob/31133dd5b25226ea897f8aa5e2e43b61392459eb/README.md)，[CPP 2026 SynthLean 论文](https://voidma.in/assets/papers/2026nawrocki_certifying_proof_assistant_synthetic_mathematics_lean.pdf)，[P26 的 CPP 2026 QIIRT 论文](https://fredriknf.com/papers/tt-qiirt_cpp2026.pdf)，[P26 Zenodo artifact](https://zenodo.org/records/17802827)。
