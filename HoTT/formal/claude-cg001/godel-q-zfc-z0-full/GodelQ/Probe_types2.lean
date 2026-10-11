import GodelQ.ZFC.Z0Full
import GodelQ.ZFC.Z0PA

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate

namespace GodelQ.ProbeTypes2

#check FFL.FirstOrder.Arithmetic.Bootstrapping.Provable.complete
#check FFL.FirstOrder.Arithmetic.Bootstrapping.tprovable_iff_provable
#check modus_ponens_sentence
#check provabilityPred
#check FFL.FirstOrder.Arithmetic.Bootstrapping.Arithmetic.provabilityPred
#check FFL.FirstOrder.Arithmetic.provabilityPred
#check FFL.FirstOrder.SetTheory.provable_D3
#check FFL.FirstOrder.Arithmetic.Bootstrapping.Arithmetic.provable_D3
#check FFL.FirstOrder.SetTheory.consistent
#check Z0Full.zfcTr.con
#check Z0Full.zfcTr.HBL3

end GodelQ.ProbeTypes2
