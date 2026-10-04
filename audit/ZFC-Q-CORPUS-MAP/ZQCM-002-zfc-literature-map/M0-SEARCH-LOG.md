# ZQCM-002 M0：公开检索日志

> **状态：** `COMPLETE_WITH_SCOPE / FIRST_PLATFORM_PROBES_COMPLETE / SOURCE-ENTRY-TRIANGULATION_COMPLETE / SOURCE-SPECIFIC_REFINEMENT_DEFERRED_TO_M1–M6`。
>
> 每一行必须记录实际 query、日期、平台、返回范围、限制和对覆盖矩阵的影响；命中数不是相关文献数。

| M0 Search ID | 日期 | 平台 | Axis | 实际 query／参数 | 返回范围 | 处置 |
|---|---|---|---|---|---|---|
| `M0-OA-A` | 2026-10-04 | OpenAlex Works API | A | `search="Zermelo Fraenkel" axioms power set replacement separation`; `per-page=5`; `select=id,doi,title,publication_year,type,cited_by_count,open_access,primary_location` | `meta.count=288`。首 5：两条 2026 Zenodo dataset（同名 Canvas Temporal Mathematics）、2023/2022 paraconsistent ZF 的 article/preprint、2007 Kaye–Wong *On Interpretations of Arithmetic and Set Theory*（DOI `10.1305/ndjfl/1193667707`）。 | **低精度，未准入 work family。** Zenodo 与 paraconsistent 条目不回答 A 轴的原典／标准防线问题；Kaye–Wong 只登记为可能的后续解释路线，尚未读原文。下一步改为按 Zermelo／Fraenkel／von Neumann 和各公理簇拆分。 |
| `M0-OA-B` | 2026-10-04 | OpenAlex Works API | B | `search="potential hierarchy" set theory predicativity impredicativity`; 同上字段与 `per-page=5` | `meta.count=14`。首 5 包括 2021 *Predicativism as a Form of Potentialism*（DOI `10.1017/s1755020321000423`）、2024 *Iterative Conceptions of Set*（DOI `10.1017/9781009227223`）和两条 2024/2025 iterative/plural iterative set 条目。 | **高信号但尚未读。** 它建立 B 轴的 potentialism/iterative-conception source family，不把哲学题名等同于固定 ZFC formation 或 same-task consumer。 |
| `M0-OA-C` | 2026-10-04 | OpenAlex Works API | C | `search=forcing model theory independence large cardinals ZFC`; 同上字段与 `per-page=5` | `meta.count=915`。首 5 全为 2025 Zenodo 预印/数据记录（forcing、inner models、multiverse、absoluteness）。 | **低精度，未准入 work family。** 该 query 被近年 Zenodo 自存档淹没；下一步分别用 Cohen／Gödel／forcing、inner models、large cardinals、determinacy 的 source-specific query，并保留普通 ZFC consumer 分离条件。 |
| `M0-OA-D` | 2026-10-04 | OpenAlex Works API | D | `search=ZFC proof assistant formalization set theory practice`; 同上字段与 `per-page=5` | `meta.count=160`。首 5 包括 2023 Coq ZFC teaching formalization、2025 Coq 比较综述、HoTT library、Lean 教学文章、HOL-in-set-theory preprint。 | **混合噪声，未发现 ordinary bare-ZFC same-Done consumer。** 它只证明需将 proof-assistant implementation、教学、HoTT 和 ordinary ZFC practice 分开筛选。 |
| `M0-OA-E` | 2026-10-04 | OpenAlex Works API | E | `search=homotopy type theory set theory foundations`; 同上字段与 `per-page=5` | `meta.count=10,714`。首 5 包括 2024 *The Category of Iterative Sets in HoTT and UF*（DOI `10.1017/s0960129524000288`）、2015 *Sets in HoTT*（DOI `10.1017/s0960129514000553`）及 HoTT/UF surveys。 | **过宽，保留两个 iterative-set 题名为 E-axis 筛选候选。** 题名不证明 `R→Z→Q` 的保真传输，也不改变既有 H0 anti-analogy control。 |
| `M0-FOR-A` | 2026-10-04 | GDZ / SEP | A | GDZ：Zermelo, *Untersuchungen über die Grundlagen der Mengenlehre*, *Mathematische Annalen* 65 (1908) 的馆藏扫描入口；SEP：ZF supplement 和 Set Theory 词条。 | GDZ 页面标识 1908 卷与 Zermelo 题名；SEP 给出 Power Set、Separation、Replacement、Foundation 的现代表述和历史定位。 | **正式原典／标准防线入口已登记。** 未获取 PDF、未视觉审读；SEP 是二级概述，不取代 Zermelo 原件。 |
| `M0-BRIDGE-A` | 2026-10-04 | SEP | A | `Set Theory` 与 `Zermelo-Fraenkel Set Theory (ZF)` 条目，含历史、公式与参考资料入口。 | 词条区分 Zermelo、Fraenkel/Skolem、von Neumann 的贡献并给出公理层参考入口。 | **bridge 已登记。** 后续要按每个公理簇和原件页码建立可核 work card。 |
| `M0-FOR-B` | 2026-10-04 | Stanford Mathematics | B | Solomon Feferman 的论文目录 `papers/`。 | 作者页面列出 `predicativity.pdf`，并将其工作定位于 constructive/predicative foundations 与数学哲学。 | **作者来源入口已登记。** 它不是 ZFC Q 的来源证明，也不完成 B 轴书目。 |
| `M0-BRIDGE-B` | 2026-10-04 | Stanford Mathematics | B | Feferman publications bibliography。 | 书目列出 1966 `Predicative provability in set theory`、1974 `Predicatively reducible systems of set theory` 等可追踪作品。 | **作者书目 bridge 已登记。** 只用于构成后续冻结作者族，不替代 Citation-network audit。 |
| `M0-FOR-C` | 2026-10-04 | PubMed / PMC | C | Paul J. Cohen, *The Independence of the Continuum Hypothesis*，PNAS 50(6), 1143–1148, DOI `10.1073/pnas.50.6.1143`。 | 题名、作者、期刊、页码、DOI 与 PMC 身份可核。 | **原典入口已登记。** 尚未将其全文加入 ZQCM-002 acquisition batch；独立性结论不是 ZFC Q。 |
| `M0-BRIDGE-C` | 2026-10-04 | IMU Fields archive | C | IMU 1966 Fields Medal archive。 | IMU 将 Cohen 的 forcing 与 AC/GCH 在集合论中的独立性明确关联。 | **历史／影响 bridge 已登记。** 它不代替 Cohen 原文或 forcing 文献网络。 |
| `M0-FOR-D` | 2026-10-04 | Isabelle official documentation | D | Isabelle `Logics: FOL and ZF` 文档。 | 官方说明将 ZF 描述为建于 FOL 之上的 Zermelo–Fraenkel set theory。 | **正式实现入口已登记。** 它是 implementation-level source，不等同 ordinary ZFC mathematical consumer。 |
| `M0-BRIDGE-D` | 2026-10-04 | Isabelle libraries | D | Isabelle libraries index。 | 索引列出 `isarmathlib` 为 Isabelle/ZF formalised mathematics。 | **bridge 已登记。** 后续只能挑一个版本固定的 consumer，冻结其输入／输出／Done 后才可筛读。 |
| `M0-FOR-E` | 2026-10-04 | HoTT Book official site | E | HoTT Book 官方主站及带版本标记的 PDF 下载入口。 | 官方介绍把 HoTT/UF 表述为数学基础方案，并提供可版本固定的书本下载。 | **正式入口已登记。** 该说明不自动支持任何 ZFC 缺陷、Q 或 H0→Z0 传输。 |
| `M0-BRIDGE-E` | 2026-10-04 | HoTT official references | E | HoTT 官方 references 页，配合既有 `audit/HOTT-MOTIVE-ZFC/` 文献地图。 | 提供 HoTT 论文分类和历史 references 入口；既有 HMZ runs 提供已处理控制。 | **bridge 已登记。** 后续按 work-by-work `R→Z→Q` fidelity card 处理，不能以广义基础叙述跨越 anti-analogy guard。 |

## M0 未决与下一判别行动

1. 当前五条 OpenAlex query 只说明候选池和噪声结构，尚不能构成各轴的层级书目或引文网络。下一轮将每轴拆成可筛的 source-specific query，并保留 query 版本、分页与筛选口径。
2. A–E 均已有最小正式／作者／bridge 入口，但还没有完成语言、时期和数据库的交叉覆盖；M0 仍为 `IN_PROGRESS`。
3. 下一条冻结条件不是“下载前排标题”，而是：按 M0 remainder 选择一条同时有原件身份、明确理论位置、可访问版本和可预注册来源屏读问题的 family。该 family 将在 M1–M5 对应波次中单独建立 batch。
