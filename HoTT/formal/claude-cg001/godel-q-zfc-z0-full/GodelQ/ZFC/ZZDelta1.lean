import GodelQ.ZFC.CG008ThresholdCorrection

open FFL FFL.FirstOrder FFL.FirstOrder.SetTheory FFL.FirstOrder.Theory
open FFL.Entailment ProvabilityAbstraction

namespace GodelQ.ZZDelta1

-- 用 inferInstanceAs 让失败显式报错（这是可判定的）
set_option maxHeartbeats 200000 in
example : Theory.Δ₁ 𝗭𝗙𝗖 := inferInstance

end GodelQ.ZZDelta1
