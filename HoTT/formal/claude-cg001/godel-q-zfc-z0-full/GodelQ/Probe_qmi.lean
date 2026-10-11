import GodelQ.ZFC.Z0Full
import GodelQ.ZFC.Z0PA

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate

namespace GodelQ.ProbeQMI

#check FFL.FirstOrder.GödelQuote.quote_model_independent
#check FFL.FirstOrder.GödelQuote.quote_model_independent (φ := (α := ℕ))
#check @FFL.FirstOrder.GödelQuote.quote_model_independent

end GodelQ.ProbeQMI
