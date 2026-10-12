import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeBypass
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 绕法：P 里 `param` 原样；层数位移由外层补
theorem iT_free_shape {n : V} : ∀ p, IsSemiformula ℒₒᵣ n p →
    iT n (free ℒₒᵣ p)
      = imp ℒₛₑₜ (subst ℒₛₑₜ ?[^&0] domZero) (free ℒₛₑₜ (iT (n + 1) p)) := by
  have key : ∀ {param n p : V}, IsSemiformula ℒₒᵣ n p → param = n →
      iT param (free ℒₒᵣ p)
        = imp ℒₛₑₜ (subst ℒₛₑₜ ?[^&0] domZero) (free ℒₛₑₜ (iT.construction.result ℒₒᵣ param p)) :=
    UformulaRec1.Construction.semiformula_result_induction
      (V := V) (c := iT.construction) (L := ℒₒᵣ)
      (P := fun param n p q => param = n →
        iT param (free ℒₒᵣ p)
          = imp ℒₛₑₜ (subst ℒₛₑₜ ?[^&0] domZero) (free ℒₛₑₜ (iT.construction.result ℒₒᵣ param q)))
      (by definability)
      (by intro n param k R v hR hv h; subst h; sorry)
      (by intro n param k R v hR hv h; subst h; sorry)
      (by intro n param h; subst h; sorry)
      (by intro n param h; subst h; sorry)
      (by intro n param p q hp hq ihp ihq h; subst h; sorry)
      (by intro n param p q hp hq ihp ihq h; subst h; sorry)
      (by intro n param p hp ih h; subst h; sorry)
      (by intro n param p hp ih h; subst h; sorry)
  intro p hp
  exact key hp rfl

end GodelQ.ProbeBypass
