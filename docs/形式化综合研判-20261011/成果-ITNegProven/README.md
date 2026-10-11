# 成果-ITNegProven：iT_neg 已证 + 七支接线（本会话扫描捕获与独立核验）

> 2026-10-11，CG-009 会话。来源：新工位 `/Volumes/D/HoTT-worktrees/cg007-w8-d3`（分支 `codex/cg007-w8-d3`）。
> **本目录是防回退副本 + 独立核验记录**；原始证明与收据在新工位。

## 一、捕获与核验（四层证据分开）

| 文件 | sha256（前 16） | 本会话独立编译 | 公理 |
|---|---|---|---|
| `ShCraigElimNegLaw-5f504b8d.lean` | `5f504b8d8d8fcde2` | **exit 0** | `[propext, Classical.choice, Quot.sound]` |
| `ShCraigElimBranches-e8ed5b33.lean` | `e8ed5b33b5ccd41c` | **exit 0** | 七支全干净 |
| `GateBranchesU.lean` | `3683a9f6f6cbf54d` | **exit 0** | `hAxL_uncond`/`hCut_uncond` 干净 |

**核验方式**：全量 47 文件从零拓扑编译（`.cg009-verification/round31/`，逐文件删 olean，
pinned Lean 4.34.0 + Foundation `1fb01b72` + Astra Mathlib `5ed29652`）。
不是"读文档"，也不是"相信缓存"。

## 二、内容

### `iT_neg`（CG001-C-398）
`iT n (neg ℒₒᵣ p) = neg ℒₛₑₜ (iT n p)`——V 内**任意公式码**（非仅引号化）的一般相容律，九支全证。
关键：归纳谓词带 `param = n` 护罩（`semiformula_result_induction` 输出层与输入层独立量化，而 `iT` 改层）。

### 七支接线（CG001-C-400）
`ShCraigElimBranches.lean`：`isFormulaSet_translateSeq`、`hWk`、`hVerumIntro`、
`hAxL`、`hAnd`、`hOr`、`hCut`——七支全部无 sorry。
`hAxL`/`hCut` 是 `iT_neg` 的直接消费者。

### 吸收实验：`GateBranchesU.lean`
用已证的 `iT_neg`，本会话把 `GateBranches` 的 `hAxL`/`hCut` 从"条件于 `iT_neg`"升级为
**无条件版**。调用形状：`fun n p' hp' => GodelQ.ShCraigElimNegLaw.iT_neg (n := n) p' hp'`。

## 三、仍未做（不得读成已完成）

- `ShCraigElim` 的 **`hAll`/`hExs`/`hShift` 三支未接线**——需 `iT` 与 `setShift`/`substs1` 的相容律，
  本机实测**不存在**（`shift` 的构造原子支用 `termShiftVec`、量词支不加 `domZero`，与 `iT` 不同构）。
- `hAxm` 支需 `codeOfREPred` 的一般 V 表示引理（O3 证书桥）。
- `ShCraigElim` 本身未证；`zfcTr_D3_internalize` 未证。

## 四、本会话的独立发现（诚实记录）

**9276 工位的 `NegInvolution.lean` 改写版不通过本会话独立核验**：
- 该文件在本会话扫描期间被连续编辑三次（sha `e8eaad10` → `757373b8` → `9906d3ce`），
  属"编辑中态"；
- 取 `757373b8` 版 + 它自己的 `NegInvolutionBranches`（`030f90f9`）做全量编译：
  **exit 1，四处 `Type mismatch`**（`graph_dom_uformula` 给出 `IsUFormula p`，
  而目标要 `IsUFormula (result … param p)`），`#print axioms` 含 `sorryAx`；
- 其 `ShCraigElimNegLaw.lean`（6601 B，`41935eb3`）是**已知失败版**（`IsUFormula.qqAlls` 不存在）。
- **对照**：cg007-w8-d3 的同名文件（`d3e03ca6` / `5f504b8d`）全部通过。
- 结论：9276 工位在**旧基线上**工作；本目录的接力信息对它价值最大。
