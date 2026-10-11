import GodelQ.ZFC.Z0Full
import GodelQ.ZFC.Z0PA

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate

namespace GodelQ.ProbeDed

#check deduction
#check FFL.FirstOrder.Entailment.deduction
#check Entailment.weaken
#check weaken
#check Entailment.cut
#check Entailment.axiom
#check Entailment.assumption
#check Entailment.mono

end GodelQ.ProbeDed
