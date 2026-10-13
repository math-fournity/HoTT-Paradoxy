-- CG-009: the func branch of the iVE opening law.
import GodelQ.ZFC.IVEOpenFunc12

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.IVEOpenFunc13b
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc2 GodelQ.IVEOpenFunc3 GodelQ.IVEOpenFunc4
open GodelQ.IVEOpenFunc5 GodelQ.IVEOpenFunc6 GodelQ.IVEOpenFunc8 GodelQ.IVEOpenFunc9
open GodelQ.IVEOpenFunc10 GodelQ.IVEOpenFunc11 GodelQ.IVEOpenFunc12


/-- The conjunct law when the outer vector is `QvecV (mm+1)` descending two `qqAlls`
    binders: inside, the vector is `qVec² (QvecV (mm+1)) = QvecV (mm+3)`. -/
lemma subst_QvecV_conjunct_qVec2 {n i y : V} (hy : IsSemiformula ℒₛₑₜ (n + 1) y)
    (hi : i < n + 3) :
    subst ℒₛₑₜ (QvecV (V := V) n) (conjunct 3 n i y) = conjunct 3 n i y := by
  sorry

/-- **`ve2` 与 `subst (QvecV (mm+1))` 交换**（`k = 2` 支）。
    `w` 是 `iVE (mm+1) v`（逐分量），`w'` 是 `iVE (mm+1) (termSubst … v)`。 -/
lemma subst_QvecV_ve2 {mm f w w' : V} (hk : (2 : V) ≠ 0)
    (hw0 : IsSemiformula ℒₛₑₜ (mm + 1 + 1) w.[0])
    (hw1 : IsSemiformula ℒₛₑₜ (mm + 1 + 1) w.[1])
    (hw'0 : subst ℒₛₑₜ (QvecV (V := V) (mm + 1)) w.[0] = w'.[0])
    (hw'1 : subst ℒₛₑₜ (QvecV (V := V) (mm + 1)) w.[1] = w'.[1]) :
    subst ℒₛₑₜ (QvecV (V := V) (mm + 1)) (ve2 (mm + 1) 2 f w) = ve2 (mm + 1) 2 f w' := by
  have hc : IsSemiformula ℒₛₑₜ 3 (cFunc 2 f) := isSemiformula_cFunc_arity2 hk f
  have hB : IsSemiformula ℒₛₑₜ (3 + (mm + 1))
      (subst ℒₛₑₜ ((^#2 : V) ∷ ?[^#0, ^#1]) (cFunc 2 f)) := by
    have htv := isSemitermVec_three_bvars (mm + 1)
    rw [show ((^#2 : V) ∷ ?[^#0, ^#1]) = (^#2 : V) ∷ (^#0 : V) ∷ (^#1 : V) ∷ (0 : V) from rfl]
    exact IsSemiformula.subst (L := ℒₛₑₜ) (m := 3 + (mm + 1)) hc htv
  have hA0 : IsSemiformula ℒₛₑₜ (3 + (mm + 1)) (conjunct 3 (mm + 1) 0 w.[0]) :=
    isSemiformula_conjunct (b := 3) (n := mm + 1) (i := 0) hw0 (zero_lt_three_add (mm + 1))
  have hA1 : IsSemiformula ℒₛₑₜ (3 + (mm + 1)) (conjunct 3 (mm + 1) 1 w.[1]) :=
    isSemiformula_conjunct (b := 3) (n := mm + 1) (i := 1) hw1 (one_lt_three_add (mm + 1))
  have hA01 : IsSemiformula ℒₛₑₜ (3 + (mm + 1)) (conjunct 3 (mm + 1) 1 w.[1] ^⋏ ^⊤) :=
    IsSemiformula.and.mpr ⟨hA1, IsSemiformula.verum⟩
  have hA : IsSemiformula ℒₛₑₜ (3 + (mm + 1))
      (conjunct 3 (mm + 1) 0 w.[0] ^⋏ (conjunct 3 (mm + 1) 1 w.[1] ^⋏ ^⊤)) :=
    IsSemiformula.and.mpr ⟨hA0, hA01⟩
  have hsa : subst ℒₛₑₜ (QvecV (V := V) (mm + 1))
      (conjunct 3 (mm + 1) 0 w.[0] ^⋏ (conjunct 3 (mm + 1) 1 w.[1] ^⋏ ^⊤))
      = conjunct 3 (mm + 1) 0 w'.[0] ^⋏ (conjunct 3 (mm + 1) 1 w'.[1] ^⋏ ^⊤) := by
    have h0lt : (0 : V) < (mm + 1) + 3 := by
      have h : (0 : V) < 3 + (mm + 1) := zero_lt_three_add (V := V) (mm + 1)
      have e : 3 + (mm + 1) = (mm + 1) + 3 := add_comm 3 (mm + 1)
      exact e ▸ h
    have h1lt : (1 : V) < (mm + 1) + 3 := by
      have h : (1 : V) < 3 + (mm + 1) := one_lt_three_add (V := V) (mm + 1)
      have e : 3 + (mm + 1) = (mm + 1) + 3 := add_comm 3 (mm + 1)
      exact e ▸ h
    rw [Bootstrapping.substs_and (L := ℒₛₑₜ) (V := V) hA0.isUFormula hA01.isUFormula,
      Bootstrapping.substs_and (L := ℒₛₑₜ) (V := V) hA1.isUFormula IsUFormula.verum,
      Bootstrapping.substs_verum (L := ℒₛₑₜ) (V := V),
      subst_QvecV_conjunct_qVec2 (n := mm + 1) (i := 0) hw0 h0lt,
      subst_QvecV_conjunct_qVec2 (n := mm + 1) (i := 1) hw1 h1lt]
    rw [hw'0, hw'1]
  sorry

end GodelQ.IVEOpenFunc13b
