# ZQCM-001 Visual Review

> **身份：** REMOTE_DERIVATIVE_VISUAL_EVIDENCE / NO_Q_CLAIM。
>
> **顺序：** 已验证 PDF → remote standard MinerU 原始导出 → 150dpi二值页图逐页核验 → 关键／异常页300dpi复核 → 文献阅读与Q资格化。
>
> **状态：** W005_SOURCE_ONLY_VISUAL_CHECK_COMPLETE / W010_TARGETED_SOURCE_ONLY_CHECK / REMOTE_DERIVATIVE_NOT_QUALIFIED。

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

## 高精度队列

已完成W-005的7个关键页和W-010的3个关键页；其余候选包括任何可能进入Q LeadCard的定义／命题／公式／量词／完成条件、脚注和表格，以及150dpi出现差异的页。

**W-005完成说明。** 已逐页生成、读取并落签pp.1–13的150dpi二值图；关键页1、5、7、9、11、12、13还读取了300dpi图。由于远程MinerU目前没有产生可用导出，这批记录验证的是期刊PDF、文本层和页图的对应关系，不能被表述为MinerU转换质量结论。
