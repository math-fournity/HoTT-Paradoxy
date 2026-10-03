# HMZ-001：来源目录与原件身份

> **读取边界：** 原件优先；`derived/` 下的纯文本与 PNG 只是定位和阅读辅助。关键措辞已回到 PDF、锁定 TeX 或可见网页核对。

## A. HoTT／UF 原典与比较文献

| ID | 文献身份与来源 URL | 原件／版本身份 | 本地原件与 SHA-256 | 实际读取 locator | 来源层与限度 |
|---|---|---|---|---|---|
| `HMZ-S-001` | The Univalent Foundations Program, *Homotopy Type Theory: Univalent Foundations of Mathematics* (2013); [official repository](https://github.com/HoTT/book). | 本仓库 `HoTT/theory-schema/upstream/book-578b85cc/`，upstream commit `578b85cc8d586b1677ec4335148adeb443057d24`. | `introduction.tex` `a1319432c822d71ee54cd8edd644d3bce1c8d816bd9f2ff6111b8d3db8e28ac4`; `preface.tex` `6dd80d576634b081b32f7c89e302eae9222170d997d4d8bbf9701ae73f05890c`; `categories.tex` `141332f0b27d5ab055419e02bada9664561758d129ebe4d52e43bb8e290b275f`; `setmath.tex` `c9684dffba31892b12839e60eac769706faa2301b7fba7b930f5acf4b097563e`. | `introduction.tex:15–24,36–51`; `preface.tex:91–92`; `categories.tex:4–21,1443–1444,1716–1723`; `setmath.tex:7–27,1755–1760`. | 集体原典；对“直接”的限定、内部 V/ZFC control 与书的工作进度同样具有约束。 |
| `HMZ-S-002` | Vladimir Voevodsky, *Univalent Foundations Project* (2010), [IAS original PDF](https://www.math.ias.edu/vladimir/sites/math.ias.edu.vladimir/files/univalent_foundations_project.pdf). | 13-page PDF，服务器 `Last-Modified: 2015-02-17`；文件正文标 2010-10-01。 | `originals/HMZ-S-002-Voevodsky-2010-Univalent-Foundations-Project.pdf`; `85e5ec7aa0ba8777e1b8343a3cbade2b2889b1552c491ff1946debe80512f840`. | PDF pp. 1–2（项目特征、direct formalization、Coq）；pp. 9（constructiveness conjecture）；derived text stored locally. | 作者项目文本；不是 ZFC 公理语义或关于 ZFC 缺陷的定理。 |
| `HMZ-S-003` | Vladimir Voevodsky, *Univalent Foundations*, IAS, 2014-03-26, [IAS PDF](https://www.math.ias.edu/~vladimir/Site3/Univalent_Foundations_files/2014_IAS.pdf). | 29-slide PDF；文件元数据 `Slides.key`. | `originals/HMZ-S-003-Voevodsky-2014-IAS-Univalent-Foundations.pdf`; `b86472fc8a722d17642f31043b01515388eea1305a330b6f717529b2075c4ccf`. | Slides 15–19；derived lines 241–339. | 作者个人历史与动机陈述；“existing foundations”须按其指定的机器验证任务解读。 |
| `HMZ-S-004` | Vladimir Voevodsky, [*The Origins and Motivations of Univalent Foundations*](https://www.ias.edu/ideas/2014/voevodsky-origins), IAS 2014. | 官方网页；2026-10-03 通过公开网页读取。直接 `curl` 获 Cloudflare `403`。 | `REMOTE_ONLY`; 没有伪造 hash 或离线副本。 | 网页段落：基础应成为日常工具、predicate-logic language limit、2-theories direct expression、computer verification。 | 作者回顾文本；可作 R 的补强，不能替代可定位的技术来源。 |
| `HMZ-S-005` | Steve Awodey, [*Type theory and homotopy*](https://arxiv.org/abs/1010.1810), 2010. | arXiv `1010.1810v1`; 20 pages. | `originals/HMZ-S-005-Awodey-2010-Type-Theory-and-Homotopy.pdf`; `d0b8906ca5f18935f9b2a0722d509cb18e1075bdd831d470e30341dc93472db7`. | PDF pp. 1–3; derived lines 22–116. | 比较来源：type theory、proof-theoretic properties、higher identity 的背景；早于 UF，不可反投为 UF 作者对 ZFC 的直接批评。 |
| `HMZ-S-006` | Steve Awodey, Álvaro Pelayo, Michael A. Warren, [*Voevodsky’s Univalence Axiom in homotopy type theory*](https://arxiv.org/abs/1302.4731), 2013. | arXiv `1302.4731v1`; 8 pages. | `originals/HMZ-S-006-Awodey-Pelayo-Warren-2013-Univalence-Axiom.pdf`; `2a40420c26cdcf8b128ec2230c993865e0f7311095549c1a22ad350d50c122ce`. | PDF pp. 3–5; derived lines 139–201. | 当期说明；作者群与 Voevodsky 有合作，但不等同于 Voevodsky 单人声明。 |

## B. ZFC／集合论形式与真实消费者

| ID | 文献身份与来源 URL | 原件／版本身份 | 本地原件与 SHA-256 | 实际读取 locator | 来源层与限度 |
|---|---|---|---|---|---|
| `HMZ-S-007` | Metamath Proof Explorer: [ax-ext](https://us.metamath.org/mpeuni/ax-ext.html), [ax-pow](https://us.metamath.org/mpeuni/ax-pow.html), [pwex](https://us.metamath.org/mpeuni/pwex.html), [rankpw](https://us.metamath.org/mpeuni/rankpw.html), [ax-reg](https://us.metamath.org/mpeuni/ax-reg.html). | Public web pages read 2026-10-03; current Web pages locally snapshotted. | `originals/metamath/`: `ax-ext.html` `a79eba75d24819d25f39cf4dce597bbe49c403877a923089bc90bbee5d81ea8b`; `ax-pow.html` `1d418aea8c4b91a4b0dda2c59c075a3ccb2f5ed36df0200ff0a7eae53cb7d0c0`; `pwex.html` `eb1b4c57776993385ff563f207ec5a0e3cb25a73fdd841c65428d9b0f2a852db`; `rankpw.html` `92d516974329f3e4b5ef8862a92a93e5113ac53a1f6b9365c277bc9fcfccd937`; `ax-reg.html` `831a94baa6c2c40384bec0985926482c5ec314130ab5f4a28bceae4e1a217c27`. | `ax-ext` description/assertion; `ax-pow` description/assertion; `pwex` hypothesis/proof; `rankpw` assertion; `ax-reg` description. | `PROOF_FORMALIZATION`: a useful formal presentation, not a complete ZFC semantic source and not a consumer contract. |
| `HMZ-S-009` | David Mumford, [*Picard Groups of Moduli Problems*](https://www.dam.brown.edu/people/mumford/alg_geom/papers/1965b--PicGpMod-EmeryScan.pdf), 1965. | 49-page scan, printed pp. 33–81. | `originals/HMZ-S-009-Mumford-1965-Picard-Groups-Moduli-Problems.pdf`; `89c8e381bda092274fadb954b438d94042d10aefa6101a4ae5a2f51a879f2f49`. | Visual source check: physical PDF pp. 1, 2, 5 = printed pp. 33, 34, 37; rendered copies in `derived/Mumford-1965-pages/front-01.png`, `front-02.png`, `front-05.png`. | `MATHEMATICAL_PRACTICE / REAL_CONSUMER_CONTROL`; it does not state ZFC axioms, but it does show how a mathematical consumer treats classification, automorphisms and required maps. |
| `HMZ-S-010` | Michael A. Shulman, [*Set Theory for Category Theory*](https://arxiv.org/abs/0810.1279), arXiv:0810.1279v2, 2008. | 39-page public arXiv PDF; source header reports v2. | `originals/HMZ-S-010-Shulman-2008-Set-Theory-for-Category-Theory.pdf`; `3f1e2d9f9a7a026ab54cd982cfad8742c9c38e9696cb60b52e18dfaa90298012`. | PDF pp. 10–14 / derived lines 500–690; abstract / lines 9–47. | `THEORY_SOURCE + MATHEMATICAL_PRACTICE`: exact ZFC class-language limit, NBG comparison and concrete choice consumers. |
| `HMZ-S-011` | Lawrence C. Paulson, [*Isabelle’s Logics: FOL and ZF*](https://isabelle.in.tum.de/website-Isabelle2021-1/dist/library/Doc/Logics_ZF/logics-ZF.pdf), Isabelle2021-1, 2021. | 85-page official manual dated 2021-12-12. | `originals/HMZ-S-011-Isabelle2021-Logics-ZF.pdf`; `2b91b2f89480e8b14201dbc93382df366737d405dbd67c39de6970ecf14cd646`. | Printed pp. 19–27 / derived lines 931–961, 969–984, 1166–1175, 1219–1342. | `PROOF_FORMALIZATION + PRACTICE`: real Isabelle/ZF source; never silently substitute it for bare ZFC semantics. |

## C. Derived-material integrity

| Derived path | Derived from | Purpose | Authority limit |
|---|---|---|---|
| `derived/HMZ-S-002-*.txt`, `derived/HMZ-S-003-*.txt`, `derived/HMZ-S-005-*.txt`, `derived/HMZ-S-006-*.txt` | Corresponding PDFs through local `pdftotext -layout`. | Fast locator and search. | Verify quotations/limits against the PDFs. |
| `derived/Mumford-1965-pages/front-01.png`, `front-02.png`, `front-05.png` | `HMZ-S-009` through local `pdftoppm`. | Visual reading of a scanned original. | Images preserve only the listed source pages; no OCR transcription is treated as source authority. |

## D. Source access events

- 2026-10-03: publicly downloadable IAS, arXiv, Brown and Metamath sources were retrieved without login.
- 2026-10-03: direct retrieval of the IAS `Ideas` pages and the Johns Hopkins mirror for Lawvere encountered Cloudflare `403`; these failures are access facts, not evidence about the literature.
- No paid, authenticated or remote OCR service was used.
