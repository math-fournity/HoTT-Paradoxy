import GodelQ.ZFC.ArrivalZFC

/-! 负控制（C-118）：硬说一个会停的过程（`Code.zero`，在输入 0 上立即停机）的跑者到达句在标准模型里为真。
到达句在 `Universe` 里的意思恰是跑者到达（`universe_arrS_iff`），而跑者到达恰是过程永不停机（`arrives_iff`）；
这里要补的“`Code.zero` 永不停机”是假的，Lean 必须拒绝。到达句因此确实区分了停与不停。 -/

open FFL FFL.FirstOrder FFL.FirstOrder.SetTheory GodelQ GodelQ.ArrivalZFC in
theorem wrong_halting_runner_arrives :
    Universe.{0}↓[ℒₛₑₜ] ⊧ arrS (Encodable.encode Nat.Partrec.Code.zero) :=
  (universe_arrS_iff _).mpr ((arrives_iff _).mpr (by simp [Done]))
