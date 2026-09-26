# “HoTT 吃掉自己”的小型展示：语法的等式是结构还是事实（C-67）

> HUMAN_EDITED；2026-09-26；Claude（Opus 5.5），会话 7f138325；目标包 CG-002，完成门 G4。
>
> - proof id：`MP-CG001-SELF-INTERPRETATION-001`（主包）；负控制 `MP-CG001-SELF-INTERPRETATION-NEG-001`。
> - claim：`CG001-C-67`。
> - 工具链：Agda 2.8.0-3d04bac + cubical 0.9，`--safe --cubical --guardedness`，无公设，零警告。
> - 索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §16（GOAL_LOCAL_INDEX_ONLY）。

## 同一任务合同（A7′）

- **输入**：一个类型论的语法，写成理论内部的归纳类型（上下文、类型、项、代换）连同其等式。
- **允许的操作**：在理论内部定义函数与类型。
- **观察**：能否写出“标准解释”：每个语法类型送到宇宙中的一个类型、每条语法等式送到它在宇宙中的含义。
- **完成标准**：理论内部有一个对完整语法（全部层级、不截断含义）忠实的标准解释，即理论能充当它自己的解释器。
- **现实对照**：许多编程语言可以写出自解释器；在满足 UIP 的类型论里，“类型论在类型论中”运作良好（Kraus 2021 摘要，【来源】）。
- **HoTT 一侧**：长期开放；Kraus 2021 摘要称根本困难似乎是“没有 UIP 时，范畴不足以刻画类型论”；例 6：HoTT 中宇宙不是集合，标准模型不是集合式 CwF，“一种可能的看法是，与许多其他编程语言不同，HoTT 用这种方法不能充当它自己的解释器”（【来源】，原句见 CG-002 工作台 §1）。

## 命题全文（`SelfInterpretation.agda`）

玩具语法只有一个基类型、函数类型与一条等式 `swap : arr a (arr b c) ≡ arr b (arr a c)`；它在宇宙中的含义是交换两个参数的等价 `flipEquiv`。

- `flipIsNotRefl : ¬ (ua (flipEquiv {Bool} {Bool} {Bool}) ≡ refl)`（沿它搬运 `first x y = x` 得到 `x y ↦ y`）。
- **(a) 等式是结构（不截断，`Syn∞`）**：`⟦_⟧∞ : Syn∞ → Type` 把 `swap a b c` 送到 `ua flipEquiv`；`faithful∞ : cong ⟦_⟧∞ (swap base base base) ≡ ua flipEquiv`（`refl`）；`faithfulForStructure : Faithful Syn∞ base arr swap`；`syntax∞IsNotASet : ¬ isSet Syn∞`。
- **(b) 等式是事实（截断成集合，`Syn`，带 `trunc : isSet Syn`）**：`⟦_⟧P : Syn → hProp ℓ-zero` 存在（命题宇宙是集合，`swap` 送到由 `hPropExt` 与 `Σ≡Prop` 给出的路径，`trunc` 送到 `isSetHProp`）；`noFaithfulForFacts : ¬ Faithful Syn base arr swap`。
- `Faithful S b ar sw` 指：存在 `f : S → Type` 与认同 `e : f (ar b (ar b b)) ≡ (Bool → Bool → Bool)`，使 `sym e ∙ cong f (sw b b b) ∙ e ≡ ua flipEquiv`。

## 这件事说明什么（解释，非机器证明）

- 【解释】这是 A7 的自指版本，缩成一条等式：理论要解释自己，就要决定语法里的等式是事实还是结构。选结构，忠实解释存在，但语法本身不再是集合，它的等式之间的相干又成为义务（与 C-64、C-66 的后退同一个前提）；选事实，语法可以干净地写成集合，却只能解释进事实式的宇宙（命题宇宙），无法忠实地解释进单价宇宙，因为宇宙里的“相同”是结构（C-63 (a)）。
- 【解释】它对着 KC-000026（“HoTT难道可以越过对其自身的自指吗？我不相信。”）与 KC-000027（HoTT“将自己对齐到了程序上……程序的问题，也就成了它的问题”）：真实的编程语言可以写自解释器，HoTT 恰恰在这一步卡住。

## 与 Codex／Astra 的 R 系列的差量（回原报告核对）

- C-223–C-226（`audit/G-HOTT-SYNTAX首个精确机器切片与2LTT边界-20260914.md`；`LIT-HOTT-COMPUTABILITY-001/004`）：把 `akaposi/cohtt` 的群胚截断语法固定为 Gödel 式 R4 的目标演算（语法、代换、`isSetTy`、与集合语法的同构），审的是“语法与算术编码是否够做不完备性”，不涉及标准解释进单价宇宙。
- C-227–C-232：2LTT 定理 2.20（把外层类型的纤维化替换内在化为代换稳定的规则，则内层满足 UIP）；当时判为 `SOURCE_REPORTED_COUNTEREXAMPLE_CANDIDATE`，后按受限接口（crisp、外层）能完成来源任务，归为 defense/qualification boundary（`MEMORY/002`）。
- 本包审的是另一件事：标准解释这一步本身的两难（等式作为结构或作为事实）；与 R 系列同一前提（没有 UIP 或宇宙不是集合），但任务不同。Session-C 父范围覆盖表中 S07“内部模型、反射与无限相干性”、E14“内部模型与半单纯/有向扩展”在其写成时为 `UNREVIEWED / UNASSIGNED`。

## 禁止外推

- 玩具语法只有函数类型与一条等式，是障碍的缩影，不是类型论的模型；不证明 HoTT 不能以任何方法解释自己（Kraus 用 2LTT 中的 ∞-CwF 给出了一条路，其初始性仍是猜想）。
- 不证明 HoTT 不一致；(b) 的否定只针对“把 swap 送到翻转”的忠实性。

## 负控制

`WrongFlipIsIdentity.agda`：断言 `transport (ua flipEquiv) first ≡ first`（`refl`）。预期被拒：`x != x₁ of type Bool`。

## 运行

- 主包：`HoTT/verification/runs/20260926-CG001-SELF-INTERPRETATION-01`。
- 负控制：`HoTT/verification/runs/20260926-CG001-SELF-INTERPRETATION-NEG-01`。
