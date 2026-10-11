# 接力：O2 的 hAll/hExs（给下一会话）

> 2026-10-11 16:0x，CG-009 会话（elegant-mclaren）。**本文件不改共享文件、不改他人源码**。

## 一句话

**`iT_shift` / `tshift` / `hShift` 已证**（本会话）。剩余 `hAll`/`hExs` 需要**另一类**相容律
——`free`/`substs1` 的相容（不是 `shift` 的），其归约结构已由 9276 实测打通，只缺一条代入律。

## 已证清单（全部 exit 0、0 sorry、公理仅三条标准公理）

### 本会话新证（`成果-IShiftDomZero/`）
| 定理 | 文件 | 内容 |
|---|---|---|
| **`iT_shift`** | `ITShift-FULL.lean` | `iT n (shift p) = shift (iT n p)`，九支全过 |
| `iTR_shift` | `ITRShift.lean` | rel 支的原子（用 iVE_shift + 9276 的零件组装） |
| **`tshift`** | `TShift.lean` | `translateSeq (setShift s) = setShift (translateSeq s)`（公式集版） |
| **`hShift_uncond`** | `TShiftBranches.lean` | O2 的 hShift 支**无条件** |
| `isFormulaSet_of_setShift_eq` | 同上 | `setShift s'` 是公式集 ⇒ `s'` 是公式集 |
| `shift_domZero` / `shift_quote` / `ishift` 六支 / `shift_ve0` | 各文件 | 本会话早期成果 |

### 吸收自 9276（本会话独立核验）
`TranslateShiftCompat-2002d386.lean`：`iVE_shift`（全称版）+ `shift_conjunct`/`shift_qqAlls`/
`shift_cRel`/`shift_subst_cFunc`/`shift_ve0`/`shift_ve2`/`nth_shiftVec` 等 16 定理。

## 剩余：`hAll` / `hExs`（精确）

**9276 已实测打通归约结构**（其 `ShCraigElimBranches.lean` 第 267 行起的"第三轮"节）：

```
hAll 目标：Derivable 𝗭𝗙𝗖 (translateSeq s)，其中 ^∀ p ∈ s
  all_m (s) (p := imp ℒₛₑₜ domZero (iT 1 p))    -- q 被 iT_all 强制成此形
    ├─ ^∀ (imp domZero (iT 1 p)) ∈ translateSeq s   ← mem_translateSeq_iff + iT_all ✅
    └─ Derivable (insert (free ℒₛₑₜ (imp domZero (iT 1 p))) (setShift (translateSeq s)))
         ← 需把 ih 从 Derivable (insert (free ℒₒᵣ p) (setShift (fstIdx d))) 搬过来
```

**两处不相容**：
1. `setShift` 那半：`translateSeq_setShift` 已证 ✅（本会话 `tshift`）
2. `insert` 那半：需 **`iT 0 (free ℒₒᵣ p) = free ℒₛₑₜ (imp ℒₛₑₜ domZero (iT 1 p))`**
   ——展开 `free L p = substs1 L ^&0 (shift L p)` 后归结为一条**代入相容律**：
   `iT 0 (subst ℒₒᵣ ?[^&0] σ)` 与 `subst ℒₛₑₜ ?[^&0] (imp domZero (iT 1 σ))` 的关系（σ 层数 1）。

**`hExs` 同形**，用 `substs1 L t p`（t 任意项），需 `iT` 与 `substs1` 的相容。

**为什么与 shift 不同类**：`shift` 是"自由变量整体加一"，两边都在 fvar 上加一；
`substs1` 是"把项塞进绑定位置"——`ℒₒᵣ` 侧塞的是**项**、`ℒₛₑₜ` 侧塞的是**公式**
（`domZero` 的引入正为此）。所以 `iT` 必须把项论证翻译成公式论证。

**建议路线**（9276 建议 + 本会话赞同）：
1. 先证项层 `iVE` 与 `subst` 的相容（可能需要 `iVE_subst`）；
2. 再证公式层 `iT_substs1`；
3. 最后 `free` 版本 → `hAll`/`hExs`。

## 下游

`hAll`/`hExs` 完成 ⇒ O2 只剩 `hAxm`（O3 证书桥：`codeOfREPred` 的一般 V 表示引理，
独立战线）⇒ `ShCraigElim` 十支全接 ⇒ `zfcTr_D3_internalize` ⇒ Z0 完整形式。

## 协作

- 9276 在同一战线，已出 `ShCraigElimBranches.lean` 的 hAll 归约结构分析与探针；
  本会话已出 `iT_shift`/`tshift`/`hShift`。**互补**。
- 引用任何"已证"前先独立重编译。
