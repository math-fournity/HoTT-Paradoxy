# P28：CFTT staged quotation、splicing 与 unstaging 的实际源码审计

**任务：** `P28-CFTT-STAGED-QUOTATION-SPLICE-UNSTAGING-CORPUS-001`

**状态：** `CLOSE_WITH_SCOPE / ACTUAL_STAGED_QUOTATION_SPLICE_UNSTAGING_CONTRACT_SOURCE_REVIEWED / AGDA_SUPPLEMENT_OBJECT_THEORY_POSTULATED_HOAS / GENERATIVITY_AXIOM_TRUSTME_BOUNDARY / NOT_OBJECT_PROVABILITY_OR_HOTT_SELF_VALIDATION / P29_CLIMBER_OBJECT_PROVABILITY_CANDIDATE_SELECTED / NO_NEW_HOTT_DEFECT_CLAIM`

**冻结版本：** `AndrasKovacs/staged` `main` = `9c4e2017669086e2f77df5014f1c215a5a7e07a3`（2026-02-01T17:46:43+01:00）。

## 1. 冻结问题

P28 检查的是目前最接近“实际 quotation/splicing/evaluation consumer”的 CFTT code supplement。问题不是 CFTT 能否生成 object code，而是：这种实际 staged operation 是否把 object code 提升成可由自身任意检视、证明其整体正确性或验证自身真理的对象；若没有，它在哪一层明确保留了边界。

| 项 | 冻结内容 |
|---|---|
| Input | ICFP 2024 CFTT paper、Agda `agda-cftt` supplement、postulated HOAS Object interface、Gen/SOP/Examples modules。 |
| Operation | 检查 object/meta representation、quote/splice/unstaging 概念、generativity、host trust primitives、proof-predicate/reflection literal denominator。 |
| Observation | object theory究竟是 concrete syntax、HOAS interface 还是 postulated operations；是否有 `Prov`/proof-code/对象 reflection/global self-soundness consumer。 |
| Done | 为固定 supplement 给出层级和信任边界，并选择一个真正含 object-level `prov` 的不同 source candidate。 |
| 正控制 | 论文有明确 quote/splice/unstaging 语义与 soundness/stability 定义；supplement 有相应 Gen/HOAS implementation。 |
| 最强反解释 | quote/splice 表面可像自指；CFTT的 Agda implementation可能保留对象 code 的结构，必须从 Object/README/SOP 源码核对。 |
| 停止 | 若 object theory本身仅为 postulated HOAS，或 generativity 阻止对象结构检视，则不再把 CFTT 当成 P24 S3–S6 consumer。 |

## 2. 实际源码与论文的对应

论文规定 CFTT 的 object level 是一阶类型理论，meta level 是依赖类型论；quote/splice 用于 staging，unstaging 是在指定 presheaf model 中对 syntax 求值。它还说明 Agda implementation 以“faithful”但**postulated** object-theory operations 进行 embedding，能观察 staging 输出，却不能编译或运行 object programs。[ICFP 2024 论文](https://andraskovacs.github.io/pdfs/2ltt_icfp24.pdf)

固定 supplement 与论文一致：

- `supplement/README.md` 说 `agda-cftt` 将 object language 作为 postulated HOAS embedding；`README.agda` 进一步说明它用 meta-level functions 表示 object binding，是 quote/splice syntax/semantics 的替代嵌入。
- `Object.agda` 从 `Ty`、`↑`、`VTy`、`CTy` 开始用 `postulate` 声明 object interface，随后把 `Let`、`LetRec`、object functions/data/monad transformers同样作为 postulates。
- `Gen.agda` 实现生成 monad 的 combinators，但它操作的是这个上层 `↑` 接口，而不是内在编码的 proof calculus。
- `SOP.agda` 的 generativity 是一个“object terms cannot be inspected”的明确合同；在 Agda supplement 内由 `primTrustMe` 实现。论文也公开说明使用该 builtin 以在 Agda 中擦除该公理。

所以 CFTT 的实际价值不是自我验证，而是一个精确的反向控制：**它允许 staged code construction 与 unstaging，同时明示限制任意 object-term introspection。**

## 3. P24 桥逐项判断

| 所需桥 | CFTT fixed supplement | 判定 |
|---|---|---|
| object code / operation | `↑ A` object-interface、`Let`/`LetRec`、`Gen` 与 paper的 quote/splice/unstaging。 | `ACTUAL_STAGED_OBJECT_OPERATION_CONTRACT` |
| 内在 object syntax | Agda supplement明确采用 HOAS，并将 object language operations postulate。 | `POSTULATED_HOAS_NOT_INTRINSIC_OBJECT_SYNTAX` |
| 结构 inspection | generativity 断言相应 object-term dependent consumer恒定；论文说明 generativity 与 inspecting quoted expressions 不相容。 | `EXPLICIT_ANTI_INTROSPECTION_BOUNDARY` |
| proof predicate / quotation of proofs | 固定 `agda-cftt` 与 `agda-opsem` literal denominator未出现 `godel`, `provability`, `provable`, `proof predicate` 或 `self-reference` 声明。 | `NO_NAMED_OBJECT_PROVABILITY_CHAIN_WITHIN_FIXED_DENOMINATOR` |
| self-soundness / global validation | paper的 unstaging soundness/stability是 CFTT syntax/model性质；没有对象层对自身全部证明或真理的验证器。 | `NOT_A_GLOBAL_SELF_VALIDATION_CONSUMER` |
| actual run | supplement README要求 Agda 2.6.4.3 与 standard library 2.0；本机获准 toolchain 是 2.8.0，未找到 2.6.4.3/2.0 pair。 | `NOT_RUN_WITH_REASON_VERSIONED_TOOLCHAIN_UNAVAILABLE` |

`primTrustMe` 与 `postulate` 的存在本身不是发现了不一致性。它们明确说明这份 Agda embedding所承担的是某个 specified staging interface的研究，而不是从 Cubical Agda 内核得到的全量 CFTT semantics。将其宣传为“CFTT 或 HoTT 已获得/失去自身真理验证”会混淆模型接口、元理论和对象理论。

## 4. 判词和目标坐标

```text
CLOSE_WITH_SCOPE
/ ACTUAL_STAGED_QUOTATION_SPLICE_UNSTAGING_CONTRACT_SOURCE_REVIEWED
/ AGDA_SUPPLEMENT_OBJECT_THEORY_POSTULATED_HOAS
/ GENERATIVITY_AXIOM_TRUSTME_BOUNDARY
/ NOT_OBJECT_PROVABILITY_OR_HOTT_SELF_VALIDATION
/ P29_CLIMBER_OBJECT_PROVABILITY_CANDIDATE_SELECTED
/ NO_NEW_HOTT_DEFECT_CLAIM
```

P28 服务最终链的“操作性 reflection 是否已经变成强 self-validation”的辨别点。它新增了真正的 staged process control：构造和执行 object code的操作可以存在，而对象结构是否可被任意检查是一个独立、甚至被明确禁止的约束。这避免了两种相反误判：把 staging 当成自指灾难，或把 quote/splice 当成全局证明谓词。

继续审计同一 supplement 不会产生新证据：其 HOAS/postulate/generativity 设计已经直接决定结论。P29 改成一个公开 source candidate，搜索结果声称存在 object-level `prov` 与 soundness gate；它是检查“有 prov 之后还是否维持层级”的更强正控制，而非 CFTT 的重复。

## 5. P29 候选卡：Climber 的 object `prov` 与 theory-construction gate

| 字段 | 冻结内容 |
|---|---|
| Candidate | `P29-CLIMBER-OBJECT-PROVABILITY-SOUNDNESS-CORPUS-001` |
| Source | `https://github.com/namin/climber.git`，P28 观测 `main`/`HEAD` = `6994d29dda860c3a82de207b1f39ea89526f61c9`。 |
| Input | Climber 的 object-level `prov`、metalanguage interpretation/soundness gate、theory construction records。 |
| Operation | 固定 commit 后审计 `prov` 的对象语义、soundness proof位于哪一层、是否有 self-proof/consistency/global truth claim，以及其与 HoTT 的关系。 |
| Observation/Done | 区分“object prov exists”与“same theory globally certifies itself”；若它是外部 meta gate或非-HoTT system，记录为正控制而不是命中。 |
| 正控制 | 公开检索结果明确描述 inert object-level `prov` 与 intended metalanguage meaning的 soundness gate。 |
| 最强反解释 | web snippet 可能不准确或过度概括；P29必须读固定源码，不能直接采信。 |
| 停止 | 若不是 HoTT或没有 P24 S3–S6的实际消费者，关闭此commit并生成新的 source/construct denominator。 |

## 6. 反思（Goal 3 §§3–3.2）

1. **新增事实：** CFTT具有实际 staged quote/splice/unstaging的理论合同，但Agda补充是postulated HOAS并以generativity限制结构检视。
2. **判词变化：** P27的候选由未审变为有界防线；没有改变 HoTT defect 状态。
3. **任务忠实性：** 论文表面语法、HOAS implementation、object operation、host trust primitive与proof predicate分别记录。
4. **控制：** staged operation是正控制；`postulate`/`primTrustMe`和generativity是边界控制；缺少版本匹配工具链如实标未运行。
5. **重复检查：** P28复用了P27冻结资产而非重审P24–P26；P29将使用不同 object-`prov` source。
6. **继续裁决：** P2 reflection path继续，P3/P4仍不触发；P29获得新 source/operation资格。
7. **不延续理由：** 对CFTT继续增加关键词或跑不匹配Agda版本不会改变合同；P29会测试更强的对象可证明性问题。

## 7. 证据边界

P28 是 paper/source audit；没有构建 supplement，也没有验证 CFTT external runtime。它不证明 CFTT 全局健全/不健全、HoTT内部矛盾、现实过程失配、原圆环 K，或 `primTrustMe` 的任意外推性质。

## 8. 复核入口

- [`P28-CFTT-SOURCE-FREEZE.json`](P28-CFTT-SOURCE-FREEZE.json)
- [`verify_p28_cftt_staged_quotation_splice_unstaging_corpus.py`](verify_p28_cftt_staged_quotation_splice_unstaging_corpus.py)
- [ICFP 2024 paper](https://andraskovacs.github.io/pdfs/2ltt_icfp24.pdf)，[source supplement repository](https://github.com/AndrasKovacs/staged)。
