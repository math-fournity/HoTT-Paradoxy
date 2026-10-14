import GodelQ.ZFC.CG008ThresholdCorrection
import GodelQ.ZFC.ZFCDelta1

open FFL FFL.FirstOrder FFL.FirstOrder.SetTheory FFL.FirstOrder.Theory
open FFL.Entailment

namespace GodelQ.CG008CarrierProbe

/-- 事实 1：`Set.Func k = Empty`（carrier 缺口的正面证据）。 -/
example (k : ℕ) : FFL.FirstOrder.Language.Set.Func k = Empty := rfl

/-- 事实 2（**回应 Master §9.15 的挂起问题**）：`Type.Δ₁ 𝗭𝗙𝗖` 非空——
本树 `ZFCDelta1.lean` 已证（`ZFC.delta1`），不是猜想。
`Theory.internalize` 只需要 `[T.Δ₁]`，故 D3 路线**不需要**退到更弱的内部理论。 -/
noncomputable example : FFL.FirstOrder.Theory.Δ₁ 𝗭𝗙𝗖 := inferInstance

end GodelQ.CG008CarrierProbe
