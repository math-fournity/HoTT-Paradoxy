# CG-006：最后的AI——把哥德尔式 Q 推进到 bare ZFC 的完全形式化，并接手全部分支

<!-- goal-x:essentials-begin -->
> goal-x 目标包；HUMAN_EDITED；v1.1；2026-10-08；本机会话 d58e0c0d（Opus 5.5）。本文件是单体开工与恢复闭包。

## 1. 目标与完成门

- **授权**【原话】（2026-10-07）：“这个repo全部的分支和git worktree，现在由你全面接手了，你就是‘最后的AI’，所以你认为应该做的，都可以做，我全面授权你。”“你要综合所有之前的AI的所有工作，推进到完全的形式化和机器证明的完成。”判词全文见 CG-005 `原话摘录.md` 0109 第 56 轮与 main README 顶部。
- **补充**【原话】（2026-10-08）：“如果你最终要切换回dev分支，那么我认为这个分支上的CLAUDE.md可以保留。……我需要你结合你的调查，写好后续工作的需要的认知闭包内容和方案，我听说很多东西其实GPT已经探索到了，所以这种回GUI导出对话录翻查的工作，或许未来工作的过程中，应该经常翻查八个对话录的内容，不能就这么一次就行了。”
- **父目标**：CG-005 的哥德尔式 Q 定理（`HoTT/formal/claude-cg001/godel-q/`，C-84..C-94）对“满足标准元性质的有效理论”成立。本目标要做三件事：
  1. 把它落到 **Foundation 中真实的 𝗭𝗙𝗖**（ℒₛₑₜ 语法、LK 证明系统），使“bare ZFC 在时间维度上的观察力不完备”成为不带未证元定理前提的 Lean 定理；
  2. 接手全部分支；
  3. 写回共享 owner，并发布。
- **技术路线与阶段**：见 `方案.md` §2（设计决定 D-A 至 D-E）与 §3（阶段与验收）。Foundation 用 `FormalizedFormalLogic/Foundation@1fb01b72`，其 Mathlib 锁定 `5ed29652`，即本项目 Astra 缓存中的 Mathlib；Lean v4.34.0。
- **完成门**：
  1. S2、S4、S5 的 Lean 文件全部过核（exit 0；只用 propext/choice/Quot.sound；无 sorry），有运行收据并逐字节重放；`CLAIM.md` 写明精确命题，并逐条对照 GPT 的“六道门”（GUI 索引 #7）。
  2. S6 过核，或照实写明卡在哪条引理，并留下最小可续的形式状态。
  3. 全部分支：保全主检出现场（S7-a）；撞号重新编号方案落地；有价值的成果并入 `dev`，或说明为何不并；不删任何分支与 worktree。
  4. 共享 owner 经 canonical checkpoint 写回；核心认知第 14 代（纳入清单先经研究发起人过目）；总索引维护；分片校验 PASS。
  5. 主检出切回 `dev`，根 `CLAUDE.md` 保留；`main` 由 `scripts/release/build_main_release.py` 生成；推送 `dev` 与 `main`；回读远端核对。（v1.3：其中 `main` 的生成与推送移交 CG-007 完成门 7。）
  6. 终局报告（S8）：按研究发起人用语风格给出调整后的判词，每句带证据身份；对照四项义务（dev-01 #20）；列出仍开放的事。
  7. 翻查记录：每个阶段至少一条，记在 `工作台.md` §5。
- **非目标与禁止**：
  - 不声称 ZFC ⊢ ⊥；
  - 不删分支或 worktree；
  - 不强推，除非确有必要并先写明理由；
  - 不改写研究发起人原话；
  - 不把 Lean 元层的 ZFC 模型（需要宇宙）说成 ZFC 内部可证；
  - 不把 GPT 的自述当证据。

## 2. 角色、权限与写入边界

- **角色**：最后的 AI，即 integrator + 研究生成 + 审计。研究发起人 2026-10-07 全面授权：全部分支与 worktree、提交、合并、下载、推送、写共享 owner。
- **工具链**：
  - Lean v4.34.0 用固定路径调用，禁网 sandbox，不走 elan 代理。
  - Mathlib 用 Astra 缓存（只读）。
  - Foundation 源码在 `/Volumes/D/HoTT-toolchain-cache/foundation-src`；构建树在 `…/foundation-build-1fb01b72-v4.34.0`，构建器是 `tools/ffl_build.py`。
  - **不得改动** Astra 目录与 CG-005 覆盖目录（它们的哈希被运行固定）。不碰无关项目（FLT 等）。
- **分支**：
  - 主检出现在在 `dev-glm-5.3`（别的会话所切），上面有它们未提交的产物；S7-a 之前不改那些文件。
  - CG-006 往 `dev` 的提交走 `.claude/worktrees/cg006-dev`（方案 §5）。
  - 根 `CLAUDE.md` 保留（研究发起人 10-08 裁定），已补入 AGENTS.md 的导入。

## 3. 闭包：开工、恢复、压缩后都要用 Read 重读

```goal-x-closure
# 路径 | 用途
最高指示-Claude版.md | 操作指令
核心认知.md | 用户原文权威（全文）
.claude/goals/CG-005-godel-q-synthesis/原话摘录.md | ZFC Failure 判词与哥德尔路线原话
.claude/goals/CG-005-godel-q-synthesis/综合报告.md | 上一阶段结论与边界
HoTT/formal/claude-cg001/godel-q/CLAIM.md | 已证命题 C-84..C-94 与禁止外推
.claude/goals/CG-006-zfc-complete-formalization/方案.md | 后续工作方案：设计决定、阶段与验收、翻查规则、分支规则
.claude/goals/CG-006-zfc-complete-formalization/GUI查阅索引.md | GPT 探索过什么、在哪一轮、实物在哪；分叉后原话清单
.claude/goals/CG-006-zfc-complete-formalization/八线分叉后复盘.md | 八条线分叉后的目标、产出、卡点与可吸收部分
.claude/goals/CG-006-zfc-complete-formalization/工作台.md | API 笔记、决定、进度、翻查记录
.claude/goals/CG-006-zfc-complete-formalization/Targets与Profile.md | 八线倒查出的五个方向、两条路线（无哥德尔／有哥德尔）与 44 个画像要点的完成对照；未来工作的线头
形式化追踪/README.md | 形式化与机器证明各线的实时进度与可能方向（2026-10-08 起的现状权威；各章在其子文件夹）
```

## 4. 阶段

| 阶段 | 实物 | 状态 |
|---|---|---|
| S1 算术落地 | `GodelQ/FoundationArith.lean` | 过核（WIP，`3f2521a9`，未收据） |
| S3 𝗭𝗙𝗖 ⊳ 𝗥₀ | `GodelQ/ZFC/{OmegaArith,ArithInterp,R0Model}.lean` | 过核（WIP，`3f2521a9`，未收据） |
| S2 ZFC 有效 | `ZFC/Effective.lean` | 下一步 |
| S4 Σ1 可靠 | `ZFC/Soundness.lean` | — |
| S5 组装 | `ZFC/GodelQZFC.lean` + 收据 + `CLAIM.md` | — |
| S6 Z0 | `ZFC/ISigma1Interp.lean`、`ZFC/SecondZFC.lean` | 卡住则照实记录 |
| S7 接手与发布 | 方案 §3 S7 的 a–h | — |
| S8 终局报告 | 报告与调整后的判词 | — |

## 5. 工作循环

1. **恢复**：读闭包，包括 GUI 查阅索引。
2. **翻查**：按方案 §4。
3. **执行**。
4. **反思**。
5. **检查点**：`goalx.py checkpoint`，然后进入下一步。

每个文件过核就写检查点；每次翻查都记进工作台 §5。
<!-- goal-x:essentials-end -->

## 6. 版本记录

- v1.0 2026-10-07 创建（会话 d58e0c0d）。
- v1.3 2026-10-08（会话 d58e0c0d）：研究发起人要求“按照你的想法进行优先级安排，完成后续所有“形式化和机器证明”工作”。后续工作开新包 CG-007。完成门 5 中 `main` 的生成与推送移交 CG-007 完成门 7，理由是后续新结果要进同一次发布。其余完成门已满足，本包关闭。
- v1.2 2026-10-08（会话 d58e0c0d）：研究发起人要求“Targets with Profile”（从八份对话录末尾倒查各线目标、合并方向、写画像并逐点对照）；新增 `Targets与Profile.md` 进入闭包。
- v1.1 2026-10-08（会话 d58e0c0d）：研究发起人裁定保留根 `CLAUDE.md`，并要求经常翻查八份对话录。新增 `方案.md`、`GUI查阅索引.md`、`八线分叉后复盘.md` 进入闭包；阶段改为 S2→S4→S5→S6→S7(a–h)→S8；完成门增加“翻查记录”和“主检出切回 dev”；写明分支规则。
