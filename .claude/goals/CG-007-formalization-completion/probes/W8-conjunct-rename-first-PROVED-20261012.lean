import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000
namespace GodelQ.ProbeA5
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

lemma lt_two_cases {i : V} (hi : i < 2) : i = 0 ∨ i = 1 := by
  have h : i < 1 + 1 := by norm_num at hi ⊢; exact hi
  rcases lt_succ_iff_eq_or_succ.mp h with h1 | h1
  · exact Or.inr h1
  · exact Or.inl (lt_one_iff_eq_zero.mp h1)

lemma W3_expand : (?[^#0, ^#1, ^&0] : V) = (^#0 : V) ∷ ((^#1 : V) ∷ ((^&0 : V) ∷ (0 : V))) := rfl
lemma W2_expand : (?[^#0, ^#1] : V) = (^#0 : V) ∷ ((^#1 : V) ∷ (0 : V)) := rfl

lemma W3_nth {i : V} (hi : i < 2) : ((?[^#0, ^#1, ^&0] : V).[i]) = (^#i : V) := by
  rw [W3_expand]; rcases lt_two_cases hi with rfl | rfl <;> simp
lemma W2_nth {i : V} (hi : i < 2) : ((?[^#0, ^#1] : V).[i]) = (^#i : V) := by
  rw [W2_expand]; rcases lt_two_cases hi with rfl | rfl <;> simp

lemma isSemitermVec_W2 : IsSemitermVec ℒₛₑₜ (2:V) (2:V) (?[^#0, ^#1] : V) := by
  rw [W2_expand, show (2:V) = 1 + 1 by norm_num, IsSemitermVec.cons_iff]
  refine ⟨IsSemiterm.bvar.mpr (by norm_num), ?_⟩
  rw [show (1:V) = 0 + 1 by norm_num, IsSemitermVec.cons_iff]
  refine ⟨IsSemiterm.bvar.mpr (by norm_num), ?_⟩
  exact IsSemitermVec.empty (L := ℒₛₑₜ) (V := V) (0 + 1 + (0 + 1))

lemma isSemitermVec_W3 : IsSemitermVec ℒₛₑₜ (3:V) (2:V) (?[^#0, ^#1, ^&0] : V) := by
  rw [W3_expand, show (3:V) = 2 + 1 by norm_num, IsSemitermVec.cons_iff]
  refine ⟨IsSemiterm.bvar.mpr (by norm_num), ?_⟩
  rw [show (2:V) = 1 + 1 by norm_num, IsSemitermVec.cons_iff]
  refine ⟨IsSemiterm.bvar.mpr (by norm_num), ?_⟩
  rw [show (1:V) = 0 + 1 by norm_num, IsSemitermVec.cons_iff]
  refine ⟨IsSemiterm.fvar (L := ℒₛₑₜ) (V := V) (n := (0 + 1 + (0 + 1))) (0:V), ?_⟩
  exact IsSemitermVec.empty (L := ℒₛₑₜ) (V := V) (0 + 1 + (0 + 1))

/-- **第一分量**：`subst W (subst ?[^#i] cDomN) = subst ?[^#i] cDomN`（`i < 2`）。 -/
lemma conjunct_rename_first {i : V} (hi : i < 2) :
    subst ℒₛₑₜ (?[^#0, ^#1, ^&0] : V) (subst ℒₛₑₜ (?[^#i] : V) (↑cDomN : V))
      = subst ℒₛₑₜ (?[^#i] : V) (↑cDomN : V) := by
  have hmid : IsSemiformula ℒₛₑₜ (2:V) (subst ℒₛₑₜ (?[^#i] : V) (↑cDomN : V)) :=
    IsSemiformula.subst (L := ℒₛₑₜ) isSemiformula_cDomN
      (isSemitermVec_single_bvar (n := (2:V)) hi)
  have hcp : subst ℒₛₑₜ (?[^#0, ^#1, ^&0] : V)
        (subst ℒₛₑₜ (?[^#i] : V) (↑cDomN : V))
      = subst ℒₛₑₜ (?[^#0, ^#1] : V) (subst ℒₛₑₜ (?[^#i] : V) (↑cDomN : V)) :=
    subst_congr_prefix (V := V) (n := (2:V)) (m := (2:V)) (k₁ := (3:V)) (k₂ := (2:V))
      (w := (?[^#0, ^#1, ^&0] : V)) (w' := (?[^#0, ^#1] : V))
      (subst ℒₛₑₜ (?[^#i] : V) (↑cDomN : V)) hmid (by norm_num) (by norm_num)
      isSemitermVec_W3 isSemitermVec_W2
      (fun j hj ↦ by rw [W3_expand, W2_expand]; rcases lt_two_cases hj with rfl | rfl <;> simp)
  rw [hcp]
  have hss := Bootstrapping.substs_substs (L := ℒₛₑₜ) (l := (1:V)) (n := (2:V)) (m := (2:V))
    (v := (?[^#i] : V)) (w := (?[^#0, ^#1] : V)) isSemiformula_cDomN
    isSemitermVec_W2 (isSemitermVec_single_bvar (n := (2:V)) hi)
  rw [hss]
  congr 1
  rw [show (?[^#i] : V) = ((^#i : V) ∷ (0 : V)) from rfl]
  rw [show (1:V) = 0 + 1 by norm_num,
    termSubstVec_cons (IsUTerm.bvar (z := i)) IsUTermVec.empty, termSubstVec_nil]
  rw [show (^#(0+1) : V) = (^#1 : V) by norm_num]
  simp only [termSubst_bvar, W2_nth hi]

end GodelQ.ProbeA5
