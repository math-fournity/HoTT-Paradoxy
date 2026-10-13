import GodelQ.ZFC.ITSubsts1

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

set_option maxHeartbeats 8000000

namespace GodelQ.ProbeSubsts1B
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 先测 definability 能否吃下带 ∀ w 的 Π1 谓词
example : 𝚷ᴬ₁-Relation (fun (n : V) (p : V) => (1:V) ≤ n →
    ∀ w, IsSemitermVec ℒₛₑₜ n n w → IsSemitermVec ℒₒᵣ n n w →
      subst ℒₛₑₜ w (iT n p) = iT (n - 1) (subst ℒₒᵣ w p)) := by
  definability

end GodelQ.ProbeSubsts1B
