# P24：ERCF-3 的对象层证明谓词、反射桥与自然消费者资格审计

**任务：** `P24-ERCF3-PROOF-PREDICATE-REPRESENTABILITY-AND-CONSUMER-001`

**状态：** `CLOSE_WITH_SCOPE / OBJECT_LEVEL_PROVABILITY_BRIDGE_NOT_ESTABLISHED / NATURAL_SELF_VERIFICATION_CONSUMER_NOT_ESTABLISHED_WITHIN_P24_DENOMINATOR / EXTERNAL_KNOWN_ANALOGUES_IDENTIFIED / P25_HOTTLEAN_CANDIDATE_SELECTED / NO_NEW_HOTT_DEFECT_CLAIM`

**日期：** 2026-09-21
**前一单元：** [P23 独立入口选择](../p23-independent-ingress-discovery-20260921/P23-INDEPENDENT-INGRESS-DISCOVERY-REPORT.md)

## 1. 这个 wave 判断什么

P23 已把 ERCF-3 的“理论是否在对象层验证自身整体真理”从泛泛的 Gödel 叙述收束成一组可检验桥：对象语法、可解码编码、对象层证明谓词的可表述性、反射/对角构造，以及一个实际的自然消费者。P24 不再重跑已经有保存收据的编码模块，也不尝试把普通 Agda 语法片段冒充 HoTT 自身。

本单元固定的问题是：

> 在版本固定的 `HoTT/formal/ercf3-t3/` 资产中，已有的 `Prov`、修复编码与 `P` 是否已经构成“原对象理论的证明关系被对象公式表达”的桥；是否已有真实 HoTT 相关系统把该桥用于同层、全局自我验证？

这里的 `Done` 只是**资格判定**：为每条桥给出已完成、已假设、缺失或外层化的证据，并选择一个非同义后继分母。它不是 Gödel定理、HoTT 定理、理论缺陷证明，亦不是对任何系统实现错误的主张。

## 2. 冻结的输入、操作、观察与控制

| 项 | 冻结内容 |
|---|---|
| Input | `Fml` / `Prov`、修复的 `codeF'`/`decF`/`substCodeF`、扩展语言 `FmlP`/`P`、`Reflect` 以及 P23 所固定的 ERCF-3 问题。 |
| Operation | 逐项检查“元层编码事实 → 对象层可表述性 → 反射 → 对角不动点 → 自然消费者”的桥；不把其中任意箭头默认为等号。 |
| Observation | 每个箭头是否在固定源文件中有 inhabitant/定理，还是只有 type alias、构造子或注释；外部资料是否展示一个同类、但分层明确的真实工程。 |
| Done | 资格矩阵完整；已有资产的可复用边界明确；若没有同层消费者，产生一个版本冻结的后继候选或新的限界 source 分母。 |
| 正控制 | `RepairedSyntax.agda` 与其 C-181–C-183 保存运行确实给出可解码公式编码、像上替换一致和引用单射；这些不是空的“编码已经做了”说法。 |
| 最强反解释 | `repr` 也许可以被解释为对象系统采取的“表示性公理”。因此 P24 不称它为程序错误；它只核对该公理是否已与原 `Prov`、证明编码、语义正确性和实际消费者建立了所需桥梁。 |
| 停止条件 | 若这些精确文件没有证明对象层桥，且没有版本冻结的同层消费者，停止在该分母；不得继续用更多脉冲重写同一语法。 |

## 3. 本地资产侦察：已存在的部分与没有被它们完成的部分

P24 先复用了 P23 所列代码和已有 `C-157`–`C-187` 运行包，而没有重新制造编码实验。`RepairedSyntax.agda` 的 C-181–C-183 已在保存的 Agda run 中被接受：修复编码上的项/公式替换一致、公式引用单射，以及一个**语法层**对角替换实例。相应的 run 自己明确排除“对象理论可表示该替换”“P 表示性”“反射”和“对角不动点”。这正是可复用的正控制，而不是 ERCF-3 已完成的证据。

下表说明 P24 实际检查到的桥。`未建立`始终只指表中列出的固定源和固定公开分母。

| 桥 | 固定源中的直接证据 | P24 判定 | 为什么不足以跨到下一桥 |
|---|---|---|---|
| S1：对象语法与元层 derivability | `ObjectSyntax.agda` 定义 `Fml`、Hilbert 式 `⊢_`，并令 `Prov φ = ⊢ φ`。 | `PRESENT_AS_METALEVEL_SYNTAX_AND_DERIVABILITY_INTERFACE` | 这是 Agda 中的归纳族；它还不是“某个对象算术公式表示给定证明码”的定理。 |
| S2：编码、解码与替换 | `RepairedSyntax.agda` 基于 `FormulaCoding` 的 `codeF'`/`decF` 给出 `substCodeF-agrees`、`⌜-injective'`、`diagonalize'-code`；C-181–C-183 有保存 kernel receipt。 | `FORMAL_CHECKED_WITH_SCOPE / SYNTAX_LAYER_ONLY` | `substCodeF` 被定义为解码—替换—再编码；它没有被 `⊢_` 所在对象理论表达。 |
| S3：对象层 proof predicate 的表示性 | `ProvRepresentability.agda` 增加 `FmlP`、原始符号 `P` 与构造子 `repr`。`reprAll` 只是调用 `repr`。 | `ASSUMED_SCHEMA_NOT_REPRESENTABILITY_THEOREM` | `repr` 给出的是扩展 Hilbert 系统内的 `P` 公式推导；文件没有给出 proof-code 类型、可判定 `Check(p,φ)`、也没有证明 `P` 与原 `Prov φ` 之间的双向或可用关联。 |
| S4：反射 | `ReflectionSketch.agda` 将 `Reflect` 写成一个类型，并令 `reflectIsNamedObligation = Reflect`。 | `NAMED_UNINHABITED_OBLIGATION` | 类型别名定位了义务，但没有构造 `Reflect` 的 inhabitant，也没有证明 code-level substitution 与 `repr` 的编码相符。 |
| S5：对象层对角不动点与可证明性条件 | `ReflectionSketch.agda` 的注释明确把 fixed-point equation、consistency side conditions 留为 gated ERCF-3 body。 | `NOT_ESTABLISHED` | 没有 `G ↔ ¬Prov(⌜G⌝)` 的对象层推导，更没有 Hilbert–Bernays–Löb 条件或以它们为前提的定理。 |
| S6：自然的同层全局自验证消费者 | 历史固定五源审计和 ERCF-3/C8 的 E6 审计均未发现这样的真实接口。 | `NOT_ESTABLISHED_WITHIN_P24_DENOMINATOR` | “未找到”不推出不存在；它只禁止将一般自指或本地公理架升级为 HoTT 现实相对失配。 |

两个特别容易混淆的点需要保留：

1. `repr` 不是 Agda 的未检查漏洞。它是该**对象 Hilbert 系统的构造子/公理架**。所以 P24 的结论不是“代码错了”，而是“从原 `Prov` 到 `P` 的语义/编码保真桥尚未由这个源文件证明”。
2. `Reflect` 也不是被 Agda 拒绝的命题。它被诚实地保存为一个尚未构造的类型。名称出现、文件通过检查、或一条局部编码等式，都不能替代该 inhabitant。

## 4. 公开资料与学术坐标

本 wave 的公开检索不是装饰。它可以改变“缺什么”的判断：如果已有类型论工作实现了真正的对象可证明性谓词和对角链，则本地的 gap 应按那个完整规格重写；如果已有 HoTT 相关系统将其内化，又会提供一个可能的 natural consumer。

### 4.1 已知正控制：完整可证明性规格比本地 `repr` 强得多

Coquand 2026 年的 Agda 形式化报告明确记载：一次早期自动形式化因**内部可证明性谓词规格过弱**而得到表面像 Gödel II、实则数学无关的命题；修复依赖明确的派生式枚举 `thmT`、内部 numeral 操作及 substitution/numeral closure 的交互。[报告](https://arxiv.org/abs/2606.01898) 与其 [Agda 开发](https://github.com/coquand/agda-godel-tree) 展示了更强的正控制：对象级 `Provable A` 被定义为一个闭存在公式，并且 Löb/Gödel链的对象理论和元理论结论严格分开。

这不是 HoTT 的缺陷证据，也不证明 ERCF-3 已成立。它的作用是可判别的：它支持 P24 对本地 `repr` 的严格读法——若没有从 proof code、对象公式、枚举/检查、替换和内部推导到 semantic linkage 的完整链，单有一个名为 `P` 的构造子不足以承担“可证明性表示”的数学角色。

### 4.2 相邻 HoTT 研究：语法、检查器与模型被明确地放在外层

HoTTLean 的公开 README 描述了 MLTT syntax 的 deep embedding、一个 certifying normalization-by-evaluation typechecker 和相对于模型的 soundness；项目同时说明它仍是 work in progress，当前不支持 higher inductive types。[项目 README](https://github.com/sinhp/HoTTLean) 还明确将内部 synthetic reasoning 与 external model reasoning 分开。作者的项目说明也把 DSL 嵌入 **Lean**，并把 semantic entities 从语法中公理化。[项目说明](https://sinhp.github.io/lean-projects/2025-06-10-HoTTLean)

因此它是 `NEARBY_NOT_SAME_TASK`：它的确是可审计的“类型论语法—检查器—模型”真实消费者，却没有从公开材料中声称同一 HoTT 层内的全局自身真理验证；而且其当前公开范围不覆盖完整 HIT HoTT。它既不能被写成 ERCF-3 已命中，也不应被忽略为无关。它为 P25 提供了一个新的、版本固定的 source denominator。

## 5. P24 的判词及其在最终目标中的坐标

**判词：**

```text
CLOSE_WITH_SCOPE
/ OBJECT_LEVEL_PROVABILITY_BRIDGE_NOT_ESTABLISHED
/ NATURAL_SELF_VERIFICATION_CONSUMER_NOT_ESTABLISHED_WITHIN_P24_DENOMINATOR
/ KNOWN_ANALOGUE_AND_SPECIFICATION_CONTROL
/ P25_HOTTLEAN_MLTT_SYNTAX_SEMANTICS_CANDIDATE_SELECTED
/ NO_NEW_HOTT_DEFECT_CLAIM
```

这个 wave 位于四分支中的 **P2：规则/对象理论级桥**，服务最终见证链的“理论是否实际把一个较弱识别或认证规格提升为强完成”的一段。它没有处理 P13 的 M/N operation contract，也没有复活已暂停的 P3 同类消费者扫描。

它的实际价值是把“自反真理验证”从模糊概念缩成六段桥，并给出能够推翻本轮结论的精确条件：出现一个证明 S3、S4 或 S5 的版本固定对象层定理；或者 P25 发现一个真实系统用该链承诺同层的全局自验证。这样，后续行动不会把已存在的编码正控制反复包装为“又一次对角化”。

继续 P24 自己是不对的：下一个动作若只是继续在 `ercf3-t3` 写更多 grammar 或关键词，将重复同一 S3/S4 缺口。暂停整个目标也不对：P25 改变了 source、理论变体、外部/内部层次和可检验 consumer，因此是一个真正的 successor。

## 6. P25 候选卡：HoTTLean 的 MLTT syntax—checker—model 路径

| 字段 | 冻结内容 |
|---|---|
| Candidate | `P25-HOTTLEAN-MLTT-SYNTAX-SEMANTICS-CORPUS-001` |
| Version source | `https://github.com/sinhp/HoTTLean.git`，P24 观测的 `master`/`HEAD` 为 `31133dd5b25226ea897f8aa5e2e43b61392459eb`。 |
| 输入 | HoTTLean 的 deep MLTT syntax、certifying typechecker、模型语义与其公开声明。 |
| Operation | 按版本冻结源码逐项审计 object syntax、checking/normalization、soundness、层级与信任边界；不把 Lean host 的元理论能力归给对象 MLTT。 |
| Observation | 是否出现已调用的对象层 proof predicate / quotation / reflection，以及它是否被真实消费者用于“同层、全局、健全完备自身验证”。 |
| Done | 若其显式保持 Lean 外层/只覆盖受限 MLTT，则记录 `NEARBY_NOT_SAME_TASK / DEFENSE_BY_STRATIFICATION`；若存在满足 S3–S6 的实际链，才按精确调用地点重开 ERCF-3。 |
| 正控制 | README 已明确给出 syntax、typechecker、soundness 的真实部件，故不是只凭关键词筛到的候选。 |
| 最强反解释 | 它可能只是构建/验证模型的普通 metatheory，而非自验证消费者；P25 必须用源码和声明检查这一点，不能预设。 |
| 停止 | 固定版本的 syntax/checker/model 入口均外层化或没有 S3–S6 调用链时，结束这个分母，不扩张为“所有 HoTT 研究都如此”。 |

## 7. 逐项反思（Goal 3 §§3–3.2）

1. **新增事实：** `Prov`/修复编码/`repr`/`Reflect` 的真实桥位置已逐项核对；Coquand 的新形式化给出独立、明确的 internal-provability specification control；HoTTLean 提供新的 source candidate。
2. **改变的判词：** P23 的“P24 未开始”变为本报告的有界否定；没有改变“未找到 HoTT defect”的总边界。
3. **任务忠实性：** Input、Operation、Observation 和 Done 都在 §2 冻结；没有将可解码 syntax 误作 strong Done，也没有把元层 normalisation 改写为现实过程结论。
4. **控制与反解释：** C-181–C-183 是正控制；`repr` 作为可选择的对象公理架是最强反解释；两者都保留，而不是以一方压倒另一方。
5. **重复检查：** P23 和 C8 已定位该资产，但没有把当下的 `repr`/`Reflect` 源码逐桥比较，也没有纳入 2026 Coquand/HoTTLean 的分层正控制；因此本单元不是重跑旧编码。
6. **分支资格：** P2/ERCF3 的本地 bridge 分母关闭；P25 获得资格，P3 旧同类扫描继续暂停，P4 仍未由可重放理论—实现差异触发。
7. **为什么停止而不是继续：** 固定源码已把 S3–S5 的缺口直接写明；没有新操作可改变该事实。继续只能重复。P25 有新的版本、真实 syntax/checker/model consumer 和可证伪的分层判断，因此应继续目标但不继续本分母。

## 8. 证据边界

- 本报告静态审计当前 Git 固定的 ERCF3 源码，并复用已登记的 C-181–C-183 run；没有把历史 `LOCAL_UNCOMMITTED` labels 升级为当前 version-closed 数学包。
- 公开项目与论文是 source-level/README-level evidence；P24 没有 clone、构建或重放 HoTTLean，也没有将其声明作为已机器复现的数学结论。
- P24 没有证明或反驳 HoTT 的一致性、HoTT 的内部完全反射、不完备性在任一特定 HoTT 变体中的精确形式，或用户的现实对齐主张。
- 若 P25 不能找到 S3–S6 的实际调用链，正确结论仍只是该版本、该入口的防线或相邻性，不是对整个 HoTT 社区的全称判断。

## 9. 可复核来源

- 机器可核的本地路径与 SHA-256：[`P24-ERCF3-SOURCE-FREEZE.json`](P24-ERCF3-SOURCE-FREEZE.json)。
- 本报告的结构/固定源校验器：[`verify_p24_ercf3_proof_predicate_qualification.py`](verify_p24_ercf3_proof_predicate_qualification.py)。
- 外部一手资料：[Coquand 2026 的 Agda Gödel II 报告](https://arxiv.org/abs/2606.01898)，[agda-godel-tree](https://github.com/coquand/agda-godel-tree)，[HoTTLean README](https://github.com/sinhp/HoTTLean)，[HoTTLean 项目说明](https://sinhp.github.io/lean-projects/2025-06-10-HoTTLean)。
