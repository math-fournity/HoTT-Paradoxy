import GodelQ.ZFC.CG008Probe9

/-!
# CG-008 · 集合语言的 `provable_internalize`：照搬算术路线

## 算术版的三步（`D3.lean:162-177`）

```
1. sigma_one_provable_of_models : V ⊨ σ → T.internalize V ⊢ ⌜σ⌝      （内部可证性）
2. sigma_one_complete           : V ⊨ σ → Provable T (⌜σ⌝ : V)        （同一句的 Provable 形式）
3. provable_internalize         : Provable T (⌜σ⌝ : V) → Provable T (⌜provabilityPred T σ⌝ : V)
                                  对 σ := provabilityPred T σ 用第 2 步，因 provabilityPred 是 Σ₁ 句
```

第 3 步的关键：`provabilityPred T σ` 是 **Σ₁ 句**（`(provable T).sigma_prop.rew`），
所以 `sigma_one_complete` 能直接作用在它上面。

## 缺口（探针 9 定型）

```
Provable 𝗭𝗙𝗖 (⌜translate τ⌝ : V) → Provable 𝗭𝗙𝗖 (⌜translate (provabilityPred 𝗭𝗙𝗖 (translate τ))⌝ : V)
```

**与算术版第 3 步同形**，只差 `T : ArithmeticTheory` → `T = 𝗭𝗙𝗖 : Theory ℒₛₑₜ`。

## 本文件要判定的

照搬第 3 步的形状：**能否对 `𝗭𝗙𝗖` 直接陈述并证明对应的 `sigma_one_complete`？**

难点在于：算术版 `sigma_one_complete` 的 `σ` 是 `ArithmeticSentence`（`ℒₒᵣ` 的句），
而这里需要的是**集合句** `translate τ` 的 `provabilityPred`。
`provable 𝗭𝗙𝗖` 本身是 `𝚺ᴬ₁.Semisentence 1`（算术 Σ₁，与 L 无关，见 `Basic.lean:556`），
所以 `provabilityPred 𝗭𝗙𝗖 (translate τ)` 是**算术句**。

**这提示一条可能的路线**：缺口的结论句是集合句，但其**算术核**是
`provabilityPred 𝗭𝗙𝗖 (translate τ)`——一个算术 Σ₁ 句。
若能证「该算术句在 V 中真」（由前提给出），则算术版 `sigma_one_complete`
直接可用，再沿 `translate` 回到集合句。

本文件逐步查实这条路线。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008SetProvInt

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.ZFCSetSigma1
  GodelQ.ZFCSetInternal GodelQ.CG008Reduce GodelQ.CG008SetAll GodelQ.CG008Raw
  GodelQ.CG008RawSigma1

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1**：`provabilityPred 𝗭𝗙𝗖 ψ` 是**算术句**（对任意集合句 ψ）。
因为 `provable 𝗭𝗙𝗖 : 𝚺ᴬ₁.Semisentence 1` 与 `L` 无关。 -/
example (ψ : SetTheorySentence) :
    (provabilityPred 𝗭𝗙𝗖 ψ : ArithmeticSentence) = provabilityPred 𝗭𝗙𝗖 ψ := rfl

/-- **查实 2**：它是 **Σ₁** 句——这正是 `sigma_one_complete` 的前提。 -/
example (ψ : SetTheorySentence) :
    ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 (provabilityPred 𝗭𝗙𝗖 ψ) := by
  rw [provabilityPred]
  exact (provable 𝗭𝗙𝗖).sigma_prop.rew (ω := _)

/-- **查实 3**：因此算术版 `sigma_one_complete` 能作用在它上面——
**但 `T` 必须是算术理论**。这一条用 `𝗜𝚺₁` 作对照确认形状。 -/
example {ψ : SetTheorySentence} (h : V↓[ℒₒᵣ] ⊧ provabilityPred 𝗭𝗙𝗖 ψ) :
    Provable 𝗜𝚺₁ (⌜provabilityPred 𝗭𝗙𝗖 ψ⌝ : V) :=
  Bootstrapping.Arithmetic.sigma_one_complete
    (T := 𝗜𝚺₁) (by rw [provabilityPred]; exact (provable 𝗭𝗙𝗖).sigma_prop.rew (ω := _)) h

/-- **查实 4（关键）**：缺口要的是 `Provable 𝗭𝗙𝗖`，而查实 3 给的是 `Provable 𝗜𝚺₁`。
**两者不是同一个理论**。这正是缺口的所在：
`sigma_one_complete` 的内部化是**在 T 自己内部**做的
（`T.internalize V ⊢ …`），而缺口要在 **𝗭𝗙𝗖 内部**证明 𝗭𝗙𝗖 的可证性句。

本探针到此为止：把「差在哪」固定下来。
-/
example : True := trivial

end GodelQ.CG008SetProvInt
