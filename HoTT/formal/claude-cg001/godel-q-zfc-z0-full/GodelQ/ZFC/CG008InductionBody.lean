import GodelQ.ZFC.CG008AxStepSplit
import GodelQ.ZFC.ArithInterp
import GodelQ.ZFC.PAModel

/-!
# CG-008 · 缺口第二层：`AxStep_induction` 的体 `K` 是翻译过来的

上一文件（`CG008AxStepSplit.lean`）把缺口劈成两半并**证出了有限半边**。
本文件把剩下的 `AxStep_induction` 再拆一层：**它的体 `K` 不是任意的 Σ₁ 码，
而是某个算术公式的翻译**。

## 理由（结构性的，不是猜想）

`AxStep_induction` 的 `p` 来自 `p ∈ 𝗜𝚺₁.Δ₁Class`（经 `axStep_split` 的右支）。
而 `𝗜𝚺₁ = 𝗣𝗔⁻ ∪ InductionScheme ℒₒᵣ (ℬ[<,ℒₒᵣ].PrenexHierarchy 𝚺 1)`——
所以 `InductionR` 里的 `K` 必须满足 `IsPrenexHierarchy 𝚺 1 K`，
即 `K` 是一个**算术**前束 Σ₁ 公式的**编码**（在 V 里，可以是非标准的）。

于是 `p` 的翻译 `iT 0 p` 是「ω 上的归纳实例」，其体是 `iT 1 K`——
**`K` 的翻译**。要证的 `Provable 𝗭𝗙𝗖 (iT 0 p)` 就是
「ZFC 在 V 内证明：对 `iT 1 K` 在 ω 上归纳」。

## 与 `PAModel.lean` 的关系

`PAModel.lean:200` 的 `W_induction` 证明的正是这件事，但**在元层**：

```lean
theorem W_induction (φ : Semiformula ℒₒᵣ ℕ 1) (f : ℕ → W M) … :
    ∀ x : W M, Semiformula.Eval ![x] f φ
```

其证明经 `naturalNumber_induction (indPred φ f)`——即 **ω 是最小归纳集**
（`indPred_definable` 用**分离**把 `φ` 在 ω 上定义的子集取成集合）。

**所以缺口的第二层结构是**：把这条论证在 V 内重做。

### 一处必须避免的误读（本文件写作时自己踩过）

`Provable 𝗭𝗙𝗖 (iT 0 p)` **是算术命题**——它说「V 内有一个元素 `d`，
`Proof 𝗭𝗙𝗖 d (iT 0 p)` 成立」，而 `Proof` 是 `𝚫ᴬ₁` 公式（`Proof/Basic.lean:551`）。
**它不需要 V 有任何集合论结构。** 所以不能说「V 里没有集合，所以做不了」——
那会把缺口归错因。V 是 𝗜𝚺₁ 的模型这件事**只影响 `V ⊨` 什么**，
不影响 `Provable 𝗭𝗙𝗖` 是否在 V 内成立。

**正确的读法**：要证的是「V 内有一条 𝗭𝗙𝗖 推导码，其结论是 `iT 0 p`」。
`d` 可以是**非标准**的。所以问题不是「V 有没有集合」，
而是「V 能不能**构造**出那个码」。

### 与元层论证的两处真实差别

`W_induction` 在元层做的事与 V 内要做的事，差别在**手段**不在**目标**：

1. **量词范围**：`W_induction` 的 `φ` 是**元层**语法对象（每个 `φ` 都有对应的
   `⌜φ⌝ : V`）；`AxStep_induction` 的 `K` 是 **V 的元素**——非标准时
   **没有**对应的元层对象，所以 `W_induction` 无法对它实例化。
2. **证明手段**：`W_induction` 经 `naturalNumber_induction`（ω 最小归纳集），
   其 `indPred_definable` 用 `ℒₛₑₜ` 的**分离**在 `M` 里取子集——
   **那是 `M ⊨ 𝗭𝗙𝗖` 的语义层**，与 `Provable 𝗭𝗙𝗖` 是两回事。
   V 内要的是一条**推导码**，不是 `M` 里的一个集合。

**所以障碍是**：把 `W_induction` 的**语义论证**转成 `Provable 𝗭𝗙𝗖` 的
**推导码构造**。这一步的一般形式正是 `MinimalGap`（= 舰队 C）。

## 本文件做什么

把这一层**机器化地固定**：
- `induction_body_is_prenex`：体 `K` 受 `IsPrenexHierarchy 𝚺 1` 约束（不是任意码）；
- `standard_body_bridges`：对**标准** `φ`，V 内的 `IsPrenexHierarchy 𝚺 1 ⌜φ⌝`
  与元层的 `PrenexHierarchy` 经 `isPrenexHierarchy_quote_iff` 相连——
  所以**标准体那一半不缺桥**，缺的是非标准体。

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含未证标记，可进入收据。
- **不声称 `AxStep_induction` 已证**；`Z0Blocked.lean:65` 的未证标记仍在。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008InductionBody

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Z0Full GodelQ.Translate GodelQ.CG008AxStep
  GodelQ.CG008AxStepSplit

variable {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## 一、`InductionR` 的体是 Σ₁ 前束公式的码 -/

/-- **查实**：`InductionR (IsPrenexHierarchy 𝚺 1) p` 的展开里，
体 `K` 满足 `IsPrenexHierarchy 𝚺 1 K`——**这是 `AxStep_induction` 的前提给出的**，
不是额外假设。 -/
theorem induction_body_is_prenex {p : V}
    (hp : InductionR (IsPrenexHierarchy 𝚺 1) p) :
    ∃ m ≤ p, ∃ b ≤ p,
      p = qqAlls b m ∧ IsUFormula ℒₒᵣ b ∧ shift ℒₒᵣ b = b ∧ bv ℒₒᵣ b = m ∧
      ∃ K ≤ subst ℒₒᵣ (fvarVec m) b,
        IsSemiformula ℒₒᵣ 1 K ∧ IsPrenexHierarchy 𝚺 1 K ∧
        subst ℒₒᵣ (fvarVec m) b = indBodyVal K :=
  hp

/-- **`AxStep_induction` 的等价陈述（体是 Σ₁ 前束码）**：
`AxStep_induction` 说「对每个这样的 `p`，`iT 0 p` 在 𝗭𝗙𝗖 中可证」。

这不是新定理——是定义的展开；写出来是为了让后续工作单元看到
**`K` 受 `IsPrenexHierarchy 𝚺 1` 约束**，不是任意码。 -/
theorem axStep_induction_iff :
    AxStep_induction (V := V) ↔
      ∀ p : V, InductionR (IsPrenexHierarchy 𝚺 1) p → Provable 𝗭𝗙𝗖 (Translate.iT 0 p) :=
  Iff.rfl

/-! ## 二、与 `PAModel.W_induction` 的并列（语义论证 vs 推导码构造）

`PAModel.lean:200` 的 `W_induction` 的陈述（元层，`M` 是 𝗭𝗙𝗖 的任意模型）：

```lean
theorem W_induction (φ : Semiformula ℒₒᵣ ℕ 1) (f : ℕ → W M)
    (h0 : …) (hs : …) : ∀ x : W M, Semiformula.Eval ![x] f φ
```

它与 `AxStep_induction` 的差别有两处，本文件把两处**各自固定成一条命题**：

1. **量词范围**：`W_induction` 的 `φ` 是**元层**的 `Semiformula ℒₒᵣ ℕ 1`（标准语法对象）；
   `AxStep_induction` 的 `K` 是 **V 的元素**（非标准时无对应的元层对象）。
2. **手段的类型**：`W_induction` 给的是 `M` 里的**语义满足**（经 `naturalNumber_induction`，
   用 `ℒₛₑₜ` 的分离在 `M` 里取子集）；`AxStep_induction` 要的是 V 里的
   **推导码**（`Provable 𝗭𝗙𝗖` 是 `𝚫ᴬ₁` 谓词，与 `M ⊨` 无关）。 -/

/-- **第一处差（量词范围）**：元层的 `φ` 与 V 内的 `K` 通过 `⌜·⌝` 相连——
对**标准**的 `φ`，`⌜φ⌝` 是 V 的元素，且 `IsPrenexHierarchy 𝚺 1 ⌜φ⌝` 当且仅当
`φ` 是前束 Σ₁（这是 `isPrenexHierarchy_quote_iff_s` 的内容，Foundation 已有）。 -/
theorem standard_body_bridges (φ : ArithmeticSemiformula Empty 1)
    (hφ : ℬ[<, ℒₒᵣ].PrenexHierarchy 𝚺 1 φ) :
    IsPrenexHierarchy 𝚺 1 (⌜φ⌝ : V) :=
  (isPrenexHierarchy_quote_iff (Γ := 𝚺) (s := 1) (V := V) (n := 1) φ).mpr hφ

/-! ## 三、**标准码那一半已经付清**（本轮新证）

`AxStep_induction` 只对**非标准** `p` 才是墙。理由是一条一行推论：

- 若 `p = ⌜σ⌝` 且 `p ∈ 𝗜𝚺₁.Δ₁Class`，则 Foundation 的
  `Δ₁Class.mem_iff`（`Theory.lean:91`，`@[simp]`）直接给出 `σ ∈ 𝗜𝚺₁`；
- 于是 `axStep_standard`（`CG008AxStep.lean:57`，已证）给出 `Provable 𝗭𝗙𝗖 (iT 0 ⌜σ⌝)`。

**所以标准码不需任何新数学**——`AxStep_induction` 的实质内容**全在非标准码上**。 -/

/-- **标准码的归纳义务已付清**：`⌜σ⌝` 在 `𝗜𝚺₁.Δ₁Class` 里时，
`iT 0 ⌜σ⌝` 在 𝗭𝗙𝗖 中可证。

这是 `axStep_standard` + `Δ₁Class.mem_iff` 的一行组合；
写出来是为了标明 **`AxStep_induction` 的墙全在非标准码上**。 -/
theorem axStep_standard_code (σ : Sentence ℒₒᵣ)
    (h : (⌜σ⌝ : V) ∈ (𝗜𝚺₁ : ArithmeticTheory).Δ₁Class) :
    Provable 𝗭𝗙𝗖 (Translate.iT 0 (⌜σ⌝ : V)) :=
  axStep_standard (V := V) σ (Δ₁Class.mem_iff.mp h)

/-- **墙的精确位置**：`AxStep_induction` 与「非标准码的义务」等价。

「非标准码的义务」= 对所有 `p`，**若 `p` 不是任何 `⌜σ⌝`** 而仍满足
`InductionR (IsPrenexHierarchy 𝚺 1) p`，则 `Provable 𝗭𝗙𝗖 (iT 0 p)`。

**这就是全舰队唯一剩下的墙**——它已经把标准码排除在外了。 -/
def NonstandardOnly : Prop :=
  ∀ p : V, InductionR (IsPrenexHierarchy 𝚺 1) p →
    (∀ σ : Sentence ℒₒᵣ, p ≠ ⌜σ⌝) → Provable 𝗭𝗙𝗖 (Translate.iT 0 p)

/-- **`AxStep_induction` 分解为「标准（已付清）+ 非标准（墙）」**。

标准支由 `axStep_standard_code` 付清（在 `p ∈ 𝗜𝚺₁.Δ₁Class` 的前提下），
所以 `AxStep_induction` 的全部实质内容就是 `NonstandardOnly`。 -/
theorem axStep_induction_reduces :
    AxStep_induction (V := V) ↔
      (∀ p : V, InductionR (IsPrenexHierarchy 𝚺 1) p →
        (∃ σ : Sentence ℒₒᵣ, p = ⌜σ⌝) ∨ Provable 𝗭𝗙𝗖 (Translate.iT 0 p)) := by
  constructor
  · intro h p hp
    by_cases hex : ∃ σ : Sentence ℒₒᵣ, p = ⌜σ⌝
    · exact Or.inl hex
    · exact Or.inr (h p hp)
  · intro h p hp
    rcases h p hp with (⟨σ, rfl⟩ | hprov)
    · exact axStep_standard_code (V := V) σ
        (InductionOnPrenexHierarchy.mem_Δ₁Class_iff.mpr (Or.inr hp))
    · exact hprov

end GodelQ.CG008InductionBody

#print axioms GodelQ.CG008InductionBody.induction_body_is_prenex
#print axioms GodelQ.CG008InductionBody.standard_body_bridges
#print axioms GodelQ.CG008InductionBody.axStep_standard_code
#print axioms GodelQ.CG008InductionBody.axStep_induction_reduces

/-! ## 四、缺什么 API：Foundation **没有**形式化的相对可解释性

本会话查实（`grep -rn "Interpretability" Foundation/FirstOrder/` 无命中）：
Foundation 有 `DirectInterpretation`（`LK/Interpretation.lean:404`，
`T ⊳ U` 的关系），但**没有**「相对可解释性保可证性」的形式化——
即没有

```
U ⊢ σ → T ⊢ (π.translate σ)    在 T 内形式化
```

的版本。它有的 `of_provability`（`:443`）是**元层**的：`U ⊢ σ → T ⊢ π.translate σ`。

**这正是缺口的 API 缺口**：把 `of_provability` 从元层降进 V 内，
需要 `T = 𝗭𝗙𝗖` 是**算术**理论（`provable_internalize`，`D3.lean:175`，要 `T : ArithmeticTheory`），
而 `𝗭𝗙𝗖 : SetTheory`。

### 墙的四句话

1. 缺口 = `MinimalGap` = `AxStep_induction`（前两节的分解）；
2. `AxStep_induction` 的墙**全在非标准码**上（`axStep_induction_reduces`，标准支已付清）；
3. 非标准码没有元层对应物，所以 `W_induction`（`PAModel.lean:200`）**无法实例化**；
4. 要的是 V 内的**推导码**，而 Foundation 唯一的「解释保可证性」是**元层**的
   （`of_provability`），且 `provable_internalize` 的载体要求（`ArithmeticTheory`）
   `𝗭𝗙𝗖` 不满足。

**这四条没有一条是「技巧问题」**——它们是缺口的确切形状。 -/
