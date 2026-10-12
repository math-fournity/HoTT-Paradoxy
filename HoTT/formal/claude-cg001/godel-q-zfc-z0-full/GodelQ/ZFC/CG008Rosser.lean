import GodelQ.ZFC.CG008Correction

/-!
# CG-008 · Rosser 路线：一条**语言无关**的内部化机制

## 为什么看这条

`RosserProvability.lean` 的 section 变量（读源码）：

```lean
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
variable {L : Language} [L.Encodable] [L.LORDefinable]
variable {T : Theory L} [T.Δ₁]
```

**与 `derivation`/`proof` 同样的通用性**——`L` 任意，只要 `T.Δ₁`。

而它提供的 `rosser_internalize`：

```lean
theorem rosser_internalize [Consistent T] {φ : Sentence L} :
    T ⊢ φ → T.RosserProvable (⌜φ⌝ : V)
```

**注意方向**：前提是**元层** `T ⊢ φ`，结论是 V 内部的 `RosserProvable`。
**这与 `internalize_provability`（D1）同形**——都是「元层 ⟹ 内部」。

**但 `RosserProvable` 的定义是**：

```lean
T.RosserProvable φ ↔ ∃ b : V, Proof T b φ ∧ ∀ b' < b, ¬Proof T b' ⌜∼φ⌝
```

**它内嵌了 `Proof T`**——正是缺口要的东西！
且它的「无更小反证」条件是 **Π₁**（有界全称），所以 `RosserProvable` 是 Δ₁。

## 关键问题

缺口要的是「`Provable 𝗭𝗙𝗖 ⌜translate τ⌝` ⟹ `Provable 𝗭𝗙𝗖 ⌜translate (zfcTr τ)⌝`」，
即**内部 ⟹ 内部**。而 `rosser_internalize` 是**元层 ⟹ 内部**。

**但 `RosserProvable.to_provable`（`RosserProvability.lean:64`）给了**：

```lean
theorem RosserProvable.to_provable {φ : V} : T.RosserProvable φ → Provable T φ
```

**这是元层的**（`→` 在 `Prop` 上）。**若它在 V 内也可证**，则 `RosserProvable` 与
`Provable` 在 V 内等价——那就能用 `rosser_internalize` 造出内部的 `Provable`。

## 本探针要查实

1. `RosserProvable` 对 `T = 𝗭𝗙𝗖`、`L = ℒₛₑₜ` 可陈述；
2. `rosser_internalize` 对 `T = 𝗭𝗙𝗖` 可用（需 `[Consistent 𝗭𝗙𝗖]`）；
3. 缺口能否经此闭合。

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含任何未证标记，可进入收据。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Rosser

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.CG008HBL3
  GodelQ.CG008HBL3Test GodelQ.CG008Final GodelQ.CG008Probe15 GodelQ.CG008Probe16
  GodelQ.CG008Probe17 GodelQ.CG008Probe18 GodelQ.CG008Probe19 GodelQ.CG008Probe20
  GodelQ.CG008Delta1Wall GodelQ.CG008Probe21 GodelQ.CG008CrossLanguage
  GodelQ.CG008InterpretationWall GodelQ.CG008Probe22 GodelQ.CG008Probe23
  GodelQ.CG008CraigRoute GodelQ.CG008CraigBridge GodelQ.CG008PureArith
  GodelQ.CG008Probe24 GodelQ.CG008Probe25 GodelQ.CG008Correction

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1（关键）**：`RosserProvable` 对 `T = 𝗭𝗙𝗖`、`L = ℒₛₑₜ` **可陈述**。

注意它的定义内嵌 `Proof T`——正是缺口要的谓词。 -/
example (φ : V) : Prop := 𝗭𝗙𝗖.RosserProvable φ

-- **查实 2**：`RosserProvable` 的展开（`RosserProvability.lean:60` 的
-- `rosser_quote_def₀`）：
--
--   `T.RosserProvable φ ↔ ∃ b : V, Proof T b φ ∧ ∀ b' < b, ¬Proof T b' ⌜∼φ⌝`
--
-- **它内嵌 `Proof T`，且额外条件是有界全称（Π₁）**，
-- 所以 `RosserProvable` 是 **Δ₁**（比 `Provable` 的 Σ₁ 更强）。
--
-- （展开需要 `rosserProvability` 的 `HTilde` 实例；本行以注释记录。）

-- **查实 3**：`rosser_internalize`——**元层** `T ⊢ φ` ⟹ V 内部 `RosserProvable ⌜φ⌝`。
--
-- 这与 D1 同形（都是元层 ⟹ 内部），**不是**缺口要的内部 ⟹ 内部。
--
-- 类型为：`[Consistent T] {σ : Sentence L} : T ⊢ σ → T.RosserProvable (⌜σ⌝ : V)`。
-- （本行以注释记录；实例化需要 `T.rosserProvability` 的 `HTilde` 实例，
-- 那是 Rosser 谓词的算术表示，与本节结论无关。）

end GodelQ.CG008Rosser
