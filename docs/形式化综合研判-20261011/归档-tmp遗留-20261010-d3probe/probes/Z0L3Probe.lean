import GodelQ.ZFC.Z0Bridge

/-! 探测 L3 困难点。 -/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.Z0Bridge GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate

namespace GodelQ.Z0L3

-- 探测:ISigma1 模型 + 一条 Prop 假设
example {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    (b : V) (P : V → Prop) (h : ∀ u ≤ b, P u) : ∀ u ≤ b, P u := h

end GodelQ.Z0L3
