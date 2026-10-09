# 共享命题编号的分支命名空间与撞号映射

> CG-006 S7-c，本机会话 d58e0c0d（Opus 5.5），2026-10-08。身份：编号与去向的治理登记，不是数学结论。共享矩阵 `HoTT/CLAIM_EVIDENCE_MATRIX.md` 登记分支命题时，以本表为准。
>
> 依据：在 `dev`、`origin/dev-01` 至 `origin/dev-09`（无 dev-05）、本地 `dev-08` 与相关 `codex/*` 分支上，逐一抽取共享矩阵中 C-357 起的命题行，以及 `HoTT/formal/*/CLAIM*.md` 中出现的编号，比较同号是否同义；再逐文件比较各分支的包与 `dev` 的同路径文件，并比较运行目录是否同名异内容。抽取脚本与结果保存在 CG-006 目标包的 `verification/` 下。

## 1. 规则

1. `dev` 上的 `C-NNN` 保持原义，不改号。它们由主干（GUI 标签 dev-08，即主检出的 `dev`）写成。
2. 只在 GPT 分支上写成的命题加分支前缀：dev-01 写成 `D01-C-NNN`，dev-02 写成 `D02-C-NNN`，dev-09 写成 `D09-C-NNN`。写法仿 Claude 线的 `CG001-C-NN`。同一个包里本来不撞号的编号也加前缀，保持包内编号连贯。
3. GPT 包的文件一字不改。包内文字仍写原编号，读者按本表换算。
4. `dev` 的下一个共享编号从 **C-387** 起。C-379 至 C-386 已在 dev-09 的文件里用过，跳过它们，免得读者把 `C-379` 与 `D09-C-379` 混淆。
5. 证明包 ID（`MP-…`）只在 dev-02 与 `dev` 之间重名（`MP-ZFC-ACTUAL-Q-HOTT-COUNTEREXAMPLE-001`、`MP-ZFC-ACTUAL-Q-ZENO-LIMIT-CONTROL-001`），而 dev-02 留在分支上（§3）。将来若要并入，写成 `D02:MP-…` 以示区分。

## 2. 撞号表

| 原编号 | `dev`（保持原义） | dev-01 | dev-02 | dev-09 |
|---|---|---|---|---|
| C-357、C-358 | HoTT 截断与粗完成不反射（归属见 §4） | — | 同义（分支沿用 `dev` 的行） | 同义 |
| C-359 | `ZFCOneUse` 政策核（`MP-ZFC-ACTUAL-Q-POLICY-001`） | — | **D02-C-359**：强 P + `PolicyScopeWitness` + B ⟹ False（`MP-ZFC-ACTUAL-Q-POLICY-002`） | — |
| C-360 | HoTT 截断反例（`HoTTCounterexample.agda`） | — | **D02-C-360**：同一定理的近同源文件，差 1 行 | — |
| C-361 | 芝诺极限控制（`ZenoLimitControl.lean`） | — | **D02-C-361**：同一定理的近同源文件，差 4 行 | — |
| C-362 | Norton 修订完成不推出严格完成 | — | **D02-C-362**：成员语言边界（`MP-ZFC-OBSERVATION-LANGUAGE-BOUNDARY-001`） | — |
| C-363 | HoTT 完成合同缺口 | — | **D02-C-363**：同一 QProfile 异判破坏 `QUniform`（`MP-ZFC-COMPLETION-POLICY-UNIFORMITY-001`） | — |
| C-364 | 粗的标准解视图决定不了 `OriginDone` | — | **D02-C-364**：未付完成提升的反模型（`MP-ZFC-UNPAID-COMPLETION-PROMOTION-001`） | — |
| C-365 | H0 有限 trace | — | **D02-C-365**：成员语言不变性（`MP-ZFC-MEMBERSHIP-LANGUAGE-INVARIANCE-001`） | — |
| C-366 | Zermelo 模型中的过程表示 | — | — | — |
| C-367、C-368 | T-OBS、T-DIAG | — | — | 同一包，文件与 `dev` 逐字相同；dev-09 的矩阵没有登记这两行，不撞号 |
| C-369 | set.mm 附录 C 的变量扩展（`MP-GODEL-Q-SETMM-APPENDIX-C-VAR-EXTENSION-001`） | **D01-C-369**：应用充分性 `ApplicationAdequacy`（`MP-ZFC-META-SUBTHEORY-ADEQUACY-001`） | — | **D09-C-369**：Foundation 第一不完备定理接口的 R3 重放（`MP-FOUNDATION-INCOMPLETENESS-R3-001`） |
| C-370 | 规范过程审计（`MP-ZFC-NORMATIVE-PROCESS-AUDIT-001`） | **D01-C-370**：量子化半步 8→4→2→1→0，第 4 步完成、第 3 步未完成（`MP-ZFC-DENSE-QUANTIZED-MOTION-001`） | — | **D09-C-370**：CCTTmini 的正控制（`MP-CUBICAL-GODEL-FRAGMENT-001`） |
| C-371 | 公开换题时审计判为修订解决 | **D01-C-371**：稠密与量子化前 0–3 阶段余量相同，稠密在任何有限阶段都不完成（`MP-ZFC-DENSE-QUANTIZED-CONTRACT-001`） | — | **D09-C-371**：正见证携带推导 |
| C-372–C-374 | 规范过程审计的三条控制 | — | — | **D09-C-372–C-374**：CCTTmini 的两个拒绝与“检查通过即携带推导” |
| C-375–C-378 | MSS 定义域与时间、阶段顺序控制 | — | — | **D09-C-375–C-378**：位编码、解析、解码、编码单射（`MP-CUBICAL-GODEL-NAT-CODING-001`） |
| C-379–C-386 | 未用（`dev` 下一个从 C-387 起） | — | — | **D09-C-379–C-386**：公式谓词、可证见证、引用、公式编码与自实例（`MP-CUBICAL-GODEL-FORMULA-PREDICATE-001`、`MP-CUBICAL-GODEL-FORMULA-CODING-001`） |

dev-03、dev-04 的 `zfc-observation-boundary` 包、dev-06、dev-07 没有使用 C 编号，不在此表中。

## 3. 分支包的去向

| 分支（提交） | 包 | 编号 | 去向 | 理由与证据 |
|---|---|---|---|---|
| dev-01（`f10899cb`） | `zfc-dense-quantized-motion`、`zfc-dense-quantized-contract`、`zfc-meta-subtheory-adequacy` | D01-C-369 至 C-371 | **已并入 `dev`**（`4a3535d9`；路径不变，逐字节相同） | 它们是研究发起人“稠密性—运动”原合同（KC-000003、004、019）的机器控制：量子化的运动在第 4 步完成，稠密的在任何有限阶段都不完成。13 个 Lean 运行在本机禁网沙盒中重新执行，退出码、stdout、stderr 逐字节一致；另有 1 个 set.mm 来源重放记录没有可执行命令，收据哈希一致。 |
| dev-09（`ac6391b6`） | `cubical-godel-fragment` | D09-C-370 至 C-386 | **已并入 `dev`**（`4a3535d9`） | Cubical Agda 中的哥德尔编码片段：编码、解码、引用与自实例的语法形状。它没有对象层的可表示性定理，不是第一不完备定理。8 个 Agda 运行在替换原工作树路径之后一致；1 个输入域记录没有可执行命令。 |
| dev-09 | `external-foundation-incompleteness` | D09-C-369 | 留在分支 | 运行依赖 `/tmp` 中已不存在的 Foundation@f3972f42 检出，本机不能重放。它的作用已由 CG-006 的 CG001-C-102（Foundation 1fb01b72 上的交叉核对）与 C-95 至 C-101（真实 𝗭𝗙𝗖）取代。 |
| dev-02（`4005fa80`） | `zfc-actual-q-policy`（分支版） | D02-C-359 至 C-365 | 留在分支 | 与 `dev` 同路径：7 个文件内容不同，8 个文件只在分支，另有 5 个运行目录同名异内容。直接合并会形成双重真值。它是条件性的政策演算（“ZFC”是命题变量 `ZFCBase`），角色已由 CG-005 的 C-90、C-94 与 CG-006 的 C-99 至 C-101 在真实 𝗭𝗙𝗖 上取代。分支自己的集成交接单写了逐文件的合并步骤：`origin/dev-02:audit/20261004-ZFC-Q-POLICY-CANDIDATE-INTEGRATION-HANDOFF.md`。 |
| dev-03（`854a6aba`）、dev-04（`f97bbcb4`） | `zfc-observation-boundary`（两版） | 无 C 编号（`MP-ZFC-OBSERVATION-BOUNDARY-001` 等） | 留在分支 | 两条分支在同一路径上各自分叉（29 个文件不同），并入任何一版都会偏向一方。它们是条件性政策演算，角色同上。来源卡（UOU 教材、SEP）在终局报告中按“分支@提交:路径”引用。 |
| dev-06（`af0d9c5c`）、dev-07（`a753f9bc`） | 无新的形式包 | — | 留在分支 | Pattern-First 的方案、卡片与审计；H0 过程锚的七个字段已由 CG-005 吸收。 |
| dev-08（本地 `3cb6a6b4`） | 无新的形式包 | — | **已并入 `dev`**（`64e5e04a`） | 主干的 dev-notes 增量（0109 含主干第 112 轮）与 GUI 对话录 README 的 10-05 初稿（保留 `dev` 的 10-07 版）。 |

## 4. 归属更正

共享编号 C-357、C-358 由 Codex 在主干（dev-08，2026-10-03）写成，却放在 `HoTT/formal/claude-cg001/observation-completion-bridge/` 与 `completion-reflection-failure/` 下，运行名带 `-CG001-`。它们不是 Claude 线的工作。Claude 线的编号形如 `CG001-C-NN`（目前到 CG001-C-118），与共享编号 C-357、C-358 是两套编号。为了收据稳定，路径与运行名不改。（CG-005 审计报告 A6、A7）

## 5. 分支的保存

- 不删除任何分支或 worktree。`origin` 上的 `dev-01` 至 `dev-09` 与各 `codex/*` 分支保持原样。
- 只在本机、远端没有的提交：本地 `dev-08`（比 `origin/dev-08` 多 3 个归档提交，已并入 `dev`）、`codex/hott-motive-zfc-literature`（比远端多 12 个提交）、`codex/t-precision-closure-repair`（1 个提交）。
- 2026-10-08 已普通推送（不带 force），推送后回读远端，四条都与本地一致：`dev` `9a25268e..28f68e99`；`dev-08` `81e2f12c..3cb6a6b4`；`codex/hott-motive-zfc-literature` `b1c14dfb..c6bdf892`；新建 `codex/t-precision-closure-repair` `eaf7b97e`。
- 其余只在本机的分支（`dev-glm-5.3`、`claude/git-worktree-path-4c282f`、`claude/gui-reaudit-continuation`）的提交都已包含在 `dev` 中，没有另行推送。主检出已切回 `dev`；worktree `.claude/worktrees/cg006-dev` 改为 detached，保留不删。
