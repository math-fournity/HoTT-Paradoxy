# 论域元素的存在性追问永不停机：宇宙在任何有限层都不落定（C-75、C-76）

> HUMAN_EDITED；2026-09-26；Claude（Opus 5.5），会话 7f138325。
>
> 起因：用户【原话】（2026-09-26，本会话）：
>
> > 你的这个理解非常好：“照罗素的样子，造一个理论自己要求完成的追问”。
> >
> > 一个理论是有论域的，论域的元素的存在性就是理论必须面对的问题。也许理论可以拒绝别的，但是理论永远无法拒绝理论论域元素的存在性问题。
> >
> > 罗素悖论就是这样，如果对于论域元素S的存在性的追问，在现实中会引发无法停机的计算（无限追溯），那么我们就成功了。
>
> - proof id：`MP-CG001-UNIVERSE-QUESTIONING-001`（`UniverseHasNoLevel.agda`）。
> - 负控制：`MP-CG001-UNIVERSE-QUESTIONING-NEG-001`（`WrongSectionReadsZero.agda`）。
> - claim：`CG001-C-75`、`CG001-C-76`。
> - 工具链：Agda 2.8.0-3d04bac + cubical 0.9，`--safe --cubical --guardedness`，无公设；用到库中的 Eilenberg–MacLane 空间。
> - 索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §19（GOAL_LOCAL_INDEX_ONLY）。

## 任务

- **论域元素**：宇宙 `Type ℓ-zero`（下称 U）是 HoTT 论域里的元素：它本身是下一层宇宙里的一个类型。
  - 单价性是关于 U 的恒等类型的陈述，所以 HoTT 不能把 U 排除在论域之外。
  - 对照：ZF 把“一切集合的总体”留在论域之外，当作真类。
- **存在性追问的一种读法**：U 作为一个总体，是一件什么样的东西？逐层追问它的成员“以什么方式相同”：两个成员以什么方式相同，这些方式之间又以什么方式相同，如此往上。
- **停机判据**：这个追问在第 m 层停下，当且仅当 U 在第 m 层落定，即 `isOfHLevel m U`。
- **要证的**：对一切 m 都不落定，也就是追问永不停机。

## 命题全文（`UniverseHasNoLevel.agda`）

- **(a) 局部—整体环路原理** `localGlobal`：对任意类型 X 与任意 n，`Ω^(2+n)(U, X) ≃ Π (x : X), Ω^(1+n)(X, x)`。单价性把每个成员内部的相同提升一层，成为宇宙自身的相同。
- **(b) 每一点处都有 ℤ**：
  - `ΩⁿK`：对 K = EM ℤ (1+n)（Eilenberg–MacLane 空间）的每一点 x，`Ω^(1+n)(K, x)` 与 `(ℤ, 0)` 相等（带点类型之间的路径）。
  - 由此得到截面 `sec`，它不等于平凡截面（`secNontrivial`）。
  - n = 0 时，内核由 `refl` 算出它在基点读回 1（`sectionReadsOne`）。
- **(c) 宇宙没有有限层**（C-75）：`universeHasNoLevel : (m : ℕ) → ¬ isOfHLevel m (Type ℓ-zero)`。
- **(d) 每一层的总体都恰好高一层**（C-76）：
  - `gatheringNeverSettled : (k : ℕ) → ¬ isOfHLevel (1+k) (TypeOfHLevel ℓ-zero (1+k))`：命题的总体不是命题（`propsGatherNotProp`），集合的总体不是集合（`setsGatherNotSet`），(3+n) 层落定者的总体不在 3+n 层（`gatheringNotLevel`）；
  - 上界 `gatheringOneUp`（即库的 `isOfHLevelTypeOfHLevel`）：k 层落定者的总体在 1+k 层落定；
  - 对照 `contractiblesSettled`：第 0 层（可缩类型）的总体本身可缩，是唯一落定的总体。

## 这件事说明什么（解释，非机器证明）

- 【解释】按用户的原则，理论可以拒绝别的请求，却不能拒绝自己论域元素的存在性问题。U 是 HoTT 论域的元素，而且单价性需要它在论域里。
- 【解释】按上面的读法，U 的存在性追问永不停机，(c) 是 HoTT 一侧的机器证据。机制是 (a)：单价性把成员内部的相同搬到宇宙上，并高一层；U 里有各种高度的成员（EM 空间），所以没有一层能收住。
- 【解释】对照事实世界：在 UIP 类型论中宇宙是集合（C-72），同一追问在第一层就停。
- 【解释】这是 C-73（罗素面）的完成版：C-73 只证了前两层；(d) 对一切层证明“每个总体都恰好比成员高一层”，(c) 说收集一切类型的那个总体根本没有高度。
- 【解释】与 ℕ 的区别：ℕ 有无穷多个元素，但它是集合，恒等追问在第一层就停。U 的无穷不在元素多，而在相同的层数没有顶。

## 禁止外推

- 不证明 HoTT 不一致。
- “存在性追问 = 逐层追问成员以什么方式相同，并要求停在某一层”是解释桥，也是现实侧前提，待用户裁定。本包只证明 HoTT 一侧：没有一层能停。
- 每一层的非平凡答案来自不同的成员（EM ℤ (1+n)），而每个成员自己那一支的追问在有限层停。宇宙的“永不停机”指没有统一的一层，不是某一个成员的追问无穷；后者的例子如 S² 的全部同伦群，本包不涉及。
- 用的是 Cubical Agda 的宇宙，其中有高阶归纳类型。没有高阶归纳类型时，上升可能要沿宇宙层级走（参见 Kraus–Sattler 2015 关于单价宇宙层级的结果），本包不涉及。
- n = 1 时基点读回的 `refl` 计算在草稿试探中 10 分钟内没有完成，已中止，未纳入；(b)(c)(d) 对一切 n 的证明不依赖它。

## 负控制

`WrongSectionReadsZero.agda` 断言截面在基点读回 0（`refl`）。预期被拒：内核算出 1，`1 != 0`。

## 运行

- 主包：`HoTT/verification/runs/20260926-CG001-UNIVERSE-QUESTIONING-01`。
- 负控制：`HoTT/verification/runs/20260926-CG001-UNIVERSE-QUESTIONING-NEG-01`。
