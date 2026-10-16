-- CG-009: the assembled `conjunct` opening law.
--
-- `conjunct 3 n i y = (subst ℒₛₑₜ ?[^#i] cDomN) ^⋏ (subst ℒₛₑₜ (^#i ∷ shiftVec 3 n) y)`.
-- `substs_and` splits the outer `subst (QvecV (n+3))` into two independent goals,
-- each closed by the corresponding vector identity:
--   * cDomN part   : `substs_substs` + `termSubstVec_one_QvecV_three`
--   * shiftVec part : `substs_substs` + `termSubstVec_cons_QvecV_three`
import GodelQ.ZFC.IVEOpenFunc11

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.IVEOpenFunc12
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc2 GodelQ.IVEOpenFunc3 GodelQ.IVEOpenFunc4
open GodelQ.IVEOpenFunc5 GodelQ.IVEOpenFunc6 GodelQ.IVEOpenFunc8 GodelQ.IVEOpenFunc9
open GodelQ.IVEOpenFunc10 GodelQ.IVEOpenFunc11


/-- `^#i ∷ shiftVec 3 n` at layer `n+4` (the layer the outer `QvecV (n+3)` substitution sees). -/
lemma isSemitermVec_cons_shiftVec_layer {n i : V} (hi : i < n + 4) :
    IsSemitermVec ℒₛₑₜ (n + 1) (n + 4) ((^#i : V) ∷ shiftVec 3 n) := by
  -- `shiftVec 3 n` is a semiterm vector at layer `3 + n`; re-express it at `n + 4`.
  have htail : IsSemitermVec ℒₛₑₜ n (n + 4) (shiftVec 3 n) := by
    have h := isSemitermVec_shiftVec_V 3 n
    refine IsSemitermVec.iff.mpr ⟨h.isUTerm.lh.symm, ?_⟩
    intro j hj
    rw [nth_shiftVec 3 n j hj]
    have h2 : (3 + j : V) < n + 3 := lt_three_add_three hj
    have h3 : (3 + j : V) < n + 4 := by
      have e : n + 3 + 1 = n + 4 := by ring
      have h4 : (3 + j : V) < n + 3 + 1 := by
        have h5 : (3 + j : V) < n + 3 := h2
        exact lt_of_lt_of_le h5 (le_of_lt (lt_add_one (n + 3)))
      rwa [e] at h4
    exact IsSemiterm.bvar.mpr h3
  exact IsSemitermVec.cons_iff.mpr ⟨IsSemiterm.bvar.mpr hi, htail⟩

/-- `QvecV (n+3)` is a `(n+4)`-long semiterm vector at layer `n+4`. -/
lemma isSemitermVec_QvecV_three {n : V} :
    IsSemitermVec ℒₛₑₜ (n + 4) (n + 4) (QvecV (V := V) (n + 3)) := by
  have h := isSemitermVec_QvecV (V := V) (n + 3)
  have e : (n + 3 : V) + 1 = n + 4 := by ring
  rwa [e] at h

/-- **The `conjunct` opening law at layer `n+3`**: `QvecV (n+3)` fixes `conjunct 3 n i y`
    whenever `i < n + 3` and `y` is a semiformula at layer `n+1`. -/
lemma subst_QvecV_conjunct {n i y : V} (hy : IsSemiformula ℒₛₑₜ (n + 1) y)
    (hi : i < n + 3) :
    subst ℒₛₑₜ (QvecV (V := V) (n + 3)) (conjunct 3 n i y) = conjunct 3 n i y := by
  have hpd : IsUFormula ℒₛₑₜ (subst ℒₛₑₜ ?[^#i] ((cDomN : ℕ) : V)) := by
    have hlt : (n + 3 : V) < (n + 3) + 1 := lt_add_one (n + 3)
    have h2 : i < (n + 3) + 1 := lt_trans hi hlt
    have e : (n + 3 : V) + 1 = n + 4 := by ring
    exact (IsSemiformula.subst (L := ℒₛₑₜ) (n := 1) (m := n + 4) isSemiformula_cDomN
      (isSemitermVec_single_bvar (n := n + 4) (by rwa [e] at h2))).isUFormula
  have hpy : IsUFormula ℒₛₑₜ (subst ℒₛₑₜ ((^#i : V) ∷ shiftVec 3 n) y) := by
    have hlt : (n + 3 : V) < (n + 3) + 1 := lt_add_one (n + 3)
    have e : (n + 3 : V) + 1 = n + 4 := by ring
    have hlt2 : i < (n + 3) + 1 := lt_trans hi hlt
    have h2 : i < n + 4 := by rwa [e] at hlt2
    exact (IsSemiformula.subst (L := ℒₛₑₜ) (n := n + 1) (m := n + 4) hy
      (isSemitermVec_cons_shiftVec_layer (n := n) (i := i) h2)).isUFormula
  unfold conjunct
  rw [Bootstrapping.substs_and (L := ℒₛₑₜ) (w := QvecV (V := V) (n + 3))
    (p := subst ℒₛₑₜ ?[^#i] ((cDomN : ℕ) : V))
    (q := subst ℒₛₑₜ ((^#i : V) ∷ shiftVec 3 n) y) hpd hpy]
  refine congrArg₂ (fun a b => a ^⋏ b) ?_ ?_
  · -- cDomN part
    have hw : IsSemitermVec ℒₛₑₜ 1 (n + 4) (?[^#i] : V) := by
      have hlt : (n + 3 : V) < (n + 3) + 1 := lt_add_one (n + 3)
      have h2 : i < (n + 3) + 1 := lt_trans hi hlt
      have e : (n + 3 : V) + 1 = n + 4 := by ring
      exact isSemitermVec_single_bvar (n := n + 4) (by rwa [e] at h2)
    have hQ := isSemitermVec_QvecV_three (n := n)
    rw [show subst ℒₛₑₜ (QvecV (V := V) (n + 3))
          (subst ℒₛₑₜ (?[^#i] : V) ((cDomN : ℕ) : V))
        = subst ℒₛₑₜ (termSubstVec ℒₛₑₜ 1 (QvecV (V := V) (n + 3)) (?[^#i] : V))
          ((cDomN : ℕ) : V) from
      Bootstrapping.substs_substs (L := ℒₛₑₜ) (l := 1) isSemiformula_cDomN hQ hw]
    rw [termSubstVec_one_QvecV_three hi]
  · -- shiftVec part
    have hb : (i : V) < 3 + n := by
      have e : (n : V) + 3 = 3 + n := by ring
      rwa [e] at hi
    have hw : IsSemitermVec ℒₛₑₜ (n + 1) (n + 4) ((^#i : V) ∷ shiftVec 3 n) := by
      have hlt : (n + 3 : V) < (n + 3) + 1 := lt_add_one (n + 3)
      have h2 : i < (n + 3) + 1 := lt_trans hi hlt
      have e : (n + 3 : V) + 1 = n + 4 := by ring
      exact isSemitermVec_cons_shiftVec_layer (n := n) (i := i) (by rwa [e] at h2)
    have hQ := isSemitermVec_QvecV_three (n := n)
    rw [show subst ℒₛₑₜ (QvecV (V := V) (n + 3))
          (subst ℒₛₑₜ ((^#i : V) ∷ shiftVec 3 n) y)
        = subst ℒₛₑₜ (termSubstVec ℒₛₑₜ (n + 1) (QvecV (V := V) (n + 3))
            ((^#i : V) ∷ shiftVec 3 n)) y from
      Bootstrapping.substs_substs (L := ℒₛₑₜ) (l := n + 1) hy hQ hw]
    rw [termSubstVec_cons_QvecV_three hi]

end GodelQ.IVEOpenFunc12

#print axioms GodelQ.IVEOpenFunc12.subst_QvecV_conjunct
