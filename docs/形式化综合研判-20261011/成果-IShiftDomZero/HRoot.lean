-- CG-009: hRoot — the axm branch. All pieces confirmed available.
import GodelQ.ZFC.ProvableSeq

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate
open GodelQ.GateBranches

namespace GodelQ.HRoot
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`hRoot`**: Craig axioms translate to 𝗭𝗙𝗖-provable sentences.
    `Sh.craig = {φ | ∃ σ ∈ Sh, s, φ = σ.padding s}`; `Sh ⪯ 𝗭𝗙𝗖` gives `𝗭𝗙𝗖 ⊢ σᵗ`;
    padding preserves provability (`Entailment.padding_iff`). -/
theorem hRoot_uncond {p : V} (hp : p ∈ Sh.craig.Δ₁Class) :
    Provable 𝗭𝗙𝗖 (iT (0 : V) p) := by
  sorry

end GodelQ.HRoot

#print axioms GodelQ.HRoot.hRoot_uncond
