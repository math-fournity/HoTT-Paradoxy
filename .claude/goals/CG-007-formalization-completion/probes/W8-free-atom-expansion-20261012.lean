import GodelQ.ZFC.ShCraigElimSetupQ

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat

set_option maxHeartbeats 800000

namespace GodelQ.ProbeRen
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## 探针：`iT_rename` 的 `k = 0` 原子情形

猜想：`iT 0 (subst ℒₒᵣ ?[^&0] p) = subst ℒₛₑₜ ?[^&0] (iT 1 p)`（`p` 层数 1）。

先只测两边各自的化简。`p = ^rel 2 0 ?[^#0, ^#0]`。 -/

-- (A) `free p` 的展开：`shift` 不动 bvar，故 `free p = subst ?[^&0] p`
example : free ℒₒᵣ (^rel 2 (0 : V) (?[^#0, ^#0] : V))
    = (^rel 2 (0 : V) (?[^&0, ^&0] : V) : V) := by
  show subst ℒₒᵣ (?[^&0] : V)
      (shift ℒₒᵣ (^rel 2 (0 : V) (?[^#0, ^#0] : V))) = _
  have hb : IsSemiterm ℒₒᵣ 1 (^#(0:V) : V) := IsSemiterm.bvar.mpr (by simp)
  have hv : IsSemitermVec ℒₒᵣ 2 1 (?[^#0, ^#0] : V) :=
    IsSemitermVec.doubleton.mpr ⟨hb, hb⟩
  rw [Bootstrapping.shift_rel (L := ℒₒᵣ) (by simp) hv.isUTerm]
  rw [Bootstrapping.substs_rel (L := ℒₒᵣ) (by simp)
    ((hv.termShiftVec).isUTerm)]
  congr 1
  simp only [termShiftVec_cons₂ hb.isUTerm hb.isUTerm, termShift_bvar,
    termSubstVec_cons₂ hb.isUTerm hb.isUTerm, termSubst_bvar]
  simp

end GodelQ.ProbeRen
