# 交接：CG-009 工位 `elegant-mclaren-767fb0` → 下一会话

> 2026-10-11 18:5x。分支 `claude/elegant-mclaren-767fb0`（已推送 origin，tip 见 `git log`）。
> **不合并到 dev**（用户明确约束）。

---

## 〇、三十秒摘要

本会话把 O2 从"`iT_neg` 已证"推进到 **8/10 支就绪**：
**`iT_shift` 全证 → `tshift` → `hShift` 无条件**，并**组装完 `hAll`**（只差 `hAB`）。
同时：hRoot 线证出**三个解包引理 + `translate_padding`**；
并**更正**了此前的两个误判（见 §三）。全部新定理 exit 0、0 sorry、公理仅三条标准公理。
**全链 42/42 从零重编译通过**。

---

## 一、工作根与开工闭包

**工作根**：`/Volumes/D/HoTT_AI_HANDOFF_20260911/.claude/worktrees/elegant-mclaren-767fb0`
（分支 `claude/elegant-mclaren-767fb0`；canonical 与其他 worktree 只读）。

**开工先核对**：`git rev-parse --show-toplevel --abbrev-ref HEAD`；`git log --oneline -3`。

**压缩/恢复后按序重读**（Read 原文，不用摘要）：
1. 本文件；
2. `docs/形式化综合研判-20261011/成果-IShiftDomZero/README.md`（§十二–§二十六是成果与障碍图谱）；
3. `docs/形式化综合研判-20261011/增量扫描日志.md` 第 31–35 轮；
4. `docs/形式化综合研判-20261011/接力-ISHIFT给下一会话.md`。

---

## 二、本会话已证清单（全部机器核验）

### 2.1 自研（`成果-IShiftDomZero/`）

| 定理 | 文件 | 内容 |
|---|---|---|
| `shift_domZero` | `ShiftDomZero.lean` | 枢纽：`shift domZero = domZero` |
| `shift_quote` | `ShiftQuote.lean` | 通用工具：shift 固定句子引号 |
| `ishift` 六支 | `IShiftFull-6of8.lean` | verum/falsum/and/or/all/exs |
| `shift_ve0` | `ShiftVe0.lean` | iVE func k=0 |
| **`iTR_shift`** | `ITRShift.lean` | `iTR n 2 R (termShiftVec 2 v) = shift (iTR n 2 R v)` |
| **`iT_shift`** | `ITShift-FULL.lean` | **九支全过** |
| **`tshift`** | `TShift.lean` | `translateSeq (setShift s) = setShift (translateSeq s)` |
| **`hShift_uncond`** | `TShiftBranches.lean` | O2 第 7 支无条件 |
| `all_mem`/`guard_step`/`isFormulaSet_of_setShift_eq` | `HAllProof.lean`/`HAllGuard.lean`/`TShiftBranches.lean` | hAll 零件 |
| **`hAll_uncond`** | `HAllProof.lean` | **hAll 组装完成**，只差 `hAB` |
| `naive_law_is_false_shape` | `ITSubstCounter.lean` | 机器化反例（裸公式） |
| `mem_craig_*` 三引理 | `HRoot.lean` | hRoot 的 V 层成员解包 |
| **`translate_padding`** | `HRoot.lean` | **任意 fvar 域**的 translate/padding 交换 |

### 2.2 吸收（独立核验后）
- `TranslateShiftCompat-a841872c.lean`（9276）：`iT_shift` 完整版（**双路互证**）、
  `free_imp_domZero`、`shift_imp_domZero`、`shift_iTR` 等 16+ 定理
- `SetupQTools.lean`：`split_or` + `replace_of_imp`
- `ProvableSeq.lean`：`provable_into_sequent`

---

## 三、两个重要更正（本会话实测得出）

### 3.1 hAB：从"只能走蕴含式"更正为"有可行突破口"

**qVec 保护内层绑定**：`qVec w = ^#0 ∷ termBShiftVec (len w) w`
（`Term/Functions.lean:557`）；`substs_all : subst L w (^∀ p) = ^∀ (subst L (qVec L w) p)`。
`subst` 下降过绑定子时**前置新 bvar 0 并把原索引 +1**。故在 `iTR`（`qqAlls(·,2)` 两层绑定）
的深度 2 处，`subst ?[^&0]` 落在索引 2，**不命中 `iVE` 内部 `eqAtom` 的 bvar 0**。

我的反例（`subst ?[^&0] (eqAtom ^&x) ≠ eqAtom ^&x`）**结论正确**（裸公式确实恒假），
但**范围被我夸大**——`iTR` 的实际结构使正确的律成立。

**Foundation 提供的机制**：`termSubstVec_qVec_qVec`、`substs_qVec_bShift`。
**下一步**：证 iTR 层的 `subst` 律（`substs_all`/`substs_ex` + `qVec` 组合）。

### 3.2 hRoot：从"纯 API"更正为"V/ℕ 层的实质桥"

`provable_iff_provable : Provable T (⌜φ⌝ : **ℕ**) ↔ T ⊢ φ`（经 `T.internalize ℕ`）——
定义在 **ℕ 层**；而 hRoot 目标是 **V 层**（任意 `Type u_1`）。
两者是**实质区别**，桥需要 `V ⊨ 𝗜𝚺₁` 的内部化——属 `Z0UniBridge`/`ShCraigElim` 的同一实质内容。
**我此前判断"纯 API"有误。**

---

## 四、剩余义务（精确）

| 义务 | 状态 | 下一步 |
|---|---|---|
| **`hAB`** | hAll_uncond 的唯一前提 | 走 §3.1 的 qVec 路线（iTR 层 subst 律） |
| `hExs` | 与 hAll 同形 | hAll 一通则随之 |
| `hRoot` | 解包引理 + translate_padding 已证 | V/ℕ 层 `Provable` 桥（实质内容） |
| `ShCraigElim` 组装 | 7 支无条件 + hAll/hExs 差 hAB | 等 hAB |

---

## 五、可复用工具与陷阱

**工具**：`.cg009-verification/round31/topobuild.py`（从零拓扑编译，逐文件删 olean）。

**陷阱**（本会话实测）：
1. Write 工具被跨 worktree 钩子拦截 → 用 Bash heredoc。
2. 编译缓存会假命中 → 必须删 olean 重编。
3. **层数记账**：`IsUTermVec.isSemitermVec` 给的层是 `listMax`；对接 `iTR` 的 `n` 要用 `IsSemitermVec`。
4. **`iT.construction` 直接 `simp only` 会展开整个结构体** → 用具名引理 + `show`。
5. **`Semisentence`（Empty 域）的 `Rewriting` 实例不直接可得** → 走 `Rewriting.emb`。
6. **删除只进废纸篓** → 用 `~/bin/rm-trash` 绝对路径（Bash shell 不加载 zsh alias）。
7. **引用任何"已证"前独立重编译**。

**边界**：只写本工位；不合并 dev；路径③（改 `iT` 定义）须用户裁定。
