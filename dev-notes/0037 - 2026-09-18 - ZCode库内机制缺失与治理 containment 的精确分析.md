# ZCode 库内机制缺失与治理 containment 的精确分析（2026-09-18）

## 用户提问（逐字）

> 在repo内ZCode与Codex治理对齐，似乎因为ZCode本身在repo内的治理机制的缺失，而导致我们无法有效地把repo内的限制在repo内，是吗？

## AI 最终回复（逐字，与对外回复一致）

**是——但要把"缺失"说精确，结论才分得开：ZCode 在 repo 内的机制面确实只有一条（根 AGENTS.md 无条件自动注入），所以"机制级"的治理无法完全关在 repo 内；但"真值级"的治理可以 100% 关在 repo 内，而且"硬强制"这一层的缺口根本不是 ZCode 特有的——Codex 同样没有项目级 Hook，两个宿主是对称的。**

分层说。第一层：**真值层**（规则、SOP、状态、收据、校验器、runtime）。这一层可以完全 confinement 在 repo 内——v5 的设计刻意只依赖两条宿主能力：根 AGENTS.md 注入（两宿主都是产品内建的无条件行为，不依赖任何全局配置）+ 文件读/Bash 执行。任何宿主附加机制（Codex 的 .codex/skills 发现、ZCode 的 ~/.zcode/skills 导入）都被降级为可选加速器，从不作为必要条件。所以在裸机、换机器、甚至没有全局宪法的情况下，repo 仍然自描述：根 AGENTS.md 会被无条件注入，它指向的全部真值都在库里。真值从不离库。

第二层：**机制层**（原生触发）。这里是你说对的的地方：ZCode 没有 repo 内 Skill 发现（只有用户级 ~/.zcode/skills）、忽略项目 Hook、project memory 默认关且在宿主侧。要让 SOP 在 ZCode 获得"原生触发"，注册必须发生在 repo 外（symlink 到 ~/.zcode/skills——真值仍在 repo，注册在外面）。这是结构性外泄，最小化后的形态就是 v5 的"可选 symlink、默认不装"。

第三层：**强制层**（把限制真正焊住）。关键事实：Codex 也没有项目级 Hook——两个宿主都不存在"repo 内声明的硬强制"。现存的强制是三种软硬结合：(1) 程序性合同（AGENTS 正文）；(2) fail-closed 工具（runtime/validator——AI 不跑就得不到收据，跑了就过不了带病状态）；(3) 治理状态机自身。S170–176 的教训恰好是正面证据：会话可以绕过流程性义务（不写 checkpoint），但绕不过 fail-closed 的状态机——HEAD 漂移最终把 canonical 出口锁死，逼出修复需求。这就是"以必然性强制"替代"以 Hook 强制"：不遵守治理的工作流会在自己的证据链上留下不可伪造的缺口。这一层的正确结论不是"ZCode 缺了什么"，而是"两个宿主都还没提供 repo 内 Hook，我们的设计已经把这个约束当作公理在用"。

第二维：**外向遏制**（repo 的东西不外漏到别的项目）。~/.zcode 全局 Skill 每轮向所有项目注入元数据税——v5 默认不装 symlink 正是这个原因；Codex 侧 .codex/skills 天然 repo-scoped，无此问题。 containment 是双向的，v5 两个方向都守了。

仍然真实存在的缺口（诚实清单）：(a) 引导层在库外——"让 AI 一开始就严肃对待 repo 治理"的全局加压（~/.zcode/AGENTS.md、~/.codex/AGENTS.md）不在 repo 内，裸机场景只剩根 AGENTS.md 的自描述（够用，但少了那层纪律加压）；(b) 每台机器的 symlink 注册是手工动作，不入库；(c) ZCode 无 CLI/ACP，双宿主验收（P2 试金石）无法自动化，必须人工执行。

如果要固化这个洞察：建议在 v5 的 003 分片把"宿主最小合同"写成显式 invariant——本 repo 治理只依赖【根 AGENTS 注入 + 文件读 + shell 执行】三件事，任何治理正文不得把宿主附加机制写成必要条件（validator 可机械检查）——等你授权 P2 时一并落地。
