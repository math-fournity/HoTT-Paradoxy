import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeFinalRW
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ### 最终判定（用 Foundation 的现成定理，不靠手写形状）

`(Theory.IsCraigAxiom.defined (T := Sh)).iff`：把 `p ∈ Sh.craig.Δ₁Class`
化成 `Sh.IsCraigAxiom p`。**注意 `T := Sh`。**

结论：`reWitness` 的参数是 `Sh`，不是 `Sh.craig`。 -/

example (p : V) (h : p ∈ (Sh.craig).Δ₁Class) :
    Theory.IsCraigAxiom (V := V) Sh p :=
  ((Theory.IsCraigAxiom.defined (V := V) (T := Sh)).iff).mp h

-- 反过来也要成立（iff）
example (p : V) (h : Theory.IsCraigAxiom (V := V) Sh p) :
    p ∈ (Sh.craig).Δ₁Class :=
  ((Theory.IsCraigAxiom.defined (V := V) (T := Sh)).iff).mpr h

end GodelQ.ProbeFinalRW
