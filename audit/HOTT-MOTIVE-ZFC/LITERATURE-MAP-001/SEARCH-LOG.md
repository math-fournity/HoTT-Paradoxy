# LITERATURE-MAP-001 检索日志

> **状态：** MAP_EXECUTION_ACTIVE；M1 初始数据库、author-primary 与 citation channel 已记录。命中数是平台返回的检索计数，不等于相关文献数。

| M-Search ID | 日期 | 平台／接口 | 实际 query／参数 | 地图轴 | 命中／导出 | 处置与限制 |
|---|---|---|---|---|---|---|
| M-OA-001 | 2026-10-03 | OpenAlex Works API | GET works?search=univalent+foundations+set+theory&per-page=20 | M-A / M-E | meta.count=2518；返回20 | 仅筛选前排与既有种子重合项；宽 query，不等于 2518 篇相关。 |
| M-OA-002 | 2026-10-03 | OpenAlex Works API | GET works?search=predicativity+ZFC&per-page=20 | M-B / M-E | meta.count=399；返回20 | 记录 predicative set theory 等 lead；含明显不相关或低可信记录，须筛选。 |
| M-OA-003 | 2026-10-03 | OpenAlex Works API | GET works?search=vicious+circle+set+theory&per-page=20 | M-B / M-E | meta.count=68194；返回20 | 查询精度极低，作为反例记录；不得按标题自动纳入。 |
| M-OA-004 | 2026-10-03 | OpenAlex Works API | GET works?search=classical+realizability+ZF&per-page=20 | M-C | meta.count=626；返回20 | 产生 Krivine／McCarty／Guide leads；与现有 HMZ-S-032 work family 去重。 |
| M-OA-005 | 2026-10-03 | OpenAlex Works API | GET works?search=ZFC+proof+assistant&per-page=20 | M-C / M-D | meta.count=378；返回20 | 产生 λZFC、proof verification、formalization leads；不将论文题名当 consumer。 |
| M-CR-001 | 2026-10-03 | Crossref Works API | GET works?query.bibliographic=univalent+foundations+set+theory&rows=20&select=DOI,title,author,published,container-title,type,URL | M-A / M-E | API total-results=2420824；返回20 | 返回计数显示该自由文本接口低精度；只作独立元数据交叉和 DOI 检查。 |
| M-AUTH-001 | 2026-10-03 | IAS official author／institution pages | Web query: Voevodsky Univalent Foundations Project official PDF 2010; Voevodsky Origins and Motivations of Univalent Foundations official IAS | M-A | 发现 IAS Origins page、Voevodsky publications bibliography、2010 Project PDF | primary author channel；现有 HMZ-S-002/004 作为同一 work family 的已读种子。 |
| M-OA-CIT-000 | 2026-10-03 | OpenAlex Works API | attempted cited_by_api_url field for DOI 10.1007/978-3-030-15655-8_6 | M-A / M-D / M-E | endpoint assumption failed; no result imported | 记录方法失败；改用 M-OA-CIT-001 的 filter=cites query。 |
| M-OA-CIT-001 | 2026-10-03 | OpenAlex Works API | GET works?filter=cites:W2938420015&per-page=20 | M-A / M-D / M-E | meta.count=10；返回10 | forward citations of Ahrens–North 2019；初步产生 M-004 至 M-006。 |
| M-ZB-001 | 2026-10-03 | zbMATH Open Document API | GET v1/document/_search?search_string=univalent+foundations&results_per_page=20&page=0 | M-A | nr_total_results=202；返回20 | 数学书目主通道已启动；含 HoTT Book、Voevodsky、Grayson 和 UniMath lead。 |
| M-ZB-002 | 2026-10-03 | zbMATH Open Document API | GET v1/document/_search?search_string=predicativity&results_per_page=20&page=0 | M-B / M-E | nr_total_results=132；返回20 | 产生 Poincaré-Weyl、Shoenfield、Simpson、Pohlers等 lead；须按 ZFC／P 关系筛选。 |
| M-ZB-003 | 2026-10-03 | zbMATH Open Document API | GET v1/document/_search?search_string=classical+realizability&results_per_page=20&page=0 | M-C | nr_total_results=524；返回20 | 产生 Krivine、effective topos 等 lead；work family 去重后再读。 |
| M-ARX-001 | 2026-10-03 | arXiv export API | GET api/query?search_query=all:"univalent foundations"&start=0&max_results=20&sortBy=relevance&sortOrder=descending | M-A | totalResults=62；返回20 | 对 HoTT/UF 预印本语料的可重算入口；与 HMZ-S-001/015去重。 |
| M-ARX-002 | 2026-10-03 | arXiv export API | GET api/query?search_query=all:"classical realizability" AND all:ZF&start=0&max_results=20&sortBy=relevance&sortOrder=descending | M-C | totalResults=3；返回3 | 小而明确的 Krivine ZF family；与 HMZ-S-032、M-008去重。 |

每一行必须保存实际执行的检索字符串和限制；概念 query family 见 PROTOCOL，不能替代本表。
