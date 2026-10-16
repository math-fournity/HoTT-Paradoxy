# A1 延伸：圆的两副面孔（用双表达碰撞法读用户的圆环悖论）

> HUMAN_EDITED；2026-09-24；Claude（Opus 5.5），会话 6fd0312a（用户指令“把下一步的工作都做了”）。
> proof id：`MP-CG001-CIRCLE-TWO-FACES-001`（主包）、`MP-CG001-CIRCLE-TWO-FACES-NEG-001`（负控制）；claims：`CG001-C-21`、`CG001-C-22`。
> 工具链：Agda 2.8.0-3d04bac + cubical 0.9，沿用 `HoTT/formal/dedekind-omega-missile/TOOLCHAIN.json`；源码选项 `--safe --cubical --guardedness`，无公设，不加公理。
> 索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §6（GOAL_LOCAL_INDEX_ONLY）；总入口 `.claude/总索引.md`；对圆环悖论的完整读法见 `.claude/思考与发现/CN-018 - 圆的两副面孔：用户圆环在 HoTT 里一分为二.md`。

## 这个包为什么存在

用户的圆环悖论（原文三，`HoTT/sources/user-originals/Z铁律-抽象-圆环-时间维度-用户原始论述-20260901.md` 第 31 行）要一个圆：既能从上面拿走一个点（得到 M），又能展开成线段（得到 N），再让 N 的两端逼近、复原到 M。HoTT 里有两个“圆”：一个是合成圆 S¹（一个点加一条环路），一个是点集圆（实数平面上的点集，是集合）。本包证明它们不可能是同一个对象：点能被坐标化的类型里没有非平凡的环，有环的 S¹ 上没有坐标，而且从 S¹ 上拿走一个点什么都不剩。点集圆一侧的精确结果由 Astra 的原生证明 C-283–C-324（共享矩阵）承担，本包不重证。

数学内容是 Book 定理 7.2.2、S¹ 的连通性与圈数的标准推论，**不主张原创**。“坐标”“拿走一个点”是解释标签。本包不声称回答了用户的圆环原案 X_h（见 CN-018 的自检）。

## 命题全文

| claim | 命题（量词与假设照实写） | 源码符号 |
|---|---|---|
| **CG001-C-21**（坐标化与环不相容） | 对任意 `A : Type ℓ`、集合 `P : Type ℓ'` 与单射 `f : A → P`（`∀ x y → f x ≡ f y → x ≡ y`）：`isSet A`；对任意 `a : A` 与 `p : a ≡ a`，`p ≡ refl`；不存在 `a`、`p : a ≡ a` 使 `¬ (p ≡ refl)`。证明用 cubical 0.9 的 `reflPropRelImpliesIdentity→isSet`（Book 定理 7.2.2），关系取“坐标相同”。 | `Coordinatized.{coordinatizedIsSet, loopsTrivial, noNontrivialLoop}` |
| **CG001-C-22**（合成圆的一副面孔） | `¬ (loop ≡ refl)`（经 `winding`）；对任意集合 `P`，不存在单射 `f : S¹ → P`；`¬ (Σ[ x ∈ S¹ ] ¬ (base ≡ x))`。负控制：以 `refl` 断言 `loop ≡ refl` 应被内核拒绝。 | `loopNontrivial`、`noCoordinateOnS¹`、`puncturedS¹Empty`；负控制 `WrongTrivialLoop.agda` |

## 禁止外推

- C-21 只说“有单射集合值坐标”的类型；不说点集圆在任何意义下都没有“圈”：点集圆的形状（例如凝聚类型论中的 shape）可以是 S¹，那需要扩展，本包不涉及。
- C-22 的 `puncturedS¹Empty` 与 Astra C-251 是同一个连通性事实，本包只是原生重述，作为两副面孔之一放在一起。
- 本包不证明圆环悖论成立或不成立；点集圆一侧的“复原覆盖需要 Markov 原则”来自 Astra C-319、C-322、C-324，本包未重放那些运行。
