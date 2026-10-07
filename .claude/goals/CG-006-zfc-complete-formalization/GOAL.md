# CG-006：最后的AI——把哥德尔式 Q 推进到 bare ZFC 的完全形式化，并接手全部分支

<!-- goal-x:essentials-begin -->
> goal-x 目标包；HUMAN_EDITED；v1.0；2026-10-07；本机会话 d58e0c0d（Opus 5.5）。本文件是单体开工与恢复闭包。

## 1. 目标与完成门

- **授权**【原话】（2026-10-07）：“这个repo全部的分支和git worktree，现在由你全面接手了，你就是‘最后的AI’，所以你认为应该做的，都可以做，我全面授权你。”“你要综合所有之前的AI的所有工作，推进到完全的形式化和机器证明的完成。”判词全文见 CG-005 `原话摘录.md` 0109 第 56 轮与 main README 顶部。
- **父目标**：CG-005 的哥德尔式 Q 定理（`HoTT/formal/claude-cg001/godel-q/`，C-84..C-94）对“满足标准元性质的有效理论”成立；本目标把它落到 **Foundation 中真实的 𝗭𝗙𝗖**（ℒₛₑₜ 语法、LK 证明系统），使“bare ZFC 在时间维度上的观察力不完备”成为不带未证元定理前提的 Lean 定理；再接手全部分支、写回共享 owner、发布。
- **技术路线**（决定，见工作台）：Foundation `FormalizedFormalLogic/Foundation@1fb01b72`（锁定 Mathlib `5ed29652` = 本项目 Astra Mathlib，Lean v4.34.0）。
  1. 算术落地：`EffectiveTheory` 实例化到 Foundation 的 `ArithmeticTheory T`（[𝗥₀ ⪯ T] [Σ1 可靠] [T.Δ₁]），用 `codeOfREPred`、`rePred_weak_representation`、`provable_iff_provable`、`rePred_iff_sigma1`。
  2. ZFC 有效公理化：`ℒₛₑₜ.LORDefinable`、`ℒₛₑₜ.Primcodable`、`𝗭𝗙𝗖.RE`；Craig（`T.craig`，对任意语言）给 Δ1 与可证性 RE。
  3. `𝗭𝗙𝗖 ⊳ 𝗥₀`（`LK/Interpretation.lean` 的 `DirectInterpretation`；义务经 `complete_on_eq_models` 化成模型语义；加乘由 `SetTheory/NaturalNumberRec` 的 Blueprint 递归定义；𝗥₀ 只需元层归纳）。
  4. Σ1 可靠：`Universe` 模型（`zfc_consistent`）中 ω = `range ofNat`，解释出的结构同构于 ℕ。
  5. 组装：ZFC 的 `EffectiveTheory`；哥德尔 I 过程形式、魔鬼交易、跑者、独立性对 bare ZFC；与 Foundation `incomplete_of_RE` 交叉核对。
  6. Z0：`𝗭𝗙𝗖 ⊳ 𝗜𝚺₁`（模型内归纳）→ `craig_consistent_unprovable_of_RE` → ZFC 证明不了自身算术影子的一致性。
  7. 接手：分支合并（先重新编号撞号命题）、STATE/MEMORY/矩阵/方向/全景经 canonical checkpoint 写回、`main` 生成与推送。
- **完成门**：
  1. 第 1–5 步的 Lean 文件全部过核（exit 0、只用 propext/choice/Quot.sound、无 sorry），运行收据与逐字节重放；`CLAIM.md` 写明精确命题。
  2. 第 6 步过核，或照实写明卡在哪一条引理并留下最小可续的形式状态（不得冒充完成）。
  3. 审计并处理全部分支：撞号重新编号方案落地；有价值的成果并入 `dev`（或说明为何不并）；不删任何分支与 worktree。
  4. 共享 owner 经 canonical checkpoint 写回（作为接手的 integrator）；总索引维护；分片校验 PASS。
  5. `main` 由 `scripts/release/build_main_release.py` 从 `dev` 生成；推送 `dev` 与 `main`；回读远端核对。
  6. 最终报告：按研究发起人用语风格给出调整后的判词（每句带证据身份），以及仍开放的事。
- **非目标与禁止**：不声称 ZFC ⊢ ⊥；不删分支或 worktree；不强推（除非确有必要并先写明理由）；不改写研究发起人原话；不把 Lean 元层的 ZFC 模型（需要宇宙）说成 ZFC 内部可证。

## 2. 角色、权限与写入边界

- 角色：最后的 AI = integrator + 研究生成 + 审计。授权：全部分支与 worktree、提交、合并、下载、推送、写共享 owner（研究发起人 2026-10-07 全面授权）。
- 工具链：Lean v4.34.0 固定路径；Mathlib = Astra 缓存（只读）；Foundation 源码 `/Volumes/D/HoTT-toolchain-cache/foundation-src`（`1fb01b72`）；构建树 `/Volumes/D/HoTT-toolchain-cache/foundation-build-1fb01b72-v4.34.0`（`tools/ffl_build.py`：符号链接镜像 + 禁网并行编译）。**不得改动** Astra 目录与 CG-005 覆盖目录（CG-005 运行固定了它们的哈希）。不碰无关项目（FLT 等）。

## 3. 闭包：开工、恢复、压缩后都要用 Read 重读

```goal-x-closure
# 路径 | 用途
最高指示-Claude版.md | 操作指令
核心认知.md | 用户原文权威（全文）
.claude/goals/CG-005-godel-q-synthesis/原话摘录.md | ZFC Failure 判词与哥德尔路线原话
.claude/goals/CG-005-godel-q-synthesis/综合报告.md | 上一阶段结论与边界
HoTT/formal/claude-cg001/godel-q/CLAIM.md | 已证命题 C-84..C-94 与禁止外推
.claude/goals/CG-006-zfc-complete-formalization/工作台.md | 本阶段 API 笔记、决定、进度
```

## 4. 阶段

| 阶段 | 实物 | 条件 |
|---|---|---|
| S1 算术落地 | `GodelQ/FoundationArith.lean` 过核 | API 理解有误则回读 Foundation 源码 |
| S2 ZFC 有效 | `ZFC/Effective.lean` 过核 | — |
| S3 𝗭𝗙𝗖 ⊳ 𝗥₀ | `ZFC/ArithInterp.lean` 过核 | — |
| S4 Σ1 可靠 | `ZFC/Soundness.lean` 过核 | — |
| S5 组装 | `ZFC/GodelQZFC.lean` 过核 + 收据 | — |
| S6 Z0 | `ZFC/ISigma1Interp.lean`、`ZFC/SecondZFC.lean` | 卡住则照实记录 |
| S7 接手与发布 | 合并、checkpoint、main、推送 | — |

## 5. 工作循环

恢复 → 定位 → 执行 → 反思 → `goalx.py checkpoint` → 下一步。每个文件过核即写检查点。
<!-- goal-x:essentials-end -->

## 6. 版本记录

- v1.0 2026-10-07 创建（会话 d58e0c0d）。
