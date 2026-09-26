# 事实世界的对照：UIP 下宇宙是集合，Bool 的自认同不能翻转（C-72）

> HUMAN_EDITED；2026-09-26；Claude（Opus 5.5），会话 7f138325；目标包 CG-003，完成门 G4。
>
> - proof id：`MP-CG001-UNIVERSE-SET-LEAN-001`（`UniverseIsSet.lean`）。
> - 负控制：`MP-CG001-UNIVERSE-SET-LEAN-NEG-001`（`WrongCastFlips.lean`）。
> - claim：`CG001-C-72`。与 C-63、C-71 对照。
> - 工具链：Lean 4.34.0 核心（`../pedometer-ablation-lean/LEAN_TOOLCHAIN.json`），经 `tools/lean_check.py` 按绝对路径调用，不经 elan；主包加 `leanchecker --fresh`。
> - 索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §17（GOAL_LOCAL_INDEX_ONLY）。

## 命题全文（`UniverseIsSet.lean`）

- `universeIsSet {A B : Type} (p q : A = B) : p = q := rfl`：宇宙是集合。
- `castIsId (p : Bool = Bool) (b : Bool) : cast p b = b := rfl`：沿 `Bool = Bool` 的任何证明做 cast，都不改变任何布尔值。
- `noFlip (p : Bool = Bool) : cast p true ≠ false`。

## 这件事说明什么（解释）

- 【解释】同一件事在两个世界里不同。
  - Cubical Agda 中，`ua notEquiv` 是 Bool 到自身的认同，把 `true` 送到 `false`：宇宙不是集合（C-63），集合的宇宙也不是集合（C-71）。
  - Lean 中，相同是事实：`A = B` 的证明全都相等，Bool 的任何自认同都作用为恒等。
- 【解释】所以在 UIP 世界里，截断成集合的语法可以用消去子解释进宇宙；在 HoTT 里，这条路被单价性挡住（C-71）。这是 A7′（HoTT 吃掉自己）在“目标是否为集合”这一点上的正反对照。

## 禁止外推

- 本包是 UIP 类型论中的命题，不是 HoTT 命题。它只是对照，不证明 HoTT 中有任何不可能性。

## 负控制

`WrongCastFlips.lean` 断言某个沿 `Bool = Bool` 的 cast 把 `true` 送到 `false`（`rfl`）。预期被拒：类型不符，因为 cast 化简为恒等。

## 运行

- 主包：`HoTT/verification/runs/20260926-CG001-UNIVERSE-SET-LEAN-01`。
- 负控制：`HoTT/verification/runs/20260926-CG001-UNIVERSE-SET-LEAN-NEG-01`。
