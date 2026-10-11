# CG-008：ZFC 的集合论 Σ₁ 完全性 / D3 内部化——闭合 Z0 完整形式

<!-- goal-x:essentials-begin -->
> goal-x 目标包；v1.0；2026-10-11；本会话 77d1ad24-488e-4847-b592-48f1da8e9072（Claude Code，worktree `dev-ef7e5239`）。承接 CG-007（ACTIVE，其 W8 的 D3 单元移交本包）。
> 本文件是单体开工与恢复闭包。**压缩或恢复后，先按 §3 用 Read 重读闭包文件，再动手。**

## 1. 目标与完成门

- **任务**【原话，2026-10-11 用户粘贴的接手工位提示词】：“你是接手工位 AI，继续 Lean 4 形式化任务 CG-008（闭合 ZFC 内部化 Σ₁ 完全性 / Hilbert–Bernays–Löb D3，从而机器证明哥德尔第二不完备 Z0）。”
- **目标**：把 `GodelQ/ZFC/Z0Blocked.lean:65` 的 `sorry`（`zfcTr_D3_internalize`）换成真实证明，经 `zfc_z0_full_of_D3_internalize`（`Z0Full.lean:117`）→ `zfc_z0_full`（`Z0Full.lean:103`）闭合完整的哥德尔第二不完备定理 Z0：
  `𝗭𝗙𝗖 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent)`
- **完成门**（每门的证据形态写在括号里）：
  1. **Z0 闭合**：`Z0Blocked.lean` 无 `sorry`；全包编译 `rc=0`（`python3 /tmp/build_z0.py --no-pin-check --package . <file>`，**不带** `--no-forbidden-check`）。
  2. **公理洁净**：`#print axioms zfcTr_D3_internalize` 与 `zfc_z0_full_unconditional` 只报 `propext` / `Classical.choice` / `Quot.sound`。
  3. **收据**：运行日志写入 `HoTT/verification/runs/2026-10-11-cg008/`（`RUN.json`、`stdout.txt`、`stderr.txt`、`source-manifest.json`），可用 `verify_cg001_run.py --rerun` 精确重放。
  4. **治理**：`HoTT/CLAIM_EVIDENCE_MATRIX.md` 把 `MP-CG001-GODEL-Q-ZFC-Z0-CG008-001` 升级为 `MACHINE_PROVED`；更新 `CLAIM.md`、`GAP_CLOSURE_PLAN.md`；更新 `形式化追踪/01-有哥德尔路线/`（README 状态表、节文件、总览行、`99-更新日志.md`）。
  5. **诚实降格**：若某步做不完，照实写明卡在哪条引理，留下最小可续的形式状态；绝不伪造收据。
- **非目标与禁止**：
  - 不改 Foundation 源码（`/Volumes/D/HoTT-toolchain-cache/foundation-src/` 只读）；
  - 不碰 `sources/` 与 `private-audit/`；
  - 不 push `main`；
  - 不伪造收据；任何称为「收据」的文件严禁 `sorry`/`admit`/`unsafe`；
  - 不调用 Agent 工具；删除只进废纸篓；不强推；不删分支或 worktree；
  - **不要重试**三条已被编译实证否掉的廉价路线（见 §4）。

## 2. 角色、权限与写入边界

- **角色**：接手工位 AI（CG-007 的 W8 单元移交本包）。
- **写入**：证明包 `HoTT/formal/claude-cg001/godel-q-zfc-z0-full/`；运行 `HoTT/verification/runs/`；本目标包；`形式化追踪/`；CG-001 证据索引；共享矩阵；`.claude/总索引*`。
- **工具链**：Lean 4 core v4.34.0 固定路径，不走 elan 代理。构建驱动 `/tmp/build_z0.py`（若丢失，见 §5 重建说明）。
- **工作根**：本 worktree `dev-ef7e5239`。**不回写 `dev`**（研究发起人 2026-10-11 重申：在独立 worktree 中工作）。

## 3. 闭包：开工、恢复、压缩后都要用 Read 重读

```goal-x-closure
# 路径 | 用途
最高指示-Claude版.md | 操作指令
核心认知.md | 用户原文权威（涉及用户原意时读相关条目）
CG008_HANDOFF_2026-10-11.md | 本轮精确状态、三条已证伪的廉价路线、唯一合法路线（包内根目录）
CG008_HANDOFF.md | 缺口形状、死路、精确路线、可引理骨架（包内根目录）
CG008_PROJECT.md | 立项书（包内根目录）
GodelQ/ZFC/Z0Blocked.lean | 待消除的精确 sorry（第 65 行）
GodelQ/ZFC/Z0Full.lean | zfcTr、models_zfcTr_iff:67、zfc_z0_full_of_D3_internalize:117
GodelQ/ZFC/ZFCSetSigma1.lean | Phase 0 锚点，新引理的落点
GodelQ/ZFC/InternalTranslate.lean | iT_quote:611（内部翻译正确性）
GodelQ/ZFC/ZFCDelta1.lean | [𝗭𝗙𝗖.Δ₁] 已证
/Volumes/D/HoTT-toolchain-cache/foundation-src/Foundation/FirstOrder/Arithmetic/Bootstrapping/DerivabilityCondition/D3.lean | 要平移的算术机器
/Volumes/D/HoTT-toolchain-cache/foundation-src/Foundation/FirstOrder/SetTheory/Basic/Hierarchy.lean | setTheory_sigma₁_induction':63（十情形）
/Volumes/D/HoTT-toolchain-cache/foundation-src/Foundation/FirstOrder/SetTheory/Basic/Misc.lean | SetTheory.complete:269
/Volumes/D/HoTT-toolchain-cache/foundation-src/Foundation/FirstOrder/Arithmetic/Bootstrapping/Syntax/Proof/Typed.lean | tprovable_iff_provable:168（通用 [T.Δ₁]）
.claude/goals/CG-007-formalization-completion/工作台.md | CG-007 的决定、进度、教训
形式化追踪/README.md | 各线现状总览
形式化追踪/01-有哥德尔路线/README.md | 有哥德尔路线的状态表与剩余步骤
```

## 4. 已证伪的路线（不要再试，均有编译实证）

| 路线 | 结果 | 证据 |
|---|---|---|
| 载体重接到标准模型：`h : Provable 𝗭𝗙𝗖 (⌜σ⌝ : V)` → 改写成 `: ℕ` → `zfcTr_D3_standard` → 升回 `: V` | **类型错误** | `Z0Probe6.lean`、`Z0Probe7.lean`。Gödel 报价把载体类型编码进结果值 |
| `Sh.craig` / `Δ₁ Sh` 捷径：`provable_D3 (T := Sh)` | **实例合成失败** | `Theory.Δ₁ Sh` 不成立（`Sh` 是 r.e./Σ₁ 而非 Δ₁） |
| 直接 `internalize_provability` 喂结论 | **两句话不同** | `Z0D3Attempt.lean`：只重写同一句，合成不出包裹 `iTDef` + `provable 𝗭𝗙𝗖` 的结论句 |
| 廉价传递 `Con(Sh.craig) ↔ Con(𝗭𝗙𝗖)` | 坍缩为同一 D3 缺口 | `Z0Final.lean`：`complete 𝗜𝚺₁` 静默回填 `sorryAx` |

## 5. 构建与验证

```bash
# Bash cwd 不跨命令持久 —— 必须在同一条命令内 cd 到包根
cd /Users/aurolafly/WorkBuddy/Worktrees/HoTT_AI_HANDOFF_20260911/dev-ef7e5239/HoTT/formal/claude-cg001/godel-q-zfc-z0-full && python3 /tmp/build_z0.py --no-pin-check --package . GodelQ/ZFC/<file>.lean
```

- 中间探针文件加 `--no-forbidden-check`，且**不得称为收据**。
- 收据文件不加该标志（FORBIDDEN 检查会拒绝 `sorry`/`admit`/`native_decide`/`unsafe`/`implemented_by`/`extern`/`opaque`）。
- `Z0_BUILD_DIR` 默认 `/tmp/z0_build_lib`（oleans 缓存；换文件时复用可加速）。

## 6. 最小可续状态

见 `工作台.md` §3。

<!-- goal-x:essentials-end -->
