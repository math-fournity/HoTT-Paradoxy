# 形式化与机器证明 · Codex 接管交接（2026-10-11）

> 研究发起人要求把 Claude 中断的“形式化与机器证明”工作完整接手，并把交接说明落进任务
> 治理系统。本文件是给**下一个 Session 的自己**（以及研究发起人）的完整交接；正文之后附
> 一段可直接贴进新 Session 的代码块。

## 1. 当前 git 位置（最重要）

- **主检出（canonical 工作根）**：`/Volumes/D/HoTT_AI_HANDOFF_20260911`
- **分支**：`dev`
- **HEAD**：`f9a734a6`（`docs(CG-007 W8): pin down the layer-bookkeeping obstacle for the nrel branch`）
- **每次动手前先 `git log --oneline -1`**：研究发起人会不定时提交增量，HEAD 会变。
- 本机 Codex 当前所在的 worktree 是 `codex/9276-w9b-residue-snapshot-20261011`
  （`/Users/aurolafly/.codex/worktrees/9276/...`），它是冻结残留用的快照分支，**不要**
  在上面做正式工作；正式改动都落到 `dev` 主检出。

## 2. 八个 git worktree 方向的覆盖状态（已全部闭合）

`形式化追踪/README.md` 总览与 `05-分支上的形式包/README.md` 已逐条登记“八个 worktree 方向”
（dev-01…dev-09，无 dev-05/08 不在形式化方向内）的形式化覆盖：

- dev-01（`f10899cb`）：稠密性/运动机器控制，已并入 `dev`（D01-C-369–371），13 个 Lean 运行重放 ✅
- dev-02（`4005fa80`）：实际 Q 政策演算，留在分支（D02-C-359–365），`dev` 已有收据 ✅
- dev-03（`854a6aba`）、dev-04（`f97bbcb4`）：观察边界，留在分支，已有 `dev` 收据 ✅
- dev-06（`af0d9c5c`）、dev-07（`a753f9bc`）：无新形式包，判不适用 ✅
- dev-09（`ac6391b6`）：Cubical Agda 哥德尔片段 + Foundation 第一不完备接口，已并入
  `dev`（D09-C-370–386）或本机 Foundation 构建树重放（D09-C-369，CG001-C-387）✅
- 结论：**八方向覆盖已闭合**；唯一剩下的主线缺口是 Z0 完整形式的 D3（见 §3）。

## 3. 真正剩下的唯一缺口：Z0 的 D3（= `ShCraigElim`）

唯一阻塞引理（带 `sorry`，不进收据源）：

```lean
-- HoTT/formal/claude-cg001/godel-q-zfc-z0-full/GodelQ/ZFC/Z0Blocked.lean:29
theorem zfcTr_D3_internalize {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    (τ : ArithmeticSentence)
    (h : Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V)) :
    Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr τ)⌝ : V) := by sorry
```

归约链（已证部分）：`ShCraigElim`（C-390/391/392/393/394/396/397 等逐文件收据）
经 `bwd_of_shcraig_elim`（`Z0UniBridge.lean`，C-390）归约到 `bwd`，再归约到 `keyE`，
最后到上面的 D3。`ShCraigElim` 的剩余零件（按 CLAIM.md / 第三位 AI 的续更）：

- `emb`/`emb_id` 的 `all`/`exs` 两例（第 2 层前置，第 1 层 `emb_commute` 就位后）；
- 第 1 层剩余 `subst`/`shift`/`free`/`setShift`（10 个 derive case 的 wkRule/shiftRule/cutRule 需要）；
- 第 1.5 层 `codeOfREPred` 的 V 层一般表示引理（`codeOfREPred_spec` 只在 ℕ 层）；
- 第 2 层 `derivTranslate`（V 内部，把 `Sh.craig` 推导编码送到 ZFC 推导编码；`axm` 是唯一用到
  ZFC 的地方，其余逻辑规则靠第 1 层 + `arithTrln` 的两条义务）；
- 组装：`keyE` ← → `Z0Full.zfc_z0_full_of_D3_internalize` → 完整形式 → 正式收据。

**已证不等于“拿到了收据”**：多个文件当前在 dev 工作树里是未提交的（见 §5），其中部分带
`sorry`/未证标记，不能进收据源。下一个 Session 要做的是把这些零件的**剩余支**证完、去掉
`sorry`、按 F-011 抓到精确重放一致的收据。

## 4. 给下一个 AI 的补全包（已建好，无需它再找缺模块）

第三位 AI 在沙箱里既无 Lean/Mathlib/Foundation、zip 又只含 4 个模块，只能手推、交不出编译过的
骨架。为此已新建并校验：

**`外部资料/Z0-D3-攻关包-完整版/`**

- `Foundation/`：Foundation 全量源码 **308 个** .lean（commit `1fb01b72`，与 `MATHLIB_CLOSURE.json`
  一致），逐字复制自 `/Volumes/D/HoTT-toolchain-cache/foundation-src`。
- `Project/`：目标证明包 `godel-q-zfc-z0-full` 全量（45 个 .lean + `LEAN_TOOLCHAIN.json` /
  `MATHLIB_CLOSURE.json`），与仓库逐字一致。
- `Plans/`：`zfcTr-D3-plan.md`、`zfcTr-D3-plan-revision.md`、`zfcTr-D3-plan-review-3.md` 三份原文。
- `FOUNDATION_MODULES.md` + `foundation_modules_urls.txt`：308 个模块名、相对路径、
  **GitHub 原始地址**（`https://raw.githubusercontent.com/FormalizedFormalLogic/Foundation/1fb01b72de.../<路径>`，
  已对 `D3.lean` 验证返回 200 / 8708 bytes），联网机器可逐条 `curl -O` 复现。
- `README.md`：缺口定位、复现环境、下一件事的精确说明。

GitHub 仓库：`https://github.com/FormalizedFormalLogic/Foundation`，固定 commit
`1fb01b72de546e1b50821fd05b1314a8d958583f`。

## 5. 复现环境与工具（完整可用）

- Lean 4.34.0：`/Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0`
  （其他机器用 `leanprover/lean4:v4.34.0`）。
- Foundation 源码：`/Volumes/D/HoTT-toolchain-cache/foundation-src`（commit `1fb01b72`，308 个 .lean）。
- Foundation olean 构建：`/Volumes/D/HoTT-toolchain-cache/foundation-build-1fb01b72-v4.34.0/lib/lean`。
- 增量编译脚本：`/tmp/d3build/devbuild.py`（拓扑序传模块列表；注意失败 run 目录要先删再重跑同名）。
- 收据工具（仓库内）：`.claude/goals/CG-007-formalization-completion/tools/capture_run.py`、
  `verify_cg001_run.py`、`.claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py`。
- 正确模块顺序见 `BUILD.md` 与 `README.md`（ProcessObservation → … → Z0Full → 目标文件）。

## 6. 陷阱（几个 Session 踩过的，勿重复）

1. `capture_run.py --source` 顺序必须是 import 拓扑序，否则 `object file ... does not exist`；
   失败的 run 目录要先删才能重跑同名 run-id。
2. `zfc_lean_check.py` 对源文件做纯文本扫描，注释里出现 `sorry` 等禁用词被判
   `FORBIDDEN_SOURCE_MARKER`；含未证标记的文件不能进收据源。
3. 先写索引行再校验（`GOAL_INDEX_ROW_COUNT`），索引行必须是裸 claim id。
4. `git commit --only <路径>` 取的是工作区版本，不是暂存区；用 `git add -- <路径>` + `git commit`。
5. 改共享物理文档前先 `git -C /Volumes/D/... diff dev -- <file>`，否则顶掉别人的节。
6. Lean 源码里嵌中文注释会让 zsh heredoc 转义坏掉——用 Python 脚本写 `.lean`。
7. `definability` 战术在复合谓词上卡住；可行模式：手写显式 `Semisentence` +
   `via <它> := .mk fun v => by simp [...]`（照 `Z0Full.lean:40` 的 `trProv`）。
8. `ℒₛₑₜ` 侧需要 `IsUFormula` 而非 `IsSemiformula`；显式传假设可避免 `isDefEq` 超时
   （需 `set_option maxHeartbeats 1600000`）。
9. `IsUTermVec.isSemitermVec` 给的层数是 `listMax (termBVVec L k v)`，不是任意层数——
   用 `IsSemiterm.def` 自己提升（W8 已证 `isSemiterm_of_isUTerm` / `iTR_isUFormula`）。
10. `Negation.construction` 的支定义要 `unfold Negation.construction; rfl`（直接 `rfl` 不行）。
11. `IsUFormula.neg_neg` 早已存在（`Foundation/.../Syntax/Formula/Functions.lean:127`），
    `NegInvolution` 那条重建路不再是必要路线。

## 7. 授权边界（未变）

- 已给多段授权（2026-10-07/08/09/10 + “继续推进”）。
- **没有**授权：`main` 推送与发布、tag、Sub Agent、碰他人未提交文件、改 `sources/` 与
  `private-audit/`、在 `dev` 之外正式提交。
- W9 的 `main` 发布需研究发起人授权，别自己推。

## 8. 给下一个 Session 的自己（可直接贴入新 Session）

见本文件末尾的代码块 `NEXT_SESSION_HANDOFF`。

```text
NEXT_SESSION_HANDOFF
（内容见第 9 节，单独成块）
```

## 9. NEXT_SESSION_HANDOFF 代码块

```text
【身份】你是接手“形式化与机器证明”主线收尾的 Codex Session。前序是 Claude Opus 的 CG-007 W8
单元与第三位 AI 的 ShCraigElim 续做；本机 Codex 已把完整交接落进
形式化追踪/08-Codex接管-交接与下一步.md 与 外部资料/Z0-D3-攻关包-完整版/。

【位置】主检出 /Volumes/D/HoTT_AI_HANDOFF_20260911，分支 dev，HEAD 见 git log --oneline -1
（动手前必看，研究发起人会不定时提交）。不要在本机 codex worktree 快照分支上做正式改动。

【唯一缺口】Z0 完整形式的 D3，即 ShCraigElim：
  ∀ σ, Provable Sh.craig ⌜σ⌝ (V) → Provable 𝗭𝗙𝗖 ⌜translate σ⌝ (V)
归约链已证：ShCraigElim → bwd（Z0UniBridge C-390）→ keyE → zfcTr_D3_internalize
（GodelQ/ZFC/Z0Blocked.lean:29，带 sorry）。它一旦无 sorry 成立，
Z0Full.zfc_z0_full_of_D3_internalize 立即给出 𝗭𝗙𝗖 ⊬ (𝗭𝗙𝗖.consistent)ᵗ，主线即完成。

【完备基础已备】外部资料/Z0-D3-攻关包-完整版/ 含 Foundation 全量 308 个 .lean（commit 1fb01b72）
与目标包 godel-q-zfc-z0-full 全量（45 个 .lean）。GitHub:
https://github.com/FormalizedFormalLogic/Foundation @ 1fb01b72de546e1b50821fd05b1314a8d958583f
单文件地址模板：
https://raw.githubusercontent.com/FormalizedFormalLogic/Foundation/1fb01b72de546e1b50821fd05b1314a8d958583f/<相对路径>
逐条清单见该目录 FOUNDATION_MODULES.md / foundation_modules_urls.txt。

【下一步顺序】
1. 先付 emb_id 的 all/exs 两例（第 2 层前置）。卡点：Semiformula.rew Rew.emb (∀¹ φ) 不归约成
   Rewriting.app 形式；试 Rew.q_emb + Rewriting.app_all，或 DFunLike/Hom 的 congrArg 展开。
2. 第 1 层剩余 subst/shift/free/setShift（wkRule/shiftRule/cutRule 需要）。
3. 第 1.5 层 codeOfREPred 的 V 层一般表示引理（codeOfREPred_spec 只在 ℕ 层）；配负控制。
4. 第 2 层 derivTranslate（V 内部；axm 是唯一用到 ZFC 的地方，其余靠第 1 层 + arithTrln 两条义务）。
5. 组装 keyE ← → Z0Full.zfc_z0_full_of_D3_internalize → 完整形式 → 正式收据。

【环境】Lean 4.34.0 @ /Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0；
Foundation 源 /Volumes/D/HoTT-toolchain-cache/foundation-src；olean 构建
/Volumes/D/HoTT-toolchain-cache/foundation-build-1fb01b72-v4.34.0/lib/lean；
增量 /tmp/d3build/devbuild.py；收据 .claude/goals/CG-007-formalization-completion/tools/capture_run.py
与 .claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py。

【陷阱】capture_run --source 必须拓扑序；含 sorry 的文件被 zfc_lean_check 拒收；先写索引行再校验；
中文注释用 Python 写 .lean；IsSemiterm 用 IsSemiterm.def 提升到任意层数；IsUFormula.neg_neg 已存在。

【授权】已授权推进与精确路径提交；未授权 main 推送/发布/tag/Sub Agent/碰他人未提交文件/改 sources。

【八方向覆盖】均已闭合（形式化追踪/05-分支上的形式包/README.md），无需再处理；只攻 Z0 的 D3。
```
