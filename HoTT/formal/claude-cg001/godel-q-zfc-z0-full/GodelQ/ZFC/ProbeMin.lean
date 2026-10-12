import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeMin
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

example : True := by
  trivial

-- 最小对照：NegLaw 形状能不能在这台机器里跑通（p 只用一次）
have key : ∀ {param n p : V}, IsSemiformula ℒₒᵣ n p → param = n →
      iT param (free ℒₒᵣ p) = free ℒₛₑₜ (iT.construction.result ℒₒᵣ param p) :=
    UformulaRec1.Construction.semiformula_result_induction
      (V := V) (c := iT.construction) (L := ℒₒᵣ)
      (P := fun param n p q => param = n → iT param (free ℒₒᵣ p) = free ℒₛₑₜ q)
      (by definability)
      (by intro n param k R v hR hv h; subst h; sorry)
      (by intro n param k R v hR hv h; subst h; sorry)
      (by intro n param h; subst h; sorry)
      (by intro n param h; subst h; sorry)
      (by intro n param p q hp hq ihp ihq h; subst h; sorry)
      (by intro n param p q hp hq ihp ihq h; subst h; sorry)
      (by intro n param p hp ih h; subst h; sorry)
      (by intro n param p hp ih h; subst h; sorry)

end GodelQ.ProbeMin
