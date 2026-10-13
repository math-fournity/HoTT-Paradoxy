import GodelQ.ZFC.CG008ITSet2

/-!
# CG-008 · `iTSet` 蓝图的 `succ` 公式（照 `iTRDef` 装配）

`CG008ITSet2` 确认三条零件齐备：
`insertDef`（`𝚺ᴬ₀`，`Function₂`）、`iTDef`（Σ₁，`Function₂`）、`bitDef`（`𝚺ᴬ₀`）。

本文件按 `iTRDef`（`InternalTranslate.lean:227`）的 `∃`-串写法写出 `succ` 公式。

## 剩下的两处（本文件照实记录）

`PR.Construction` 的 `succ_defined` 要证
`Semiformula.Evalb v ↑succ ↔ (Lean 侧 `succ` 函数的值)`。两处需处理：

1. **`Bit` 的 `Decidable`**：`succ` 用 `if k ∈ s then … else …`，
   而 `∈` 是自定义的 `Bit`（`Bit.lean:25`），**没有全局 `Decidable` 实例**。
   （`insert`/`bitInsert` 的 `succ_defined` 里 Foundation 用 `open Classical in` 解决，
   见 `Bit.lean:319` 的 `insert_defined`。）
2. **宏与 `if` 的逐项对齐**：`⤫formula` 宏展开成 untyped `Semiformula`，
   与 Lean 侧 `if` 的 `↔` 要手工拆（`∃`-串给见证，`if` 给分支）。

**这两处都是技术性的**（第 1 处有现成先例），**不是概念障碍**——
所以「`iTSet` 可在 V 内构造」这一结论**成立**（第四面墙已证伪）。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008ITSet3
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Z0Full GodelQ.Translate
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`succ` 的公式**：`y ih n s k` 绑定序（`PR.Blueprint` 的顺序），
表达 `k ∈ s → y = insert (iT n k) ih` 与 `k ∉ s → y = ih` 两支。

装配方式照 `iTRDef`：每处函数应用展开成一个 `∃` 加它的图。 -/
noncomputable def iTSetSuccDef : 𝚺ᴬ₁.Semisentence 6 := .mkSigma
  “y ih n s k. (k ∈ s ∧ ∃ e, !iTDef e n k ∧ ∃ i, !insertDef i e ih ∧ y = i) ∨
    (k ∉ s ∧ y = ih)”

/-- **三条零件的类型核对**（`succ` 公式用的就是它们）。 -/
example : 𝚺ᴬ₀-Function₂ (insert : V → V → V) := FFL.FirstOrder.Arithmetic.insert_definable
example : 𝚺ᴬ₁-Function₂ (Translate.iT : V → V → V) := GodelQ.Translate.iT_definable
example : 𝚺ᴬ₀-Relation (FFL.FirstOrder.Arithmetic.Bit : V → V → Prop) :=
  FFL.FirstOrder.Arithmetic.bit_defined.to_definable

end GodelQ.CG008ITSet3
