/-! ## ★★ `AllBlockerQ` **无条件证成**——9276 线独立核验（2026-10-14）

Master（001-Master）报「`AllBlockerQ` 已在私有装配树无条件证成」。
本文件记**我自己的独立复现**——不是转述。

### 复现方法

* 资产：`origin/claude/infallible-mestorf-ce08c0` @ `701a0e3d`
  （`elegant-mclaren/.cg009-verification/master-assembly-poc-20261014/`，97 文件）
* `git archive` 提取到 `/private/tmp/cg007-master-verify-*/`（**不动任何共享树**）
* **自写 driver**（不用 Master 的 `driver.py`——它硬编码其私有路径）：
  `cwd = ASM` + `LEAN_PATH` 模式（照 `devbuild_ns.py:36` 的形状），拓扑序编译
* 种子 = **9276 自己的 52 个 olean**（`.claude/goals/.../devbuild_ns/godel-q-zfc-z0-full/`）
* `LEAN_PATH` 需含：build / Foundation / Mathlib / 8 个 Mathlib 包
  （`Batteries`、`ImportGraph`、`Qq`、`aesop`、`plausible`、`proofwidgets`、
  `Cli`、`LeanSearchClient`——**少任一个都编译不过**）

### 结果（本机实跑）

```
closure=74  seed=33  tocompile=41
compiled OK=41/41   ← exit 0
```

`#print axioms` 三条：

```
GodelQ.MasterAssemblyProbe.bridgeB           : [propext, Classical.choice, Quot.sound]
GodelQ.MasterAssemblyProbe.allKey_uncond     : [propext, Classical.choice, Quot.sound]
GodelQ.MasterAssemblyProbe.allBlockerQ_uncond : [propext, Classical.choice, Quot.sound]
```

**无 `sorryAx`。**

### 装配链（谁证了什么）

```
ITSubstOpen9.iT_subst_open (∀m 含 0)        [001-Flash，795d2faa+965c63fa]
  ── m=0 + QvecVOr_zero/QvecV_zero + zero_add ──▶
bridgeB : subst ?[^&0] (iT 1 q) = iT 0 (subst ?[^&0] q)   [Master 探针]
  ── allKey_of_bridge ──▶ AllKey              [本线 ebf88dcf]
  ── allBlockerQ_of_key ──▶ AllBlockerQ       [本线 e51f6806]
```

**⟹ `hAll` 支收口：`ShCraigElim ⟺ (AllBlockerQ ∧ ExsBlockerQ ∧ RootBlockerQ)`，现已 AllBlockerQ ✅。**

### 独立核实的两件事

1. **`ShCraigElimSetupQ.lean` 逐字相同**（`diff` 对 `HEAD:HoTT/…/ShCraigElimSetupQ.lean`
   与装配树同名文件）——装配用的是**我推的版本**，没有本地魔改。
2. **桥的依赖链 11 个文件零真 sorry**（`ITSubstOpen{,2..9}`、`QvecV`、`HAllProof`）。
   树里别处（如 `ITShift.lean:39,41`）确有 2 处真 sorry，但**不在**该闭包内——
   **决定性判据是公理表无 `sorryAx`**（若在闭包内，`sorryAx` 必出现）。

### 边界照实写明

* 这是**装配**收据：`AllBlockerQ` 在「9276 包 + 40 移植文件」的**合并树**里成立；
  9276 **单独**仍只有条件版（`allKey_of_bridge` 以 `hB` 为参数）。
* 若要让 9276 生产包**自包含**，须把 `iT_subst_open` 链（11 文件 + `QvecV`/`SubstDomZero`）
  移植进 9276——那才是**无条件**收据落在生产包内。
* 移植已知冲突：`len_qVec` 与 Foundation `Term/Functions.lean:576` 撞名
  （加 `Bootstrapping.` 前缀，`ITSubstOpen4` 里 5 处；纯命名歧义）。

**三条 blocker 现况**：`AllBlockerQ` ✅（装配树，已独立复现）／
`ExsBlockerQ` ⬜（剩 `ExsBridge2`，一般 `p`）／`RootBlockerQ` ⬜（= D3）。 -/
