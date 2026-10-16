import GodelQ.ZFC.Z0Full
import Foundation.FirstOrder.Incompleteness.StandardProvability

/-! 探针 3：验证 keyE 的 → 方向能否走通（临时文件，不进收据） -/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCZ0 GodelQ.Z0Full

namespace Probe3

-- A. Sh.reCh 的 V 内部语义：reCh ↔ ∃w reWitness
#check @FFL.FirstOrder.Theory.reWitness_spec
#check @FFL.FirstOrder.Theory.reCh
#check @FFL.FirstOrder.Theory.reWitness

-- B. 尝试：V ⊧ Sh.reCh ⌜σ⌝ ↔ Provable 𝗭𝗙𝗖 ⌜σᵗ⌝
example {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] (σ : ArithmeticSentence) :
    (V↓[ℒₒᵣ] ⊧ ((Sh.reCh.val)/[⌜σ⌝] : ArithmeticSentence)) ↔
      Provable 𝗭𝗙𝗖 (⌜arithTrln.translate σ⌝ : V) := by
  sorry

-- C. 尝试：V ⊧ Sh.reCh ⌜σ⌝ ↔ V ⊧ zfcTr σ
example {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] (σ : ArithmeticSentence) :
    (V↓[ℒₒᵣ] ⊧ ((Sh.reCh.val)/[⌜σ⌝] : ArithmeticSentence)) ↔
      (V↓[ℒₒᵣ] ⊧ zfcTr σ) := by
  rw [models_zfcTr_iff]
  sorry

-- D. 尝试：由 B 得到 → 方向（zfcTr σ → provabilityPred Sh.craig σ）
example (σ : ArithmeticSentence) :
    𝗜𝚺₁ ⊢ (↑(zfcTr σ) 🡒 (↑(provabilityPred (Theory.craig Sh) σ) : Sentence ℒₒᵣ)) := by
  sorry

end Probe3
