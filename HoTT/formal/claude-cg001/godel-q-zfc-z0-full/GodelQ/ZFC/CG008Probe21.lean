import GodelQ.ZFC.CG008Delta1Wall

/-!
# CG-008 探针 21（非收据）：`sigma_one_provable_of_models` 能否换成 `T = 𝗭𝗙𝗖`

## 动机

`D3.lean:162`：

```lean
theorem sigma_one_provable_of_models {σ : ArithmeticSentence}
    (hσ : ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 σ) :
    V↓[ℒₒᵣ] ⊧ σ → T.internalize V ⊢ ⌜σ⌝
```

**关键**：`σ` 是**算术**句，结论是 `T.internalize V ⊢ ⌜σ⌝`——
`⌜σ⌝` 是算术码，而 `T.internalize V` 只要 `T : Theory L` + `[T.Δ₁]`。

**若 `T` 可以取 `𝗭𝗙𝗖`**，那么（经 `tprovable_iff_provable`）就得到

```
V ⊨ σ → Provable 𝗭𝗙𝗖 (⌜σ⌝ : V)
```

**这正是缺口需要的那一步！** 缺口的前提 `Provable 𝗭𝗙𝗖 ⌜translate τ⌝`
展开就是 `V ⊨ provable 𝗭𝗙𝗖 (⌜translate τ⌝)`——
而 `provable 𝗭𝗙𝗖` 是 **Σ₁ 句**，所以若上式对 `T = 𝗭𝗙𝗖` 成立，
取 `σ := (provable 𝗭𝗙𝗖).val/[⌜translate τ⌝]` 就直接得到
`Provable 𝗭𝗙𝗖 (⌜(provable 𝗭𝗙𝗖).val/[⌜translate τ⌝]⌝ : V)`。

**剩下的是编码对齐问题**：要把它与缺口的结论
`Provable 𝗭𝗙𝗖 (⌜translate (zfcTr τ)⌝ : V)` 接上，
需要 `translate (zfcTr τ)` 与 `(provable 𝗭𝗙𝗖).val/[⌜translate τ⌝]` 的关系。

## 本探针查实
1. `sigma_one_provable_of_models` 对 `T = 𝗭𝗙𝗖` 能否**陈述**；
2. 若不能，卡在哪一条约束上。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Probe21

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.CG008HBL3
  GodelQ.CG008HBL3Test GodelQ.CG008Final GodelQ.CG008Probe15 GodelQ.CG008Probe16
  GodelQ.CG008Probe17 GodelQ.CG008Probe18 GodelQ.CG008Probe19 GodelQ.CG008Probe20
  GodelQ.CG008Delta1Wall

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1**：`sigma_one_provable_of_models` 的原形——注意 `T` 的类型。

它的 ambient 约束是 `variable {T : ArithmeticTheory} [𝗣𝗔⁻ ⪯ T] [T.SoundOnHierarchy 𝚺 1]`
（`D3.lean` 的 section），**不是** `Theory L`。
所以 `T = 𝗭𝗙𝗖 : Theory ℒₛₑₜ` **不满足**类型。

下面用 `T := 𝗜𝚺₁` 确认这条引理本身工作正常。 -/
example {σ : ArithmeticSentence} (hσ : ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 σ)
    (h : V↓[ℒₒᵣ] ⊧ σ) : 𝗜𝚺₁.internalize V ⊢ ⌜σ⌝ :=
  Bootstrapping.Arithmetic.sigma_one_provable_of_models (T := 𝗜𝚺₁) hσ h

/-- **查实 2（本探针的要点）**：缺口的**结论**需要的形状——
`𝗭𝗙𝗖.internalize V ⊢ ⌜σ⌝`，其中 `σ` 是算术句。

**这一条可以陈述**（`𝗭𝗙𝗖.internalize V` 只要 `[𝗭𝗙𝗖.Δ₁]`，探针 16 查实有），
所以问题**不在陈述**，而在 `sigma_one_provable_of_models` 的**证明**
用了 `T : ArithmeticTheory` 专属的机器（`bold_sigma_one_complete` 的
`toNumVec`、`term_complete`）。

**本探针的结论**：`sigma_one_provable_of_models` 的 ambient 约束是
`variable (T : ArithmeticTheory)`（`D3.lean:14`），而 `𝗭𝗙𝗖 : Theory ℒₛₑₜ`
**不满足**。这不是可以靠改写法绕过的——它的证明依赖算术理论专属的
`term_complete`（项求值完全性）与 `toNumVec`（把自由变量值命名成数字项），
而 `ℒₛₑₜ` 无常项（`CG008GapShape.lean` 已机器确认 `IsEmpty ((ℒₛₑₜ).Func 0)`）。

**即：这条路线把问题精确地还原为「集合语言版本的
`sigma_one_provable_of_models`」，而那正是缺口的原始形状。** -/
example : True := trivial

end GodelQ.CG008Probe21
