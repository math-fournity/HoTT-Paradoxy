import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeArith
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 正对照（已知可过）
theorem ctrl_shift {n : V} : ∀ p, IsSemiformula ℒₒᵣ n p →
    iT n (shift ℒₒᵣ p) = shift ℒₛₑₜ (iT n p) := by
  have key : ∀ {param n p : V}, IsSemiformula ℒₒᵣ n p → param = n →
      iT param (shift ℒₒᵣ p) = shift ℒₛₑₜ (iT.construction.result ℒₒᵣ param p) :=
    UformulaRec1.Construction.semiformula_result_induction
      (V := V) (c := iT.construction) (L := ℒₒᵣ)
      (P := fun param n p q => param = n → iT param (shift ℒₒᵣ p) = shift ℒₛₑₜ q)
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

-- 失败对照：`param + 1`
theorem bad_plus_one {n : V} : ∀ p, IsSemiformula ℒₒᵣ n p →
    iT n (free ℒₒᵣ p)
      = imp ℒₛₑₜ (subst ℒₛₑₜ ?[^&0] domZero) (free ℒₛₑₜ (iT (n + 1) p)) := by
  have key : ∀ {param n p : V}, IsSemiformula ℒₒᵣ n p → param = n →
      iT param (free ℒₒᵣ p)
        = imp ℒₛₑₜ (subst ℒₛₑₜ ?[^&0] domZero) (free ℒₛₑₜ (iT.construction.result ℒₒᵣ (param+1) p)) :=
    UformulaRec1.Construction.semiformula_result_induction
      (V := V) (c := iT.construction) (L := ℒₒᵣ)
      (P := fun param n p q => param = n →
        iT param (free ℒₒᵣ p)
          = imp ℒₛₑₜ (subst ℒₛₑₜ ?[^&0] domZero) (free ℒₛₑₜ (iT.construction.result ℒₒᵣ (param+1) q)))
      (by definability)
      sorry

end GodelQ.ProbeArith
