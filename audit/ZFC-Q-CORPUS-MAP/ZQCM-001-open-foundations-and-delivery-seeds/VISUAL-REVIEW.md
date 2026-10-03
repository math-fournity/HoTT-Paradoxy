# ZQCM-001 Visual Review

> **身份：** REMOTE_DERIVATIVE_VISUAL_EVIDENCE / NO_Q_CLAIM。
>
> **顺序：** 已验证 PDF → remote standard MinerU 原始导出 → 150dpi二值页图逐页核验 → 关键／异常页300dpi复核 → 文献阅读与Q资格化。
>
> **状态：** W005_W011_W013_SOURCE_ONLY_VISUAL_CHECK_COMPLETE / W010_TARGETED_SOURCE_ONLY_CHECK / REMOTE_DERIVATIVE_NOT_QUALIFIED。

## 结果语义

| 结果 | 含义 | 对后续阅读的作用 |
|---|---|---|
| `VISUAL_PASS` | 所核页的题录／结构／公式锚点与远程派生物未见材料差异。 | 派生物可作为导航和检索辅助；原PDF仍是引文权威。 |
| `VISUAL_PASS±` | 版面、连字、间距等瑕疵不改变所核内容。 | 记录具体瑕疵后可作导航；关键引文仍回PDF。 |
| `SOURCE_PRIORITY` | 派生物在该页或段落发生材料性遗漏、误读或无法可靠对齐。 | 该段只能从原PDF阅读和引用；不编辑 remote 原始输出。 |
| `SOURCE_ONLY_VISUAL_CHECK` | remote MinerU未取得可用导出时，页图与原PDF文本层的身份／可读性核验。 | 只证明原件页的视觉证据和文本层对齐；不构成MinerU输出质量结论。 |
| `UNREVIEWED` | 尚未作实际视觉检查。 | 不得作为Q LeadCard或关键来源断言的依据。 |

## 页级记录

remote MinerU恢复后，按一页一条追加派生物与原PDF的对照。当前已对source-only页面记录 PDF 页、150dpi图、文本层定位、核对项目、结果和必要300dpi图。

| VR ID | Work ID | PDF页 | 150dpi图 | MinerU定位 | 核对／结果 | 300dpi仲裁 |
|---|---|---:|---|---|---|---|
| VR-W005-001 | W-005 | 1 | visual/W-005/150dpi/p001.png | `pdftotext` PDF p.1；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：150dpi核标题、作者、期刊／DOI、摘要、关键词、§1和两条脚注；均与文本层及PDF metadata一致。 | visual/W-005/300dpi/p001.png：复核期刊题录、题名、作者和摘要，未见材料性差异。 |
| VR-W005-002 | W-005 | 2 | visual/W-005/150dpi/p002.png | `pdftotext` PDF p.2；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核页眉、集合论／类型论段落、元素归属记号、判断与命题的区分、定义性等式示例及脚注3–4；可读且与文本层逐段对应。 | 不适用：本页不承担Q相关关键公式的最终引用。 |
| VR-W005-003 | W-005 | 3 | visual/W-005/150dpi/p003.png | `pdftotext` PDF p.3；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核§1.1题名、Maddy讨论、关于“what is wrong with ZFC”的作者表述、ETCS脚注及其后对论文目标的限定；页图与文本层一致。该处只是作者动机来源，尚非ZFC Q。 | 不适用：待R/Z/Q路线实际资格化后决定是否作高精度复核。 |
| VR-W005-004 | W-005 | 4 | visual/W-005/150dpi/p004.png | `pdftotext` PDF p.4；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核§2题名、propositions-as-types段落、蕴含／全称／否定翻译、子集的Σ型表示及脚注7–11；公式与文本层可对齐。 | 不适用：页5处理存在／选择的关键后续。 |
| VR-W005-005 | W-005 | 5 | visual/W-005/150dpi/p005.png | `pdftotext` PDF p.5；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：150dpi核Σ型存在、`ac`公式、propositional truncation、第二个choice公式、Diaconescu和排中式；文本层与版面一致。该页是R/Z映射的潜在线索，不是Q结论。 | visual/W-005/300dpi/p005.png：逐符号复核两个choice公式、`\|\|A\|\|`、脚注12–14；未见材料性差异。 |
| VR-W005-006 | W-005 | 6 | visual/W-005/150dpi/p006.png | `pdftotext` PDF p.6；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核`Prop`／negative propositions、classical existence、`Prop_class`、unique choice公式和定义；与文本层和页脚15一致。 | 不适用：页5已承担这一存在／choice段的高精度核验。 |
| VR-W005-007 | W-005 | 7 | visual/W-005/150dpi/p007.png | `pdftotext` PDF p.7；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核§3、von Neumann／Zermelo自然数编码、Infinity／Replacement表述、非结构性质的转移问题和递归原则；均与文本层对齐。 | visual/W-005/300dpi/p007.png：复核两组编码、`n⊆n+1`、`1⊄2`及递归记号；未见材料性差异。 |
| VR-W005-008 | W-005 | 8 | visual/W-005/150dpi/p008.png | `pdftotext` PDF p.8；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核initial-algebra／自然数对象、数系嵌入、subset／comprehension的对照、最小性与W-types／HIT段落及脚注16；文本层与视觉页一致。 | 不适用：表示线的关键编码已在p.7高精度核验。 |
| VR-W005-009 | W-005 | 9 | visual/W-005/150dpi/p009.png | `pdftotext` PDF p.9；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核§4、`f(x)=x+0`／`g(x)=0+x`、ITT equality段落、function／propositional extensionality、univalence脚注17和结构的表述；版面与文本层一致。 | visual/W-005/300dpi/p009.png：逐符号复核函数等式、`refl(a):a=a`与脚注17的equivalence限定；未见材料性差异。 |
| VR-W005-010 | W-005 | 10 | visual/W-005/150dpi/p010.png | `pdftotext` PDF p.10；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核同构结构、proof-relevant equality、setoid、无限等式塔／weak infinity groupoids及脚注18–22；视觉页与文本层对应。 | 不适用：p.9已对§4入口和等式公式做高精度核验。 |
| VR-W005-011 | W-005 | 11 | visual/W-005/150dpi/p011.png | `pdftotext` PDF p.11；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核§5、显式choice／proposition、univalent category与skeletal category段落，以及§6开头；与文本层一致。该页提供动机和竞争解释来源，尚未建立ZFC同一任务。 | visual/W-005/300dpi/p011.png：复核结构主义／构造性、choice和category段的限定词及脚注23；未见材料性差异。 |
| VR-W005-012 | W-005 | 12 | visual/W-005/150dpi/p012.png | `pdftotext` PDF p.12；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核§6余段、作者关于set representation／machine-language的比较、逻辑与可解释性段、开放许可和脚注24；视觉页与文本层一致。所有评价保持作者立场，非本项目结论。 | visual/W-005/300dpi/p012.png：复核“assign”段、CC BY 4.0许可与脚注24；未见材料性差异。 |
| VR-W005-013 | W-005 | 13 | visual/W-005/150dpi/p013.png | `pdftotext` PDF p.13；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核References逐条、尤其Altenkirch 2019、Ahrens–North 2019、Maddy 2019、HoTT Book与Cubical Agda来源；页图和文本层可对齐。 | visual/W-005/300dpi/p013.png：复核关键书目作者、年份、页码和arXiv标识，未见材料性差异。 |
| VR-W010-001 | W-010 | 1 | visual/W-010/150dpi/p001.png | `pdftotext` PDF p.1；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核chapter题名、副题、作者、摘要、foundation jobs的限定及DOI／页码；与文本层和PDF身份一致。 | visual/W-010/300dpi/p001.png：复核摘要与“不同jobs”的限定，未见材料性差异。 |
| VR-W010-016 | W-010 | 16 | visual/W-010/150dpi/p016.png | `pdftotext` PDF p.16；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核Univalent Foundations／formalized ZFC比较、Essential Guidance／Generous Arena／Shared Standard、Metamathematical Corral／Risk Assessment，以及脚注25–29。 | visual/W-010/300dpi/p016.png：逐字复核脚注28的“I'm not sure what these thinkers take to be wrong with ZFC”与ETCS/ZFC比较限定；该不确定性是来源反控制，非ZFC无问题结论。 |
| VR-W010-017 | W-010 | 17 | visual/W-010/150dpi/p017.png | `pdftotext` PDF p.17；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核§13.4结论中对Risk Assessment、Metamathematical Corral、Generous Arena、Shared Standard、Proof Checking及set theory与新理论并存的表述；与文本层一致。 | visual/W-010/300dpi/p017.png：复核结论限定，尤其“不需要替换set theory”的作者判断；这是竞争读法／控制，不是项目结论。 |
| VR-W009-002 | W-009 | 2 | visual/W-009/150dpi/p002.png | `pdftotext` PDF p.2；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核§2标题、naive Set／Type Theory对照、`3∈N`／`3:N`、judgement与静态type information及脚注1–2；与文本层一致。 | visual/W-009/300dpi/p002.png：复核归属记号、judgement限定和subtyping脚注；该是R-source，不是ZFC Q。 |
| VR-W009-015 | W-009 | 15 | visual/W-009/150dpi/p015.png | `pdftotext` PDF p.15；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核weak `ω`-groupoid、choice／cubical alternative、§5.2、choice公式、Σ型existence、`isProp`和negative fragment；与文本层一致。 | visual/W-009/300dpi/p015.png：逐符号复核choice公式、Σ、`isProp A`与“witness explicit”限定；只作为P5对照来源，尚非ordinary ZFC consumer。 |
| VR-W009-020 | W-009 | 20 | visual/W-009/150dpi/p020.png | `pdftotext` PDF p.20；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核`A,B:Set`、`1+2`／`2+1`、isomorphism、`eq2iso`、`extSet`及练习25；与文本层一致。 | visual/W-009/300dpi/p020.png：逐符号复核等式、isomorphism和extensionality定义；该是类型论内部 `Set` 的作者比较，不能直接投射为ZFC Q。 |
| VR-W011-001 | W-011 | 1 | visual/W-011/150dpi/p001.png | `pdftotext` PDF p.1；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核标题、作者、abstract四主题、标准axiomatic set theory／ZFC范围与identity／extensionality声明；与文本层一致。 | visual/W-011/300dpi/p001.png：复核abstract中关于identity criterion与extensionality的作者论证范围；不是Q结论。 |
| VR-W011-016 | W-011 | 16 | visual/W-011/150dpi/p016.png | `pdftotext` PDF p.16；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核§4起始、identity judgement/proposition区分、`Id`形成规则和function application regress段；与文本层一致。 | visual/W-011/300dpi/p016.png：复核逻辑语法层的范围、identity formula和作者限定；需要另建ZFC语义／consumer桥，不能直接外推。 |
| VR-W011-017 | W-011 | 17 | visual/W-011/150dpi/p017.png | `pdftotext` PDF p.17；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核Well-def公式、functionhood预设identity、judgemental versus propositional identity与概念优先论证；与文本层一致。 | visual/W-011/300dpi/p017.png：复核循环论证条件、primitive rule和版本依赖限定；当前只可作P2逻辑层／R-source比较。 |
| VR-W011-018 | W-011 | 18 | visual/W-011/150dpi/p018.png | `pdftotext` PDF p.18；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核rational-number example、criterion-of-identity论证、ZFC extensionality公式、universe `V` 的预设性及type-theory对照；与文本层一致。 | visual/W-011/300dpi/p018.png：逐符号复核`a=b↔∀x(x∈a↔x∈b)`、`V`和作者的“cannot be regarded”限定；形成Extensionality site seed，不构成Q。 |
| VR-W011-002 | W-011 | 2 | visual/W-011/150dpi/p002.png | `pdftotext` PDF p.2；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核作者把本文限定为conceptual comparison、四个主题及`sets and types`入口；与文本层一致。 | 不适用：不承担Q相关最终引文。 |
| VR-W011-003 | W-011 | 3 | visual/W-011/150dpi/p003.png | `pdftotext` PDF p.3；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核Cantor／Zermelo sets/domains区分、Aczel 1978的CZF／type `V`引文及ordinal domains段；与文本层一致。 | 不适用：Aczel原典由W-013单独高精度审读。 |
| VR-W011-004 | W-011 | 4 | visual/W-011/150dpi/p004.png | `pdftotext` PDF p.4；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核pluraliy/unity、set与type的哲学区分及脚注；与文本层一致。 | 不适用：本页是概念背景。 |
| VR-W011-005 | W-011 | 5 | visual/W-011/150dpi/p005.png | `pdftotext` PDF p.5；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核set与type的topic-neutral／sort区别及历史性脚注；与文本层一致。 | 不适用：本页不固定ZFC consumer。 |
| VR-W011-006 | W-011 | 6 | visual/W-011/150dpi/p006.png | `pdftotext` PDF p.6；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核§2 syntax、type structure、higher types／dom及dependent-function说明；与文本层一致。 | 不适用：类型论框架背景。 |
| VR-W011-007 | W-011 | 7 | visual/W-011/150dpi/p007.png | `pdftotext` PDF p.7；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核propositions-as-types、type `V`的比较描述、functions和`Terms and types`入口；与文本层一致。 | 不适用：不是ordinary ZFC形成记录。 |
| VR-W011-008 | W-011 | 8 | visual/W-011/150dpi/p008.png | `pdftotext` PDF p.8；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核set-theory language、variable binding、type-theoretic primitive vocabulary与introduction／elimination rules；与文本层一致。 | 不适用：比较性语言论证。 |
| VR-W011-009 | W-011 | 9 | visual/W-011/150dpi/p009.png | `pdftotext` PDF p.9；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核type theory openness和§2.3 judgements的开始、categorical judgement forms；与文本层一致。 | 不适用：不承担Q相关最终引文。 |
| VR-W011-010 | W-011 | 10 | visual/W-011/150dpi/p010.png | `pdftotext` PDF p.10；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核`a:A`与`a∈b`对照、set-theoretic universe `V`、metalinguistic statement限制；与文本层一致。 | 不适用：该是作者的语言层比较，不能直接外推ZFC object-layer问题。 |
| VR-W011-011 | W-011 | 11 | visual/W-011/150dpi/p011.png | `pdftotext` PDF p.11；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核judgement／proposition、theorem、assertion与truth段；与文本层一致。 | 不适用：未交付ZFC actual consumer。 |
| VR-W011-012 | W-011 | 12 | visual/W-011/150dpi/p012.png | `pdftotext` PDF p.12；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核set-theory object／meta-language judgement、hypothetical judgements及context；与文本层一致。 | 不适用：不形成P再入结论。 |
| VR-W011-013 | W-011 | 13 | visual/W-011/150dpi/p013.png | `pdftotext` PDF p.13；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核§3 functions、type-theoretic application rules、set-theoretic function说明；与文本层一致。 | 不适用：函数比较背景。 |
| VR-W011-014 | W-011 | 14 | visual/W-011/150dpi/p014.png | `pdftotext` PDF p.14；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核elementhood／identity的predicate-functional分析、Def-F与set-theoretic definition of application；与文本层一致。 | 不适用：作者没有在该页提供actual consumer。 |
| VR-W011-015 | W-011 | 15 | visual/W-011/150dpi/p015.png | `pdftotext` PDF p.15；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核function types、lambda/application及Frege comparison；与文本层一致。 | 不适用：不把关于Frege的论述外推为ZFC Q。 |
| VR-W011-019 | W-011 | 19 | visual/W-011/150dpi/p019.png | `pdftotext` PDF p.19；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核concluding remarks；作者称比较为conceptual architecture／ideology，并写set theory作为foundation的成功；与文本层一致。 | 不适用：这是`SOURCE_PRECISION_GAIN_NOT_Q`的反控制。 |
| VR-W011-020 | W-011 | 20 | visual/W-011/150dpi/p020.png | `pdftotext` PDF p.20；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核references中Aczel 1978、Klev 2018a/b、Linnebo 2010及其他相邻来源；与文本层一致。 | 不适用：书目只产生受限的citation lead。 |
| VR-W011-021 | W-011 | 21 | visual/W-011/150dpi/p021.png | `pdftotext` PDF p.21；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核references尾部、Linnebo/Rayo、Martin-Löf、Zermelo及末页边界；与文本层一致。 | 不适用：不承担Q相关引文。 |
| VR-W013-001 | W-013 | 1 | visual/W-013/150dpi/p001.png | `pdftotext` PDF p.1；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核Logic Colloquium '77／North-Holland 1978题录、题名、Peter Aczel、摘要和Introduction开头；视觉页与metadata／文本层一致。 | visual/W-013/300dpi/p001.png：复核“type of sets”、constructive interpretation和cumulative hierarchy限定；为CZF／类型论控制，不是ZFC Q。 |
| VR-W013-002 | W-013 | 2 | visual/W-013/150dpi/p002.png | `pdftotext` PDF p.2；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核ZFC/CZF／类型论动机、explicit constructive notions、extensionality、constructive meaning与stages of Leversha's construction；与文本层一致。 | visual/W-013/300dpi/p002.png：逐句复核CZF是使用intuitionistic logic的ZF子系统、type theory是constructions的framework等范围限定；不投射为ordinary ZFC consumer。 |
| VR-W013-003 | W-013 | 3 | visual/W-013/150dpi/p003.png | `pdftotext` PDF p.3；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核§1、CZF first-order language、structural／set-existence axioms、Subset Collection、Infinity及remarks；公式块可读且与文本层对应。 | 不适用：p.4–5承担Power Set关系的高精度核验。 |
| VR-W013-004 | W-013 | 4 | visual/W-013/150dpi/p004.png | `pdftotext` PDF p.4；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核§2、CZF与ZF关系、`A`-full set、2.1及2.2 Power Set→Subset Collection→Exponentiation、2.3；与文本层一致。 | visual/W-013/300dpi/p004.png：逐符号复核2.2／2.3结论及其CZF范围；这是Power Set control，不是候选Q。 |
| VR-W013-005 | W-013 | 5 | visual/W-013/150dpi/p005.png | `pdftotext` PDF p.5；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核2.4–2.7、restricted excluded middle、full separation、ZF结论及POW／SEP／REM图前文字；与文本层一致。 | visual/W-013/300dpi/p005.png：复核条件化的Power Set推演与三系统同定理的表述；标准支付／理论变体保持分层。 |
| VR-W013-006 | W-013 | 6 | visual/W-013/150dpi/p006.png | `pdftotext` PDF p.6；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核CZF／IZF／ZF系统图、`IZF`说明与§3 type-theoretic framework开头；视觉和文本层一致。 | 不适用：p.7–8承担`U`／set recursion的高精度核验。 |
| VR-W013-007 | W-013 | 7 | visual/W-013/150dpi/p007.png | `pdftotext` PDF p.7；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核proposition/type对应、`U`为type of sets、intro／elimination、set recursion和§4的集合形成例；与文本层一致。 | visual/W-013/300dpi/p007.png：逐符号复核indexed family→new set、small type及set recursion的限定；这是明示形成规则。 |
| VR-W013-008 | W-013 | 8 | visual/W-013/150dpi/p008.png | `pdftotext` PDF p.8；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核有限／无限集合例、ordinary/double set recursion、extensional equality、membership、validity目标；与文本层一致。 | visual/W-013/300dpi/p008.png：复核递归定义、equality／membership类型及`Every theorem of CZF is valid`的范围；不跨层认定ZFC Q。 |
| VR-W013-009 | W-013 | 9 | visual/W-013/150dpi/p009.png | `pdftotext` PDF p.9；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核§5 structural axioms validity、equality／membership/invariance与§6开头；公式及页眉可读。 | 不适用：本页不承担新的Q相关最终引文。 |
| VR-W013-010 | W-013 | 10 | visual/W-013/150dpi/p010.png | `pdftotext` PDF p.10；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核Pairing、Union、Restricted Separation、Strong／Subset Collection与Infinity的type-theoretic validity constructions；与文本层一致。 | 不适用：p.11处理presentation／choice的高精度页。 |
| VR-W013-011 | W-013 | 11 | visual/W-013/150dpi/p011.png | `pdftotext` PDF p.11；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核§7、DC、base／presentation定义、PA、representational availability及CZF^I／realizability补偿路线；与文本层一致。 | visual/W-013/300dpi/p011.png：逐字复核“particular way the set is given”、`Every set has a presentation`与缺少可用表示的限定；这是显式payment control。 |
| VR-W013-012 | W-013 | 12 | visual/W-013/150dpi/p012.png | `pdftotext` PDF p.12；remote output unavailable | `SOURCE_ONLY_VISUAL_CHECK`：核References、Aczel／Friedman／Grayson／Leversha／Martin-Löf／Myhill等书目和末页边界；与文本层一致。 | 不适用：不承担Q相关引文。 |

## 高精度队列

已完成W-005的7个关键页、W-010的3个关键页、W-011的4个关键页和W-013的7个关键页；其余候选包括任何可能进入Q LeadCard的定义／命题／公式／量词／完成条件、脚注和表格，以及150dpi出现差异的页。

**W-005完成说明。** 已逐页生成、读取并落签pp.1–13的150dpi二值图；关键页1、5、7、9、11、12、13还读取了300dpi图。由于远程MinerU目前没有产生可用导出，这批记录验证的是期刊PDF、文本层和页图的对应关系，不能被表述为MinerU转换质量结论。

**W-013完成说明。** 已逐页生成、读取并落签pp.1–12的150dpi二值图；关键页1、2、4、5、7、8、11还读取了300dpi图。远程MinerU的第一次命令被本地CLI page-range检查拒绝，第二次在默认全文范围内65秒无输出／无导出后中止；所以本批记录验证的是Aczel原件、文本层和页图的对应关系，不能被表述为MinerU转换质量结论。

**W-011完成说明。** 已逐页生成、读取并落签pp.1–21的150dpi二值图；关键页1、16、17、18还读取了300dpi图。远程MinerU目前没有产生可用导出，这批记录验证的是Klev公开作者预印本、文本层和页图的对应关系，不能被表述为MinerU转换质量结论。
