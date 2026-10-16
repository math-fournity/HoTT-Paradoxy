# HoTT 不可停机与不完备性研究资料索引

> 角色：机器统观研究线的来源地图。原始论文和官方项目入口以
> `../HOTT-NONTERMINATION-MACHINE-OVERVIEW-PLAN.md` 的 `LIT-*` 表为当前书目 owner；本目录只保存必须跨工作树稳定引用的本地资料快照及其来源身份。

## 本地快照

| ID | 快照 | 一手位置与身份 | SHA-256 | 研究作用 | 证据边界 |
|---|---|---|---|---|---|
| `LOCAL-PLAN-001` | [在 HoTT 中寻找不可停机—不完备性边界](snapshots/在HoTT中寻找不可停机不完备性边界-20260914.md) | `/Volumes/D/HoTT_AI_HANDOFF_20260911/外部资料/在 HoTT 中寻找“不可停机—不完备性边界”的研究方案：从计算性限制到 Gödel 型自指的可执行路线.md`；读取时为主工作树 untracked 文件，1115 行 / 54,342 bytes | `a1d541e551f001bbb6c204ae673a583e00098dd0b69c2308e54738d488db2613`；快照与来源 `cmp` 相同 | 提供 `Machine → Halts/Diverges → undecidability`、Coq-HoTT Gödel/Rosser、MiniHoTT 自编码、R0–R5 结果等级和三平台比较 | AI 研究方案与文献综合，不是其中命题已在本 repo 重放的证明；原文内 `turn*` 引用标记不具有当前会话可解析的来源身份，必须由计划中的一手 URL 重新资格化 |

## 外置论文原件与可重放文本提取

论文原件保存在挂载磁盘的外置研究 cache：

`/Volumes/D/HoTT-machine-overview-cache/literature/`

本目录的 [`PDF-MANIFEST.json`](PDF-MANIFEST.json) 是外置 cache manifest 的 byte-identical 项目副本，记录 PDF 路径、字节、SHA-256、页数、逐页文本路径、文本 SHA-256 与提取器版本（本轮 `pypdf 6.10.0`）。外置 cache 避免把逐步扩大的论文库直接混入实现 diff；下表使每份当前决定性来源仍可精确资格化。

| ID | 一手入口 | PDF 身份 | 提取文本身份 | 本轮读取范围 |
|---|---|---|---|---|
| `LIT-SYNTHETIC-INCOMPLETENESS-2021` | DOI `10.4230/LIPIcs.ITP.2021.23` | 20 页 / 801,450 B / `b5738da6699457c88a9040baf022ad4b750260bbbc8def2e6c3df4422e302d8a` | 69,100 B / `1b21dd7a678af847d93f2598a0ae58b02231b333196007854cb9a5e2c5aade71` | 摘要、synthetic reduction、不完备性与 standard-model 条件 |
| `LIT-GODEL-WITHOUT-TEARS-2023` | DOI `10.4230/LIPIcs.CSL.2023.30` | 18 页 / 749,481 B / `422aa3f3aa6ee7d6721c029560d156fe86e34e96144ced5a68e495feea7231bf` | 63,431 B / `5475d25d751a0d370a3ca8a67c22826f81b7d3094e544042f781cc21d54fe2de` | Definitions 1–4、7–8、11、14、17–18；Facts 15/19；Theorems 12/16/20/21/28–30 |
| `LIT-GODEL-COQ-2005` | arXiv `cs/0505034` / DOI `10.1007/11541868_16` | paper 17 页 / 188,561 B / `d5acae99fa9a5a55e041c99af50829225498083b134cdf2a10ca68fd367d9610` | 38,780 B / `0335e74fab7319af5607d0360696b9b7070ddcbbc661d7693919e998a185ab9f` | representability、code substitution trace、proof checker、fixed point、Rosser、unary self-code 成本、第二不完备性缺口 |
| `LIT-TWO-LEVEL-TT` | arXiv `1705.03307` | 58 页 / 1,100,607 B / `ac2a753e2e2e923d1aad19d324032299591b7d41504cfc289db65369a9fa958a` | 184,494 B / `272f16568323c88041587313e195b686675a74605dfd54b1870c3fd505b6a9bd` | inner/outer theory、不可直接内部表达的元理论陈述、conservativity 与 strict equality 角色 |
| `LIT-CT-CUBICAL-ASSEMBLIES` | arXiv `1905.03014` / DOI `10.1017/S0960129522000068` | 23 页 / 291,460 B / `417e713e4a4a2e9353d892551e52453c3e603f3b6b3e9340ca52cec41750fff0` | 55,480 B / `86729bc7a69810b82fa2f3b34ad3b915aadb817527fc32ec16f49dec5f3b7d65` | Church thesis 在完整 cubical assemblies 与反射子宇宙中的相反模型论地位 |

O’Connor 的 28 页演示稿另以 SHA-256 `af5a5ccdbf83aa0030e9c2c77dacbcb0b3949d506207f9dc7d4559b4ef52a79f` 保留；研究主引用使用 17 页论文正文。五份论文首页均已渲染并核对标题/作者；数学读取仍以逐页正文文本和原 PDF 为准。

## 外置机器化源码

| 项目 | 固定位置 | Git 身份 | 本轮作用 |
|---|---|---|---|
| `coq-synthetic-incompleteness` | `/Volumes/D/HoTT-machine-overview-cache/community-frameworks/coq-synthetic-incompleteness` | branch `csl`；commit `cd7d8490f8542bfe85658c465bcb26b2ed163f53`；807 tracked paths；clean shallow clone | Coq 8.15.2 固定历史环境中从两个独立干净 worktree 构建 `FOL/Incompleteness/fol_incompleteness.vo`；1,284 个稳定内核产物和日志 exact；资格化五个核心定理并 exact rerun。Receipt 与审计见 `../evaluations/COQ-SYNTHETIC-INCOMPLETENESS-REPLAY-001/` |

## 当前综合裁决

`LOCAL-PLAN-001` 与当前机器统观一致地主张：证明搜索在观察窗内不完成、具体程序发散、停机不可判定、Gödel 不完备和形式矛盾是不同层级；可信内核对给定证明的检查与全局 theoremhood 判定也必须分开。作者 Coq 重放进一步确认，`Q_incomplete` 的构建成功不消除其定理签名中的 Peirce、CTQ、包含 Robinson `Q`、可枚举性与一致性前提。

本项目同时保留一个比该方案更严格的现实对应门：一般不可判定性或不完备性可以成为 HoTT 中可形式化的计算边界，却不能仅凭这一点称为“现实相对非现实性悖论”。要达到该身份，还必须固定现实任务、理论任务、同一输入、同一观察量与完成标准，并证明理论表示恢复、预先保留或新增了什么。

## 维护规则

- 外部资料原件只读；本快照按字节保存，不润色、不替换其引文标记。
- 书目信息在总方案中用原始论文、出版社、官方文档或官方代码库重新核对。
- 新资料进入本目录前记录来源路径/URL、读取日期、字节、hash、作者身份与证据等级。
- 文献主张与本项目机器结果分开；只有当前 repo 的冻结 proof/run receipt 才能提高本项目实验状态。
