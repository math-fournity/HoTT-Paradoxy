import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeHTP
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- hExs 的 t' 反推：第一步 substs1 → substs_rel
example : substs1 ℒₒᵣ (^&(0:V) : V) (^rel (0+1+1) (↑cEqN) ((?[^#0, ^#(0+1)] : V)) : V)
    = (^rel (0+1+1) (↑cEqN)
        (termSubstVec ℒₒᵣ (0+1+1) ((?[^&0] : V)) ((?[^#0, ^#(0+1)] : V))) : V) := by
  have hR : (ℒₒᵣ).IsRel (0+1+1) (↑cEqN) := by
    rw [show (0:V) + 1 + 1 = 2 by norm_num, cEqN]; exact codeIn_rel_quote _
  have hv : IsUTermVec ℒₒᵣ (0+1+1) ((^#0 : V) ∷ ((^#(0+1) : V) ∷ (0 : V))) :=
    IsUTermVec.adjoin (IsUTermVec.adjoin IsUTermVec.empty (IsUTerm.bvar (z := (0:V))))
      (IsUTerm.bvar (z := (0+1:V)))
  show subst ℒₒᵣ ((?[^&0] : V)) (^rel (0+1+1) (↑cEqN) ((?[^#0, ^#(0+1)] : V)) : V) = _
  rw [Bootstrapping.substs_rel hR hv]

end GodelQ.ProbeHTP
