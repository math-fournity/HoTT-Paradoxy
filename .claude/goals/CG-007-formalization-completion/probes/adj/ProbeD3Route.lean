import GodelQ.ZFC.ShCraigElimSetup
/-!
裁决探针 5（**不是收据**）：004-Step 报告的 Foundation 现成 D3 能否接上我们的 `zfcTr_D3_internalize`。

Foundation `DerivabilityCondition/D3.lean`（文件头 `variable (T : ArithmeticTheory) [Theory.Δ₁ T] [𝗣𝗔⁻ ⪯ T]`）：
```
theorem provable_internalize {σ : ArithmeticSentence} :
    Provable T ⌜σ⌝ → Provable T ⌜provabilityPred T σ⌝
```

我们的义务（`Z0Blocked.lean:31`）：
```
Provable 𝗭𝗙𝗖 ⌜translate τ⌝ → Provable 𝗭𝗙𝗖 ⌜translate (zfcTr τ)⌝
```

两端 LHS 同形（Foundation 的 `σ` 取 `translate τ`）。差别在 RHS 的理论：Foundation 是 `T`，
我们是 `𝗭𝗙𝗖`；谓词也不同（`provabilityPred T` vs `zfcTr`）。

本探针逐条核三件事：
  (a) `Theory.Δ₁ Sh` 能否合成；
  (b) `𝗣𝗔⁻ ⊑ Sh` 能否合成；
  (c) `σ ∈ Sh` 与 `Provable 𝗭𝗙𝗖 ⌜translate σ⌝` 是不是一回事（这是 `Sh` 的定义，`Z0Shadow.lean:35`）。
-/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup

namespace GodelQ.ProbeD3Route

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- (c) Sh 的定义：σ ∈ Sh ↔ 𝗭𝗙𝗖 ⊢ translate σ
#check @Sh_provable_iff

-- Foundation 的现成 D3（形状核对）
#check @Bootstrapping.Arithmetic.provable_internalize

-- (a) Theory.Δ₁ Sh
#synth (Sh.RE)

-- (b) 𝗣𝗔⁻ ⊑ Sh
#synth (𝗣𝗔⁻ ⪯ 𝗜𝚺₁)

end GodelQ.ProbeD3Route
