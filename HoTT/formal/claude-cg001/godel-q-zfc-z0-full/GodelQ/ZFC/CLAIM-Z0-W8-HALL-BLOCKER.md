# CG001-C-401：Z0 D3 的 `hAll`/`hExs` 支——归约定型与**阻塞引理**的精确陈述

> **证明包**：`MP-CG001-Z0-W8-HALL-BLOCKER-001`。
> **目标包**：CG-007，单元 W8 第 2 层（依据 `.claude/goals/CG-007-formalization-completion/GOAL.md` 完成门 2：
> 「W8 内部化，**或者照实写明阻塞引理**」）。
> **理论变体**：Lean 4.34.0 + Foundation（`1fb01b72`），经典逻辑，
> 内核公理只有 `propext`、`Classical.choice`、`Quot.sound`。

## 0. 位置与身份

**身份**：**机器证明（有范围）+ 照实写明的阻塞**。按 GOAL.md 完成门 2 的允许，
本文件给出 `hAll`/`hExs` 两支的**精确剩余**，并把阻塞定位到**一条具体的、形状已收紧的引理**。

**不声称**：`ShCraigElim` 已完成。**本线未证完 `hAll`/`hExs`**。

## 1. 已机器验证的部分（全部 exit 0，公理只有三条）

### 1.1 `hAll` 的归约定型——**缺的不是等式，是弱化**

`ShCraigElimSetupQ.lean` 新增四条（全部 exit 0）：

| 引理 | 内容 |
|---|---|
| `imp_wk` | `Derivable (insert X S) → Derivable (insert (D 🡒 X) S)` |
| `all_m_premise` | `free_imp_domZero` + `imp_wk`：`all_m` 前提从 `free Y` 归约到 `free (imp domZero Y)` |
| `hAll_mem` | `^∀ (imp domZero (iT 1 p)) ∈ translateSeq s` |
| `hAll_reduce` | 上面两条拼装完毕，`all_m` 的两条前提**全部就位** |

**关键更正**：此前三轮把 `hAll` 卡点记成「需要
`iT 0 (free ℒₒᵣ p) = free ℒₛₑₜ (imp domZero (iT 1 p))` 这条等式」。
**那条等式确实为假，但 `hAll` 从来不需要它**——
`free_imp_domZero` 已把 `domZero` 层完全剥离到一次 ∨ 弱化里。

### 1.2 本轮新入生产包的基建

`TranslateShiftCompat.lean`（全部 exit 0）：
`termSubstVec_congr'`、`termSubst_congr'`、`subst_congr_prefix'`（**语言多态**）、
`substs_qqAlls`、`qVec_two`、`substs_qqAlls_two`、`iVE_resultVec_two`、
`subst_qVec_domZero'`。

### 1.3 三条结构性事实（各有 exit 0 的探针）

| 事实 | 探针 |
|---|---|
| `qVec` 迭代让尾部分量**整体 +1**（保护语义） | `W8-qVec-iterate-two-CORRECT-20261012` |
| `subst` 按**公式层数**给向量、`termSubstVec` 按**关系元数**走 ⟹ 越界补零 | `W8-subst-arity-zerofill-PROVED-20261013` |
| `iT n p` 在 `p` **符号**时**陈述层**就 `whnf` 超时 ⟹ 陈述须写成 `∀ p, … → …` | `W8-rel-correct-statement-shape-20261013` |

**另**：此前记录的三条「机器证伪」**已撤回**——对应探针**无法编译**，
从未经过真实 kernel 运行。按 F-011 标准不算证据。
（舰队侧 CG-009 独立佐证：其保留的负面结果只有 `naive_law_is_false_shape`
一条同索引朴素律，与 `iT_free` 不是同一条，且过核 exit 0。）

## 2. 精确剩余（**阻塞引理**）

`hAll` 只剩一条：

```
iT_free : ∀ p, IsSemiformula ℒₒᵣ 1 p → iT 0 (free ℒₒᵣ p) = free ℒₛₑₜ (iT 1 p)
```

其证法四步（零件已齐三件）：

```
iT 0 (free p) = iT 0 (subst ?[^&0] (shift p))     -- free 的定义
              = subst ?[^&0] (iT 1 (shift p))     -- ← 缺的就是这一步（iT_substs1）
              = subst ?[^&0] (shift (iT 1 p))     -- iT_shift（已证）
              = free (iT 1 p)                     -- free 的定义
```

**`iT_substs1` 的精确陈述**（长度 1 的向量、层 1 的公式）：

```
iT_substs1 : ∀ σ, IsSemiformula ℒₒᵣ 1 σ →
    iT 0 (subst ℒₒᵣ ?[^&0] σ) = subst ℒₛₑₜ ?[^&0] (iT 1 σ)
```

## 2.5 ⚠ 2026-10-13 更正：阻塞引理的**正确形状**（本会话最终定位）

本文件 §2 最初写的 `iT_substs1` 形状（右端向量用 `w`）**不完整**。
`ShCraigElimBranches.lean` §11 已给出正确形状——**右端向量是 `qVec (iVE-像 w)`**：

```
iT_substs1 : ∀ m p w, IsSemiformula ℒₒᵣ (m+1) p → IsSemitermVec ℒₒᵣ (len w) (m+1) w →
    iT m (subst ℒₒᵣ w p) = subst ℒₛₑₜ (qVec ℒₛₑₜ (iVE-像 w)) (iT (m+1) p)
```

**为什么**：`iVE` 把 `ℒₒᵣ` 的项送到 `ℒₛₑₜ` 的**公式**（`eqAtom`），
而 `subst ℒₛₑₜ` 要的是**项**——两者层次不同，`iVE-像 w` 是必需的中间物。

**本会话已验证的部分**（探针 exit 0）：
* `iT_substs1_gen` 的 4 支（`verum`/`falsum`/`and`/`or`）——
  它们的证法**不依赖右端向量**，故在修正后的形状下**同样成立**；
* 闸门问题（`all` 支是否为真）——**为真**，但 §12.41 的推演需按新向量重走；
* `subst_qVec_domZero'`、`len_qVec`、`subst_qVec_shrink`、`substs_qqAlls` 族
  （均入生产包，exit 0）——**与形状修正无关，仍然有效**。

## 3. 为什么它难——三条**机器确认的**结构性障碍

### 3.1 向量长度的三种含义混淆

`subst` 的向量长度由**公式层数**定；`termSubstVec` 按**关系元数**走；
`iT` 的 `all` 支又把层数**推一格**。三者不同步 ⟹ 越界补零。
（`W8-subst-arity-zerofill-PROVED-20261013`：`subst ?[^&0] (^rel 2 cEqN ?[^#1,^#0]) = ^rel 2 cEqN ?[0, ^&0]`。）

### 3.2 归纳谓词的偏移

`semiformula_result_induction` 的 `q` 被固定成 `result … param p`，
而目标要 `iT (param+1) p`——谓词右端只能提到一个位置。
候选 1（把 `subst` 侧也推一格，令两边 `param` 相同）的谓词
`P param n p q := param = n → 0 < param → iT param (subst ?[^#0,^&0] p) = subst ?[^&0] q`
**已被 Lean 接受**，`verum`/`falsum` 两支已证。

### 3.3 `iT` 与 `subst` 在 `∀` 上**错开一格**（§12.22，**本轮最后发现**）

`σ = ^∀ X`（层 1）时两侧展开：

| | 值 |
|---|---|
| 左 `iT 0 (subst ?[^&0] σ)` | `^∀ (imp domZero (iT 1 (subst (qVec ?[^&0]) X)))` |
| 右 `subst ?[^&0] (iT 1 σ)` | `^∀ (neg (subst (qVec ?[^&0]) domZero) ⋎ subst (qVec ?[^&0]) (iT 2 X))` |

**第一分量**：左 `domZero` vs 右 `subst (qVec ?[^&0]) domZero`——
**后者已证等于 `domZero`**（`subst_qVec_domZero'`，exit 0），**故这一分量对上了**。

**第二分量**：左 `iT 1 (subst (qVec ?[^&0]) X)` vs 右 `subst (qVec ?[^&0]) (iT 2 X)`。
**层数 1 vs 2**——这正是 `iT_substs1` 自身的形状，但**向量是 `qVec ?[^&0]`（长度 2）、层数错开一格**。

**所以 `iT_substs1` 的 `all` 支需要一条更强的、带 `qVec` 的版本**：

```
iT_substs1_qVec : ∀ m σ, IsSemiformula ℒₒᵣ (m+1) σ →
    iT m (subst (qVec w) σ) = subst (qVec w) (iT (m+1) σ)      （len w = m+1）
```

**⚠ 本条尚未机器验证为真或为假。** 按本仓纪律（`probe-simp-residual-is-not-a-goal`），
它现在的身份是「**候选，未验证**」——**不是**「已定位的下一步」。
下一位应先做**反驳实验**（取 `σ = ^rel` 等最小例，比对两侧的补零方式），再决定。

## 4. 未完成的部分（照实写）

* `hAll` 支：`ShCraigElimSetupQ.lean` 的 `induction_setup_Q` 里仍是 `sorry`；
* `hExs` 支：同形，未开工；
* `hRoot` 支：归约到 `p ∈ Sh.craig.Δ₁Class → Provable 𝗭𝗙𝗖 (iT 0 p)`，
  难点在 Foundation 的 `codeOfREPred` 一般 V 表示引理（现只有 ℕ 层）；
* `conjunct_rename_second_gen` 的 `func` 支：`ve2` 展开已通（探针 exit 0），
  但两侧最终比对未完成。

## 5. 收据位置

* 生产包：`GodelQ/ZFC/TranslateShiftCompat.lean`、`GodelQ/ZFC/ShCraigElimSetupQ.lean`（均 exit 0）；
* 探针：`.claude/goals/CG-007-formalization-completion/probes/`（204+ 份，
  本文件引用的均有 exit 0 记录）；
* 交接：`形式化追踪/11-Claude交接-第二次接手-20261011.md` §11–§12；
* 构建：`python3 -B .claude/goals/CG-007-formalization-completion/tools/devbuild_ns.py <pkg> <module>`。
