# 同一个定义在 UIP 内核中自动相干（C-65）

> HUMAN_EDITED；2026-09-26；Claude（Opus 5.5），会话 7f138325；目标包 CG-002，完成门 G2。
>
> **起因**：与 Cubical 包 `wild-sst`（C-64）组成“同一定义两侧”的对照：现实一侧取“相同是事实”的世界。
>
> - proof id：`MP-CG001-WILD-SST-LEAN-001`（主包）；负控制 `MP-CG001-WILD-SST-LEAN-NEG-001`。
> - claim：`CG001-C-65`。
> - 工具链：Lean 4.34.0 核心，不用 Mathlib（`../pedometer-ablation-lean/LEAN_TOOLCHAIN.json`）；`leanchecker --fresh` 重放；零警告。
> - 索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §16（GOAL_LOCAL_INDEX_ONLY）。

## 命题全文（`WildSSTUIP.lean`，命名空间 `CG001.WildSSTUIP`）

- **定义**，与 `../wild-sst/WildSST.agda` 逐项相同：`Fin'`（`Fin' 0 = Empty`，`Fin' (n+1) = Sum Unit (Fin' n)`）、`fzero`、`fsuc`、`weaken`、`LeF`（值在 `Prop`）；引理 `LeF_trans`、`weaken_le`、`weaken_le_fsuc`；结构 `WildSST`（`X`、`d`、`sid`）；两条路线 `routeA`、`routeB`；六边形相干 `Coh2`。
- **定理** `coh2 : ∀ S, Coh2 S`，证明为 `fun _ _ _ _ _ _ _ => rfl`：两条路线是同一个等式命题的两个证明，Lean 的相等证明无关，所以它们定义性相等。
- `#print axioms`：`LeF_trans`、`weaken_le`、`weaken_le_fsuc`、`coh2` 均不依赖任何公理。

## 这件事说明什么（解释，非机器证明）

- 【解释】在相同是事实的世界里，“点、面映射、面之面相合”这一行定义就是完整的定义：一切更高的相干都自动成立，后退在第一步就停。Cubical 一侧的同一段文字接受不相干的数据（C-64），差别只在“相同”是事实还是结构。
- 【来源】UIP 与单价性不相容（HoTT Book 例 3.1.9；Cubical 一侧见 C-63 (a)）。

## 禁止外推

- 不陈述任何关于 HoTT 路径的事：Lean 的相等满足 UIP。
- “自动相干”只对本定义的六边形条件机器证明；更高层同理的说法是解释，理由相同（证明无关）。

## 负控制

`WrongRoute.lean`：路线 A 的最后一步把一对面映射的顺序颠倒（`weaken j, weaken i`）。预期被拒：这一步需要 `LeF (weaken j) (weaken i)`，所给的是 `LeF (weaken i) (weaken j)`（“Application type mismatch”）。

## 运行

- 主包：`HoTT/verification/runs/20260926-CG001-WILD-SST-LEAN-01`。
- 负控制：`HoTT/verification/runs/20260926-CG001-WILD-SST-LEAN-NEG-01`。
