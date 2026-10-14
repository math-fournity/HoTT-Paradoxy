# Master 装配收据：AllBlockerQ 无条件证成（2026-10-14）

## 结果

```lean
theorem allBlockerQ_uncond : ShCraigElimSetupQ.AllBlockerQ (V := V)
```
- `#print axioms` = `[propext, Classical.choice, Quot.sound]`，**无 sorryAx**
- 编译：exit=0，全链 74 文件从零编译 74/74 OK

## 装配链

```
ITSubstOpen9.iT_subst_open (∀m 含 0)          [001-Flash, 795d2faa+965c63fa]
  ──m=0 实例 + QvecVOr_zero/QvecV_zero + zero_add──▶
bridgeB : subst ?[^&0] (iT 1 q) = iT 0 (subst ?[^&0] q)
  ──allKey_of_bridge──▶ AllKey                [004-Flash, ebf88dcf]
  ──allBlockerQ_of_key──▶ AllBlockerQ         [004-Flash]
```

## 资产来源（双核验）

| 部件 | 来源树 | 提交 | Master 核验 |
|---|---|---|---|
| iT_subst_open | nice-lovelace | 795d2faa+965c63fa | exit=0, 无 sorryAx |
| allKey_of_bridge / allBlockerQ_of_key | 9276 | ebf88dcf | exit=0, 五条全核 |
| bridgeB（本探针） | 本树 | — | exit=0, 无 sorryAx |

## 装配方法

- 基线 = 9276 包全量（49 文件）
- 移植 = nice-lovelace round31 链 40 文件
- 冲突 1：`TranslateShiftCompat` 两版不同 → 用 9276 版（超集，61 vs 38 声明）
- 冲突 2：`len_qVec` 撞名（TranslateShiftCompat vs Bootstrapping）→ ITSubstOpen4 里
  5 处加 `Bootstrapping.` 前缀（纯命名歧义，语义未变）
- 复现：`python3 driver.py`（driver 自动拓扑排序 + 增量编译）

## 文件哈希

- MasterAssemblyProbe.lean: `34e2afea21706906b17133cb746c5c4a246bdf70a5c6583f50727a87713c3d01`
- ITSubstOpen4.lean（修改版）: `5d918a99d16fecbab18ec424473883b60f5d0b612f3c62f4f99d21f116626876`
- driver.py: `d39808b3dbed520e1414a5b68f85334f675e9efce2cd496c64fa7ad671fcc24e`

## 意义

`ShCraigElim ⟺ (AllBlockerQ ∧ ExsBlockerQ ∧ RootBlockerQ)`（004-Step 已证等价）
——**第一条 blocker 落地**。hAll 支收口。
剩余：ExsBridge2（hExs，001-Step 攻）+ RootKey（hRoot，= D3）。

## 复现指引（2026-10-14 更新，004-Flash 独立复现后）

**driver.py 已参数化**（`ASM` / `ASM_OUT` / `ASM_SEED` 环境变量可覆盖）：
```bash
ASM=<你的装配树路径> ASM_OUT=<输出目录> ASM_SEED=<种子 olean 目录> \
  python3 .cg009-verification/master-assembly-poc-20261014/driver.py
```

**LEAN_PATH 必须含 11 项**（少任一个都编译不过——004-Flash 前 5 次失败全在这）：
1. 输出目录（`build/`）
2. 种子 olean 目录（9276 自己的 build，52 个 olean）
3. Foundation `1fb01b72` `/Volumes/D/HoTT-toolchain-cache/foundation-build-1fb01b72-v4.34.0/lib/lean`
4-11. Mathlib 8 个包（`astra-real-geometry` 下 `.lake/packages/`）：
   `batteries` `aesop` `Qq` `proofwidgets` `importGraph` `LeanSearchClient` `plausible` `Cli`

**LEAN_SYSROOT** = `/Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0/lib/lean`（pinned，不走 elan 代理）

**拓扑序**编译（driver 自动算）；种子供 9276 侧 33 个基线文件，41 个待编译。

## ★ 004-Flash 独立复现（2026-10-14，`1a2e1214`）

`git archive origin/claude/infallible-mestorf-ce08c0 @ 701a0e3d` 提取到私有 temp 目录
（不动任何共享树），自写 driver、种子 = 9276 自己的 52 个 olean：

```
closure=74  seed=33  tocompile=41
compiled OK=41/41     ← exit 0
GodelQ.MasterAssemblyProbe.bridgeB            : [propext, Classical.choice, Quot.sound]
GodelQ.MasterAssemblyProbe.allKey_uncond      : [propext, Classical.choice, Quot.sound]
GodelQ.MasterAssemblyProbe.allBlockerQ_uncond : [propext, Classical.choice, Quot.sound]
```

**无 sorryAx——Master 的报告已被第三方独立复现确认。**

另核实：`ShCraigElimSetupQ.lean` 与 9276 生产包逐字相同（无本地魔改）；
桥的依赖链 11 文件零真 sorry（`ITShift.lean:39,41` 的 sorry **不在**该闭包内）。

**注意**：`grep -c sorry` 在这棵树上会误报（`ShCraigElimNegGen` 8 处、`Z0Layer1Emb`/`IVEOpenFull`
各有文本命中但真 sorry = 0）——**判据只有公理表**。

## 第二条独立路线（收据可换用）

`fd8b8305`（001-Flash 的 `HABElim.hAB_derivable` + 001-Step 的 `HAllUncond`）也到 `AllBlockerQ`，
依赖更少（3 文件）。Master 受控核验：70 模块从零、skipped=0、公理三条。
两条独立证明互证；生产包收据建议取依赖短的一条移植。
