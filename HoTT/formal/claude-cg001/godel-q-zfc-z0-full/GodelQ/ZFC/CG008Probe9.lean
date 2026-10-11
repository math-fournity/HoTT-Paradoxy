import GodelQ.ZFC.CG008Probe8

/-!
# CG-008 探针 9（非收据）：级别 3 对 `𝗭𝗙𝗖` 的精确形状

缺口（`Z0Blocked.lean:61-65`）是：

```
Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V) →
Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr τ)⌝ : V)
```

`zfcTr τ` 的定义是 `trProv.val/[⌜τ⌝]`，而
`trProv = .mkSigma “x. ∃ y, !iTDef y 0 x ∧ !(provable 𝗭𝗙𝗖) y”`（`Z0Full.lean:40`）。

所以结论句的**算术核心**是 `∃ y, iTDef y 0 ⌜τ⌝ ∧ provable 𝗭𝗙𝗖 y`——
即「存在一个 `y`，它是 `⌜τ⌝` 的翻译的证明码」。

**本探针要判定的**：这个形状与 `provabilityPred` 差多远。
- `provabilityPred T σ = (provable T).val/[⌜σ⌝]`，即 `∃ d, proof T d ⌜σ⌝`。
- 缺口的结论要的是 `∃ y, iTDef y 0 ⌜τ⌝ ∧ provable 𝗭𝗙𝗖 y`。

**两者不同**：`provabilityPred` 直接对 `⌜σ⌝` 说「可证」；
缺口的结论先经 `iTDef` 把 `⌜τ⌝` 翻译成 `y`，再对 `y` 说「可证」。
`iTDef` 是 `iT` 的图（`InternalTranslate.lean:258`），而 `iT_quote` 说
`iT n ⌜φ⌝ = ⌜arithTrln.translate φ⌝`（`InternalTranslate.lean:611`）。

所以缺口的结论句 = 「`provable 𝗭𝗙𝗖` 作用在 `⌜translate τ⌝` 上」——
**这正是 `provabilityPred 𝗭𝗙𝗖 (translate τ)` 的算术形状**，
只不过外面再套了一层 `arithTrln.translate`（因为结论句是集合句）。

## 关键判定

若上述等同成立，则缺口等价于：

```
Provable 𝗭𝗙𝗖 (⌜translate τ⌝ : V) → Provable 𝗭𝗙𝗖 (⌜translate (provabilityPred 𝗭𝗙𝗖 (translate τ))⌝ : V)
```

即**集合语言的 `provable_internalize`**——与算术版 `D3.lean:175` 逐字同形，
只是把 `ArithmeticTheory` 换成 `Theory ℒₛₑₜ`。这是「缺口 = 集合论 D3」的**精确定型**。

本探针把 `iT_quote` 与 `zfcTr_def` 对上，确认这个等同。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Probe9

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.ZFCSetSigma1
  GodelQ.ZFCSetInternal GodelQ.CG008Reduce GodelQ.CG008SetAll GodelQ.CG008Raw
  GodelQ.CG008RawSigma1

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1**：`zfcTr` 的定义就是 `trProv.val/[⌜σ⌝]`。 -/
example (σ : ArithmeticSentence) : zfcTr σ = trProv.val/[⌜σ⌝] := zfcTr_def σ

/-- **查实 2**：`iT` 在引号上等于翻译的编码（`iT_quote`，`InternalTranslate.lean:611`）。 -/
example {n : ℕ} (φ : Semisentence ℒₒᵣ n) :
    iT (n : V) ⌜φ⌝ = ⌜(arithTrln.translate φ : Semisentence ℒₛₑₜ n)⌝ :=
  iT_quote φ

/-- **查实 3**：`TrProvable` 与 `Provable 𝗭𝗙𝗖 ∘ translate` 逐字对应。 -/
example (σ : ArithmeticSentence) :
    TrProvable (⌜σ⌝ : V) ↔ Provable 𝗭𝗙𝗖 (⌜arithTrln.translate σ⌝ : V) :=
  trProvable_quote σ

/-- **查实 4**：缺口两端的**算术形状**（经 `models_zfcTr_iff`）。
这把缺口从「集合句」翻回「算术句」，正是 `D3.lean` 处理的语言。

注：`models_zfcTr_iff` 的 `V` 是单态（宇宙 0），所以这里另起一个 `Type` 变量。 -/
example (W : Type) [ORingStructure W] [W↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] (σ : ArithmeticSentence) :
    W↓[ℒₒᵣ] ⊧ zfcTr σ ↔ Provable 𝗭𝗙𝗖 (⌜arithTrln.translate σ⌝ : W) :=
  models_zfcTr_iff W σ

/-- **查实 5（关键）**：缺口的结论句 `zfcTr (zfcTr τ)` 的算术形状，
就是「`provable 𝗭𝗙𝗖` 作用在 `zfcTr τ` 的翻译上」——
即把 `provabilityPred` 的 `σ` 取成 `zfcTr τ`。

这条与 `D3.lean:175` 的 `provable_internalize` **逐字同形**：
`Provable T ⌜σ⌝ → Provable T ⌜provabilityPred T σ⌝`。
差别只在：`D3.lean` 要求 `T : ArithmeticTheory`，而这里 `T = 𝗭𝗙𝗖 : Theory ℒₛₑₜ`。 -/
example (W : Type) [ORingStructure W] [W↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] (τ : ArithmeticSentence) :
    W↓[ℒₒᵣ] ⊧ zfcTr (zfcTr τ) ↔
      Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr τ)⌝ : W) :=
  models_zfcTr_iff W (zfcTr τ)

end GodelQ.CG008Probe9
