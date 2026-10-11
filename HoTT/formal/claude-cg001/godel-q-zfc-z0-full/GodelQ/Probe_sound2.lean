import GodelQ.ZFC.Z0Full
import GodelQ.ZFC.Z0PA

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate

namespace GodelQ.ProbeSound2

-- more soundness variants
#check FFL.Entailment.sound
#check Entailment.sound
#check Theory.sound
#check Semantics.sound
#check Models.sound
#check FFL.FirstOrder.Semantics.true_of_provable
#check Entailment.true_of_provable
#check FFL.FirstOrder.Entailment.sound
#check FFL.FirstOrder.true_of_provable
#check true_in_all_models
#check FFL.FirstOrder.Theory.soundness
#check FFL.FirstOrder.Semantics.soundness
#check FFL.FirstOrder.Soundness.theorem
#check entails
#check FFL.FirstOrder.Entailment.entails
#check FFL.FirstOrder.Models.true_of_provable
#check provabilityPred 𝗭𝗙𝗖

end GodelQ.ProbeSound2
