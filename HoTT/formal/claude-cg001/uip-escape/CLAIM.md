# 单价性关掉的那条退路（C-63）

> HUMAN_EDITED；2026-09-26；Claude（Opus 5.5），会话 7f138325。
>
> **起因**：新方向“无穷相干”（`.claude/思考与发现/CN-034 …` §5）的前提敏感性检验。已知的每一种半单纯类型定义，都在某一层加回了“作为事实的相等”（外层或严格相等、带 UIP，或 display 原语）。本包把喂养无穷后退的那一个前提单独拿出来：在单价宇宙中，“相同”不是事实，而是结构。
>
> - proof id：`MP-CG001-UIP-ESCAPE-001`（主包）；负控制 `MP-CG001-UIP-ESCAPE-NEG-001`。
> - claim：`CG001-C-63`。
> - 工具链：Agda 2.8.0-3d04bac + cubical 0.9，`--safe --cubical --guardedness`，无公设。
> - 索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §15（GOAL_LOCAL_INDEX_ONLY）。

## 命题全文（`UIPEscape.agda`）

- **(a) 宇宙不是集合**：`notPath = ua notEquiv : Bool ≡ Bool`；`alongNot : transport notPath true ≡ false`（`uaβ`）；`alongRefl : transport refl true ≡ true`；`twoIdentifications : ¬ (notPath ≡ refl)`；`typeIsNotASet : ¬ isSet Type`。
- **(b) 集合之上，上一层分不出下一层用的是哪条证明**：`overASet : isSet A → (B : A → Type) (p q : x ≡ y) (b : B x) → subst B p b ≡ subst B q b`。
- **(c) 宇宙之上分得出**：`overTheUniverse : ¬ ((b : Bool) → subst (λ X → X) notPath b ≡ subst (λ X → X) refl b)`。

## 这件事说明什么（解释，非机器证明）

- 【解释】在集合层，“面之面相合”的两条证明彼此相等，建在它们上面的下一层数据与选哪条证明无关：相干的要求走一步就停。
- 【解释】在单价宇宙里，同样的边界可以沿两条不同的认同搬运，得到不同的结果；所以在类型之上的构造必须记下用了哪一条认同，而这个记录本身又要在更上一层回答同样的问题。这就是无穷后退的燃料。
- 【解释】单价性推出宇宙不是集合（(a)），于是“所有类型都满足 UIP”这条让后退停止的退路在 HoTT 中是关着的；不带单价性的内涵类型论可以一致地加上 UIP（K 公理），HoTT 不能。归因见 CN-034 §5.4。

## 禁止外推

- (a)–(c) 都是标准事实，(a) 即 HoTT Book 例 3.1.9。它们不证明半单纯类型在 HoTT 中不可定义（开放问题），也不证明 HoTT 的任何不一致。
- (c) 只用了一个具体的边界 (Bool, Bool) 与两条认同；它说明依赖确实存在，不刻画一般的相干结构。

## 负控制

`WrongTransport.agda`：断言 `transport (ua notEquiv) true ≡ true`，由 `refl`。预期被拒：`false != true of type Bool`。两条认同由计算分开，不只由证明分开。

## 运行

- 主包：`HoTT/verification/runs/20260926-CG001-UIP-ESCAPE-01`。
- 负控制：`HoTT/verification/runs/20260926-CG001-UIP-ESCAPE-NEG-01`。
