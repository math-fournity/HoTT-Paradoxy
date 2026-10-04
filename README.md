<!-- governance-shard-index:v2
logical_id: README
mode: topical
shard_root: README
last_shard: README/007 - 怎样审计、复现与反驳.md
append_target: -
soft_line_target: 300
-->

> ⚠️ 逻辑文档索引：全文 = 本索引 + 下方 7 个分片；缺一片即未完成，按表顺序读取；300 行只是软目标，不是上限。

# HoTT-Paradoxy：在同伦类型论中寻找相对现实的悖论

<!-- readme-snapshot:v1
snapshot_date: 2026-10-02
state_revision: 298
core_generation: core-cognition-generation-13
core_kc_count: 62
direction_projection: 20261002-direction-onepass-298
panorama_projection: 20261002-outcome-onepass-298
-->

> 合同：`docs/quality/长治理文档分片与索引合同.md`。本页快照截至 2026-10-02（STATE revision 298；核心认知第 13 代，62 条；方向追踪 v1.19，全景视野 v1.20）。状态的权威在各自的 owner 文件，本页只做路由；快照过期时以 owner 为准。
>
> **分支**（2026-09-30 起）：本分支是 `dev`，放全部研究过程，所有工作都在这里进行。对外展示的结论与证据在 `main` 分支，由 `scripts/release/build_main_release.py` 从 `dev` 生成，不直接编辑（`rulings.md` 2026-09-30 末节）。

## 一屏读懂

- **在找什么**：理论为了好用，会把现实里的某个条件改掉。我们在同伦类型论（HoTT）里找这样的改动，再设计一件专门需要那个条件的事，看它显出哪一种“非现实”：现实里做得完、理论里做不完；或者现实里做不完、理论却当作已经做完。要找的不是 HoTT 的内部矛盾。2026-09-30，研究发起人给了一个可操作的定义 UR：【用户原话，KC-000054，节选】「本来应该很简单的事情，甚至在X理论中，都做不到」。（这一条的其余部分是 AI 的概括，研究发起人的原话见 002。）
- **第一阶段已收尾**：【用户判定，2026-09-30】「把所有该做的，全部做完，我认为我们要阶段性地收尾HoTT悖论查找工作了，因为我们很可能已经找到了。」收尾报告：`docs/HoTT悖论查找阶段收尾报告-20260930.md`。
- **找到了什么**【解释，AI；“不合理”的判定属于研究发起人】：两个东西是不是同一个，本来是一句话的事。HoTT 为了省事，规定同构的就是同一个（单价性）；又为了普适，让任意高维的形状在宇宙里一次齐备（高阶归纳类型）。于是在它的宇宙里，“是同一个”永远了结不了。把“逐层追问这份相同到哪一层了结”写成程序，HoTT 在内部证明：对任何判定器，它在宇宙上、在 HoTT Book 例 8.8.6 的乘积上都等于永不停机的 `never`（CG001-C-78、CG001-C-81）；在“相同是事实”的世界（按同一组方程转写到 Lean）里第 1 问就停（CG001-C-80）；成员的高度封顶，就恰好在封顶处停（CG001-C-79、CG001-C-82）；对集合截断发问也是第 1 问停，可截断把“相同”的多种方式合成了一种，而且解码不回宇宙（CG001-C-83）。研究发起人把它读作与芝诺同形的非现实性悖论：每一层都确定地还没了结，这个确认永远完成不了。
- **证据走到哪一步**：各命题由证明器内核检查通过，各有负控制；CG001-C-77 至 C-80 在 Linux 与 macOS 两个平台上重放一致，C-81 至 C-83 只在 macOS 上重放；共享证据矩阵 `HoTT/CLAIM_EVIDENCE_MATRIX.md` 末节已登记这批命题，运行的 canonical 登记待 integrator。用户 2026-09-27 的总判定仍是研究发起人的判断，不是数学定理；用户 2026-10-01 澄清，其中“芝诺悖论的幽灵”指圆环悖论及本仓库对此的后续讨论、分析。A7 无穷相干是另一条 AI 提出的芝诺式候选，不是该句判定的指称对象；它的统一定义是否存在仍是公开问题。详见 005。
- **不宣称**：HoTT 不一致；“很可能已经找到”是数学定理（它是研究发起人的判断）；数学事实是新的（乘积是 HoTT Book 的例子；宇宙一侧书里写的是“预计如此、尚未做出”，本仓库给出了机器证明；新的主要是读法）；“永不停”对现实中的运行无条件成立（还要以所用理论一致为前提）；“在有限范围里没找到”等于“不存在”。
- **从哪读起**：先读收尾报告；想用最短的篇幅看懂，读社区审计稿 `docs/社区审计提交/03-HoTT的芝诺.md`，再读 02 与 01；想知道来龙去脉，读 002 至 006；想复核或反驳，读 007；接着做后续工作的人或 AI，先读交接说明 `后续工作交接说明-20260930.md`（文首有阶段收尾加注），再按 001 完成开工闭包。

**English summary.** This repository records a search, carried out with several AI systems under one researcher's direction, for reality-relative paradoxes in homotopy type theory (HoTT): places where the theory, to be economical or general, drops a condition that real processes depend on, so that a task built to need that condition either cannot be finished in the theory although it can be finished in reality (type A), or is treated as finished by the theory although it cannot be finished in reality (type B). It does not look for internal inconsistency, and none is claimed. On 2026-09-30 the researcher gave an operational definition, "UR": something that should be simple, yet even in theory X it cannot be done; judged that such a paradox has very likely been found; and closed the first phase of the search (report: `docs/HoTT悖论查找阶段收尾报告-20260930.md`). The finding, in the researcher's reading: whether two things are the same is, in ordinary logic and mathematics, a one-sentence matter. HoTT, for economy, makes isomorphic things identical (univalence) and, for generality, supplies shapes of every dimension at once (higher inductive types), so in its universe "being the same" never settles. A program that asks level by level whether sameness has settled (a delay-monad program with a judge that returns a proof either way) is proved inside the theory to equal the non-terminating program for every judge, both on the universe and on the product of Eilenberg–MacLane spaces from Example 8.8.6 of the HoTT Book. The same equations, transcribed to Lean (where equality is a mere fact), stop at stage 1; in HoTT the program stops exactly at the cap when the height of the members is capped; asked about the set truncation it also stops at stage 1, but truncation merges the ways of being the same and cannot be decoded back into the universe. The researcher reads this as Zeno's shape: every stage is definitely not yet settled. The underlying mathematics is mostly not new (the product is the Book's example; for the universe the Book wrote in 2013 that the result was expected but not yet done, and this repository machine-checks it); what is offered is the reading and the premise it points to, first univalence. The researcher clarified on 2026-10-01 that the 2026-09-27 reference to Zeno's ghost points to the circle paradox and the repository's further discussion and analysis of it. A7 infinite coherence is a separate AI-proposed Zeno-like candidate, not the referent of that verdict; whether its uniform definition exists remains open. Formal statements are kernel-checked in Cubical Agda 2.8.0 (cubical 0.9) and Lean 4.34.0, with negative controls and exact replays, part of them on two platforms; reading "never halts" as a statement about actual runs still assumes the theory's consistency and canonicity. The shortest audit paper is `docs/社区审计提交/03-HoTT的芝诺.md`; chapter 007 explains how to replay and how to challenge the results; a handoff for follow-up work is in `后续工作交接说明-20260930.md`.

<!-- governance-shard-table:start -->
| Shard | 文件 | 语义范围 | 状态 |
|---|---|---|---|
| 001 | [当前入口与关键文件](<README/001 - 当前入口与关键文件.md>) | 人和 AI 各从哪里进；谁拥有哪份当前真值；按用途分组的仓库地图；关键入口登记表（含收尾报告与算思对话存档）；来源边界；本 README 的维护规则 | current |
| 002 | [我们在找什么](<README/002 - 我们在找什么.md>) | 研究发起人的问题意识（原话逐字）、UR 这一操作定义、要找的不是内部矛盾、两个方向、罗素原则与项目目标、“精彩”的标准、归因是正题 | current |
| 003 | [历史](<README/003 - 历史.md>) | 2026-08-31 至 09-30 的十二个阶段：发生了什么、哪次转折、学到了什么；研究发起人的纠偏线；参与者 | current |
| 004 | [路线地图](<README/004 - 路线地图.md>) | 走过和正在走的路线全景：每条路问什么、谁提出、停在哪、留下什么；41 条方向全部归位 | current |
| 005 | [当前最强前缘：两个幽灵](<README/005 - 当前最强前缘：两个幽灵.md>) | 用户所说的芝诺幽灵（圆环及后续讨论）、罗素线与 UR（阶段收尾时的发现）、独立的 A7 候选、证据阶梯、开放问题与归因 | current |
| 006 | [后续候选前缘](<README/006 - 后续候选前缘.md>) | 阶段收尾之后的排序与九组候选：审计与传播优先；下一个判别动作、升级与撤回条件、谁来做；范围内已关上的；第一阶段收尾意味着什么 | current |
| 007 | [怎样审计、复现与反驳](<README/007 - 怎样审计、复现与反驳.md>) | 证据门禁、工具链、重放命令、证据身份词汇、怎样挑战本仓库的结论、声明层核对工具 | current |
<!-- governance-shard-table:end -->
