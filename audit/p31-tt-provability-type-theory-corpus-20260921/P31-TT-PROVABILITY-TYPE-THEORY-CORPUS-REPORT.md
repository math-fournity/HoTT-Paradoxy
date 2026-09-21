# P31：`tt-provability` 的类型论模态/Löb 源码审计

**任务：** `P31-TT-PROVABILITY-TYPE-THEORY-CORPUS-001`

**状态：** `CLOSE_WITH_SCOPE / MODAL_BOX_QUOTATION_AND_LOB_SYNTAX_CONFIRMED / NOT_A_GODEL_STYLE_OBJECT_PROVABILITY_CHAIN / SOUNDNESS_NOT_ESTABLISHED_AND_TRUST_BOUNDARIES_EXPLICIT / NOT_HOTT_AND_NO_SAME_TASK_CONSUMER / P32_HOTT_SPECIFIC_DISCOVERY_SELECTED / NO_NEW_HOTT_DEFECT_CLAIM`

**前一单元：** [P30 六项反射义务交叉表](../p30-hott-reflection-obligation-crosswalk-20260921/P30-HOTT-REFLECTION-OBLIGATION-CROSSWALK-REPORT.md)

## 1. 固定问题与完成标准

P30 从公开 Agda 目录中选择 `GallagherCommaJack/tt-provability`，因为其仓库描述直接指向 “provability logic in type theory”。P31 不从标题推断它是 HoTT，也不将 Löb 形状自动解释为 Gödel式对象可证明性。本单元只按 P30 的 O1–O6 规格读取固定源。

| 项 | 冻结内容 |
|---|---|
| Input | `tt-provability` `master`=`69de7983019f2f044a40624b81662d862aca3dff`，包含 `Syntax/Typed`、`Syntax/Untyped`、`Universes/Tarski.agda`、`WTLob.agda` 与 `lib.agda`。 |
| Operation | 只读 clone、commit/hash 固定、结构与 literal scan、O1–O6 映射、检查 toolchain 与源内 trust/unfinished 边界。 |
| Observation | `box`、quotation、Löb、对象 proof-code/derivability、semantic soundness、theory rung、HoTT 特征和实际同任务消费者分别是否存在。 |
| Done | 给出 source-level 判词和后继 HoTT-specific discovery denominator；若没有可信 kernel replay，则明确保持 source audit，绝不输出该工程的数学定理。 |
| 正控制 | `Syntax/Typed/Def.agda` 与 `Defn.agda` 都有明确 `box`、quotation 与 Löb 形状构造，不能把本 source 错列为“没有反射语法”。 |
| 最强反解释 | 这些构造子可能正是完整可证明性/自验证实现；P31 因此检查 `prov` relation、解释、soundness、层级、placeholder 与 toolchain，而不以名称判定。 |
| 停止 | 若固定源仅给 experimental modal syntax，或其可信语义/HoTT/O6链未建立，就关闭该 source，不把它写成 HoTT 反例或缺陷。 |

## 2. 版本、来源和运行边界

P31 将公开仓库 clone 到 `/tmp/tt-provability-p31-69de7983`，detached checkout 后 `HEAD` 精确为 `69de7983019f2f044a40624b81662d862aca3dff`，工作树 clean。该提交日期为 2015-12-03，主题是 “Add new well typed syntax definition”。13 个 tracked 文件的 manifest 和 literal scan 已保存为 run receipt。

本机 PATH 中没有 `agda` 可执行器，也未发现匹配 toolchain；故 P31 **没有**运行任何 Agda kernel。`NOT_RUN_WITH_REASON_AGDA_EXECUTABLE_NOT_AVAILABLE_ON_HOST` 只说明当前复现能力的边界，不能被写成该源码永不检查、该理论不终止或 Agda 有错误。

## 3. 实际源码中有什么

这一仓库并非空标题：它有两个相关的 typed syntax 试验。

- `Syntax/Typed/Def.agda` 定义 dependent `Con`、`Ty`、`Tm`，有 type former `‘□’`、quotation `⌜_⌝t`，以及 `Löb : Tm Γ (‘□’ T ‘→’ T) → Tm Γ T`。
- `Syntax/Typed/Defn.agda` 定义带 universe level 的 `Γ ⋆ n` 和 judgement `Γ ⊢ T`；它有 `box`、`⌜_⌝t`、`Löb`，并导出 `löb : Γ ⊢ box T ‘→’ T → Γ ⊢ T`。
- `WTLob.agda` 尝试为前一类 typed syntax 写 Tarski universe/interpretation；它有 `Tm⇓ (Löb l) Γ⇓ = Tm⇓ l Γ⇓ (Löb l)`，但 quotation case `Tm⇓ ⌜ x ⌝ Γ⇓ = {!!}` 仍是洞，且若干旨在使用该解释的函数被注释。

这些是 **modal/Löb type-theory syntax** 的实际、可定位实现事实。它们不是自动等同于“某个 HoTT 具有 Gödel可证明性谓词”。

## 4. O1–O6 交叉表

| 义务 | 固定源码的证据 | P31 判定 |
|---|---|---|
| O1：对象 calculus、proof-code 与 `prov_T` | 有 `Con`/`Ty`/`Tm` 或 `Γ ⋆ n`/`Γ ⊢ T` syntax；`box` 是 type former，`⌜_⌝t` 是 quotation 构造。没有一个 named `prov_T` formula、proof-code datatype，或 `Check(p,φ)`。 | `PARTIAL_MODAL_SYNTAX_NOT_OBJECT_PROVABILITY_PREDICATE` |
| O2：与有限 derivability/checker 的关系 | `_⊢_` 是 Agda 中的 typed judgement family；源码没有将 proof code 连接到独立有限 checker，且 literal scan 没有 named `provability`/`soundness`/`consistency` chain。 | `PARTIAL_HOST_LEVEL_JUDGEMENT_NO_CHECKER_REPRESENTABILITY_CHAIN` |
| O3：实际 reflection consumer | `Löb` 作为 typed constructor，`Defn.agda` 还定义 `löb`；这满足一个 **syntax-level modal/Löb rule**。 | `PRESENT_AS_EXPERIMENTAL_MODAL_RULE_NOT_GLOBAL_SELF_VALIDATION_CONSUMER` |
| O4：interpretation/soundness owner | `WTLob.agda` 只有未完成 `Tm⇓` interpretation；没有 named soundness theorem。`lib.agda` 显式 postulate `⋆⋆TODO⋆⋆ : ∀ {i}{A : Set i} → A`，并有其他 postulates、holes、`--no-positivity-check` 与 `--no-termination-check`。 | `SOUNDNESS_NOT_ESTABLISHED_WITHIN_FIXED_SOURCE / TRUST_BOUNDARY_EXPLICIT` |
| O5：theory rung 更新 | 有 universe levels，但没有 P29 意义的 `T₀ → T₁` theory extension、level-indexed `prov` 或每 rung soundness；`box` 的层级不是该义务的替代物。 | `NO_THEORY_RUNG_PROVABILITY_UPDATE_ESTABLISHED` |
| O6：同一任务/实际使用桥 | 固定源没有 HoTT/univalence/HIT/cubical implementation 声明，也没有原 X、ABX consumer 或现实强完成任务。唯一 “cubical” 命中只是 source comment。 | `NO_HOTT_OR_SAME_TASK_CONSUMER_WITHIN_FIXED_SOURCE` |

## 5. 为什么 trust boundary 不应被误读

`⋆⋆TODO⋆⋆` 的源文本类型是对任意 `Set i` 的 inhabitant。再加上 postulates、禁用的 positivity/termination 检查和语义洞，P31 **不能**把该仓库中的 Löb 句式作为可信 kernel-checked semantic theorem。这个结论不是在指控 Agda、HoTT 或作者的理论“不一致”：它只是如实区分一个带显式 placeholder/axiom 的实验源码与一个通过相应受信任内核、无此开放信任洞的形式化结果。

同样，P31 不把 `--without-K` 或 “cubical syntax” 的注释升级为 univalence/HIT/Cubical Agda 资格。没有 `--cubical` option、univalence、HoTT 或 HIT 的实现入口被本单元建立。

## 6. 判词、波次价值与不延续理由

```text
CLOSE_WITH_SCOPE
/ MODAL_BOX_QUOTATION_AND_LOB_SYNTAX_CONFIRMED
/ NOT_A_GODEL_STYLE_OBJECT_PROVABILITY_CHAIN
/ SOUNDNESS_NOT_ESTABLISHED_AND_TRUST_BOUNDARIES_EXPLICIT
/ NOT_HOTT_AND_NO_SAME_TASK_CONSUMER
/ P32_HOTT_SPECIFIC_DISCOVERY_SELECTED
/ NO_NEW_HOTT_DEFECT_CLAIM
```

P31 是 P2 反射资格线的独立正控制：它证明未来审计不能简单写“类型论从不包含 Löb/quotation”；确有一个真实 Agda tree 把这些构造写进实验语法。但它也显示，**存在 modal rule 与完成可信自身真理验证是不同命题**。这一对照让 P30 的 O1–O6 更具判别力。

继续在相同 2015 commit 中增加关键词、解释 `Löb` 的直觉或反复尝试缺失的 Agda binary，都不会改变其 trust/HoTT/O6边界。P32 将回到 HoTT-specific source discovery，并把“有 univalence/cubical/HIT 的版本固定实现”与“有实际对象 reflection/provability consumer”同时设为入选条件。

## 7. P32 候选卡：HoTT-specific reflection consumer discovery

| 字段 | 冻结内容 |
|---|---|
| Candidate | `P32-HOTT-SPECIFIC-REFLECTION-CONSUMER-DISCOVERY-2026-001` |
| Input | 公开一手论文、官方/project repository、artifact 与本地文献登记；候选必须能固定版本。 |
| Operation | 按 `HoTT OR Cubical OR univalence OR HIT` 和 `object provability OR quotation/evaluation OR modal/Löb reflection` 的双维条件检索，先做本地去重，再读实际源码/论文段落。 |
| Observation | 每个候选分别判断 O1–O6，并明确其是 HoTT、邻近类型论、host metaprogramming 或实验 modal syntax。 |
| Done | 选择一项合格 version-pinned HoTT-specific source，或记录已声明分母内 `NO_QUALIFIED_SOURCE_YET` 并生成下一不同 discovery axis；不得把结果外推为全局不存在。 |
| 正控制 | P31：modal/Löb syntax 的非 HoTT、非可信语义控制。 |
| 最强反解释 | 相关术语可能只存在于 theorem-prover reflection 或一般 modal type theory；P32 必须逐项排除。 |
| 停止 | 该 discovery denominator 关闭后，只在新年份、来源族、实际 consumer 或 HoTT feature有变化时继续。 |

## 8. 证据边界

- P31 的 source facts是 fixed tree static evidence；没有 Agda kernel replay，也没有建立该项目的可编译性、soundness、consistency、normalization或任意 theorem。
- P31 不证明或反驳 HoTT 中 Gödel不完备性、内部 reflection、univalence、HIT、原圆环 M/N、数学现实同一性，或任何现实对齐判词。
- 对 P31 的 strongest positive finding 是“存在 experimental modal/Löb syntax”；对它的 strongest negative finding 只限于 source tree 的 named/visible chain与当前可用工具链。

## 9. 复核入口

- [`P31-TT-PROVABILITY-SOURCE-FREEZE.json`](P31-TT-PROVABILITY-SOURCE-FREEZE.json)
- [`runs/20260921-P31-TT-PROVABILITY-SOURCE-01`](runs/20260921-P31-TT-PROVABILITY-SOURCE-01)
- [`verify_p31_tt_provability_type_theory_corpus.py`](verify_p31_tt_provability_type_theory_corpus.py)
- [public repository](https://github.com/GallagherCommaJack/tt-provability)
