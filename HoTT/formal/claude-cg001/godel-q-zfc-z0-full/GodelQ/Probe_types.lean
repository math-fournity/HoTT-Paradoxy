import GodelQ.ZFC.Z0Full
import GodelQ.ZFC.Z0PA

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate

namespace GodelQ.ProbeTypes

-- types of primitives already known to exist (this file should compile)
#check WeakerThan.pbl
#check complete
#check provable_D3
#check provable_sigma_one_complete
#check Z0Full.zfcTr.D1
#check Sh_provable_iff
#check Z0Full.zfcTr_con_iff
#check Z0Full.zfcTr_D3_standard

end GodelQ.ProbeTypes
