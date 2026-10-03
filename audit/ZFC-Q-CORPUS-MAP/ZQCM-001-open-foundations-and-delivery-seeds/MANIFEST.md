# ZQCM-001：开放基础与交付种子语料

> **身份：** FROZEN_CORPUS_BATCH / EXTENSION-003_ITERATIVE_SET_SEED / ACQUISITION_ACTIVE / NO_Q_CLAIM。
>
> **总 SOP：** [ZFC-Q-CORPUS-MAP-SOP](../../../dev-docs/ZFC-Q语料落盘与文献地图SOP.md)。
>
> **冻结日期：** 2026-10-03。
>
> **工作根／分支：** `/Users/aurolafly/.codex/worktrees/ff3b/HoTT_AI_HANDOFF_20260911` / `codex/hott-motive-zfc-literature`。

## 1. 本批问题与范围

本批不是对 ZFC 整个文献的穷尽搜索。它处理当前文献地图中最直接的开放／可定位 work family，回答：

1. HoTT／UF 的 foundations 与 predicative variants 如何表述其集合论、构造、计算或交付关系？
2. Krivine 的 ZF／choice／realizability 语料如何进一步限定“存在、程序与 delivery”这条 P5 控制线？
3. 哪些 foundations、数学实践或形式化文献值得形成 Q LeadCard，哪些只成为 source payment 或 control？

本批不主张 ZFC 有矛盾、HoTT 有内部矛盾、P5 已命中或任何新的 ZFC Q。

## 2. 冻结 work family

| Work ID | 标题／身份 | 来源地图记录 | 首选获取路线 | 预期作用 |
|---|---|---|---|---|
| ZQCM-W-001 | Daniel R. Grayson, *An introduction to univalent foundations for mathematicians*, arXiv:1711.01477v3 | M-009 | arXiv official PDF | M-A reception／foundation explanation。 |
| ZQCM-W-002 | Tom de Jong, *Domain Theory in Constructive and Predicative Univalent Foundations*, arXiv:2301.12405v8 | M-010 | arXiv official PDF | M-A/M-C constructive/predicative control。 |
| ZQCM-W-003 | Jean-Louis Krivine, *Bar recursion in classical realisability: dependent choice and continuum hypothesis*, arXiv:1502.00112v4 | M-011 | arXiv official PDF | M-C P5 model-semantic extension。 |
| ZQCM-W-004 | Fontanella, Geoffroy, Matthews, *Realizability Models for Large Cardinals*, DOI:10.4230/LIPIcs.CSL.2024.28 | M-003 | Dagstuhl/LIPIcs official PDF | M-C classical-realizability/ZF／large-cardinal control。 |
| ZQCM-W-005 | *Should Type Theory Replace Set Theory as the Foundation of Mathematics?*, DOI:10.1007/s10516-023-09676-0 | M-002 | DOI → publisher/author/institutional route | M-A/M-E foundations comparison。 |
| ZQCM-W-006 | *Reflections on the Foundations of Mathematics: Univalent Foundations, Set Theory and General Thoughts* work family | M-001 | DOI / publisher table of contents / chapter sources | M-A/M-E edited-volume map。 |
| ZQCM-W-007 | *One Mathematic(s) or Many? Foundations of Mathematics in 20th Century Mathematical Practice* work family | M-005 | DOI / author / publisher route | M-E historical practice control。 |
| ZQCM-W-008 | Richard Matthews, *A Guide to Krivine Realizability for Set Theory*, arXiv:2307.13563 | M-013 | arXiv official PDF | M-C modern guide／control。 |
| ZQCM-W-009 | Thorsten Altenkirch, *Naïve Type Theory*, DOI:10.1007/978-3-030-15655-8_5 | W-006 `V-UF-01`; W-005 B-03 | author-hosted PDF | M-A primary-motive extension。 |
| ZQCM-W-010 | Penelope Maddy, *What Do We Want a Foundation to Do?*, DOI:10.1007/978-3-030-15655-8_13 | W-006 `V-CMP-04`; W-005 B-11 | author-hosted PDF | M-E foundation-criterion/control。 |
| ZQCM-W-011 | Ansten Klev, *A Comparison of Type Theory with Set Theory*, DOI:10.1007/978-3-030-15655-8_12 | W-006 `V-CMP-03` | author-hosted preprint | M-A/M-E direct comparison／identity route。 |
| ZQCM-W-012 | Ansten Klev, *The Purely Iterative Conception of Set*, DOI:10.1093/philmat/nkae018 | Klev author trace / PhilPapers metadata | author preprint / PhilArchive route | M-B/M-E stage／iterative-set route。 |

## 3. Inclusion and exclusion

- **Include:** works with a direct foundation, set-theory, type-theory, predicativity, realizability, proof-formalization, actual-consumer or standard-control relation to the declared questions.
- **Exclude from this batch:** merely keyword-related works; entries whose accessible abstract shows no theory/task connection; duplicate reports of an already identified work family.
- **Defer:** works with incomplete metadata, inaccessible full text or unclear relevance; preserve reason and next route.

## 4. Source channels and limits

This batch consumes the existing HOTT-MOTIVE map records, arXiv, DOI resolution, author/institution pages, publisher/conference archives, zbMATH/OpenAlex metadata and backward/forward citation leads. User-provided browser access routes may be recorded as acquisition provenance. No access route alone establishes work identity or content.

Metadata correction: the initial OpenAlex M-003 record conflated the Matthews Guide with DOI 10.4230/LIPIcs.CSL.2024.28. DOI verification identifies the latter as *Realizability Models for Large Cardinals*; the Guide is arXiv:2307.13563. Both are retained as separate work families.

Current language scope is English-first. Strong non-English citations discovered during acquisition are registered as `LANGUAGE_LIMIT` or queued for an explicit language route; they are not silently excluded.

## 5. Completion and stopping

ZQCM-001 reaches `COMPLETE_WITH_SCOPE` only when every frozen work family has a full acquisition, alternate version, unavailable or exclusion disposition; every accepted PDF has identity evidence; required MinerU attempts have receipts; work-family/citation/coverage/Q-lead owners state their remainder.

Natural successors are newly discovered direct references, official versions, accessible author copies, actual consumer sources or a Q lead that satisfies a specialized SOP's entry conditions. Similar titles or a raw search hit do not automatically extend the batch.

**Extension-001 rationale.** W-009 and W-010 are direct chapter-level references from the fully read W-005, already indexed as priority chapter leads in the W-006 map, and each has a public author-hosted PDF. They extend the frozen batch under the declared successor rule; they do not create a Q candidate.

**Extension-002 rationale.** W-011 is a volume chapter already mapped as `V-CMP-03`; an exact author-page query exposed a public 21-page preprint. Its abstract and introduction directly distinguish standard axiomatic set theory/ZFC, types, functions and identity. Acquisition admits it to source screening, not to Q.

**Extension-003 rationale.** W-012 was exposed by the same author trace and directly differentiates stage formation from iterated set-of formation. Public metadata/abstract establishes a high-priority ZFC-time/formation source seed; both direct fetch and BrowserOS test-profile access hit security verification, so it is admitted only as an `UNAVAILABLE_FULLTEXT_SEED`, not as read evidence.
