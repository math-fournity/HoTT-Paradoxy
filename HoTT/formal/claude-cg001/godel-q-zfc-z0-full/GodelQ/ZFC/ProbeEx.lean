import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeEx
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- hExs 核心等式（原子支）：用 iT_rel 展开两侧
example : iT (0:V) (substs1 ℒₒᵣ (^&(0:V) : V) (^rel (0+1+1) (↑cEqN) (?[^#0, ^#0] : V)))
    = substs1 ℒₛₑₜ (iVE (0:V) (^&(0:V) : V))
        (iTR (0:V) (0+1+1) (↑cEqN) ((qVec ℒₛₑₜ)^[0+1] (?[iVE 0 ^#0, iVE 0 ^#0] : V) : V)) := by
  sorry

-- 先只展开左：substs1 与 iTR 的相容
example : iT (0:V) (substs1 ℒₒᵣ (^&(0:V) : V) (^rel (0+1+1) (↑cEqN) (?[^#0, ^#0] : V)))
    = (^rel (0+1+1) (↑cEqN) (?[^#0, iVE 0 ^&0] : V) : V) := by
  sorry

-- 右侧 iT 0 p 展开后，substs1 应给出什么
example : iT (0:V) (^rel (0+1+1) (↑cEqN) ((?[^#0, ^#0] : V)))
    = (^rel (0+1+1) (↑cEqN) ((?[iVE 0 ^#0, iVE 0 ^#0] : V)) : V) := by
  have hR : (ℒₒᵣ).IsRel (0+1+1) (↑cEqN) := by rw [cEqN]; exact codeIn_rel_quote _
  have hv : IsUTermVec ℒₒᵣ (0+1+1) ((?[^#0, ^#0] : V)) := by
    apply IsUTermVec.adjoin (IsUTermVec.adjoin IsUTermVec.empty (IsUTerm.bvar (z := (0:V))))
    exact IsUTerm.bvar (z := (0:V))
  rw [iT_rel (V := V) hR hv]

end GodelQ.ProbeEx
