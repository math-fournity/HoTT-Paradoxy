# 成果：NrelFix——证伪"层数记账障碍"，打通 iT_neg 的 nrel 支

> 2026-10-11，CG-009。文件 `NrelFixProbe.lean`，sha256 `5b8006c3…`。
> 本会话 pinned Lean 4.34.0 + Foundation `1fb01b72` 编译 **exit 0**；
> 三条定理 `#print axioms` 均仅 `[propext, Classical.choice, Quot.sound]`。

## 背景：一个被误判为"走不通"的障碍

canonical 新提交 `b271e69d` 加入了 9276 会话的 GUI 对话导出。该会话在攻
`iT_neg`（一般码 `iT`/`neg` 相容律）的 `nrel` 支时，需要
`IsUFormula ℒₛₑₜ (iTR param k R v)`，并写下结论（导出 7506/7544 行）：

> "两条来路都卡在同一层数不等式 `listMax (termBVVec ℒₒᵣ k v) ≤ param`，
> **而这在 `IsUTermVec` 下不成立**……这不是数学障碍，是层数记账。**这条路走不通。**"

## 证伪（本会话，机器证明）

**它漏了公式侧的假设。** 归纳原理给 `nrel` 支的假设不止 `IsUTermVec k v`，
还有 **`IsSemiformula ℒₒᵣ n (^nrel k R v)`**——后者是两字段结构，带
`bv_le : bv ℒₒᵣ (^nrel k R v) ≤ n`，而
`bv (^nrel k R v) = listMax (termBVVec ℒₒᵣ k v)`（Foundation `bv_nrel`，Basic:1289）。
Foundation 自己在 `IsSemiformula.rel`（Basic:1361）就从这个字段推同一个不等式。

三条定理（全部过核）：

| 定理 | 内容 |
|---|---|
| `listMax_le_of_semiformula` | `IsSemiformula ℒₒᵣ n (^nrel k R v) → listMax (termBVVec k v) ≤ n` |
| `isUTermVec_of_nrel` | 同假设 → `IsUTermVec ℒₒᵣ k v`（经 `IsUFormula.nrel` 分解） |
| `isSemiformula_iTR_of_nrel` | **同假设 → `IsSemiformula ℒₛₑₜ n (iTR n k R v)`**（即 `nrel` 支所需的形状） |

## 结论与用法

- **9276 的"走不通"判定应撤销**：`iT_neg` 的 `nrel` 支（以及 all/exs 支的同类层数记账）
  有明确出路——**始终携带公式侧的 `IsSemiformula` 假设**（连同护罩 `param = n`），
  而非只带 `IsUTermVec`。层数不等式由 `bv_le` 免费提供。
- 升层 `IsSemitermVec k (listMax …) → IsSemitermVec k n` 用 `IsSemiterm.def` 逐点构造。
- 该结论对 canonical 的 `ShCraigElimNegLaw.lean` 修复与新工位 `cg007-w8-d3` 的工作直接适用。

## 边界

- 这三条是**工具引理**，本身不是 `iT_neg`；`iT_neg` 的其余支与组装仍需完成。
- 文件可整体复制进正式包（新文件、不改既有）；依赖 `Z0Full`、`SeqTranslate`、
  `SeqTranslateFormula`、`InternalTranslate`（均已过核）。
