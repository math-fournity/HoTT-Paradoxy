import GodelQ.ZFC.Z0Full
import GodelQ.ZFC.Z0PA

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate

namespace GodelQ.ProbeDed2

#check FFL.Entailment.deduction_iff
#check FFL.Entailment.weakening
#check FFL.Entailment.Deduction.inv
#check FFL.Entailment.Deduction.ofInsert
#check FFL.Entailment.axiom
#check FFL.Entailment.adjoin

end GodelQ.ProbeDed2
