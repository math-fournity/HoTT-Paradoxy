# 连集合的宇宙也不是集合：自指两难真正卡住的地方（C-71）

> HUMAN_EDITED；2026-09-26；Claude（Opus 5.5），会话 7f138325；目标包 CG-003，完成门 G4。
>
> - proof id：`MP-CG001-HSET-UNIVERSE-001`（`HSetNotSet.agda`）。
> - 负控制：`MP-CG001-HSET-UNIVERSE-NEG-001`（`WrongFlipSetTrivial.agda`）。
> - claim：`CG001-C-71`。回答 019 的 T-041，与 C-67 配套。
> - 工具链：Agda 2.8.0-3d04bac + cubical 0.9，`--safe --cubical --guardedness`，无公设。
> - Lean 对照：`../universe-set-lean/`（C-72）。
> - 索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §17（GOAL_LOCAL_INDEX_ONLY）。

## 命题全文（`HSetNotSet.agda`）

- `notPath = ua notEquiv : Bool ≡ Bool`。`notPath≢refl : ¬ (notPath ≡ refl)`：沿它搬运 `true` 得到 `false`。
- `BoolSet = (Bool , isSetBool) : hSet ℓ-zero`。`flipSet = Σ≡Prop (λ _ → isPropIsSet) notPath : BoolSet ≡ BoolSet`，它的第一分量就是 `notPath`。
- `hSetNotSet : ¬ isSet (hSet ℓ-zero)`：若 hSet 是集合，`flipSet ≡ refl`，取第一分量得 `notPath ≡ refl`，矛盾。

## 为什么要做（解释）

- 【解释】对 C-67 最强的反对是：玩具语法预设了一条本应解释成非平凡回路的等式（`swap` 对应翻转），而真实类型论语法的等式（β、η、代换律）在标准模型中都由 `refl` 解释。所以 C-67 的第二支（集合式语法无法忠实地解释进单价宇宙）比真实情形更强，不是 Kraus 所说障碍的公平缩影。
- 【解释】本包给出更公平的一支。把语法截断成集合之后，要用截断的消去子解释语法，目标必须是集合，这与语法里有哪些等式无关。自然的目标是宇宙（不是集合，C-63）；退一步只把类型解释成集合，目标是 hSet，单价性仍使它不是集合（本包）。所以即使每条语法等式都送到 `refl`，消去子这条路在宇宙上、甚至在 hSet 上都走不通。卡住它的是目标里结构式的相同，也就是 A7 的同一个前提。
- 【解释】在 UIP 世界（Lean）中，宇宙是集合，Bool 到自身的任何认同作用都是恒等（C-72），这一条路就是通的。这与“UIP 下类型论在类型论中运作良好”（Kraus 2021 摘要，来源已在 CG-002 核对）相合。

## 禁止外推

- 不证明 HoTT 不能以任何方法解释自己：这里只说明截断语法的消去子这条路被挡住。Kraus 2021 用 2LTT 中的 ∞-CwF 给出了另一条路，其初始性仍是猜想。
- 不证明 HoTT 不一致。

## 负控制

`WrongFlipSetTrivial.agda` 断言沿 `cong fst flipSet` 搬运 `true` 仍得 `true`（`refl`）。预期被拒：`false != true of type Bool`。

## 运行

- 主包：`HoTT/verification/runs/20260926-CG001-HSET-UNIVERSE-01`。
- 负控制：`HoTT/verification/runs/20260926-CG001-HSET-UNIVERSE-NEG-01`。
