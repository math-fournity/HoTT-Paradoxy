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
snapshot_date: 2026-09-30
state_revision: 290
core_generation: core-cognition-generation-9
core_kc_count: 51
direction_projection: 20260930-direction-290
panorama_projection: 20260930-outcome-290
-->

> 合同：`docs/quality/长治理文档分片与索引合同.md`。本页和各分片里的状态是 2026-09-30 的快照（STATE revision 290；核心认知第 9 代，51 条；方向追踪与全景视野 v1.13）。状态的权威在各自的 owner 文件，本页只做路由；快照过期时以 owner 为准。

## 一屏读懂

- **在找什么**：理论为了好用，会把现实里的某个条件改掉。我们在同伦类型论（HoTT）里找这样的改动，再设计一件专门需要那个条件的事，看它显出哪一种“非现实”：现实里做得完、理论里做不完；或者现实里做不完、理论却当作已经做完。要找的不是 HoTT 的内部矛盾。（这是 AI 的概括，研究发起人的原话见 002。）
- **找到了什么**：【用户判定，2026-09-27】「本repo复活了芝诺悖论的幽灵和罗素悖论的幽灵，并且找到的HoTT理论的问题。」两条线的形式命题由证明器内核检查通过、各有负控制，关键运行在 macOS 与 Linux 两个平台上重放。芝诺线的“统一定义写不出”是公开的开放问题，没有被证明。罗素线的“追问永不停机”在 2026-09-30 从元层推论变成了理论内部的定理：把逐层追问写成带判定器的程序，内核检查它在最低宇宙上对任何判定器都永远交不出答案（CG001-C-78；运行只在 Linux 上捕获与重放，尚未在第二个平台重放；Claude 线的目标本地索引，共享 owner 尚待更新）；读到现实中的运行上，仍以所用理论一致为前提。它依赖的两个哲学前提待研究发起人逐字确认，并交社区审计。详见 005。
- **不宣称**：HoTT 不一致；“在有限范围里没找到”等于“不存在”；研究发起人的判定等于数学定理。
- **从哪读起**：想先看结果，读两份社区审计稿 `docs/社区审计提交/01-芝诺悖论的幽灵.md` 与 `docs/社区审计提交/02-罗素悖论的幽灵.md`；想知道来龙去脉，读 002 至 006；想复核或反驳，读 007；接着做后续工作的人或 AI，先读交接说明 `后续工作交接说明-20260930.md`，再按 001 完成开工闭包。

**English summary.** This repository records a search, carried out with several AI systems under one researcher's direction, for reality-relative paradoxes in homotopy type theory (HoTT): places where the theory, to be economical or general, drops a condition that real processes depend on, so that a task built to need that condition either cannot be finished in the theory although it can be finished in reality (type A), or is treated as finished by the theory although it cannot be finished in reality (type B). It does not look for internal inconsistency, and none is claimed. As of 2026-09-30, two lines stand by the researcher's verdict of 2026-09-27. The *ghost of Zeno*: univalence turns sameness into structure. Semi-simplicial structure is a one-line definition where equality is a mere fact (Lean 4, UIP); in HoTT the same line accepts incoherent data, adding each coherence as data leaves the next one open, and the number of levels needed grows with the truncation level, without bound in the universe. Each fixed level can be written (machine-checked up to level 5), while a definition uniform in n is a well-known open problem. The *ghost of Russell*: questioning the existence of the universe level by level ("in which ways are its members the same?") gets the answer "no" at every level in HoTT with higher inductive types (machine-checked). Written as a program in the delay monad that asks level by level, with a judge that returns a proof either way, the questioning is proved inside the theory to equal the non-terminating program for every judge (kernel-checked on 2026-09-30, so far on Linux only), while the same program stops at stage 1+n on the catalogue of types of h-level 1+n, and its transcription to Lean by the same equations stops at stage 1; reading this as a statement about actual runs still assumes that the theory is consistent. Yet HoTT hands the universe over at once by a formation rule. The formal statements are kernel-checked in Cubical Agda 2.8.0 (cubical 0.9) and Lean 4.34.0, with negative controls and cross-platform replays; the Zeno-side impossibility claim and the philosophical premises remain open and are submitted for community audit. Each audit paper in `docs/社区审计提交/` opens with its own English summary; chapter 007 explains how to replay and how to challenge the results; a handoff for follow-up work is in `后续工作交接说明-20260930.md`.

<!-- governance-shard-table:start -->
| Shard | 文件 | 语义范围 | 状态 |
|---|---|---|---|
| 001 | [当前入口与关键文件](<README/001 - 当前入口与关键文件.md>) | 人和 AI 各从哪里进；谁拥有哪份当前真值；按用途分组的仓库地图；关键入口登记表（含算思对话存档）；来源边界；本 README 的维护规则 | current |
| 002 | [我们在找什么](<README/002 - 我们在找什么.md>) | 研究发起人的问题意识（原话逐字）、要找的不是内部矛盾、两个方向、罗素原则、“精彩”的标准、归因是正题 | current |
| 003 | [历史](<README/003 - 历史.md>) | 2026-08-31 至 09-30 的十一个阶段：发生了什么、哪次转折、学到了什么；研究发起人的纠偏线；参与者 | current |
| 004 | [路线地图](<README/004 - 路线地图.md>) | 走过和正在走的路线全景：每条路问什么、谁提出、停在哪、留下什么；41 条方向全部归位 | current |
| 005 | [当前最强前缘：两个幽灵](<README/005 - 当前最强前缘：两个幽灵.md>) | 芝诺幽灵与罗素幽灵：一句话、短链、证据阶梯、判定与未逐字回答之处、最强反方与撤回条件、归因 | current |
| 006 | [后续候选前缘](<README/006 - 后续候选前缘.md>) | 排序标准与九组候选：下一个判别动作、升级与撤回条件、谁来做；范围内已关上的；对“收尾了吗”的回答 | current |
| 007 | [怎样审计、复现与反驳](<README/007 - 怎样审计、复现与反驳.md>) | 证据门禁、工具链、重放命令、证据身份词汇、怎样挑战本仓库的结论、声明层核对工具 | current |
<!-- governance-shard-table:end -->
