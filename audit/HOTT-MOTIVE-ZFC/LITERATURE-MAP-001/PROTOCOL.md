# LITERATURE-MAP-001 协议

> **身份：** FROZEN_M0_PROTOCOL / MAP_PROTOCOL_DEFINED / SEARCH_PEER_REVIEW_NOT_AVAILABLE。
>
> **冻结日期：** 2026-10-03。
>
> **范围：** HoTT／UF 创建动机、其集合论基础对比、罗素模式 P 的历史前身、形成／交付／realizability、以及实际数学／证明助手消费者。

## 1. 研究问题

| ID | 问题 | 地图轴 |
|---|---|---|
| M-Q1 | HoTT／UF 作者和早期权威文本怎样说明已有集合论基础下的动机、限制或能力目标？ | M-A |
| M-Q2 | 哪些 ZF/ZFC、NBG、ETCS、类理论、predicatitivity 或逻辑史来源讨论与 formation、completed totality、自指、Power Set、Separation、Replacement 有关的立场？ | M-B / M-E |
| M-Q3 | 哪些构造主义、realizability、类型论、证明论与形式化文献区分 set existence、proof、program、termination、verification 或 delivery？ | M-C |
| M-Q4 | 哪些已发表数学、类别论或 proof-assistant 消费者实际使用这些对象，并公开给出 choice、label、map、formation 或 computation 的 payment？ | M-D |
| M-Q5 | 上述语料中是否有来源足以生成一个新的、尚未被现有 P 矩阵控制的 R/Z/Q/E 输入？ | M-A 至 M-E 的 bridge |

## 2. 语料边界

| 维度 | 冻结规则 |
|---|---|
| 时期 | Russell／Poincaré 的历史原典至 2026-10-03；对 HoTT/UF 的 primary motive 重点覆盖 2006 至今。 |
| 语言 | 首轮优先英语；德语、法语、俄语及其他语言的强引用必须记录为可得、不可得或语言限制，不能静默排除。 |
| 发表类型 | 期刊、书、会议卷、作者讲演、arXiv、正式项目文档、证明助手源码／文档、博士论文和可核验学术综述。 |
| 排除 | 只有泛泛关键词相似、没有理论／任务关系的材料；无法识别作品身份的转载；有一手来源时不作为同一主张的唯一二手依据。 |
| 非目标 | 统计元分析、引用数排名、用文献数量替代 Q 资格，或直接证明 ZFC 有矛盾。 |

## 3. 检索来源宇宙

| Source family | 首轮角色 | 访问与记录要求 |
|---|---|---|
| zbMATH Open / MathSciNet | 数学与逻辑书目主检索；MathSciNet 仅在实际访问可用时进入。 | 保存平台、query、日期、命中和访问限制。 |
| arXiv | HoTT、类型论、逻辑、形式化项目的开放预印本。 | 保存 search endpoint、query、版本和 arXiv ID。 |
| Crossref / OpenAlex | 跨学科元数据、DOI、作者和 cited-by／references discovery。 | 保存 API URL、参数、日期、分页和字段限制。 |
| PhilPapers / logic-history bibliographies | 数学哲学、逻辑史与 predicatitivity 语料。 | 保存网站 query、日期、命中与导出／截断限制。 |
| 作者／机构／会议／出版社页面 | primary motive、讲演、正式版本和历史 archive。 | 记录 provenance 和不能由网页检索替代的版本边界。 |
| proof-assistant 官方源码／文档 | actual consumer 和 implementation layer。 | 固定 repo、commit／release、路径和 source layer。 |
| 普通网页／Google Scholar | 只作补充发现、访问失败替代或 author lead。 | 不作为唯一可重复分母；保存 query 和截断事实。 |

## 4. 初始 query family

每个平台按其语法分别记录实际执行的 query；下列仅是概念族，不能代替 SEARCH-LOG 中的原样字符串。

| Query family | 目标 |
|---|---|
| univalent foundations AND set theory; homotopy type theory AND foundations | M-A 的 author／early authority corpus。 |
| Voevodsky AND set theory; Voevodsky AND type systems; Voevodsky AND proof assistant | 作者动机与具体对比。 |
| ZFC AND predicativity; ZFC AND vicious circle; power set AND impredicative | M-B／M-E 的历史和基础立场。 |
| classical realizability AND ZF; constructive logic AND set existence; proof program correspondence AND ZF | M-C 的 delivery contract。 |
| ZFC AND proof assistant; set theory AND formalization; category theory AND choice AND skeleton | M-D 的实际消费者和 payment。 |
| univalence AND equivalence principle; structure identity principle AND set theory | M-A 至 M-D 的 bridge 与反控制。 |

## 5. 筛选、去重与引文追踪

同一 intellectual work 的预印本、正式版、讲演、译本和转载合并为一个 work family；每个 report 的版本身份仍保留。每条结果进入 SCREENING 后才计入 covered corpus。

种子 backward/forward tracing 以既有 HMZ-S-001、002、003、010、011、028、029、030、031、032 为起点。每轮引文追踪必须记录所用平台、被追踪种子、得到记录数、去重数、纳入数、排除数和停止原因。

## 6. 质量、停止与局限

首轮达到 MAP_EXECUTION_ACTIVE 的最低条件，是至少一个书目 API／数据库、一个 author-primary source channel 和一个 citation channel 都按 SEARCH-LOG 记录实际执行。达到 MAP_COMPLETE_WITH_SCOPE 前，必须完成所有冻结 query family、声明的来源平台、种子双向追踪和 COVERAGE-MAP 余项处置。

本 protocol 没有独立的人类或信息检索专家同行复核，因此必须始终保留 SEARCH_PEER_REVIEW_NOT_AVAILABLE。AI 的第二次阅读、来源卡或 P-DAG worker 都不等同于独立检索审阅。
