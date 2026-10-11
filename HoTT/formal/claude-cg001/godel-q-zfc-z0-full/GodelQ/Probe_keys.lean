import GodelQ.ZFC.Z0Full
import GodelQ.ZFC.Z0PA

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate

namespace GodelQ.ProbeKeys

-- The newly discovered candidates (full paths)
#check FFL.FirstOrder.Arithmetic.Bootstrapping.Arithmetic.sigma_one_provable_of_models
#check FFL.FirstOrder.Arithmetic.Bootstrapping.Arithmetic.provable_internalize
#check FFL.FirstOrder.Arithmetic.Bootstrapping.Provable.sound
#check FFL.FirstOrder.Arithmetic.Bootstrapping.tprovable_iff_provable
#check FFL.FirstOrder.Arithmetic.Bootstrapping.derivable_quote
#check FFL.FirstOrder.Arithmetic.Bootstrapping.internal_provable_of_outer_provable
#check FFL.FirstOrder.Theory.internalize
#check FFL.FirstOrder.Sentence.typed_quote_def

end GodelQ.ProbeKeys
