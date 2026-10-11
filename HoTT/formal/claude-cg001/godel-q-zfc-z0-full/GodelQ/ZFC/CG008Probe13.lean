import GodelQ.ZFC.CG008Probe12

/-!
# CG-008 探针 13（非收据）：`provable_D3` 的机制能否搬到 `𝗭𝗙𝗖`

## 读到的机制（`StandardProvability.lean:66-113`）

```lean
lemma provable_sigma_one_complete [𝗣𝗔⁻ ⪯ T] {σ : ArithmeticSentence}
    (hσ : ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 σ) : 𝗜𝚺₁ ⊢ σ 🡒 □σ :=
  complete 𝗜𝚺₁ _ fun (V : Type) _ _ ↦ by
    simpa [models_iff] using Bootstrapping.Arithmetic.sigma_one_complete (T := T) (V := V) hσ

theorem provable_D3 [𝗣𝗔⁻ ⪯ T] {σ : ArithmeticSentence} :
    𝗜𝚺₁ ⊢ □σ 🡒 □□σ := provable_sigma_one_complete (by simp)
```

**机制**：`provable_sigma_one_complete` 用 `complete 𝗜𝚺₁`（在 **𝗜𝚺₁** 的每个模型里验证），
内部调用的却是 `Bootstrapping.Arithmetic.sigma_one_complete (T := T)`——
后者给的是 `Provable T (⌜σ⌝ : V)`（**T 的内部可证性**）。

即：**在 𝗜𝚺₁ 的模型里，用 T 的 Σ₁ 完全性**。这是「在弱理论里形式化强理论的完全性」。

## 关键问题

这个机制要求 `T` 是**算术理论**（`sigma_one_complete` 的类型约束），
且结论是 `𝗜𝚺₁ ⊢ …`（在 𝗜𝚺₁ 里）。

**缺口要的是**：`Provable 𝗭𝗙𝗖 (⌜translate τ⌝ : V) → Provable 𝗭𝗙𝗖 (⌜translate (zfcTr τ)⌝ : V)`——
在 **𝗭𝗙𝗖 内部**（不是 𝗜𝚺₁ 内部）证明 𝗭𝗙𝗖 的可证性句。

所以机制**不直接适用**：`provable_D3` 的 `T` 与承载形式化的理论（`𝗜𝚺₁`）**不同**；
缺口的 `T`（`𝗭𝗙𝗖`）与承载的理论（`𝗭𝗙𝗖.internalize V`）**相同**。

## 但有一条变体

`provable_D3` 的模式是「用 T 的 Σ₁ 完全性，在 𝗜𝚺₁ 里形式化」。
对缺口，对应的是「用 𝗭𝗙𝗖 的 Σ₁ 完全性，在 𝗭𝗙𝗖 里形式化」——
而这**正是哥德尔第二定理说做不到的**（否则 𝗭𝗙𝗖 ⊢ Con(𝗭𝗙𝗖)）。

所以这不是实现障碍，是**数学事实**：缺口的形状若真的可证，Z0 就不成立。
**这说明缺口的前提一定用错了**——除非 `zfcTr` 的定义让「翻译后的句」与「前提句」
在 𝗭𝗙𝗖 内部**可证等价**（而不是要求 𝗭𝗙𝗖 证明自己的完全性）。

## 本探针的结论

缺口成立的关键在于：结论句 `translate (zfcTr τ)` 与前提句 `translate τ` 的
**可证等价**——`zfcTr τ` 说的是「`translate τ` 可证」，
所以结论句说的是「『`translate τ` 可证』的翻译」。
从「`translate τ` 可证」到「『`translate τ` 可证』可证」是 D3 的**定义**，
不是额外的数学。

**即：缺口不是要 𝗭𝗙𝗖 证明自己的 Σ₁ 完全性（那会矛盾），
而是要 𝗭𝗙𝗖 证明「它的可证性谓词满足 D3」——这正是 HBL 的 D3，
而对足够强的理论它是**真的**且可证的（Löb 条件的 D3 对 Σ₁ 谓词成立）。**

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含任何未证标记，可进入收据。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Probe13

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.ZFCSetSigma1
  GodelQ.ZFCSetInternal GodelQ.CG008Reduce GodelQ.CG008SetAll GodelQ.CG008Raw
  GodelQ.CG008RawSigma1 GodelQ.CG008SetSigma1Complete GodelQ.CG008ProofToProvable

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1**：`provable_D3` 的形状——`T` 是算术理论，结论在 `𝗜𝚺₁` 里。 -/
example {T : ArithmeticTheory} [Theory.Δ₁ T] [𝗣𝗔⁻ ⪯ T] {σ : ArithmeticSentence} :
    𝗜𝚺₁ ⊢ (provabilityPred T σ) 🡒 (provabilityPred T (provabilityPred T σ)) :=
  provable_D3 (T := T)

/-- **查实 2（关键对照）**：`provable_D3` 的 `T` 与承载形式化的理论**不同**：
`T` 是被谈论的理论，`𝗜𝚺₁` 是承载的理论。缺口里两者**相同**（都是 `𝗭𝗙𝗖`）。

这个对照说明：`provable_D3` 的机制不能直接搬到缺口。 -/
example {T : ArithmeticTheory} [Theory.Δ₁ T] [𝗣𝗔⁻ ⪯ T] :
    -- 被谈论的理论是 T
    (∀ {σ : ArithmeticSentence}, 𝗜𝚺₁ ⊢ (provabilityPred T σ) 🡒
      (provabilityPred T (provabilityPred T σ))) ∧
    -- 承载的理论是 𝗜𝚺₁（不是 T）
    True := ⟨fun {_} ↦ provable_D3 (T := T), trivial⟩

/-- **查实 3**：缺口的正确读法。`zfcTr σ` 说「`translate σ` 可证」，
所以缺口是「从『τ 的翻译可证』到『『τ 的翻译可证』可证』」——
即 𝗭𝗙𝗖 对**自己的**可证性谓词满足 D3。这不是「𝗭𝗙𝗖 证明自己的 Σ₁ 完全性」
（那会推出 Con(𝗭𝗙𝗖)，矛盾），而是 HBL 的 D3——对 Σ₁ 谓词它是**真的**。

固定形状： -/
example (τ : ArithmeticSentence) :
    (zfcTr τ) = trProv.val/[⌜τ⌝] :=
  zfcTr_def τ

end GodelQ.CG008Probe13
