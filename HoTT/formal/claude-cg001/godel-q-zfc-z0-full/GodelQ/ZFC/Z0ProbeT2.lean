import GodelQ.ZFC.Z0Full

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.Z0ProbeT2

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full

-- Probing the set-language internalized proof calculus API.
example {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] (t : Term V ℒₛₑₜ) :
    𝗭𝗙𝗖.internalize V ⊢ t ≐ t := by
  sorry

example {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] (t u : Term V ℒₛₑₜ) :
    𝗭𝗙𝗖.internalize V ⊢ (t ≐ u) 🡒 (u ≐ t) := by
  sorry

-- does bold_sigma style helper exist generically?
example {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] {n} {φ ψ : SetTheorySemiformula V n}
    (hφ : 𝗭𝗙𝗖.internalize V ⊢ φ) (hψ : 𝗭𝗙𝗖.internalize V ⊢ ψ) :
    𝗭𝗙𝗖.internalize V ⊢ φ ⋏ ψ := by
  sorry

end GodelQ.Z0ProbeT2
