# ZQCM-002 M0：查询与覆盖矩阵

> **状态：** `COMPLETE_WITH_SCOPE / QUERY_DICTIONARY_FROZEN / COVERAGE_SEED_PROJECTION_COMPLETE / FIRST_PLATFORM_PROBES_COMPLETE / FORMAL_AUTHOR_AND_BRIDGE_ENTRIES_COMPLETE / FIRST_ACQUISITION_BATCH_READY_TO_FREEZE`。
>
> **证据边界：** 本表规定地图分母和检索入口；它不表示任何条目已经取得、筛读或成为 Q。

## A–E 轴查询卡

| Axis | 精确问题 | OpenAlex 首轮 query | 交叉平台／作者入口 | 现有种子 | 当前缺口 |
|---|---|---|---|---|---|
| A 基础形成 | ZFC 的对象如何由公理形成，Power Set／Replacement／Separation／Foundation 的范围和标准防线如何被表述？ | `"Zermelo Fraenkel" axioms power set replacement separation` | zbMATH：`Zermelo Fraenkel power set replacement`；原典／历史：Zermelo、Fraenkel、von Neumann、标准集合论文本 | ZQCM-001 W-005、V-SET-02、W-013；HMZ-007/010 | 原典、正式公理史、Power Set/Replacement 实际 consumer 与反控制未系统映射。 |
| B 总体与阶段 | potential/actual hierarchy、impredicativity、Vicious Circle、truth/schema、reflection 如何与固定 ZFC formation 相连？ | `"potential hierarchy" set theory predicativity impredicativity` | PhilPapers：potential hierarchy / iterative conception / impredicativity；zbMATH：predicativity / reflection / truth predicate | W-012/W-014 metadata、W-013、HMZ-014/015/016 | W-012/W-014全文、阶层与schema的ZFC侧consumer、非英语历史原典。 |
| C 语义与独立性 | forcing/model/independence/large-cardinal/inner-model 文献如何明示支付与理论层边界？ | `forcing model theory independence large cardinals ZFC` | zbMATH：forcing / large cardinals / inner model；作者：Cohen、Gödel、Jech、Kunen、Woodin、Shelah | W-004、W-008、W-015、V-SET-01/02；HMZ-008/013 | 主要 forcing／inner-model／determinacy/large-cardinal 文献与普通ZFC consumer尚未建立分母。 |
| D 真实消费者 | 哪些 ordinary set-theoretic、formalization、proof-checking 或具体数学工作固定 `u/F/C/I/O/Done`？ | `ZFC proof assistant formalization set theory practice` | Isabelle/ZF、Metamath、Lean/Mathlib；实践访谈／专题论文；作者/项目源码 | V-SET-01、W-007、HMZ-003/010/018/020 | 真实 bare-ZFC consumer、数学实践消费者及同一Done仍是核心缺口。 |
| E 外部反投影 | HoTT/UF、MLTT、CZF/IZF、realizability、ETCS/结构主义怎样精确给出 R→Z→Q 或 payment control？ | `homotopy type theory set theory foundations` | arXiv：HoTT/UF；作者／IAS／会议；PhilPapers；HOTT-MOTIVE map | ZQCM-001 W-001/002/003/005–011/013；HMZ 9 runs | HoTT作者全语料、CZF/IZF/ETCS、结构主义与ZFC侧保真桥尚未地图化。 |

## 已覆盖种子投影

| Axis | 已有冻结控制 | 覆盖等级 | 不可从该种子推出的结论 |
|---|---|---|---|
| A | Power Set／Replacement邻域、CZF formation、ZFCS/NBGS比较、标准Russell防线 | `PARTIAL_CONTROL` | 不能据此说已覆盖 ZFC 原典、公理史或 Power Set 的全部消费者。 |
| B | predicativity/Vicious Circle、schema/truth、potential/iterative metadata 与 CZF control | `PARTIAL_SEED` | 不能据此说阶段形成已给出 ZFC Q。 |
| C | classical realizability、large-cardinal models、singular-cardinal quasi-completeness、实践模型支付 | `PARTIAL_CONTROL` | 不能据此说 forcing/independence/large-cardinal 文献全覆盖。 |
| D | Isabelle/ZF、Metamath、实践访谈、proof/program与realizability controls | `PARTIAL_CONTROL` | 没有 ordinary bare-ZFC same-Done consumer。 |
| E | HoTT/UF 动机、H0 anti-analogy、CZF/realizability/category comparison | `PARTIAL_CONTROL` | HoTT动机不等于 ZFC 缺陷或保真传输。 |

## M0 完成条件

1. 每个 A–E 轴至少有一个实际执行的书目平台探针、一个原典/作者或正式来源入口、一个引文／bridge入口；
2. 每个 axis 的已覆盖种子、未覆盖 cell、语言与访问余项都可重算；
3. 所有平台的 query、日期、分页/限制与前排结果进入 `M0-SEARCH-LOG.md`；
4. 只有在该表能指出未覆盖 cell 时，才建立 M1–M6 的 acquisition batch。

## 已执行的 M0 入口检查

| Axis | 书目平台探针 | 原典／作者／正式入口 | 引文／bridge 入口 | 当前 M0 判词 |
|---|---|---|---|---|
| A | `M0-OA-A`：OpenAlex 精确 query，288 条原始返回，首屏噪声高。 | `M0-FOR-A`：GDZ 的 Zermelo 1908 扫描；SEP 的 ZF 公理与历史页面。 | `M0-BRIDGE-A`：SEP set-theory/ZF 的历史、公式与参考文献入口。 | `ENTRY_COMPLETE / ORIGINAL_AND_AXIOM_HISTORY_NOT_YET_ACQUIRED_OR_SCREENED` |
| B | `M0-OA-B`：OpenAlex 精确 query，14 条原始返回。 | `M0-FOR-B`：Feferman Stanford 作者论文目录。 | `M0-BRIDGE-B`：Feferman publications bibliography。 | `ENTRY_COMPLETE / POTENTIALISM_AND_PREDICATIVITY_SOURCE_FAMILY_NOT_YET_FROZEN` |
| C | `M0-OA-C`：OpenAlex 精确 query，915 条原始返回，首屏 Zenodo 噪声高。 | `M0-FOR-C`：Cohen 1963 PNAS/PMC 记录。 | `M0-BRIDGE-C`：IMU 1966 Fields archive 对 forcing／独立性的归档入口。 | `ENTRY_COMPLETE / FORCING_AND_MODEL_FAMILY_REQUIRES_SOURCE-SPECIFIC_QUERIES` |
| D | `M0-OA-D`：OpenAlex 精确 query，160 条原始返回，混有教学与非 ZFC 系统。 | `M0-FOR-D`：Isabelle 官方 `Logics: FOL and ZF` 文档。 | `M0-BRIDGE-D`：Isabelle libraries 对 `isarmathlib` 的索引。 | `ENTRY_COMPLETE / ORDINARY_BARE-ZFC_SAME-DONE_CONSUMER_NOT_FOUND_BY_METADATA_PROBE` |
| E | `M0-OA-E`：OpenAlex 精确 query，10,714 条原始返回，过宽。 | `M0-FOR-E`：HoTT Book 官方站及版本化下载入口。 | `M0-BRIDGE-E`：HoTT 官方 references 页，另接既有 HOTT-MOTIVE map。 | `ENTRY_COMPLETE / R-Z-Q_BRIDGES_REQUIRE_WORK-BY-WORK_FIDELITY_SCREEN` |

这些入口满足 M0 的最小平台／来源／bridge 条件，因此本轮 M0 骨架达到 `COMPLETE_WITH_SCOPE`。A–E 的语言、时期、数据库交叉覆盖、重复消解、引文外延和高优先级 remainder 是 M1–M6 的工作分母；若某一新理论位置、来源平台或语言改变本页 A–E 分类，M0 以新增版本重开。任何记录中的标题或题录均只是筛选候选，不是来源内容、Q lead 或数学结论。

## 语言、时期、访问与平台 remainder

| Axis | 当前已显式覆盖 | 尚未覆盖或未核对 | 访问／版本状态 | 进入下一波的条件 |
|---|---|---|---|---|
| A | 英文现代公理概述；德文 1908 Zermelo 原典的馆藏定位；OpenAlex 元数据。 | Fraenkel／Skolem／von Neumann 原典、Zermelo 后期版本、每个公理簇的教材与实际 consumer；非英语二级史料。 | GDZ 扫描入口为公开访问线索，未取得/核验工作版本。 | M1 只可选身份可核、理论位置明确、可取得版本的一条原典或标准文本路线。 |
| B | 英文 Feferman 作者目录/书目、英语 potentialism/iterative-conception 元数据。 | 早期法德文原典、truth/reflection 的逻辑学文献、与固定 ZFC formation 的实际连接。 | Feferman PDF 入口公开；尚未作为 ZQCM-002 原件处理。 | M2 需要一个来源可将阶段／总体论述接到固定规则或 consumer，否则只留 seed/control。 |
| C | 英文 Cohen PNAS 身份、IMU 影响入口、OpenAlex 高噪声原始池。 | Gödel／forcing 经典文献、inner model、large cardinal、determinacy、不同语言的历史/技术来源；普通 ZFC 用法。 | Cohen 有 PMC/PNAS 访问入口；未冻结 version。 | M3 先拆 source-specific query，并区分模型、相对一致性和普通消费者。 |
| D | 英文 Isabelle 官方文档、libraries index、OpenAlex formalization/teaching 混合池。 | Metamath、Lean/Mathlib、ordinary set-theoretic papers、实践记录、非英语 formalization；same-Done consumer。 | 官方在线文档可访问；源码版本与具体 consumer 尚未冻结。 | M4 只接受可固定输入、输出、观察和 Done 的 source card。 |
| E | 英文 HoTT Book 官方版本入口、官方 reference 页、OpenAlex HoTT/set-theory候选池、既有 HMZ runs。 | HoTT 作者完整动机文本、CZF/IZF/ETCS/结构主义的独立文献族、非英语来源、版本间差异与精确 ZFC bridge。 | HoTT Book 公开版本化下载；既有 HMZ 原件按其 own manifest 处理。 | M5 只接受具有可审 `R→Z→Q` 或明确 anti-analogy 的 work-by-work route。 |

这张 remainder 表的分母是本计划 §2 的 A–E 轴与本页查询卡，不是世界书目。它使下一波的冻结选择可从确定的缺口出发，而不从搜索排序或训练记忆出发。
