# 罗素式的必须完成的追问：把相同已落定的东西收成总体，总体总比成员少落定一层（C-73）

> HUMAN_EDITED；2026-09-26；Claude（Opus 5.5），会话 7f138325（CG-003 关包之后）。
>
> 起因：用户【原话】“其实此刻应该想想罗素悖论，因为罗素悖论要求对S的计算必须完成。我们是否可以参考罗素悖论来构造必须完成的‘追问’呢？”
>
> - proof id：`MP-CG001-TOTALITY-ESCALATION-001`（`TotalityEscalates.agda`）。
> - 负控制：`MP-CG001-TOTALITY-ESCALATION-NEG-001`（`WrongRotateTrivial.agda`）。
> - claim：`CG001-C-73`。
> - 工具链：Agda 2.8.0-3d04bac + cubical 0.9，`--safe --cubical --guardedness`，无公设。
> - 索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §18（GOAL_LOCAL_INDEX_ONLY）。

## 任务（罗素式的构造）

- **“落定”的含义**：按 h-层级。集合层（库中的 2）里，“x 与 y 以什么方式相同”至多一个答案；群胚层（3）里，答案可以不同，但答案之间的方式唯一；依此类推。
- **总体**：`TypeOfHLevel ℓ n` 把所有在 n 层落定的类型收成一个总体。
- **要求**：总体本身也在同一层落定。这样它才能与它的成员同类，才能把自己算进去。罗素的要求是 S 必须作为集合完成，这里对应的是“相同已落定者的总体”必须作为落定者完成。

## 命题全文（`TotalityEscalates.agda`）

- **(a) 上界（库）**：n 层落定者的总体在 n+1 层落定。
  - `setsGatherIntoGroupoid : isGroupoid (hSet ℓ-zero)`；
  - `groupoidsGatherInto2Type : isOfHLevel 4 (hGroupoid ℓ-zero)`；
  - `ladderUpper : (n : ℕ) → isOfHLevel (suc n) (TypeOfHLevel ℓ-zero n)`（即库的 `isOfHLevelTypeOfHLevel`）。
- **(b) 前两级恰好少一层**：
  - `setsGatherNotSet : ¬ isSet (hSet ℓ-zero)`：Bool 的自认同 `ua notEquiv` 沿 `Σ≡Prop` 成为 hSet 在 (Bool, isSetBool) 处的环，它不是 `refl`；
  - `groupoidsGatherNotGroupoid : ¬ isGroupoid (hGroupoid ℓ-zero)`：`rotateOnce = equivEq (funExt rotLoop)` 是 S¹ 的恒等自等价处的环，`winding (cong (λ e → equivFun e base) rotateOnce) ≡ pos 1` 由 `refl` 成立，所以 `S¹ ≃ S¹` 不是集合；而 hGroupoid 在圆周处的环等价于 `S¹ ≃ S¹`（`Σ≡PropEquiv` 加 `univalence`）。
- **(d) 用截断强行落定会毁掉总体**：`noDecoding`，不存在从 `∥ hSet ℓ-zero ∥₂` 回到 hSet 的映射使截断可逆，因为那会使 hSet 成为集合的收缩，从而是集合。
- **(c) 对照（另包）**：Lean 4（UIP）中宇宙是集合（C-72），总体一步落定。

## 这件事说明什么（解释，非机器证明）

- 【解释】要把总体算进去，就得升一层；升一层后的新总体又少落定一层。于是这个要求永远合不上，形状正是 KC-000016 说的“总是在拿入和拿出它自己”，只是发生在相同的层级上，而不是在成员关系上。
- 【解释】要把两种上升分开：
  - 宇宙的大小（`Type` 在 `Type 1` 里）在 HoTT 与 Lean 中都上升，这是罗素、Girard 本身的围栏，不是 HoTT 特有的；
  - 本包证明的是相同层级的上升，在 Lean 中不发生，来源是单价性。
- 【解释】这一要求在 HoTT 自己的工作中真实出现：
  - 自解释（KC-000026）：截断语法的消去子要求目标是集合，而 U 与 hSet 都不是（C-63、C-71）；
  - 统一定义半单纯类型（A7）：需要把一切层级收成一个总体。
- 【解释】类比只借用一条关系：“总体被要求与成员同类、而且必须完成”。罗素的 S 在任何理论中都是非法的要求；这里的要求在事实世界（Lean）中合法而且一步完成，是单价性使它合不上。

## 禁止外推

- 不证明 HoTT 不一致。
- “对一切 n，n 层落定者的总体都不是 n 层”（精确上升）只在 n = 0、1 两级有机器证明；一般情形为已知结果（用 Eilenberg–MacLane 型类型），本包不证明。
- 上界 (a) 是库定理（HoTT Book 定理 7.1.11 的形式化），本包只是引用。
- 不证明罗素悖论与本构造之间存在形式等价。

## 负控制

`WrongRotateTrivial.agda` 断言 `rotateOnce` 带着 base 走的环绕数为 0（`refl`）。预期被拒：`1 != 0`。

## 运行

- 主包：`HoTT/verification/runs/20260926-CG001-TOTALITY-ESCALATION-01`。
- 负控制：`HoTT/verification/runs/20260926-CG001-TOTALITY-ESCALATION-NEG-01`。
