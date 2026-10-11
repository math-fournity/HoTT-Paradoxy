import GodelQ.ZFC.Z0Full
import GodelQ.ZFC.Z0PA

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate

namespace GodelQ.ProbeD3Final

-- Decisive test: does `Sh` carry [Theory.Δ₁]?  If yes, provable_D3 (T := Sh) gives D3 for zfcTr
-- (since zfcTr σ ↔ provabilityPred Sh σ), closing the gap. If no, the gap is genuine (CG-008).
#check Theory.Δ₁ Sh
#check provable_D3 (T := Sh)
#check FFL.FirstOrder.Arithmetic.Bootstrapping.provabilityPred
#check Z0Full.zfcTr.D1  -- to confirm it is D1 of the zfcTr Provability

end GodelQ.ProbeD3Final
