import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeEx
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- hExs 核心等式 RHS 展开
example : iT (0:V) (^rel (0+1+1) (↑cEqN) ((?[^#0, ^#0] : V)))
    = (^rel (0+1+1) (↑cEqN) ((?[iVE 0 ^#0, iVE 0 ^#0] : V)) : V) := by
  have hv : IsUTermVec ℒₒᵣ (0+1+1) ((?[^#0, ^#0] : V)) :=
    IsUTermVec.adjoin (IsUTermVec.adjoin IsUTermVec.empty (IsUTerm.bvar (z := (0:V))))
      (IsUTerm.bvar (z := (0:V)))
  rw [show iT (0:V) (^rel (0+1+1) (↑cEqN) ((?[^#0, ^#0] : V)))
      = iTR (0:V) (0+1+1) (↑cEqN) ((?[^#0, ^#0] : V)) from
    (UformulaRec1.Construction.result_rel (c := iT.construction) (L := ℒₒᵣ)
      (by rw [show (0:V) + 1 + 1 = 2 by norm_num, cEqN]; exact codeIn_rel_quote _) hv)]

end GodelQ.ProbeEx
