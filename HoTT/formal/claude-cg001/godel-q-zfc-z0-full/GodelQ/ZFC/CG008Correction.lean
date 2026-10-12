import GodelQ.ZFC.CG008Probe25

/-!
# CG-008 · 更正 `CG008PureArith.lean` 的一处过强说法

## 我在 `CG008PureArith.lean` 里写了什么

> 「所以缺口完全不涉及 `V↓[ℒₛₑₜ] ⊧ ·`。集合语言的语义、十情形归纳、
> `ℒₛₑₜ` 无常项——**这些都不在缺口的路径上**。」

**前半句对，后半句过强。** 本文件更正。

## 对的部分

缺口的**陈述**确实纯算术：两个句子都是 `Provable 𝗭𝗙𝗖 (⌜·⌝ : V)`，
其中 `⌜·⌝` 是 `GödelNumber ℒₒᵣ (Sentence ℒₛₑₜ)`（一个数），
`Provable`/`Proof` 是算术谓词。**陈述里没有 `V↓[ℒₛₑₜ] ⊧ ·`。**

## 过强的部分

「路径」不是「陈述」。缺口要证的是 D3，而 D3 的标准证法是这样的：

1. `□σ` 是 Σ₁ 句（`provable T : 𝚺ᴬ₁.Semisentence 1`）；
2. **形式化 Σ₁ 完全性**：对 Σ₁ 句 `ψ`，`V ⊨ ψ → V ⊨ □ψ`；
3. 取 `ψ := □σ`，得 `V ⊨ □σ → V ⊨ □(□σ)`——正是 D3。

**第 2 步是引擎。** 对算术理论 `T`，它由 `bold_sigma_one_complete`
（`D3.lean:82`）给出，其证明靠两样东西：

- `term_complete`（`D3.lean:45`）：**项求值完全性**——
  `T.internalize V ⊢ (toNumVec w ⤕ ⌜t⌝) ≐ 𝕹(t.valb w)`；
- `toNumVec`：把 V 的元素 `w` 代换成**数字项** `𝕹(w)`。

**注意 `𝕹(w)` 是 V 内部的数字**——对**非标准**的 `w` 也存在，
所以这条机制对非标准模型也工作。

## 对 `𝗭𝗙𝗖` 为什么这一步难

`□ψ` 对 `𝗭𝗙𝗖` 要换成 `Provable 𝗭𝗙𝗖 (⌜translate ψ⌝ : V)`，
而 `translate` 把算术**项** `t` 映成集合论的**公式**（`arithTrln` 是
`DirectTranslation`，没有项到项的映射）。

**所以 `𝕹(w)` 在集合语言里没有对偶**：集合语言没有常项，
写不出「值为 `w` 的那个项」。这正是 P1 在 `CG008MemCase.lean` 里
定位的 `hMem`/`hNMem` 障碍——**`IsEmpty ((ℒₛₑₜ).Func 0)`**。

**即：P1 的障碍分析是对的**，而且它就是缺口真正的难点；
`CG008PureArith.lean` 说它「不在路径上」是错的。

## 更正后的结论

- 缺口的**陈述**：纯算术（`CG008PureArith.lean` 对）；
- 缺口的**证法**：标准路线要「集合语言的项求值完全性」，
  而 `ℒₛₑₜ` 无常项使这一步没有算术版的对偶（本文件更正）。

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含任何未证标记，可进入收据。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Correction

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.CG008HBL3
  GodelQ.CG008HBL3Test GodelQ.CG008Final GodelQ.CG008Probe15 GodelQ.CG008Probe16
  GodelQ.CG008Probe17 GodelQ.CG008Probe18 GodelQ.CG008Probe19 GodelQ.CG008Probe20
  GodelQ.CG008Delta1Wall GodelQ.CG008Probe21 GodelQ.CG008CrossLanguage
  GodelQ.CG008InterpretationWall GodelQ.CG008Probe22 GodelQ.CG008Probe23
  GodelQ.CG008CraigRoute GodelQ.CG008CraigBridge GodelQ.CG008PureArith
  GodelQ.CG008Probe24 GodelQ.CG008Probe25

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1（对的部分）**：缺口的陈述是纯算术的——`provable 𝗭𝗙𝗖` 是 Σ₁ 句。 -/
noncomputable example : 𝚺ᴬ₁.Semisentence 1 := provable 𝗭𝗙𝗖

/-- **查实 2（过强的部分）**：`term_complete` 是算术版的引擎，
它把 V 的元素 `w` 代换成**数字项** `𝕹 w`（`D3.lean:45`）。

`toNumVec w : SemitermVec V ℒₒᵣ n k` 就是 `(𝕹 ·) ⨟ w`——**逐元素取数字项**。 -/
noncomputable example {n : ℕ} (w : Fin n → V) :
    SemitermVec V ℒₒᵣ n 0 := Bootstrapping.Arithmetic.toNumVec w

/-- **查实 3（更正的关键）**：`ℒₛₑₜ` **没有常项**——
所以 `𝕹(w)`（数字项）在集合语言里没有对偶。

这是 P1 的 `hMem`/`hNMem` 障碍，也是缺口真正的难点。 -/
example : IsEmpty ((ℒₛₑₜ).Func 0) := inferInstance

end GodelQ.CG008Correction
