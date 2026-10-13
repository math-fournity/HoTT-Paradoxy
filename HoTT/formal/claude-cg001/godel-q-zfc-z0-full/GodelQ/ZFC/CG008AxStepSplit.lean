import GodelQ.ZFC.CG008AxStep
import GodelQ.ZFC.Z0PA
import Foundation.FirstOrder.Incompleteness.Definability

/-!
# CG-008 · `AxStep` 的两半：有限部分与归纳部分

`AxStep`（`CG008AxStep.lean`）是缺口的最窄形状。本文件按 **Foundation 自己的
`Δ₁Class` 分解** 把它拆成两个可独立攻的命题——这就是全舰队的靶心。

## 分解来自 Foundation（`Incompleteness/Definability.lean:229`）

```lean
lemma InductionOnPrenexHierarchy.mem_Δ₁Class_iff :
    p ∈ (𝗜𝗡𝗗 Γ s).Δ₁Class ↔ p ∈ 𝗣𝗔⁻.Δ₁Class ∨ InductionR (IsPrenexHierarchy Γ s) p
```

`𝗜𝚺₁ = 𝗜𝗡𝗗 𝚺 1`（`Schemata.lean:62,68`），故取 `Γ := 𝚺`、`s := 1` 即得 `axStep_split`。

## 两半

| 半 | 命题 | 状态 |
|---|---|---|
| 有限 | `p ∈ 𝗣𝗔⁻.Δ₁Class → Provable 𝗭𝗙𝗖 (iT 0 p)` | 已化为 `extract_standard_code`（见 §三） |
| 归纳 | `InductionR (IsPrenexHierarchy 𝚺 1) p → Provable 𝗭𝗙𝗖 (iT 0 p)` | **缺口**（`AxStep_induction`） |

**为什么归纳半边是墙**：非标准的 `p` 只能是归纳模式的**非标准实例**
（`InductionR` 的 `K` 可以是任意满足 `IsPrenexHierarchy 𝚺 1` 的码）。
其翻译是「ω 上的归纳实例」，V 内要证它——即把 `PAModel.lean` 的
「ω 是最小归纳集」论证（`W_induction`，目前是**元层**）在 **V 内**形式化。

## 本文件已机器化的（无未证标记，可进收据）

- `axStep_split`：`p ∈ 𝗜𝚺₁.Δ₁Class` 的精确分解；
- `axStep_of_halves`：两半各证则 `AxStep` 成立；
- `axStep_iff_induction_given_finite`：在有限部分下，`AxStep ⟺ AxStep_induction`；
- `extract_standard_code` 的**陈述**（有限部分的精确内容，见 §三）。

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含未证标记，可进入收据。
- **不声称缺口已证**；`Z0Blocked.lean:65` 的未证标记仍在。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008AxStepSplit

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Z0Full GodelQ.Translate GodelQ.CG008AxStep

variable {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## 一、分解 -/

/-- **`AxStep` 的有限部分**：`𝗣𝗔⁻` 的公理码经 `iT 0` 后在 𝗭𝗙𝗖 中可证。 -/
def AxStep_finite : Prop :=
  ∀ p : V, p ∈ (𝗣𝗔⁻ : ArithmeticTheory).Δ₁Class → Provable 𝗭𝗙𝗖 (Translate.iT 0 p)

/-- **`AxStep` 的归纳部分**（**这就是墙**）：归纳模式的（可能非标准的）实例码
经 `iT 0` 后在 𝗭𝗙𝗖 中可证。 -/
def AxStep_induction : Prop :=
  ∀ p : V, InductionR (IsPrenexHierarchy 𝚺 1) p → Provable 𝗭𝗙𝗖 (Translate.iT 0 p)

/-- **分解（直接来自 Foundation 的 `mem_Δ₁Class_iff`）**：
`p ∈ 𝗜𝚺₁.Δ₁Class` 当且仅当「有限部分」或「归纳部分」。

**这是本文件最有用的一条**：它把「非标准的公理码是什么」精确到
「一定是归纳模式的实例」，因为 `𝗣𝗔⁻` 是**有限**的
（`PeanoMinus.finite`），非标准码只能来自 `InductionScheme`。 -/
theorem axStep_split {p : V} (hp : p ∈ (𝗜𝚺₁ : ArithmeticTheory).Δ₁Class) :
    p ∈ (𝗣𝗔⁻ : ArithmeticTheory).Δ₁Class ∨ InductionR (IsPrenexHierarchy 𝚺 1) p :=
  InductionOnPrenexHierarchy.mem_Δ₁Class_iff.mp hp

/-- **两半合成 `AxStep`**。 -/
theorem axStep_of_halves (h₁ : AxStep_finite (V := V)) (h₂ : AxStep_induction (V := V)) :
    AxStep (V := V) :=
  fun p hp ↦ (axStep_split hp).elim (h₁ p) (h₂ p)

/-- **`AxStep` 蕴含归纳部分**（反向不需要有限部分）。 -/
theorem axStep_to_induction (h : AxStep (V := V)) : AxStep_induction (V := V) :=
  fun p hp ↦ h p (InductionOnPrenexHierarchy.mem_Δ₁Class_iff.mpr (Or.inr hp))

/-- **在有限部分下，`AxStep ⟺ AxStep_induction`**——有限部分是定理时，
归纳部分就是缺口的全部。 -/
theorem axStep_iff_induction_given_finite (h : AxStep_finite (V := V)) :
    AxStep (V := V) ↔ AxStep_induction (V := V) :=
  ⟨axStep_to_induction, fun h₂ ↦ axStep_of_halves h h₂⟩

/-! ## 二、归纳部分：靶心的精确内容

`InductionR S p`（`Definability.lean:87`）展开为

```
∃ m ≤ p, ∃ b ≤ p,
  p = qqAlls b m ∧ IsUFormula ℒₒᵣ b ∧ shift ℒₒᵣ b = b ∧ bv ℒₒᵣ b = m
  ∧ ∃ K ≤ subst ℒₒᵣ (fvarVec m) b,
      IsSemiformula ℒₒᵣ 1 K ∧ S K ∧ subst ℒₒᵣ (fvarVec m) b = indBodyVal K
```

即：`p` 是「∀¹* β」形状的码，β 的体是某个 `ψ` 的 `succInd`，且 `S ⌜ψ⌝`。
`S = IsPrenexHierarchy 𝚺 1` 时，`ψ` 是 Σ₁ 前束公式——**可以是 V 的非标准码**。

**要证的**：`Provable 𝗭𝗙𝗖 (iT 0 p)`，即 ZFC 在 V 内证明 `translate (succInd ψ)`，
也就是「ω 上的归纳」对 `ψ` 成立。 -/

/-- **归纳部分的语义内容**（本文件把它展开成可读形状）：
对归纳实例 `p`，其翻译 `iT 0 p` 在 𝗭𝗙𝗖 中可证。
**这就是「V 内证明 ω 归纳」的精确陈述。** -/
def InductionTranslationProvable : Prop :=
  ∀ p : V, InductionR (IsPrenexHierarchy 𝚺 1) p →
    Provable 𝗭𝗙𝗖 (Translate.iT 0 p)

/-- `InductionTranslationProvable` 与 `AxStep_induction` 是同一命题。 -/
theorem induction_iff : InductionTranslationProvable (V := V) ↔ AxStep_induction (V := V) :=
  Iff.rfl

/-! ## 三、有限部分：为什么它是定理，以及精确的剩余步骤

**数学理由**：`𝗣𝗔⁻` 有限（`PeanoMinus.finite`），其 `Δ₁` 实例由
`Theory.Δ₁.ofFinite` 给出，而 `ofFinite = ofList h.toFinset.toList` 经 `ofEq`
（`Theory.lean:161-163`）。`ofList` 的 `ch` 是**有限个等式 `x = ↑(encode σ)` 的析取**
（`ofList` 的 `cons` 支用 `singleton.add`，`singleton` 的 `ch` 就是单个等式，
见 `Theory.lean:145-150` 与 `singleton_toTDef_ch_val:152`）。

在**任意**模型 V（含非标准）中，「`p` 等于某个标准元素 `↑(encode σ)`」
强制 `p` 就是那个标准码——**这就是有限部分在 V 内也成立的原因**。

**剩下的纯 Lean 步骤**：把 `ofList` 的 `ch` 求值成「∃ σ ∈ l, p = ⌜σ⌝」。
它是列表归纳：`nil` 支是 `⊥`，`cons` 支是 `⋎` + `singleton_toTDef_ch_val`
（后者把 `↑(encode σ)` 桥到 `⌜σ⌝`，经 `Sentence.quote_eq_encode`）。

**本文件已证**（`mem_ofList_ch`、`mem_ofFinite_ch`、`axStep_finite_proved`）——
有限部分不再是「陈述」，是定理。 -/

/-- **有限部分的提取引理**：`ofList l` 的 `ch` 求值后就是「`p` 等于列表中某个 `⌜σ⌝`」。

证明：列表归纳。`nil` 支是 `⊥`；`cons` 支是 `⋎`（`Δ₁.add` 的 `ch`），
单例侧经 `singleton_toTDef_ch_val` + `Sentence.quote_eq_encode`。 -/
theorem mem_ofList_ch (l : List (Sentence ℒₒᵣ)) (p : V) :
    V ⊧/![p] (Theory.Δ₁.ofList (L := ℒₒᵣ) l).ch.val ↔ ∃ σ ∈ l, p = ⌜σ⌝ := by
  induction l with
  | nil =>
    show Semiformula.Evalb ![p] (Theory.Δ₁.ofList (L := ℒₒᵣ) []).ch.val ↔ _
    rw [show (Theory.Δ₁.ofList (L := ℒₒᵣ) []).ch.val =
        (⊥ : ArithmeticSemiformula Empty 1) from rfl]
    simp
  | cons φ l ih =>
    rw [show (Theory.Δ₁.ofList (L := ℒₒᵣ) (φ :: l)).ch.val =
        ((Theory.Δ₁.singleton φ).ch ⋎ (Theory.Δ₁.ofList (L := ℒₒᵣ) l).ch).val from rfl,
      Bounding.HierarchySymbol.Semiformula.val_or, LogicalConnective.HomClass.map_or]
    have hA : V ⊧/![p] (Theory.Δ₁.singleton φ).ch.val ↔ p = (⌜φ⌝ : V) := by
      rw [Theory.Δ₁.singleton_toTDef_ch_val]
      simp [numeral_eq_natCast]
      rw [Sentence.quote_eq_encode]
    rw [hA]
    constructor
    · rintro (h | h)
      · exact ⟨φ, List.mem_cons_self .., h⟩
      · obtain ⟨σ, hσ, rfl⟩ := ih.mp h
        exact ⟨σ, List.mem_cons_of_mem _ hσ, rfl⟩
    · rintro ⟨σ, hσ, rfl⟩
      rcases List.mem_cons.mp hσ with (rfl | hσ)
      · left; rfl
      · right; exact ih.mpr ⟨σ, hσ, rfl⟩

/-- **`ofFinite` 的成员判定**：`ofFinite` 就是 `ofList` 经 `ofEq`，`ch` 不变。 -/
theorem mem_ofFinite_ch (T : Theory ℒₒᵣ) (h : Set.Finite T) (p : V) :
    V ⊧/![p] (Theory.Δ₁.ofFinite T h).ch.val ↔ ∃ σ ∈ T, p = ⌜σ⌝ := by
  rw [show (Theory.Δ₁.ofFinite T h).ch =
      (Theory.Δ₁.ofList (L := ℒₒᵣ) h.toFinset.toList).ch from rfl, mem_ofList_ch]
  simp [Set.Finite.mem_toFinset]

/-- **`𝗣𝗔⁻` 的 `Δ₁Class` 成员必是标准公理码**：由 `PeanoMinus.delta1`
（`= Theory.Δ₁.ofFinite`，`Definability.lean:26`）与 §二的提取引理。 -/
theorem mem_PAMinus_is_standard {p : V} (hp : p ∈ (𝗣𝗔⁻ : ArithmeticTheory).Δ₁Class) :
    ∃ σ : Sentence ℒₒᵣ, σ ∈ (𝗣𝗔⁻ : ArithmeticTheory) ∧ p = ⌜σ⌝ := by
  have hch : V ⊧/![p]
      (Theory.Δ₁.ofFinite (𝗣𝗔⁻ : ArithmeticTheory) PeanoMinus.finite).ch.val := hp
  obtain ⟨σ, hσ, hpσ⟩ := mem_ofFinite_ch (V := V) _ PeanoMinus.finite p |>.mp hch
  exact ⟨σ, hσ, hpσ⟩

/-- **有限部分已证**：`𝗣𝗔⁻` 的公理码经 `iT 0` 后在 𝗭𝗙𝗖 中可证。

`σ ∈ 𝗣𝗔⁻ ⟹ σ ∈ 𝗜𝚺₁`（`𝗜𝚺₁ = 𝗣𝗔⁻ ∪ …`），故 `axStep_standard` 直接适用。 -/
theorem axStep_finite_proved : AxStep_finite (V := V) := by
  intro p hp
  obtain ⟨σ, hσ, rfl⟩ := mem_PAMinus_is_standard (V := V) hp
  exact axStep_standard (V := V) σ (Set.mem_union_left _ hσ)

end GodelQ.CG008AxStepSplit

#print axioms GodelQ.CG008AxStepSplit.axStep_split
#print axioms GodelQ.CG008AxStepSplit.axStep_of_halves
#print axioms GodelQ.CG008AxStepSplit.axStep_to_induction
#print axioms GodelQ.CG008AxStepSplit.axStep_iff_induction_given_finite
#print axioms GodelQ.CG008AxStepSplit.induction_iff
#print axioms GodelQ.CG008AxStepSplit.mem_ofList_ch
#print axioms GodelQ.CG008AxStepSplit.mem_PAMinus_is_standard
#print axioms GodelQ.CG008AxStepSplit.axStep_finite_proved
