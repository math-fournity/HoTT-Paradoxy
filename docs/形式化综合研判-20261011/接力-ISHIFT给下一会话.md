# 接力：`ishift` 只剩 `func` 支（给下一会话）

> 2026-10-11 13:3x，CG-009 会话（elegant-mclaren）。**本文件不改共享文件、不改他人源码**。
> 供 canonical 或新工位 `cg007-w8-d3` / `9276-cg007-w8-d3` 上攻 O2 三支的会话取用。

## 一句话

**`ishift`（`iT n (shift x) = shift (iT n x)`）的九支里，**七支已证**，
只剩 `rel`/`nrel` 两支——它们的唯一障碍是 `iVE`/`termShift` 相容律的 **`func` 支**。**

## 已证清单（全部 exit 0、`#print axioms` 仅三条标准公理）

### 本会话（elegant-mclaren-767fb0）产出
文件：`docs/形式化综合研判-20261011/成果-IShiftDomZero/`

| 定理 | 文件 | 内容 |
|---|---|---|
| `shift_domZero` | `ShiftDomZero.lean` | **枢纽**：`shift domZero = domZero` |
| `rew_shift_emb` | 同上 | Rewriting 层 |
| `shift_quote` / `rew_shift_quote` | `ShiftQuote.lean` | **通用工具**：`shift` 固定任意句子引号 |
| `shift_cFunc0` / `shift_subst_cFunc0` / `shift_ve0` | `ShiftVe0.lean` | `func` 支 **k=0** |
| `shift_imp` / `ishift_all` / `ishift_exs` | `IShiftAllExs.lean` | 量词支 |
| `ishift` 六支（verum/falsum/and/or/all/exs） | `IShiftFull-6of8.lean` | 主定理骨架 |

### 9276 产出（本会话独立核验后吸收）
文件：`成果-IShiftDomZero/TranslateShiftCompat-966fb6a7.lean`

| 定理 | 内容 |
|---|---|
| `shift_eqAtom_bvar` | `shift (eqAtom ^#z) = eqAtom ^#z` |
| `shift_eqAtom_fvar` | `shift (eqAtom ^&x) = eqAtom ^&(x+1)` |
| `iVE_shift_bvar` | `iVE n (termShift ^#z) = shift (iVE n ^#z)` |
| `iVE_shift_fvar` | `iVE n (termShift ^&x) = shift (iVE n ^&x)` |

**注意**：9276 该文件仍是**未跟踪**（不在 git）。本会话已防回退复制。

## 剩余：`func` 支（双方确认的唯一障碍）

目标：`iVE n (termShift t) = shift (iVE n t)`，对 `t = ^func k f v`（`k ≠ 0`，即 `ve2`）。

展开（`iVE_func`）：
```
LHS: iVE n (^func k f (termShiftVec k v))
   = ve2 n k f (resultVec ![n] k (termShiftVec k v))        [iVE_func]
RHS: shift (ve2 n k f (resultVec ![n] k v))
```
而 `ve2 n k f w = qqAlls (imp (conjunct 3 n 0 w.[0] ^⋏ (conjunct 3 n 1 w.[1] ^⋏ ⊤))
                              (subst (^#2 ∷ ?[^#0, ^#1]) (cFunc k f))) 2`

**需要的新引理**（本机实测不存在）：
1. `shift_conjunct`：`shift (conjunct 3 n i x) = conjunct 3 n i (shift x)`——
   `conjunct` 是 `x ^⋏ x ^⋏ …` 的叠合，用 `shift_and` + 归纳；
2. `shift (subst (^#2 ∷ [#0,#1]) (cFunc k f)) = 自身`——**闭项**，走 `shift_quote` 路线
   （`cFunc k f` 是 numeral = 句子引号；本会话的 `shift_cFunc0` 是其 k=0 版）；
3. `resultVec` 与 `termShiftVec` 的点相容（`nth_resultVec` 逐分量 + 项级 IH）。

**建议路径**：用 `IsSemiterm.sigma1_induction` 做项归纳（三支 bvar/fvar/func），
bvar/fvar 已有（上表），func 支按上述三点展开。`isSemiformula_iVE`（`SeqTranslateFormula.lean:266`）
是现成的写法模板（它用了 `nth_resultVec`）。

## 下游链条

`iVE_shift` 完成 ⇒ `iT_shift`（`iTR` 只经 `iVE` 的 `v.[0]`/`v.[1]`）
⇒ `translateSeq_setShift` ⇒ `hShift`/`hAll`/`hExs` 三支 ⇒ `ShCraigElim` 十支全接
⇒ `zfcTr_D3_internalize` ⇒ Z0 完整形式。

`tshift ⇐ ishift` 的归约已过核（`GateBranches.tshift_of_ishift`，`成果-GateBranches/`）。

## 协作注意

- 本会话与 9276 在同一战线**并行**且互补；两边的零件都已在本目录有防回退副本。
- **不要**在错误的依赖集里硬修（`SeqTranslateFormula` 各工位版本有差异）。
- 引用任何"已证"前先独立重编译（本会话即以此证伪了 9276 的两处旧断言）。
