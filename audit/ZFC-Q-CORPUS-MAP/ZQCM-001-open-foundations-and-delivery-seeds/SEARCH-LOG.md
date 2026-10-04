# ZQCM-001 Search Log

> **已继承 discovery：** HOTT-MOTIVE LITERATURE-MAP-001 的 M-OA、M-ZB、M-ARX、M-AUTH 和 M-NET 初始检索。
>
> **本批新增检索：** acquisition／PDF身份核验已开始；下一阶段是引用网络和access remainder。

| Search ID | 平台／query | 日期 | 命中／导出 | 用途 | 状态 |
|---|---|---|---|---|---|
| ZQCM-S-001 | arXiv exact IDs 1711.01477, 2301.12405, 1502.00112, 2111.06368, 2301.08131, 2307.13563 | 2026-10-03 | W-001/002/003/005/007/008 PDF取得并经file/pdfinfo/首页/SHA256核验。 | 官方arXiv acquisition | COMPLETE_WITH_SCOPE |
| ZQCM-S-002 | DOI routes 10.4230/LIPIcs.CSL.2024.28; 10.1007/s10516-023-09676-0; 10.1093/philmat/nkaa005 | 2026-10-03 | W-004 Dagstuhl PDF取得并核验；W-005 DOI／仓储路径403且展示页安全验证，但由arXiv作者版本补足；W-006 PDF直取403、只得catalog线索。 | DOI metadata/acquisition remainder | PARTIAL_WITH_ACCESS_LIMITS |
| ZQCM-S-003 | Springer volume DOI `10.1007/978-3-030-15655-8`; OUP review DOIs `nkaa005`, `nkab026` | 2026-10-03 | 确认494页volume身份、三大章节组与12条直接相邻chapter leads；尚未取得章节全文。 | W-006 catalog → author acquisition map | COMPLETE_CATALOGUE_WITH_SCOPE |
| ZQCM-S-004 | Bristol accepted-manuscript endpoint for V-SET-03 | 2026-10-03 | direct fetch 403；BrowserOS `test` profile独立会话显示Cloudflare human-verification challenge；未交互绕过。 | public author-manuscript acquisition control | ACCESS_LIMITED_NO_BYPASS |
| ZQCM-S-005 | W-005 backward citations → Altenkirch `fomus19.pdf`; Maddy author-hosted chapter PDF | 2026-10-03 | 两份公开作者版本均取得并通过file／pdfinfo／首页／SHA256核验。 | Extension-001 chapter acquisition | COMPLETE_WITH_SCOPE |
| ZQCM-S-006 | Ansten Klev author page → public preprint Drive ID `1FIfAvSkt9uJh6R2uS7gz-fWh5hLKVx5w` | 2026-10-03 | W-011 21页PDF取得并通过file／pdfinfo／首页／SHA256核验。 | Extension-002 direct-comparison acquisition | COMPLETE_WITH_SCOPE |
| ZQCM-S-007 | Klev author page / PhilArchive `KLETPI-3.pdf` / DOI `nkae018` | 2026-10-03 | metadata与摘要确认；direct fetch 403，BrowserOS `test` profile呈Cloudflare verification，未交互绕过。 | Extension-003 iterative-set seed | FULLTEXT_ACCESS_LIMITED_NO_BYPASS |
| ZQCM-S-008 | exact Aczel 1978 title → Elsevier DOI metadata → [Cornell course PDF](https://www.cs.cornell.edu/courses/cs6180/2017fa/notes/week4/lecture8/Aczel_type-theory-set-theory.pdf) | 2026-10-03 | DOI `10.1016/S0049-237X(08)71989-X`确认出版身份；Cornell公开副本通过file／12页／首页／SHA256核验。 | Extension-004 primary CZF／Power Set／formation control | COMPLETE_WITH_SCOPE |
| ZQCM-S-009 | exact Linnebo title / DOI `10.1017/S1755020313000014` → [Cambridge Core](https://www.cambridge.org/core/journals/review-of-symbolic-logic/article/abs/potential-hierarchy-of-sets/334647199574BFA9ADBCEFE379CDDB14) | 2026-10-03 | 官方题录、作者、期刊页码与abstract已读取；当前未取得合法可核全文。 | Extension-005 potential／actual hierarchy seed | METADATA_ABSTRACT_ONLY |
| ZQCM-S-010 | exact Linnebo title / author publication list / university-domain query | 2026-10-03 | Cambridge与作者publications list继续确认书目；没有定位到作者、机构或出版社开放的可核PDF。第三方转载不接受为原件或内容来源，未对其做下载或互动尝试。 | W-014 access-remainder qualification | NO_LEGITIMATE_FULLTEXT_LOCATED_IN_DECLARED_SEARCH |
| ZQCM-S-011 | W-012 exact author page / PhilPapers `KLETPI-3` / PhilArchive / OpenAlex DOI metadata | 2026-10-04 | 作者页与PhilPapers都列preprint；公开端点`https://philpapers.org/archive/KLETPI-3.pdf`及PhilArchive record的普通HTTPS请求均返回Cloudflare `403`。OpenAlex登记submitted-version repository location，却标`is_oa:false`／`has_fulltext:false`。搜索结果中的文本预览没有被当作原件。 | W-012 public-preprint access recheck | ACCESS_LIMITED_NO_BYPASS_RECONFIRMED |
| ZQCM-S-012 | W-014 OpenAlex DOI metadata → Birkbeck `eprint/7048` institutional record → Crossref/Cambridge metadata | 2026-10-04 | Birkbeck HTML元数据可公开读取，但声明`full_text_status=none`及“Full text not available from this repository”；OpenAlex也标`is_oa:false`／`pdf_url:null`／无repository fulltext。没有下载第三方转载或尝试绕过限制。 | W-014 institutional-route qualification | INSTITUTIONAL_METADATA_ONLY_FULLTEXT_NONE |
