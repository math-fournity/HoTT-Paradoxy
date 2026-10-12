-- CG-009: the full `iVE`-level opening law (bvar case isolated).
import GodelQ.ZFC.IVESubstOpen2

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.IVESubstOpen3
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.TranslateShiftCompat

/-- The bvar case of the opening law. -/
lemma iVE_open_bvar {mm z : V} (hz : z < mm + 1) :
    iVE (mm + 1) (termSubst ℒₒᵣ (QvecVOr (V := V) mm) (^#z : V)) =
      subst ℒₛₑₜ (QvecV (V := V) (mm + 1)) (iVE (mm + 1) (^#z : V)) := by
  rcases lt_or_ge z mm with hlt | hge
  · rw [termSubst_bvar, show (QvecVOr (V := V) mm).[z] = ^#z from nth_QvecVOr_lt mm z hlt]
    simp only [iVE_bvar]
    exact (subst_QvecV_eqAtom_bvar_lt (m := mm) (z := z + 1) (by
      have h := add_lt_add_right hlt 1
      simpa using h)).symm
  · have hzle : z ≤ mm := lt_succ_iff_le.mp hz
    have hzeq : z = mm := le_antisymm hzle hge
    rw [hzeq]
    exact iVE_open_bvar_last mm

-- **注意**：完整的 `iVE_open` 在 `IVEOpenFull.lean`（func 支依赖本文件之后
-- 才证成的零件，此处声明会循环 import）。本文件只保留 bvar 支。

end GodelQ.IVESubstOpen3

#print axioms GodelQ.IVESubstOpen3.iVE_open_bvar
