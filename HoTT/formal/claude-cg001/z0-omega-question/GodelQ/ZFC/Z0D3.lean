import GodelQ.ZFC.TransSigma1

/-!
# 012-Opus · W8：D3（经翻译）与完整的 Z0

`zfcTr`（Z0Full.lean）是“𝗭𝗙𝗖 证明它的翻译”这一可证性谓词，`zfcTr τ` 是 Σ1 句（`zfcTr_sigma1`）。
由经翻译的形式化 Σ1 完全性（`tr_sigma1_provable`）立得 D3 的内化形式，从而
`zfc_z0_full_of_D3_internalize` 的前提成立：𝗭𝗙𝗖 证明不了“𝗭𝗙𝗖 一致”的翻译，不带任何未证前提。
Gödel 第二不完全性所需的一致性由 Foundation 的 `zfc_consistent`（Lean 元层的 `Universe` 模型）
经 `Sh_consistent`（Z0Shadow.lean）提供。
-/

namespace GodelQ.SetNum

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment FFL.Entailment.FiniteContext
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCNum GodelQ.ZFCArith GodelQ.IntLogic GodelQ.Translate

open GodelQ.Z0Full in
/-- **D3（经翻译）**：𝗭𝗙𝗖 证明 τ 的翻译，则 𝗭𝗙𝗖 证明“𝗭𝗙𝗖 证明 τ 的翻译”的翻译（V 中）。 -/
theorem zfcTr_D3 (V : Type) [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] (τ : ArithmeticSentence) :
    Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V) → Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr τ)⌝ : V) := by
  intro h
  have hm : V↓[ℒₒᵣ] ⊧ zfcTr τ := (models_zfcTr_iff V τ).mpr h
  have := tr_sigma1_provable (V := V) (zfcTr_sigma1 τ) hm
  exact tprovable_iff_provable.mp this

open GodelQ.Z0Full in
/-- **完整的 Z0，不带前提**：𝗭𝗙𝗖 证明不了“𝗭𝗙𝗖 一致”（Foundation 的一致性句经翻译）。 -/
theorem zfc_z0_unconditional :
    𝗭𝗙𝗖 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent : ArithmeticSentence) :=
  zfc_z0_full_of_D3_internalize (fun V _ _ τ h ↦ zfcTr_D3 V τ h)

end GodelQ.SetNum

#print axioms GodelQ.SetNum.zfcTr_D3
#print axioms GodelQ.SetNum.zfc_z0_unconditional
