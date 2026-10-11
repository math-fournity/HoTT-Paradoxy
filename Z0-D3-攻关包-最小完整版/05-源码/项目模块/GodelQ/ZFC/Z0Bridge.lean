import GodelQ.ZFC.Z0Full

/-!
# CG-007 · W8 续：把 D3 收成一条内部解释引理

`Z0Blocked.zfcTr_D3_internalize` 说的是：在任意 𝗜𝚺₁ 模型 V 中，
若 𝗭𝗙𝗖 证明了算术句 τ 的集合论翻译，则 𝗭𝗙𝗖 也证明
“𝗭𝗙𝗖 证明了该翻译”这句算术话的翻译。

本文件不证明那条引理，也不证明 `Z0Blocked` 里宇宙多态的原陈述。
它证明一个归约，宇宙取 `Type`，与 `zfc_z0_full_of_D3_internalize` 的前提一致：

* `zfcTr τ` 是 Σ1 算术句，而且 `V ⊧ zfcTr τ` 正好是假设；
* Foundation 的 `sigma_one_complete` 因此给出
  `Provable 𝗜𝚺₁ (⌜zfcTr τ⌝ : V)`，这是 V 内部的算术证明编码；
* 还缺的只是：把这个编码沿 `arithTrln` 变成 V 内部的 𝗭𝗙𝗖 证明编码。

Foundation 的 `DirectInterpretation.of_provability`（`LK/Interpretation.lean`）
只把**外部**推导经完备性变成另一条外部推导，不产生非标准模型 V 里的证明编码。
所以它不能填这个桥。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.Z0Bridge

open GodelQ.Z0Full GodelQ.ZFCArith

/-- **归约**。`bridge` 是尚未证明的内部解释：
每个 𝗜𝚺₁ 模型里，一条 Σ1 算术句的内部证明编码都能变成
它沿 `arithTrln` 的翻译在 𝗭𝗙𝗖 中的内部证明编码。
在这个前提下，C-122 所消费的 `Type` 层 D3 形状成立。 -/
theorem zfcTr_D3_internalize_of_sigma1_bridge
    (bridge :
      ∀ {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
        {σ : ArithmeticSentence},
        ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 σ →
        Provable 𝗜𝚺₁ (⌜σ⌝ : V) →
        Provable 𝗭𝗙𝗖 (⌜arithTrln.translate σ⌝ : V))
    {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    (τ : ArithmeticSentence)
    (h : Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V)) :
    Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr τ)⌝ : V) := by
  have hσ : ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 (zfcTr τ) := zfcTr_sigma1 τ
  have hv : V↓[ℒₒᵣ] ⊧ zfcTr τ := (models_zfcTr_iff V τ).mpr h
  have hI : Provable 𝗜𝚺₁ (⌜zfcTr τ⌝ : V) :=
    Bootstrapping.Arithmetic.sigma_one_complete (T := 𝗜𝚺₁) (V := V) hσ hv
  exact bridge hσ hI

/-- **归约接到完整形式**。同一条内部解释前提，对每个 `Type` 层的 𝗜𝚺₁ 模型
都给出 C-122 所消费的 D3 形状，因此 `𝗭𝗙𝗖 ⊬ (𝗭𝗙𝗖.consistent)ᵗ` 随之成立。
宇宙是 `Type`，与 `zfc_z0_full_of_D3_internalize` 的前提一致。
`Z0Blocked` 里的 `Type*` 陈述更强，这里不声称它。 -/
theorem zfc_z0_full_of_sigma1_bridge
    (bridge :
      ∀ {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
        {σ : ArithmeticSentence},
        ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 σ →
        Provable 𝗜𝚺₁ (⌜σ⌝ : V) →
        Provable 𝗭𝗙𝗖 (⌜arithTrln.translate σ⌝ : V)) :
    𝗭𝗙𝗖 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent : ArithmeticSentence) :=
  zfc_z0_full_of_D3_internalize fun V _ _ τ h =>
    zfcTr_D3_internalize_of_sigma1_bridge bridge τ h

end GodelQ.Z0Bridge

#print axioms GodelQ.Z0Bridge.zfcTr_D3_internalize_of_sigma1_bridge
#print axioms GodelQ.Z0Bridge.zfc_z0_full_of_sigma1_bridge
