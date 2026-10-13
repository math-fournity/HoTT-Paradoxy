import GodelQ.ZFC.ITSubstOpen7
open FFL FFL.FirstOrder FFL FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate
namespace GodelQ.Probe10
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc8 GodelQ.IVEOpenFull GodelQ.LayerMono
open GodelQ.ITSubstOpen3 GodelQ.ITSubstOpen4 GodelQ.ITSubstOpen5 GodelQ.ITSubstOpen6
open GodelQ.ITSubstOpen7

-- Vw := ^#j ∷ shiftVec 2 m  (长 m+1)
-- Ww := termSubstVec (m+2) (QvecV (m+2)) (^#j ∷ shiftVec 2 (m+1))
-- (a) k ≤ m：Vw.[k] = Ww.[k]
example (m j : V) (hj : j < m + 2) (k : V) (hk : k ≤ m) :
    ((^#j : V) ∷ shiftVec 2 m).[k] =
      (termSubstVec ℒₛₑₜ (m + 2) (QvecV (V := V) (m + 2))
        ((^#j : V) ∷ shiftVec 2 (m + 1))).[k] := by
  have hk1 : k < m + 1 := by
    have h := lt_add_one m
    -- k ≤ m < m+1
    exact lt_of_le_of_lt hk h
  have hk2 : k < m + 2 := lt_trans hk1 (by
    have h := lt_add_one (m + 1)
    rw [show ((m + 1) + 1 : V) = m + 2 by ring] at h
    exact h)
  rw [nth_termSubstVec (isSemitermVec_cons_shiftVec2 (m := m) (i := j) hj).isUTerm hk2]
  rw [nth_cons_shiftVec2 (m := m + 1) (i := j) (by
    -- need k < (m+1)+2 = m+3
    have h := lt_add_one (m + 1)
    have h2 : k < (m + 1) + 1 := hk1
    calc k < (m + 1) + 1 := h2
      _ < (m + 1) + 2 := by
        have h3 := lt_add_one ((m + 1) + 1)
        rw [show (((m + 1) + 1) + 1 : V) = (m + 1) + 2 by ring] at h3
        exact h3)]
  rw [nth_cons_shiftVec2 (m := m) (i := j) (by
    calc k < m + 1 := hk1
      _ < m + 2 := by
        have h := lt_add_one (m + 1)
        rw [show ((m + 1) + 1 : V) = m + 2 by ring] at h
        exact h)]
  sorry

end GodelQ.Probe10
