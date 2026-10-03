# ZQCM-001 Acquisition

> **状态：** ACQUISITION_ACTIVE / NINE_WORK_FAMILIES_VALIDATED / TEN_PDF_FILES_VALIDATED / TWO_ACCESS_LIMITS_RECORDED。

| ACQ ID | Work ID | Route | 获取状态 | PDF／版本判词 | 下一动作 |
|---|---|---|---|---|---|
| ZQCM-ACQ-001 | W-001 | arXiv official PDF | ACQUIRED_VALIDATED | arXiv:1711.01477v3；33页；SHA256 `3b2d4c…8bc71` | 等待remote standard重新资格化，再作视觉核验。 |
| ZQCM-ACQ-002 | W-002 | arXiv official PDF | ACQUIRED_VALIDATED | arXiv:2301.12405v8；192页；SHA256 `1a6d4c…1b160` | 等待remote standard重新资格化及分段视觉核验。 |
| ZQCM-ACQ-003 | W-003 | arXiv official PDF | ACQUIRED_VALIDATED | arXiv:1502.00112v4；11页；SHA256 `4bbed1…62ba3` | 等待remote standard重新资格化及视觉核验。 |
| ZQCM-ACQ-004 | W-004 | Dagstuhl/LIPIcs official PDF | ACQUIRED_VALIDATED | DOI `10.4230/LIPIcs.CSL.2024.28`；18页；SHA256 `425e91…fc0f` | 等待remote standard重新资格化及视觉核验。 |
| ZQCM-ACQ-005 | W-005 | DOI → repository → arXiv author route → user-provided publisher PDF | PUBLISHER_VERSION_VALIDATED | repository `OutputFile/16794952`直取403且展示页安全验证；arXiv:2111.06368v4和用户提供的期刊版均已入库。期刊版13页、Springer metadata、DOI、标题、作者与首页一致，SHA256 `14d904…aa8d`。 | 期刊版已做source-only视觉核验；remote derivative待独立通道修复。 |
| ZQCM-ACQ-006 | W-006 | Springer catalog → OUP reviews → chapter author routes | CATALOGUE_MAPPED_FULLTEXT_LIMITED | volume DOI `10.1007/978-3-030-15655-8`；OUP `nkaa005`／`nkab026`已确认目录，PDF直取403。 | 依[`VOLUME-CHAPTER-MAP.md`](VOLUME-CHAPTER-MAP.md)取得优先章节的作者公开版本。 |
| ZQCM-ACQ-007 | W-007 | arXiv official PDF | ACQUIRED_VALIDATED | arXiv:2301.08131；37页；SHA256 `64517f…4cb2a` | 等待remote standard重新资格化及视觉核验。 |
| ZQCM-ACQ-008 | W-008 | arXiv official PDF | ACQUIRED_VALIDATED | arXiv:2307.13563v2；65页；SHA256 `2297f7…05fac` | 等待remote standard重新资格化及视觉核验。 |
| ZQCM-ACQ-009 | W-009 | author-hosted PDF | ACQUIRED_VALIDATED | DOI `10.1007/978-3-030-15655-8_5`；29页；SHA256 `0a7373…3bd67`。 | remote derivative待修复；排入视觉核验队列。 |
| ZQCM-ACQ-010 | W-010 | author-hosted PDF | ACQUIRED_VALIDATED | DOI `10.1007/978-3-030-15655-8_13`；18页；SHA256 `eb3c8a…df3d5`。 | remote derivative待修复；排入视觉核验队列。 |
