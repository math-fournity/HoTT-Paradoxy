import GodelQ.ZFC.CG008SetProvInt

/-!
# CG-008 · 集合语言的 Σ₁ 完全性：直接攻击

## 目标（探针 9 定型的缺口形状）

```
Provable 𝗭𝗙𝗖 (⌜translate τ⌝ : V) → Provable 𝗭𝗙𝗖 (⌜translate (provabilityPred 𝗭𝗙𝗖 (translate τ))⌝ : V)
```

## 算术版的机制（`D3.lean`）

`sigma_one_complete (T := T) : V ⊨ σ → Provable T (⌜σ⌝ : V)`，其中
- `σ : ArithmeticSentence` 是 **Σ₁** 句；
- `T : ArithmeticTheory`，`[T.Δ₁]`，`[𝗣𝗔⁻ ⪯ T]`。

证明经 `bold_sigma_one_complete`：对 Σ₁ 结构归纳，十情形，
`hEQ`/`hLT` 用 `term_complete`（项求值完全性），
`hBall`/`hExs` 用 `ball_intro`/`TProof.exs!`。

## 集合版需要什么

1. **`σ` 换成集合句**：`translate τ` 是集合句。但 `sigma_one_complete` 的 `σ` 必须是
   `ArithmeticSentence`（`Semiformula ℒₒᵣ`）。
2. **`T` 换成 `𝗭𝗙𝗖 : Theory ℒₛₑₜ`**：`bold_sigma_one_complete` 的 `T.internalize V ⊢ …`
   只要求 `[T.Δ₁]`，但它的**证明**用了 `numeral_add`/`numeral_lt`/`subst_lt` 等
   算术专属工具。

## 本文件做什么

先做**最小可行的一步**：证 `𝗭𝗙𝗖` 版的 `provable` 是 Σ₁ 句（已有，`CG008SetSigma1`），
然后把缺口的**结论句形状**与 `provabilityPred` 精确对上，
最后固定「还差什么」。

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含任何未证标记，可进入收据。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008SetSigma1Complete

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.ZFCSetSigma1
  GodelQ.ZFCSetInternal GodelQ.CG008Reduce GodelQ.CG008SetAll GodelQ.CG008Raw
  GodelQ.CG008RawSigma1

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## 1. 缺口的结论句 = 一个算术 Σ₁ 句的翻译

探针 9 说：缺口结论句是 `⌜translate (provabilityPred 𝗭𝗙𝗖 (translate τ))⌝`。
内层 `provabilityPred 𝗭𝗙𝗖 (translate τ)` 是**算术句**（`provable 𝗭𝗙𝗖` 与 L 无关）。 -/

/-- **结论句的内层是算术句**。 -/
theorem conclusion_core_is_arithmetic (τ : ArithmeticSentence) :
    (provabilityPred 𝗭𝗙𝗖 (arithTrln.translate τ) : ArithmeticSentence) =
      provabilityPred 𝗭𝗙𝗖 (arithTrln.translate τ) := rfl

/-- **它是 Σ₁ 句**——`sigma_one_complete` 的前提。 -/
theorem conclusion_core_sigma1 (τ : ArithmeticSentence) :
    ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 (provabilityPred 𝗭𝗙𝗖 (arithTrln.translate τ)) := by
  rw [provabilityPred]
  exact (provable 𝗭𝗙𝗖).sigma_prop.rew (ω := _)

/-! ## 2. 缺口的两端都是「V 内部可证性」

按 `CG008Reduce.provable_iff_internal`，缺口等价于内部演算形状。
把两端都写成内部演算，缺口就是：

```
𝗭𝗙𝗖.internalize V ⊢ ⌜translate τ⌝ → 𝗭𝗙𝗖.internalize V ⊢ ⌜translate (provabilityPred 𝗭𝗙𝗖 (translate τ))⌝
```

**注意**：`𝗭𝗙𝗖.internalize V` 是「V 内部的 ZFC 推导」。
所以这一步要在 **ZFC 内部**证明「`translate τ` 可证 ⟹ 它的可证性句可证」——
这正是 D3，也正是 ZFC 无法对任意 τ 证明的东西（否则 ZFC ⊢ Con(ZFC)）。

## 3. 关键分辨：D3 不是「反射原理」

`Z0Blocked.lean` 文档第 16-18 行说 `zfcTr_D3_syntactic : 𝗭𝗙𝗖 ⊢ translate τ 🡒 translate (zfcTr τ)`
不是 ZFC 定理——那是对的，**但缺口的形状不是它**。

缺口是 `Provable 𝗭𝗙𝗖 ⌜translate τ⌝ → Provable 𝗭𝗙𝗖 ⌜…⌝`，
**前提取的是 `Provable 𝗭𝗙𝗖`（V 内部有一条推导）**，不是「`translate τ` 为真」。
从「V 内部有一条 `translate τ` 的推导」造出「V 内部有一条『它可证』的推导」——
这是 Σ₁ 完全性（真 Σ₁ 句可证），而**不是**反射原理（真句可证）。

区别的关键：前提给的是**推导的存在**（一个 V 的元素），
而 D3 要的是把这个存在**编码**成可证性句的证明。这正是 HBL 的 D3。

## 4. 因此需要的是

`bold_sigma_one_complete` 的**集合语言对偶**，且 `T = 𝗭𝗙𝗖`：

对 Σ₁ **集合句** `ψ`，从 `V↓[ℒₛₑₜ] ⊧ ψ` 造出 `𝗭𝗙𝗖.internalize V ⊢ ⌜ψ⌝`。

但缺口的前提不是 `V ⊨ ψ` 而是 `Provable 𝗭𝗙𝗖 ⌜ψ⌝`——这两者在 V 内部**等价**吗？
在 V 内部，`Provable 𝗭𝗙𝗖 ⌜ψ⌝` 给出一个见证 `d`，而 `d` 编码了一条推导。
要把它变成 `⌜provabilityPred⌝` 的证明，需要 V 内部**对推导做归纳**——
即证明「若 `d` 是一条推导，则 `provable 𝗭𝗙𝗖 ⌜结论⌝` 成立」。

**这就是缺口的最终形状**：V 内部对 `Derivation` 谓词的归纳。
`Derivation` 是 Δ₁（`derivation T : 𝚫ᴬ₁.Semisentence 1`），
所以这个归纳是 Δ₁ 归纳——`𝗜𝚺₁` **能**做，但要在**集合语言的 `provable 𝗭𝗙𝗖`** 下做。

## 治理

- 本文件不含任何未证标记，可进入收据。
-/

end GodelQ.CG008SetSigma1Complete
