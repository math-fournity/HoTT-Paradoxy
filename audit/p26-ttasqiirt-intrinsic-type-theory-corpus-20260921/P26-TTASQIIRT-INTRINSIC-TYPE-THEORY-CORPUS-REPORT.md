# P26：TTasQIIRT 的 native intrinsic type-theory syntax 审计

**任务：** `P26-TTASQIIRT-INTRINSIC-TYPE-THEORY-CORPUS-001`

**状态：** `CLOSE_WITH_SCOPE / NATIVE_INTRINSIC_SYNTAX_AND_METATHEORY_ENTRYPOINT_ACCEPTED_WITH_SCOPE / INTRINSIC_SYNTAX_NOT_GLOBAL_SELF_VALIDATION / EXPLICIT_UIP_AND_TERMINATION_TRUST_BOUNDARIES / P27_REFLECTION_CONSUMER_DISCOVERY_CANDIDATE_SELECTED / NO_NEW_HOTT_DEFECT_CLAIM`

**冻结版本：** `L-TChen/TTasQIIRT` `master` = `8db08306287333067b2749f95f8ad3ba7a0e14d1`（2025-12-17T00:27:42Z，`fix typo`）。

## 1. P26 的问题与冻结合同

P25 的 HoTTLean 表明真实 syntax/checker/model 工程可以存在，但它把对象语言装在 Lean 宿主中。P26 改变的是这个决定性维度：TTasQIIRT 使用 Cubical Agda 的 QIIRT 定义 `Ctx`、`Ty`、`Tm` 和 `tyOf`，所以它是检验“类型论能否在同类类型论中内在地表示其 syntax/metatheory”的真实分母。

| 项 | 冻结内容 |
|---|---|
| Input | TTasQIIRT 主 `src/index.agda`、三种 initial natural-model theory、QIIRT syntax/recursor/model/NbE 路径、未完成模块和工具选项。 |
| Operation | 固定 commit 上核对 intrinsic syntax、standard-model/NbE/strictification、对象 proof-predicate/reflection、全局自验证、univalence/UIP/termination 信任边界。 |
| Observation | 主入口实际检查了什么；哪些模块明确不完整；“Reflection”是否是对象理论反射还是 Agda 元编程；可证明性是否出现为对象层 consumer。 |
| Done | 区分 intrinsic syntax 成功、主入口受限检查、额外假设/工具边界与未建立的 global self-validation；生成不同的后继发现分母。 |
| 正控制 | `Syntax.agda` 的 QIIRT declarations 与 `index.agda` 的主 imports；在固定 Agda 2.8.0 上 `--ignore-interfaces` 重检 `index.agda` 退出码 0。 |
| 最强反解释 | “intrinsic”可能已经等同于“同层自证”。P26 直接检查 proof predicate、reflection 和主入口，而不是由词义推断。 |
| 停止 | 若主入口只给 syntax/model/NbE 而没有对象证明谓词与全局自身验证，就关闭该 commit；不将工程难点、`--safe` 拒绝或未完成模块夸大为 HoTT 矛盾。 |

## 2. 本地和公开资产侦察

当前 repo 的早期 groupoid-syntax/2LTT 资产已经有独立记录，不能因 P26 再次重复。对于 TTasQIIRT，本地/历史目录没有既有 checkout 或同版本报告；因此以 P25 source freeze 中的 remote SHA 为起点，克隆到临时工作目录并 detached checkout。公开的 CPP 2026 论文、Zenodo v1 artifact 和 README 相互给出了论文—artifact—source 的路径。

论文的摘要与 README 都明确把它定位为 **Cubical Agda 中的 intrinsic representation of type theory**：初始 natural model 用 QIIRT 定义，形成 standard model、NbE 和 strictification；但更复杂的 metatheory 仍遇到 transport difficulty。[CPP 2026 论文](https://fredriknf.com/papers/tt-qiirt_cpp2026.pdf)；[Zenodo artifact](https://zenodo.org/records/17802827)。这使它是 `KNOWN_NEARBY_INTRINSIC_SYNTAX_RESULT`，而非凭名称筛出的候选。

## 3. 已确认的正面能力

`Theory/SC/QIIRT-tyOf/Syntax.agda` 在 Cubical Agda 中前向声明并随后定义 `Ctx`、`Sub`、`Ty`、`Tm` 和依赖的 `tyOf`，同时把 substitution/calculus equations 和 set-truncation构造列入 QIIRT。它不是 P25 那样的外部 Lean AST；在这个精确意义上，P26 确认了 **native intrinsic syntax**。

主 `index.agda` 导入三条当前线路：

1. substitution calculus (`SC`) 的 syntax、model、recursor、displayed/indexed model、NbE 与 strict syntax isomorphism；
2. `SC+Pi+B` 的 QIIRT syntax、model、recursor与相应模型；
3. `SC+El+Pi+B` 的 universe、Pi、Bool扩展及模型。

在固定 `Agda 2.8.0-3d04bac` 工具链上，`agda --ignore-interfaces index.agda` 退出码 `0`。保存的 P26 run receipt说明这是一项**外部源码的主入口接受**，不是本 repo 的新 HoTT 定理，也不证明全部未导入模块。

## 4. 边界：intrinsic syntax 不等于 global self-validation

P26 的关键结论来自三个独立源面。

| 桥/主张 | 固定源码证据 | P26 判定 |
|---|---|---|
| 内在 syntax | `Ctx`/`Ty`/`Tm`/`tyOf` 由 QIIRT 同时定义；`index` 导入 syntax、model、NbE。 | `NATIVE_INTRINSIC_SYNTAX_CONFIRMED_WITH_SCOPE` |
| 对象证明谓词或 Gödel编码 | 在 `src/Theory/` 与 `index.agda` 的固定 literal denominator 搜索 `godel`, `provability`, `provable`, `proof predicate`, `self-reference` 没有对应声明路径。 | `NO_NAMED_OBJECT_PROVABILITY_CHAIN_WITHIN_LITERAL_DENOMINATOR` |
| “Reflection”目录 | `Cubical/Reflection/StrictEquiv.agda` 导入 `Agda.Builtin.Reflection`，生成 strict-equivalence 宏和 declarations；它是 proof-assistant metaprogramming。 | `HOST_TOOL_REFLECTION_NOT_OBJECT_PROOF_REFLECTION` |
| 全局自验证/可判定性 | 主入口没有 `Prov`/quotation/semantic truth predicate consumer；论文谈的是 syntax/metatheory，而不是整个对象理论真理的内部二值裁决。 | `NOT_A_P24_STRONG_SELF_VALIDATION_CONSUMER` |
| 已完成范围 | `index.agda` 明确注释并不导入 `Canonicity`、`LogPred`、`StrictLogPred`；其源文件含 unsolved metas。 | `INCOMPLETE_ADVANCED_METATHEORY_EXPLICITLY_EXCLUDED` |

P26 因此实际推进了 P24 的 S1/S2：内在语法与许多 metatheory construction 可以在 cubical QIIRT 的设定中形成真实工作面。它**没有**建立 S3–S6，即对象 proof-code、可证明性谓词、反射/对角不动点、同层全局自身验证消费者。

## 5. 工具链、假设和运行边界

两种运行必须并列阅读：

1. 默认的 `--ignore-interfaces` 主入口重检接受了 `index.agda`。这证明固定 Agda 2.8.0 配置下的该入口可检查；它不把所有 source text、所有 archive、或未导入的 advanced modules升级为已完成结果。
2. 加 `--safe` 的同一重检在 `Theory.SC.QIIRT-tyOf.Rec.agda:14` 因 `{-# TERMINATING #-}` 被 Agda 拒绝，退出码 `42`。该诊断表明主入口不具有这个 `--safe` 配置的证明资格；它不证明算法错误、非终止或 HoTT 不一致。

源码还显式写出标准模型的假设：`Theory.SC.QIIRT-tyOf.Model.Set` 和 `SC+Pi+B...Model.Set` 都用 `postulate UIP`，以便相应 set model 成为 set；多处 recursor/model 使用 `TERMINATING` pragmas。README 中的 `--cubical=no-glue` 路径依赖尚未正式发布的 Agda 2.9.0，因此 P26 在本机 2.8.0 不能把“无 Glue/无 univalence”升级为已重放的运行事实。默认 run 也实际检查了 `Cubical.Core.Glue`；这只说明当前 replay 的 import/configuration，不能单独判断 formalisation 是否使用 univalence。

这些是清晰的 scope 与 trust boundary。它们可能成为未来关于特定工具链保真性的研究输入，但当前没有“实现声称遵守某规则而运行违背”的差分，所以 P4 不被触发。

## 6. 判词与最终目标坐标

```text
CLOSE_WITH_SCOPE
/ NATIVE_INTRINSIC_SYNTAX_AND_METATHEORY_ENTRYPOINT_ACCEPTED_WITH_SCOPE
/ INTRINSIC_SYNTAX_NOT_GLOBAL_SELF_VALIDATION
/ EXPLICIT_UIP_AND_TERMINATION_TRUST_BOUNDARIES
/ P27_REFLECTION_CONSUMER_DISCOVERY_CANDIDATE_SELECTED
/ NO_NEW_HOTT_DEFECT_CLAIM
```

P26 位于 P2/ERCF3 的对象理论桥段。它的重要价值不是“又没有发现问题”，而是明确推翻了一个过强的技术前提：不能说 HoTT 风格类型论无法内在表示 syntax。与此同时，它证明了另一个关键区分仍不可省略：**内在 syntax + 有限 metatheory + NbE** 并不自动给出对象层的 global provability/truth/reflection package。

继续在同一 TTasQIIRT commit 上重复 index run、搜索更多相同关键词或把 `TERMINATING` pragma包装成错误，都不会改变该判词。P27 因此改为版本固定的发现单元：面向 2025–2026 公开 source/artifact，寻找一个**实际调用** object-level provability、quotation、reflection 或 self-soundness 的 type-theory/HoTT-related consumer，并严格排除 P24 Coquand BRA、P25 HoTTLean、P26 TTasQIIRT 和已审 P3 consumers。

## 7. P27 候选卡：反射消费者的异类发现分母

| 字段 | 冻结内容 |
|---|---|
| Candidate | `P27-REFLECTION-CONSUMER-DISCOVERY-2026-001` |
| Input | 2025–2026 的一手论文、artifact、正式源码和现有本地 source inventory；查询围绕 object proof predicate、quotation/evaluation、internal reflection、provability logic、self-soundness 和 HoTT/type-theory implementions。 |
| Operation | 先排除 P24/P25/P26/已审 P3 资产，再为每个新候选固定 commit/version、Input/Operation/Observation/Done 与调用入口。 |
| Observation/Done | 至少选择一个不与既有分母同义、并有实际 source entry point 的 consumer；若没有合格结果，输出其公开/本地检索分母和下一类 source route。 |
| 正控制 | Coquand BRA 是“完整对象可证明性”正控制；P25/P26 是“syntax/metatheory≠global self-validation”反控制。 |
| 最强反解释 | 关键词可能只命中 proof-assistant host reflection 或一般 Gödel论文；P27 要逐项排除它们。 |
| 停止 | 不因无命中停止 active goal；产生下一个不同理论构造、consumer或source-coverage分母。 |

## 8. 反思（Goal 3 §§3–3.2）

1. **新增事实：** 版本固定的 native intrinsic syntax、主入口 runtime acceptance、`--safe` 的精确 rejection、UIP/`TERMINATING`边界、三项明确排除的 advanced modules。
2. **判词变化：** P25 的“外部 host 分层”不再能被当作内在化不可能性的证据；P26 将该点升级为有界正控制，同时保持 global self-validation 未建立。
3. **任务忠实性：** QIIRT syntax、host reflection、object reflection、safe configuration、semantic soundness和现实桥分开记录。
4. **控制：** 默认入口接受是正控制；`--safe`拒绝、源中 UIP/postulate/unfinished module是边界控制；都不被提升为理论错误。
5. **反重复：** 先检查本地已有 groupoid/2LTT资产，未重跑它们；P26 是版本固定的不同 artifact 和内在化机制。
6. **分支资格：** P2/ERCF3获得内在 syntax 的正控制；P3和P4仍不具资格。P27获得一个新公开 source discovery 分母。
7. **为什么停止：** 当前 commit 的主入口和缺失/未完成面已足够区分；继续它不增加 S3–S6证据。P27改变来源与消费者分母，因此 active goal 应继续。

## 9. 证据限制

- 主入口 run 发生在临时 external checkout；其保存收据固定命令、toolchain、commit、文件 hash、stdout/stderr，不将第三方代码复制为本 repo 的新 formal proof package。
- `--safe` 的退出码只表示这个 Agda 配置拒绝 `TERMINATING` pragma，不能证明运行会不终止或系统不健全。
- P26 不证明完整 HoTT、univalence-free semantics、实际 K、圆环 H/R/Done mismatch、现实任务失配或任何 HoTT defect。

## 10. 复核入口

- External commit、局部 source hash 和公开来源：[`P26-TTASQIIRT-SOURCE-FREEZE.json`](P26-TTASQIIRT-SOURCE-FREEZE.json)。
- Default/safe run：[`runs/20260921-P26-TTASQIIRT-INDEX-01`](runs/20260921-P26-TTASQIIRT-INDEX-01)。
- 审计验证：[`verify_p26_ttasqiirt_intrinsic_type_theory_corpus.py`](verify_p26_ttasqiirt_intrinsic_type_theory_corpus.py)。
