# HMZ-007：来源目录与原件身份

| ID | 原件／版本 | 本地原件与 SHA-256 | 实读 locator | 来源层与限度 |
|---|---|---|---|---|
| `HMZ-S-021` | Voevodsky, WoLLIC 2011；IAS PDF。 | 见 HMZ-006；SHA `0afa5e2825480f63c04778753db9cebf99323ba6c60916cde3882a0863624159`. | slide 2，及 slide 8 的 Coq universe-management 控制。 | 作者讲演；不命名其所说 ZFC-in-Coq attempts。 |
| `HMZ-S-022` | Werner, *Sets in Types, Types in Sets*, TACS 1997；作者 17-page PDF draft。 | `originals/HMZ-S-022-Werner-1997-Sets-in-Types-Types-in-Sets.pdf`; `4e5f4816e57e0e4f4283eed13eb0ffb973053b124ecac05e6bfa4edeaf8c317b`. | PDF pp. 1–2（双向编码与 TTDA）；pp. 6–8（ZFC semantics、Choice）；pp. 10–13（Aczel encoding、Power、Replacement、choice）。 | 同行论文的作者 draft；关键结论是来源报告，未由本项目重跑。 |
| `HMZ-S-023` | `https://github.com/rocq-archive/zfc`, commit `ede7126560844c381c2b021003a8dbcb0668ecad`，2022-12-17 port。 | `originals/HMZ-S-023-rocq-archive-zfc-ede7126560844.tar.gz`; `9181e163607d1e58ecc7f2c2e06b4f952268623461a43e519a42a2c6903522ac`. | `README`; `zfc.v:27–74`; `Axioms.v:160–166,428–510`; `Replacement.v:21–93`; `Russell.v:19–55`; `Hierarchy.v:77–136`; `Omega.v:175–178`. | 现行 archive port 保存的是历史 Coq/ZF contribution 的可读快照；不是 1996/1997 工具链运行收据。 |

## 派生阅读物

| 文件 | SHA-256 | 用途 |
|---|---|---|
| `derived/HMZ-S-022-Werner-1997-Sets-in-Types-Types-in-Sets.txt` | `7138842d31fea0f2a4a35ab27200308f5f0bb722925059728885d9896ccba6bd` | PDF locator，关键解释回 PDF。 |
| `derived/HMZ-S-023-rocq-archive-zfc-tree.txt` | `9235f8ad26a45bf54bece68a8c56adf482a3fddb2ed810ed5e482c7468a2087f` | source tree manifest。 |
| `derived/HMZ-S-023-SOURCE-MAP.md` | 本目录的 readable map。 | 从原始 tar 中定位 `README`、`zfc.v`、`Axioms.v`、`Replacement.v`、`Russell.v`、`Hierarchy.v`、`Omega.v`；不以副本改写源代码空白／换行。 |

`HMZ-S-023` 的原始 `.v` 文件只保留在可复算 tarball 中。这样 archive 同时保留源字节和清晰的阅读 locator；不将
legacy source formatting 误改成新的权威文本。需要核代码时先从 tar 提取相应成员，并与 frozen tree manifest 对照。

未运行历史 Coq 6.3/6.1 代码；原始 README 的“make 会编译”仅是 `SOURCE_REPORTED`，不升级为本项目运行事实。
