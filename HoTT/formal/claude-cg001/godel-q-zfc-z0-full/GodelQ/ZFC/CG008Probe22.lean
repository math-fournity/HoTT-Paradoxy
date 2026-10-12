import GodelQ.ZFC.CG008InterpretationWall

/-!
# CG-008 探针 22（非收据）：缺口能否化归为**一条**算术句

## 动机

缺口（`CG008HBL3.lean`）是**逐句**的：

```
∀ σ : ArithmeticSentence, 𝗜𝚺₁ ⊢ zfcTr σ 🡒 zfcTr (zfcTr σ)
```

`∀ σ` 是**元层**的（Lean 的 `∀`），不是 `𝗜𝚺₁` 内部的量词。
所以它不是一条 `𝗜𝚺₁` 定理，而是**一族**定理。

**但 Z0 只需要它的一条实例**吗？看 `Z0Full.zfc_z0_full_of_D3_internalize`
的用法：它建的是 `zfcTr.HBL3`，而 `HBL3.D3` 是

```lean
D3 {σ : Sentence L} : T₀ ⊢ 𝔅 σ 🡒 𝔅 (𝔅 σ)
```

**注意 `{σ}` 是隐式的 `∀`，所以 `HBL3` 本身也是元层的逐句族。**
即 `zfc_z0_full` 需要**全部** σ，不能只用一条实例。

**所以这条路线不成立**——除非能证明某个更强的**单句**形式蕴含整个族。

## 本探针要查实

1. `HBL3.D3` 的 `{σ}` 确实是元层全称（不是 `𝗜𝚺₁` 内部量词）；
2. 是否存在「单句版本」——例如 `𝗜𝚺₁ ⊢ ∀¹(□x → □□x)`（**内部**全称）。

第 2 条若有，则缺口可化归为一条句；若无（因为 `□` 吃**元层**的 `Sentence L`），
则缺口**本质上是模式**（schema），不能化为单句。

## 关键障碍（预判）

`provabilityPred T σ` 的定义是 `(provable T).val/[⌜σ⌝]`——
它把**元层的** `σ : Sentence L` 的 Gödel 码代入。
所以 `□x`（`x` 是内部变量）**无法定义**：
`provable T` 吃的是**数**（码），而「数 ⟹ 句子」需要解码，
而解码后的句子才能再编码——这要求 `□` 在内部可表达为「对码的谓词」，
即 `provable T` 本身已经是「码的谓词」。**它确实是**：
`provable T : 𝚺ᴬ₁.Semisentence 1` 吃一个数。

所以内部版本 `∀¹(provable T x → provable T (provable T x))` **可能**可陈述！
关键在于 `provable T (provable T x)` 里内层 `provable T x` 是**项**还是**句**。

- 作为**句**：`provable T x` 是 Σ₁ 句，`provable T` 要它的**码**——
  但 `provable T x` 的码是 `⌜provable T x⌝`，在内部由 `quote` 函数给出；
- 作为**项**：需要 `provable T` 的值（真值），而句的真值不是项。

**所以内部版本要写对**：应该是
`∀¹x, provable T x → provable T ⌜provable T x⌝` 之类，
其中 `⌜·⌝` 是**内部的** quote 函数。

本探针查实 Foundation 是否有这样的内部 quote。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Probe22

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.CG008HBL3
  GodelQ.CG008HBL3Test GodelQ.CG008Final GodelQ.CG008Probe15 GodelQ.CG008Probe16
  GodelQ.CG008Probe17 GodelQ.CG008Probe18 GodelQ.CG008Probe19 GodelQ.CG008Probe20
  GodelQ.CG008Delta1Wall GodelQ.CG008Probe21 GodelQ.CG008CrossLanguage
  GodelQ.CG008InterpretationWall

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1**：`HBL3.D3` 的 `{σ}` 是**元层**全称——它是 Lean 的隐式参数。

所以 `HBL3` 是**一族**定理，不是一个 `𝗜𝚺₁` 句。
`zfc_z0_full` 消费的是整个族。 -/
example (𝔅 : Provability 𝗜𝚺₁ Sh) [𝔅.HBL3] :
    ∀ σ : ArithmeticSentence, 𝗜𝚺₁ ⊢ 𝔅 σ 🡒 𝔅 (𝔅 σ) :=
  fun σ ↦ Provability.D3 (𝔅 := 𝔅) (σ := σ)

/-- **查实 2（关键）**：`provable T` 是**数的谓词**——`𝚺ᴬ₁.Semisentence 1` 吃一个数。

所以「内部版本」是**可陈述的**：内部变量 `x` 就是一个码。 -/
noncomputable example : 𝚺ᴬ₁.Semisentence 1 := provable 𝗭𝗙𝗖

/-- **查实 3（本探针的要点）**：缺口的内部版本要的是
「码 `x` 满足 `provable` ⟹ `provable` 对**该句的码**成立」。

即需要**内部 quote**：把「`provable T x` 这个句」的码算出来。
Foundation 有 `quote`（`Semiformula.quote`）作为**元层**函数，
但内部版本需要它在 V 内可定义（Δ₁/Σ₁ 函数）。

**本探针固定这个待查项**——它是缺口化归为单句的**唯一**可能通道。 -/
example : True := trivial

end GodelQ.CG008Probe22
