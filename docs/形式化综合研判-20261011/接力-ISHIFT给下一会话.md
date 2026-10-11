# 接力：`ishift` 只剩 `iTR_shift` 的组装（给下一会话）

> 2026-10-11 15:0x，CG-009 会话（elegant-mclaren）。**本文件不改共享文件、不改他人源码**。

## 一句话

**`ishift` 的最后障碍已由 9276 清除**（`iVE_shift` 全称版已证，本会话独立核验）。
现在只剩 **`iTR_shift` 的组装**（把已证的零件拼起来），然后 `ishift`/`iT_shift`/`tshift` 连锁打通。

## 已证清单（全部 exit 0、公理仅三条标准公理）

### A. 9276 产出（本会话独立核验后吸收）
文件：`成果-IShiftDomZero/TranslateShiftCompat-2002d386.lean`（sha `2002d386`，0 sorry，16 定理）
- `iVE_shift`：**全称版** `iVE n (termShift t) = shift (iVE n t)` ← **关键解锁项**
- `shift_conjunct`、`shift_qqAlls`、`shift_cRel`、`shift_cFunc`、`shift_cDomN`、
  `shift_ve0`、`shift_ve2`、`shift_quote_sentence`、`shift_eqAtom_*`、`iVE_shift_bvar/fvar`、
  `termShiftVec_shiftVec_V`、`nth_shiftVec`

### B. 本会话产出
文件：`成果-IShiftDomZero/` 下各文件
- `shift_domZero`（枢纽）、`shift_quote`（通用工具）
- `ishift` 六支（verum/falsum/and/or/all/exs）
- `iT_shift` 七支（`ITShift-7of9.lean`）——九支中除 rel/nrel 外全过核

## 剩余工作（精确）

### 1. `iTR_shift`（进行中，`ITRShift-inprogress.lean`）

目标：`iTR n 2 R (termShiftVec ℒₒᵣ 2 v) = shift (iTR n 2 R v)`（`hv : IsSemitermVec ℒₒᵣ 2 n v`）

**已完成的部分**（文件里已写、编译到只剩最后一步）：
- `h0`/`h1`：`(termShiftVec 2 v).[i] = termShift v.[i]`（`nth_termShiftVec`）
- `e0`/`e1`：两个 conjunct 分量用 `iVE_shift` + `shift_conjunct` 对接 ✅
- `hA0`/`hA1`/`hA01`/`hA`/`hB`：各分量的公式性 ✅

**剩余**：把 `shift` 从 `qqAlls` 外推到内（`shift_qqAlls` + `shift_or`/`shift_neg`/`shift_and`/`shift_cRel`）。
编译错误在两处：
- 第 56 行附近：`hbody` 的类型标注（`IsUFormula` 的组装）；
- 第 66 行：`shift_qqAlls` 的 rewrite 未匹配（可能需先 `show` 出目标形状）。

**提示**：照 9276 的 `shift_ve2`（同文件 331–390 行）的写法——
它用 `show` 把目标显式写出，再用 `rw [shift_qqAlls hbody, shift_or …, shift_neg …, hsa, hsb]`。

### 2. 之后的连锁

`iTR_shift` → `iT_shift` 的 `rel`/`nrel` 两支（用 `iT_rel`/`iT_nrel` + `iTR_shift`）
→ **`ishift` 完整** → `iT_shift` 完整 → `tshift`（`GateBranches.tshift_of_ishift` 已过核）
→ `hShift` 支 → O2 只剩 `hAll`/`hExs`/`hAxm`。

### 3. 注意

- `hExs` 另需 `iT_substs1`（同形但用 `substs1`）——可仿 `iVE_shift` 写 `iVE_substs1`。
- `iVE_shift` 的层参数与 `iTR` 的 `n` 必须**同一层**（用 `IsSemitermVec` 而非
  `IsUTermVec`+`listMax`）——这是本会话踩过的坑，`isSemiformula_iTR` 是先例。

## 协作

- 本会话与 9276 在同一战线**互补**：9276 出 `iVE_shift` 全链，本会话出 `shift_domZero`/
  `shift_quote`/六支/七支。两边的零件都有防回退副本。
- 引用任何"已证"前先独立重编译。
