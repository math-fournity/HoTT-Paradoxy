# HoTT-Paradoxy：同伦类型论中的非现实性悖论——结论与证据

**中文** · [Русский](README-RU.md) · [Deutsch](README-DE.md) · [Français](README-FR.md) · [English](README-EN.md)

**摘要**　同伦类型论（HoTT）为了经济与普适，把“相同”从一次检查就落定的事实，改成了可以一层层追问“以什么方式相同”的结构：同构的东西就是同一个（单价性），任意高维的形状在宇宙里一次齐备（高阶归纳类型）。我们把“确认两个东西是不是同一个”写成一个逐层追问的程序：第 k 问检查这份相同是否已在第 k 层了结（即是否为 h-层 k+1 的类型），每一问由判定器交出带证明的“是”或“否”，答“是”就停并报出层数。我们在 Cubical Agda 中证明：对任何判定器，这个程序在宇宙上（含高阶归纳类型）与乘积 ∏ₙ K(ℤ,n+1) 上都等于永不停机的程序 `never`；成员高度封顶时，它恰好在封顶所决定的那一问停；按同一组方程转写到“相同是事实”的 Lean 4，第 1 问就停；对集合截断发问也在第 1 问停，但截断把相同的多种方式合成了一种，而且解码不回宇宙。研究发起人把非现实性悖论定义为“本来应该很简单的事情，甚至在X理论中，都做不到”（UR），把这一结果读作与芝诺悖论同形的悖论，并判断它很可能就是本项目要找的那一个。数学事实大多不新：乘积一侧是 HoTT Book 的例 8.8.6；宇宙一侧，书中（2013）写为预计可证、尚未做出，本仓库给出了机器证明。新的主要是读法，以及它指向的前提，首先是单价性。第二条线：半单纯类型的统一定义在书式 HoTT 中至今写不出，这是公开的开放问题；研究发起人判定这条线“复活了芝诺悖论的幽灵”。全部正向命题由证明器内核检查（Cubical Agda 2.8.0 与 cubical 0.9；Lean 4.34.0），附负控制与 107 个可重放的运行收据。我们不宣称 HoTT 不一致；“很可能已经找到”是研究发起人的判断，不是定理。

**关键词**　同伦类型论；单价性；高阶归纳类型；截断层级；Delay 单子；无穷相干；芝诺悖论；非现实性悖论

> **关于本分支**：`main` 只放支撑结论的关键内容：结论文档、精确命题、证明源码、运行收据与重放方法。研究的全部过程在 [`dev` 分支](https://github.com/math-fournity/HoTT-Paradoxy/tree/dev)：研究发起人的原话账本、方向与结果投影、各 AI 的工作区与审计往来、治理与状态。本分支由 `dev` 的提交 [`24950d5d`](https://github.com/math-fournity/HoTT-Paradoxy/commit/24950d5d19ee6d0e7edc6c2d6ff93f1c18a2c2e1) 按清单生成（[`RELEASE-MANIFEST.json`](RELEASE-MANIFEST.json)），不在本分支上直接修改。本说明另有俄、德、法、英文版本，内容相同。

## 1. 研究发起人的定义与判定

研究发起人对“非现实性悖论”的操作定义（2026-09-30，原话）：

> `UR`=`本来应该很简单的事情，甚至在X理论中，都做不到`，我想这就是一种类似芝诺悖论的`不合理`。

“现实”指 UR 的前半句，“悖论”指整句；判定“不合理”的，是一眼看过去的人。这一判定属于研究发起人，不是数学定理。研究发起人的两句判定（原话）：

> 本repo复活了芝诺悖论的幽灵和罗素悖论的幽灵，并且找到的HoTT理论的问题。

（2026-09-27）

> 把所有该做的，全部做完，我认为我们要阶段性地收尾HoTT悖论查找工作了，因为我们很可能已经找到了。

（2026-09-30）

## 2. HoTT 的芝诺：“是同一个”永远了结不了

**那件本来很简单的事**：确认两个东西是不是同一个。

**专门碰它的过程**：一个逐层追问的程序 Q。它问“这份目录里的相同，到第 k 层了结了没有”（技术上：它是不是 h-层 k+1 的类型）；每一问由判定器交出带证明的“是”或“否”；答“是”就停，并报出层数。Q 停下，当且仅当在某个有限层了结（CG001-C-77）。

**结果**（机器证明）：

| 情形 | 同一个程序的结局 | 命题 |
|---|---|---|
| 相同是事实（按同一组方程转写到 Lean 4） | 宇宙第 1 问停 | CG001-C-80 |
| HoTT，h-层 1+n 的类型的目录 | 恰好第 1+n 问停 | CG001-C-79 |
| HoTT，同一乘积、成员高度封顶 b | 恰好第 2+b 问停 | CG001-C-82 |
| HoTT，乘积 ∏ₙ K(ℤ,n+1)（HoTT Book 例 8.8.6） | 对任何判定器都等于永不停机的 `never` | CG001-C-81 |
| HoTT（含高阶归纳类型），宇宙 | 对任何判定器都等于 `never` | CG001-C-75、CG001-C-78 |
| HoTT，集合截断 | 第 1 问停；但截断把相同的多种方式合成了一种，而且解码不回宇宙 | CG001-C-83 |

**与芝诺对位**（模式匹配，不是数学上的同构）：

| | 芝诺 | HoTT |
|---|---|---|
| 本来很简单的事 | 从这里走到那里 | 确认两个东西是不是同一个 |
| 理论为了好用改掉的条件 | 位置可以无限细分 | 相同可以无限细分 |
| 每一步看到什么 | 还剩一半，确定没到 | 这一层还没了结，确定的“否” |
| 结局 | 永远走不完 | 程序等于 `never` |
| 教科书的消解 | 极限 | 截断 |

**最强的反对**：“对集合截断发问，第 1 问就停，所以只是问法不对。”回应：截断回答的是“有几个分支”，它把相同的多种方式合成了一种，而且回不到宇宙，被问的对象已经换了。这像用极限回答芝诺：一条定义把“走到了”宣布回来，被改掉的条件本身并没有恢复。这一回应是解读，交审计。

**它不是什么**：

- 不是 HoTT 的内部矛盾。
- 数学事实大多不新：这类乘积没有有限层，是 HoTT Book 的例 8.8.6；宇宙本身，书里（2013）写的是预计可以证明、但尚未做出；Kraus–Sattler 2015 证明了单价宇宙层级里的第 n 个宇宙不是 n-型；含高阶归纳类型的单个宇宙在本仓库有机器证明（CG001-C-75）。新的主要是读法，以及它指向的前提，首先是单价性。
- “永不停”是理论内部的定理。读成“现实中照程序跑永远拿不到答案”，还要所用理论一致，对任意判定器另需典范性。
- “很可能已经找到”是研究发起人的判断，不是定理。

详读：[社区审计稿 03《HoTT 的芝诺》](docs/社区审计提交/03-HoTT的芝诺.md)（最短，末尾有五个审计问题）；[02《罗素悖论的幽灵》](docs/社区审计提交/02-罗素悖论的幽灵.md)；[第一阶段收尾报告](docs/HoTT悖论查找阶段收尾报告-20260930.md)。

## 3. 芝诺悖论的幽灵：无穷相干

- **取舍**：单价性让同构即相同，“相同”变成了数据。例如 Bool 与自己“相同”有两个真的不同的证明，沿第二个搬运 `true` 得到 `false`（CG001-C-63）。
- **过程**：写下半单纯结构，用点、线、三角形、四面体一层层粘出形状，要求“面的面”对得上。经典数学里这是一行定义。
- **观察**：在“相同是事实”的世界（Lean 4）里，这一行就是完整定义，六边形相干由 `rfl` 成立（CG001-C-65）；在 HoTT 里，同一行定义接受对不上的数据，两条化简路线在圆周上一条绕 1 圈、一条绕 2 圈（CG001-C-64）；补上六边形之后补法不唯一，再下一级（P₄）对其中一种补法不成立（CG001-C-66、CG001-C-68）；要补几级由“相同”有几层决定（CG001-C-70）；每个固定层都写得出（机器检查到第 5 层，CG001-C-62）。
- **边界**：对层数 n 统一的内部定义是公开难题，它的不可能性没有被证明。书式 HoTT 里一旦出现半单纯类型的统一定义，这条线的强形式撤回。

详读：[社区审计稿 01《芝诺悖论的幽灵》](docs/社区审计提交/01-芝诺悖论的幽灵.md)。

## 4. 命题与证据

- [`CLAIMS.md`](CLAIMS.md)：每个命题的精确陈述、证据与禁止外推；按证明包列出主运行、负控制与跨平台重放。
- 证明源码：`HoTT/formal/`。每个包的 `CLAIM.md` 写明命题全文与范围。
- 运行收据：`HoTT/verification/runs/`，共 107 个，其中 49 个被内核接受，58 个是预期被拒的负控制（它们检验的是精确的边界，不是失败的历史）。部分命题在 macOS 与 Linux 两个平台上各有运行。
- [`RELEASE-MANIFEST.json`](RELEASE-MANIFEST.json)：本分支 699 个文件各自的 SHA-256 与角色，以及它们取自 `dev` 的哪个提交。

工具链：Cubical Agda 2.8.0 与 cubical 库 v0.9（选项写在各源文件里：`--safe --cubical --guardedness`）；Lean 4.34.0，只用核心库、不含 Mathlib，用来做“相同是事实”的对照。收据引用的工具链记录在 `HoTT/formal/dedekind-omega-missile/`（macOS 上的 Agda）、`HoTT/formal/claude-cg001/pedometer-ablation-lean/`（macOS 上的 Lean）与 `HoTT/formal/cloud-opus-glm-audit/`（Linux）；前两个目录沿用 `dev` 上的位置，在本分支里只放这些记录文件。

## 5. 怎样重放

装好 Agda 2.8.0、cubical v0.9 与 Lean 4.34.0 之后，在仓库根目录运行：

```sh
python3 tools/replay.py --agda /path/to/agda --cubical-lib /path/to/cubical/cubical.agda-lib --lean-sysroot /path/to/lean-4.34.0 --jobs 4
```

它用相对路径重建每个收据里的命令，逐个运行，再与收据比较：结局（接受或拒绝）必须一致；输出在把仓库根与库路径换成占位符之后逐行比较。负控制只有再次被拒才算通过；输出也一致，就说明它是因为记录的理由被拒。只看一个：`--only <运行编号>`；列出全部：`--list`。全部运行串行约需一个半小时。

收据里的命令记录的是捕获时那台机器的绝对路径。逐字节重放的原始工具在 `dev` 分支（`.claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py`、`Cloud-Opus审计并补完GLM/tools/verify_copus_run.py`）。

## 6. 文中提到、但不在本分支的路径

结论文档里还提到研究过程中的文件：研究发起人的原话账本 `核心认知.md`、方向与结果投影、各 AI 的工作区、审计往来、目标内索引等。它们都在 `dev` 分支：

| 路径 | 在 `dev` 上 |
|---|---|
| `.claude/goals/CG-001-targeted-overview` | [打开](https://github.com/math-fournity/HoTT-Paradoxy/tree/dev/.claude/goals/CG-001-targeted-overview) |
| `.claude/goals/CG-001-targeted-overview/证据索引.md` | [打开](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/.claude/goals/CG-001-targeted-overview/%E8%AF%81%E6%8D%AE%E7%B4%A2%E5%BC%95.md) |
| `.claude/goals/CG-002-a7-infinite-coherence` | [打开](https://github.com/math-fournity/HoTT-Paradoxy/tree/dev/.claude/goals/CG-002-a7-infinite-coherence) |
| `.claude/goals/CG-003-a7-self-audit` | [打开](https://github.com/math-fournity/HoTT-Paradoxy/tree/dev/.claude/goals/CG-003-a7-self-audit) |
| `.claude/思考与发现` | [打开](https://github.com/math-fournity/HoTT-Paradoxy/tree/dev/.claude/%E6%80%9D%E8%80%83%E4%B8%8E%E5%8F%91%E7%8E%B0) |
| `.claude/总索引.md` | [打开](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/.claude/%E6%80%BB%E7%B4%A2%E5%BC%95.md) |
| `.claude/调研请求/20260930-相同永远了结不了-社区先例调研请求.md` | [打开](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/.claude/%E8%B0%83%E7%A0%94%E8%AF%B7%E6%B1%82/20260930-%E7%9B%B8%E5%90%8C%E6%B0%B8%E8%BF%9C%E4%BA%86%E7%BB%93%E4%B8%8D%E4%BA%86-%E7%A4%BE%E5%8C%BA%E5%85%88%E4%BE%8B%E8%B0%83%E7%A0%94%E8%AF%B7%E6%B1%82.md) |
| `Cloud-Opus审计并补完GLM` | [打开](https://github.com/math-fournity/HoTT-Paradoxy/tree/dev/Cloud-Opus%E5%AE%A1%E8%AE%A1%E5%B9%B6%E8%A1%A5%E5%AE%8CGLM) |
| `Cloud-Opus审计并补完GLM/01-工具链与复现.md` | [打开](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/Cloud-Opus%E5%AE%A1%E8%AE%A1%E5%B9%B6%E8%A1%A5%E5%AE%8CGLM/01-%E5%B7%A5%E5%85%B7%E9%93%BE%E4%B8%8E%E5%A4%8D%E7%8E%B0.md) |
| `Cloud-Opus审计并补完GLM/02-断裂审计-逐命题（D1）.md` | [打开](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/Cloud-Opus%E5%AE%A1%E8%AE%A1%E5%B9%B6%E8%A1%A5%E5%AE%8CGLM/02-%E6%96%AD%E8%A3%82%E5%AE%A1%E8%AE%A1-%E9%80%90%E5%91%BD%E9%A2%98%EF%BC%88D1%EF%BC%89.md) |
| `Cloud-Opus审计并补完GLM/11-收据核验结果.json` | [打开](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/Cloud-Opus%E5%AE%A1%E8%AE%A1%E5%B9%B6%E8%A1%A5%E5%AE%8CGLM/11-%E6%94%B6%E6%8D%AE%E6%A0%B8%E9%AA%8C%E7%BB%93%E6%9E%9C.json) |
| `Cloud-Opus审计并补完GLM/13-外部复核请求.md` | [打开](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/Cloud-Opus%E5%AE%A1%E8%AE%A1%E5%B9%B6%E8%A1%A5%E5%AE%8CGLM/13-%E5%A4%96%E9%83%A8%E5%A4%8D%E6%A0%B8%E8%AF%B7%E6%B1%82.md) |
| `Cloud-Opus审计并补完GLM/14-罗素面终局判词.md` | [打开](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/Cloud-Opus%E5%AE%A1%E8%AE%A1%E5%B9%B6%E8%A1%A5%E5%AE%8CGLM/14-%E7%BD%97%E7%B4%A0%E9%9D%A2%E7%BB%88%E5%B1%80%E5%88%A4%E8%AF%8D.md) |
| `Cloud-Opus审计并补完GLM/README.md` | [打开](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/Cloud-Opus%E5%AE%A1%E8%AE%A1%E5%B9%B6%E8%A1%A5%E5%AE%8CGLM/README.md) |
| `Cloud-Opus审计并补完GLM/tools` | [打开](https://github.com/math-fournity/HoTT-Paradoxy/tree/dev/Cloud-Opus%E5%AE%A1%E8%AE%A1%E5%B9%B6%E8%A1%A5%E5%AE%8CGLM/tools) |
| `Cloud-Opus审计并补完GLM/tools/capture_zeno_line_replays.sh` | [打开](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/Cloud-Opus%E5%AE%A1%E8%AE%A1%E5%B9%B6%E8%A1%A5%E5%AE%8CGLM/tools/capture_zeno_line_replays.sh) |
| `Cloud-Opus审计并补完GLM/附件/20260926-Session问答原文存档（用户上传，GLM-Auditor会话）.md` | [打开](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/Cloud-Opus%E5%AE%A1%E8%AE%A1%E5%B9%B6%E8%A1%A5%E5%AE%8CGLM/%E9%99%84%E4%BB%B6/20260926-Session%E9%97%AE%E7%AD%94%E5%8E%9F%E6%96%87%E5%AD%98%E6%A1%A3%EF%BC%88%E7%94%A8%E6%88%B7%E4%B8%8A%E4%BC%A0%EF%BC%8CGLM-Auditor%E4%BC%9A%E8%AF%9D%EF%BC%89.md) |
| `Cloud-Opus审计并补完GLM/附件/工作过程文件/自查轮/verify-all-rerun-46个运行.json` | [打开](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/Cloud-Opus%E5%AE%A1%E8%AE%A1%E5%B9%B6%E8%A1%A5%E5%AE%8CGLM/%E9%99%84%E4%BB%B6/%E5%B7%A5%E4%BD%9C%E8%BF%87%E7%A8%8B%E6%96%87%E4%BB%B6/%E8%87%AA%E6%9F%A5%E8%BD%AE/verify-all-rerun-46%E4%B8%AA%E8%BF%90%E8%A1%8C.json) |
| `GLM-5.3-Flash/README.md` | [打开](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/GLM-5.3-Flash/README.md) |
| `GLM-5.3-Flash/审计请求` | [打开](https://github.com/math-fournity/HoTT-Paradoxy/tree/dev/GLM-5.3-Flash/%E5%AE%A1%E8%AE%A1%E8%AF%B7%E6%B1%82) |
| `GLM-5.3-Flash/思考与发现` | [打开](https://github.com/math-fournity/HoTT-Paradoxy/tree/dev/GLM-5.3-Flash/%E6%80%9D%E8%80%83%E4%B8%8E%E5%8F%91%E7%8E%B0) |
| `GLM-5.3-Flash/策略快照/20260926-D2后罗素线策略-大白话快照.md` | [打开](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/GLM-5.3-Flash/%E7%AD%96%E7%95%A5%E5%BF%AB%E7%85%A7/20260926-D2%E5%90%8E%E7%BD%97%E7%B4%A0%E7%BA%BF%E7%AD%96%E7%95%A5-%E5%A4%A7%E7%99%BD%E8%AF%9D%E5%BF%AB%E7%85%A7.md) |
| `GLM-5.3-Flash/裁定问题/20260926-M2-形成规则是回答还是回避-两面陈词.md` | [打开](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/GLM-5.3-Flash/%E8%A3%81%E5%AE%9A%E9%97%AE%E9%A2%98/20260926-M2-%E5%BD%A2%E6%88%90%E8%A7%84%E5%88%99%E6%98%AF%E5%9B%9E%E7%AD%94%E8%BF%98%E6%98%AF%E5%9B%9E%E9%81%BF-%E4%B8%A4%E9%9D%A2%E9%99%88%E8%AF%8D.md) |
| `HoTT/CLAIM_EVIDENCE_MATRIX.md` | [打开](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/HoTT/CLAIM_EVIDENCE_MATRIX.md) |
| `HoTT/verification/PROOF_VERSION_CLOSURE.json` | [打开](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/HoTT/verification/PROOF_VERSION_CLOSURE.json) |
| `README.md` | [打开](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/README.md) |
| `Terra对Opus的审计` | [打开](https://github.com/math-fournity/HoTT-Paradoxy/tree/dev/Terra%E5%AF%B9Opus%E7%9A%84%E5%AE%A1%E8%AE%A1) |
| `Terra对Opus的审计/Opus给GPT的回应` | [打开](https://github.com/math-fournity/HoTT-Paradoxy/tree/dev/Terra%E5%AF%B9Opus%E7%9A%84%E5%AE%A1%E8%AE%A1/Opus%E7%BB%99GPT%E7%9A%84%E5%9B%9E%E5%BA%94) |
| `rulings.md` | [打开](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/rulings.md) |
| `scripts/audit/verify_math_proof_delivery_governance.py` | [打开](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/scripts/audit/verify_math_proof_delivery_governance.py) |
| `scripts/audit/verify_proof_version_closure.py` | [打开](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/scripts/audit/verify_proof_version_closure.py) |
| `sources/prompts/Claude-UR与芝诺的模式匹配-用户原文-20260930.md` | [打开](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/sources/prompts/Claude-UR%E4%B8%8E%E8%8A%9D%E8%AF%BA%E7%9A%84%E6%A8%A1%E5%BC%8F%E5%8C%B9%E9%85%8D-%E7%94%A8%E6%88%B7%E5%8E%9F%E6%96%87-20260930.md) |
| `sources/prompts/Claude-归因是正题-用户原文-20260924.md` | [打开](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/sources/prompts/Claude-%E5%BD%92%E5%9B%A0%E6%98%AF%E6%AD%A3%E9%A2%98-%E7%94%A8%E6%88%B7%E5%8E%9F%E6%96%87-20260924.md) |
| `sources/prompts/Claude-罗素原则P1至P3-用户原文-20260926.md` | [打开](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/sources/prompts/Claude-%E7%BD%97%E7%B4%A0%E5%8E%9F%E5%88%99P1%E8%87%B3P3-%E7%94%A8%E6%88%B7%E5%8E%9F%E6%96%87-20260926.md) |
| `sources/prompts/Codex-非现实性悖论的目标与A向读法-用户原文-20260930.md` | [打开](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/sources/prompts/Codex-%E9%9D%9E%E7%8E%B0%E5%AE%9E%E6%80%A7%E6%82%96%E8%AE%BA%E7%9A%84%E7%9B%AE%E6%A0%87%E4%B8%8EA%E5%90%91%E8%AF%BB%E6%B3%95-%E7%94%A8%E6%88%B7%E5%8E%9F%E6%96%87-20260930.md) |
| `sources/prompts/GLM-算符先行于存在性落定-用户原文-20260926.md` | [打开](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/sources/prompts/GLM-%E7%AE%97%E7%AC%A6%E5%85%88%E8%A1%8C%E4%BA%8E%E5%AD%98%E5%9C%A8%E6%80%A7%E8%90%BD%E5%AE%9A-%E7%94%A8%E6%88%B7%E5%8E%9F%E6%96%87-20260926.md) |
| `全景视野.md` | [打开](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/%E5%85%A8%E6%99%AF%E8%A7%86%E9%87%8E.md) |
| `扩展认知.md` | [打开](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/%E6%89%A9%E5%B1%95%E8%AE%A4%E7%9F%A5.md) |
| `扩展认知/011 - 本来应该很简单的事：UR 与芝诺的模式匹配.md` | [打开](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/%E6%89%A9%E5%B1%95%E8%AE%A4%E7%9F%A5/011%20-%20%E6%9C%AC%E6%9D%A5%E5%BA%94%E8%AF%A5%E5%BE%88%E7%AE%80%E5%8D%95%E7%9A%84%E4%BA%8B%EF%BC%9AUR%20%E4%B8%8E%E8%8A%9D%E8%AF%BA%E7%9A%84%E6%A8%A1%E5%BC%8F%E5%8C%B9%E9%85%8D.md) |
| `方向追踪.md` | [打开](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/%E6%96%B9%E5%90%91%E8%BF%BD%E8%B8%AA.md) |
| `核心认知.md` | [打开](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/%E6%A0%B8%E5%BF%83%E8%AE%A4%E7%9F%A5.md) |

## 7. 分支

- `main`（本分支）：结论与证据。由 `dev` 上的 `scripts/release/build_main_release.py` 按 `scripts/release/main-release-spec.json` 生成。要更新，就在 `dev` 上改清单或结论文档，再重新生成；不在本分支上直接提交。
- `dev`：全部研究过程，所有工作都在那里进行。
