import GodelQ.ZFC.Z0Full
import GodelQ.ZFC.Z0PA
import Foundation.FirstOrder.Incompleteness.StandardProvability

/-! Expected rejection: Craig D3 is not the D3 instance of zfcTr. -/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCZ0 GodelQ.Z0Full

namespace GodelQ.WorkBuddyZ0Negative

example : zfcTr.HBL3 :=
  (inferInstance : (Sh.craig.standardProvability).HBL3)

end GodelQ.WorkBuddyZ0Negative
