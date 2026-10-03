# HOTT-MOTIVE-ZFC：HoTT 创建动机反投影 ZFC 文献调查档案

> **身份：** `PROJECT_ARCHIVE_ROOT / HUMAN_EDITED / SEVEN_CLOSED_SOURCE_RUNS / NO_ZFC_Q_CLAIM`。
>
> **SOP：** [HOTT-MOTIVE-ZFC-SOP](../../dev-docs/HoTT创建动机反投影ZFC文献调查SOP.md)
>
> **路线种子：** [HoTT创建动机反投影ZFC候选路线](../../dev-docs/菲尔兹奖后续理论级目标路线图/009%20-%20HoTT创建动机反投影ZFC候选路线.md)

> **阶段综合：** [第一阶段来源综合](PHASE-1-SOURCE-SYNTHESIS.md)。
>
> **首批动机覆盖综合：** [R 种子覆盖综合](R-SEED-COVERAGE-SYNTHESIS.md)。

## 项目边界

本目录是文献调查项目 `HOTT-MOTIVE-ZFC-INVESTIGATION` 的档案根。它保存每次已启动调查的冻结来源分母、
原件与派生阅读材料的身份、R/Z/Q 卡、消费者控制、覆盖收据与 findings；它不保存或替代项目的数学证明资产。

当前状态：首个来源 run 已闭合：[20261003-HMZ-001-primary-motives](20261003-HMZ-001-primary-motives/MANIFEST.md)。
它已对十个冻结来源保存 R/Z/Q/control cards，并完成其范围内的来源追踪；结果是一个 ZFC 的
class/meta-language 表示边界和两类显式支付，而不是 `ZFC_Q`、`H0→Z0` 传输判词或全项目的“文献已完成”结论。

第二个来源 run 已闭合：[20261003-HMZ-002-voevodsky-set-theory](20261003-HMZ-002-voevodsky-set-theory/MANIFEST.md)。
它检验 Voevodsky 对 ZFC formalization 和 equivalence problem 的更明确原典表述，并以 Ahrens/North 的
equivalence-principle 文献和已有 ZFC consumers 校正；结果仍是来源支持的表示边界与显式语言支付，未产生候选。

第三个来源 run 已闭合：[20261003-HMZ-003-formalization-delivery](20261003-HMZ-003-formalization-delivery/MANIFEST.md)。
它研究 ZF 的 bare-existence axioms 如何在实际形式化中通过命名 constants、条件化规则和语法层支付，结论仍是
formation/payment control，未产生 P-qualified Q。

第四个来源 run 已闭合：[20261003-HMZ-007-werner-zfc-coq-pair](20261003-HMZ-007-werner-zfc-coq-pair/MANIFEST.md)。
它以 Voevodsky 2011 的 WoLLIC 机器基础动机与 Werner 的 CIC↔ZFC 编码配对，但保留“不是作者归因”的边界；`Ens`／`Power`／Replacement／Russell source cards 显示 Choice、host 条件和 universal-container guard，而不是 P-qualified Q。

第五个来源 run 已闭合：[20261003-HMZ-008-higher-hits-set-semantics](20261003-HMZ-008-higher-hits-set-semantics/MANIFEST.md)。它把 HoTT Book 的 `R-HIGHER` 与 Lumsdaine–Shulman、Swan 的 Set/ZF HIT/QW semantic constructions 对照：语义模型、stability与cardinal/Choice条件都被明确支付，direct formation 的同一 Done 没有被偷换为 ZFC Q。

第六个来源 run 已闭合：[20261003-HMZ-012-totality-partition-reality-source](20261003-HMZ-012-totality-partition-reality-source/MANIFEST.md)。它以 Dochtermann 的有限分类／无限 complete partition／Power Set 叙述为 E-source bridge，再与 HoTT Book、Shulman/Metamath的 formation sources和Isabelle/ZF actual consumer对照。结果保存了 `REALITY_TASK_TO_TOTALITY_CONSTRUCTION_BRIDGE`，但 finite-process Done 与 formal set-existence Done 没有来源证明为同一任务；P2/P3和H0 transport仍不成立，因此是 `P_REQUALIFICATION_REQUIRED`，不是 Q。

第七个来源 run 已闭合：[20261003-HMZ-016-community-antecedent-p-comparison](20261003-HMZ-016-community-antecedent-p-comparison/MANIFEST.md)。它将 Feferman 对 predicativity、Vicious Circle、completed totalities与ZF Separation/Power Set的历史分析，同 HoTT context、ZF formation、finite-task与显式 computation controls作字段对齐。结果承认社区对P0/P3/P4有实质 antecedent，同时保留用户P的P1/P2/P5/P6为未由该分母覆盖的独立义务；因此为`COMMUNITY_ANTECEDENT_PARTIAL / P_REQUALIFICATION_REQUIRED`，不是 Q。

## Run 命名与目录合同

用户在 `/goal` 中引用 `HOTT-MOTIVE-ZFC-SOP` 后，执行者为每次冻结的来源分母建立：

```text
audit/HOTT-MOTIVE-ZFC/YYYYMMDD-HMZ-###-scope/
```

其中 `scope` 是短的、可读的来源范围名。每个 run 至少按 SOP 保存：

```text
MANIFEST.md
SOURCE-CATALOG.md
R-CARDS.md
Z-CARDS.md
Q-CARDS.md
E-CARDS.md               # only when an E-source is central to the denominator
CONSUMER-CONTROLS.md
COVERAGE.md
FINDINGS.md
```

`README.md` 只维护项目级入口和 run registry；不能复制任一 run 的 current findings，也不能把已关闭的
`Q-R`、`SOURCE_PAYMENT` 或 `ANTI_ANALOGY_CONTROL` 自动重开。

## Run registry

| Run ID | 冻结范围 | 状态 | Findings | 备注 |
|---|---|---|---|---|
| `20261003-HMZ-001-primary-motives` | HoTT／UF 首批创立动机、Shulman 的 ZFC/NBG 分析、Isabelle/ZF、Metamath 形式呈现、Mumford 与 Shulman 真实消费者控制。 | `CLOSED_WITH_SCOPE / DENOMINATOR_COMPLETE_WITH_SCOPE` | [FINDINGS](20261003-HMZ-001-primary-motives/FINDINGS.md) | 0 个 `CANDIDATE_SEED`；class/meta-language 是来源支持的表示边界且有 NBG 支付；结构／choice／machine 路径均有显式支付；Power Set 与 H0 transport 未资格化。 |
| `20261003-HMZ-002-voevodsky-set-theory` | Voevodsky 2011/2013 对 ZFC、equivalence、type systems 与 set theory 的原典；Ahrens/North 2022；复用 HMZ-001 的 Shulman/Isabelle/Mumford controls。 | `CLOSED_WITH_SCOPE / DENOMINATOR_COMPLETE_WITH_SCOPE` | [Findings](20261003-HMZ-002-voevodsky-set-theory/FINDINGS.md) | equivalence problem 是来源支持的表示边界；typed language/FOLDS、NBG、Choice、maps、well-ordering是明确支付；0 个 P-qualified Q。 |
| `20261003-HMZ-003-formalization-delivery` | Grayson 2018、Rijke/Spitters 2016、HoTT Library 2017 与 Isabelle/ZF/ Shulman 控制。 | `CLOSED_WITH_SCOPE / DENOMINATOR_COMPLETE_WITH_SCOPE` | [Findings](20261003-HMZ-003-formalization-delivery/FINDINGS.md) | ZF existence axioms → named formal constants / rules 是显式支付；HoTT自身也有阻断计算的axioms；0 个 P-qualified Q。 |
| `20261003-HMZ-007-werner-zfc-coq-pair` | WoLLIC 2011 的 ZFC-in-proof-assistant 动机，与 Werner 1997 CIC↔ZFC 编码、`rocq-archive/zfc` code snapshot、既有 Paulson/Grayson controls 的冻结配对。 | `CLOSED_WITH_SCOPE / DENOMINATOR_COMPLETE_WITH_SCOPE` | [Findings](20261003-HMZ-007-werner-zfc-coq-pair/FINDINGS.md) | `Ens`／Power／Replacement／Russell guard 都处在 CIC model/formalization layer；TTDA/Choice、host条件和 bounded universal-set guard明确，0 个 P-qualified Q。 |
| `20261003-HMZ-008-higher-hits-set-semantics` | HoTT Book `R-HIGHER`，Lumsdaine–Shulman HIT semantics 与 Swan 的 ZF QW/HIT source。 | `CLOSED_WITH_SCOPE / DENOMINATOR_COMPLETE_WITH_SCOPE` | [Findings](20261003-HMZ-008-higher-hits-set-semantics/FINDINGS.md) | Set/ZF中存在一类 HIT/QW semantic constructions，也有明确ZF/cardinal/Choice边界；model semantic task不等于HoTT direct formation Done，0 个 P-qualified Q。 |
| `20261003-HMZ-012-totality-partition-reality-source` | HoTT `R-STRUCT`／Book Power Set–quotient bridge、Dochtermann 2011 reality/task source、Shulman/Metamath/Paulson/Isabelle controls。 | `CLOSED_WITH_SCOPE / DENOMINATOR_COMPLETE_WITH_SCOPE` | [Findings](20261003-HMZ-012-totality-partition-reality-source/FINDINGS.md) | finite categorization→infinite totality→Power Set quotient 是来源支持的 construction bridge；但同一 Done、P2/P3与H0 transfer都未成立，0 个 P-qualified Q。 |
| `20261003-HMZ-016-community-antecedent-p-comparison` | Feferman 2002 predicativity/VCP、HoTT context、Shulman、Dochtermann、Koepke–Koerwien controls。 | `CLOSED_WITH_SCOPE / DENOMINATOR_COMPLETE_WITH_SCOPE` | [Findings](20261003-HMZ-016-community-antecedent-p-comparison/FINDINGS.md) | 历史/社区已识别totality、vicious-circle、impredicativity和ZF loci；该分母未给user-P的actual consumer/preemptive use/same Done，0 个 P-qualified Q。 |

三个 run 的跨分母判断由 `PHASE-1-SOURCE-SYNTHESIS.md` 拥有；本 README 只保留入口与 run registry。

一份未通过 successor admission 的作者技术原典保存在 [HMZ-004 Hλ预检](20261003-HMZ-004-hlambda-preflight/MANIFEST.md)。
它是可复核来源，不是完整 run，也不产生 Q。

第二份预检是 [HMZ-005 Makkai anafunctor 消费者控制](20261003-HMZ-005-makkai-anafunctor-preflight/MANIFEST.md)。它以实际范畴论 consumer 分开“逐对存在 binary products”“指定 ordinary product functor”与“anafunctor 的不同输出契约”：Choice／selection 被来源明确支付，替代构造改变 `Done`，所以同样不是完整 run 或 Q。

第三份预检是 [HMZ-006 Voevodsky WoLLIC 机器基础动机](20261003-HMZ-006-wollic-machine-preflight/MANIFEST.md)。它新增一条作者直接陈述：ZFC-based proof-assistant formalization 曾导致“不自然构造”；[HMZ-007](20261003-HMZ-007-werner-zfc-coq-pair/MANIFEST.md) 已提供可审计的 comparable pairing，但 WoLLIC 未点名 Werner，故历史指称仍未解决，且没有 Q。

第四份预检是 [HMZ-009 HoTT Book 的 Power Set—quotient 建构桥](20261003-HMZ-009-book-powerset-quotient-preflight/MANIFEST.md)。Book 明确把集合论式 quotient 写成等价类构成 \(\mathcal P(A)\) 的子集，并与 HoTT 的 quotient constructions 对照；这补上了一个精确的 `R-SET-CONTROL` construction bridge，但 Book 本身没有提供 bare-ZFC actual consumer 的同一 `C/I/O/Done`，且 universe/resizing/external-versus-internal costs 被来源明示。因此状态是 `PAIRING_SOURCE_REQUIRED`，不是完整 run 或 Q。

第五份预检是 [HMZ-010 Isabelle/ZF quotient consumer](20261003-HMZ-010-isabelle-zf-quotient-consumer-preflight/MANIFEST.md)。它完成 HMZ-009 所需的第一份 actual-consumer pairing：`EquivClass.thy` 定义 \(A//r\)，以 `RepFun`/functional replacement 形成等价类集合，并在 unary/binary operations 前明示 `equiv`、congruence、membership和type guards。它正因 formation route 与 Book 的 \(\mathcal P(A)\)-subset route 不同，且 payment 已明示，而被判为 `ADMISSION_REJECTED_WITH_SCOPE`；这是一项 route-split control，不是 Q。

第六份预检是 [HMZ-011 Dochtermann totality bridge](20261003-HMZ-011-dochtermann-totality-preflight/MANIFEST.md)。它不是 HoTT 动机来源，而是一个有明示有限 Done／无限 totality／Power Set hand-off的 E-source；因此被准入为 HMZ-012 的冻结分母。HMZ-012 已表明它支撑一项 `REALITY_TASK_TO_TOTALITY_CONSTRUCTION_BRIDGE`，却没有让有限分类过程与形式 set-existence成为同一 Done；不能借其哲学修辞宣称 ZFC Q。

第七份预检是 [HMZ-013 universe shift 的 H0 传输](20261003-HMZ-013-universe-shift-h0-preflight/MANIFEST.md)。Voevodsky 的 type-universe 模型确实连接到“ZFC with \(\omega+2\) universes”，Shulman 的 Grothendieck universe source 也给出实际 universe-juggling consumer；但它们运行在 model/large-cardinal scope，并且 Shulman 明说换 universe 后没有理由认为同一个 \(G\) 保持原性质。该来源因此成为 `H0→Z0` 的反类比／payment control，状态为 `ADMISSION_REJECTED_WITH_SCOPE`。

第八份预检是 [HMZ-014 schema/operator/truth](20261003-HMZ-014-schema-operator-truth-preflight/MANIFEST.md)。它检查 H9 的逐公式 Separation schema 是否会被实际来源升级为 whole-\(V\) 的统一 `Build(p,a)`。Koepke–Koerwien 的可用 truth 装置反而明示 formula code、语言、结构、ordinal recursion、machine semantics和reflection；Shulman也区分单个 schema 与代码化的 all-axioms truth。故这是 `SCHEMA_OPERATOR_CONTROL / ADMISSION_REJECTED_WITH_SCOPE`，没有形成P2/P3/P4/P5的ZFC Q。

第九份预检是 [HMZ-015 predicativity/VCP](20261003-HMZ-015-predicativity-vcp-preflight/MANIFEST.md)。Feferman 2002 的历史与哲学来源表明，Russell/Poincaré、vicious circle、completed totality和ZF impredicativity已有深厚的社区 antecedent；这足以触发 HMZ-016 的完整字段比较，却不足以把用户P的consumer/preemptive-use/same-Done要求视为已经被该文献穷尽。

## 本次整备的影响边界

| 项目面 | 处置 |
|---|---|
| 用户要求／路线 | `UPDATE`：调用名、来源调查和存档范围已固定。 |
| SOP／Skill／任务路由 | `UPDATE`：项目 Skill、SOP、AGENTS、TASK_ROUTING和SKILL_ROLES已连接。 |
| Archive／证据 | `UPDATE`：档案根、run ID、coverage与原件身份合同已定义。 |
| 外部来源／下载 | `UPDATE`：已归档可公开取得的 IAS/arXiv/Brown/Metamath 原件，并保留访问失败的边界；未使用登录、付费或远程 OCR。 |
| worker／P-DAG／数学结论／STATE／Power Set station | `NO_CHANGE`：本 run 没有启动 worker、P-DAG、STATE mutation 或数学证明；Power Set 未被升级为候选。 |
