import GodelQ.ZFC.Z0Full
import GodelQ.ZFC.Z0PA

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate

namespace GodelQ.Probe

-- Can provable_sigma_one_complete be used with T := Sh?
#check provable_sigma_one_complete (T := Sh)
-- Does Sh satisfy the required instances?
#check (inferInstance : Theory.Δ₁ Sh)
#check (inferInstance : 𝗣𝗔⁻ ⪯ Sh)
-- soundness lemma candidates
#check FFL.FirstOrder.Entailment.sound
#check FFL.FirstOrder.Semantics.Models.sound
#check Theory.entails_of_provable
#check FFL.FirstOrder.entails_of_provable
#check FFL.FirstOrder.Semantics.true_of_provable
#check sound_of_provable

end GodelQ.Probe
