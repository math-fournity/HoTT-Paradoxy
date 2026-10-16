# 有限的收集也合不上：所有二元集合按相同归并，计数为一，收集本身却不落定（C-74）

> HUMAN_EDITED；2026-09-26；Claude（Opus 5.5），会话 7f138325。与 C-73 同包，是它的有限版本，用来排除罗素本身的大小问题。
>
> 起因同 C-73：用户【原话】“我们是否可以参考罗素悖论来构造必须完成的‘追问’呢？”
>
> - proof id：`MP-CG001-COPIES-OF-BOOL-001`（`CopiesOfBool.agda`）。
> - 负控制：`MP-CG001-COPIES-OF-BOOL-NEG-001`（`WrongSwapStays.agda`）。
> - claim：`CG001-C-74`。
> - 工具链：Agda 2.8.0-3d04bac + cubical 0.9，`--safe --cubical --guardedness`，无公设。
> - 索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §18（GOAL_LOCAL_INDEX_ONLY）。

## 为什么要有有限版本

在用户对罗素的读法里，“收集一切集合”本身就是完成不了的过程（KC-000016）。C-73 用到“一切 n 层类型的总体”，不免牵涉宇宙的大小。本包只收集与 Bool 相同的东西，不涉及“一切集合”，所以罗素、Girard 的大小围栏在这里不起作用。

## 命题全文（`CopiesOfBool.agda`）

- `CopiesOfBool = Σ[ X ∈ Type ] ∥ X ≃ Bool ∥₁`：所有（仅存在性地）与 Bool 等价的类型。
- **(a)** `oneUpToSameness : isContr ∥ CopiesOfBool ∥₂`：按相同计数，二元集合恰好只有一个。
- **(b)** `gatheringNotSettled : ¬ isSet CopiesOfBool`：单价性把 Bool 的交换变成收集中的一个环 `swapLoop`；沿它搬运 `true` 得 `false`（`swapMoves`，`refl` 算出），所以它不是 `refl`。

## 这件事说明什么（解释，非机器证明）

- 【解释】问“把相同的归并，二元集合有几个”，HoTT 与事实世界都答“一个”。但在事实世界里，这个“一个”就是一个落定的点；在 HoTT 里，这个“一个”仍带着“Bool 以两种方式中的哪一种与自己相同”的问题，没有落定。
- 【解释】所以罗素式的上升（C-73）并不依赖“一切集合”这样的大总体：只要按单价性把相同的东西归并，收集就比成员少落定一层。上升的来源是单价性，不是大小。
- 【解释】这把现实一侧的裁定变得具体：把所有二元集合按相同归并，得到的是一个落定的点，还是一个带着自身两种认同的东西？

## 禁止外推

- 不证明 HoTT 不一致；只涉及 Bool，不作一般断言（一般地，收集与 A 相同者得到 A 的自同构的分类空间，是已知事实，本包只证 Bool 的情形）。

## 负控制

`WrongSwapStays.agda` 断言沿 `swapLoop` 搬运 `true` 仍得 `true`（`refl`）。预期被拒：`false != true`。

## 运行

- 主包：`HoTT/verification/runs/20260926-CG001-COPIES-OF-BOOL-01`。
- 负控制：`HoTT/verification/runs/20260926-CG001-COPIES-OF-BOOL-NEG-01`。
