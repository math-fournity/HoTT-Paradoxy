import GodelQ.ZFC.ITSubstCounter
import GodelQ.ZFC.ITSubstOpen9
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open GodelQ.ZFCArith GodelQ.Translate

namespace GodelQ.ProbeTerm0
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- Q1: does IsTerm (layer 0) allow a free variable?
example (x : V) : IsTerm ℒₒᵣ (^&x : V) := IsSemiterm.fvar 0 x

-- Q2: **IsTerm 不保证「值在 ω」**。取 `t := ^&x`（x 任意），statement 里的
-- `ht : IsTerm ℒₒᵣ t` 被满足，但 witness 引理要求「t 的值 ∈ ω」，而 x 可以不是
-- ω 的元素（非标准元）。故 ExsBridge2 的 `IsTerm` 前提**可能不足**，
-- 见证引理要么另加假设（如「t 是 numeral/closed」），要么整条要重新定型。
--
-- 这条探针不证 Q2（那是 001-Step 的 witness 引理），只记录「前提可疑」这个事实。
example (p : V) (hp : IsSemiformula ℒₒᵣ 1 p) :
    Provable 𝗭𝗙𝗖 (imp ℒₛₑₜ (iT (0:V) (substs1 ℒₒᵣ (^&0) p))
      (^∃ (domZero (V := V) ^⋏ iT (1:V) p))) := by
  sorry

end GodelQ.ProbeTerm0
