import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimSetupQ GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFL
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`iT_substs1_atom` 的一般化**（`v` 放开到一般层 1 向量）。 -/
lemma iT_substs1_atom_gen {v : V} (hv : IsSemitermVec ℒₒᵣ (2:V) (1:V) v) :
    iT (0:V) (subst ℒₒᵣ (?[^&0] : V) (^rel 2 (↑cEqN) v))
      = subst ℒₛₑₜ (?[^&0] : V) (iT (1:V) (^rel 2 (↑cEqN) v)) := by
  have hR : (ℒₒᵣ).IsRel (2:V) (↑cEqN : V) := by rw [cEqN]; exact codeIn_rel_quote _
  have hw : IsSemitermVec ℒₒᵣ (2:V) (1:V) (?[^&0, ^&0] : V) :=
    IsSemitermVec.doubleton.mpr
      ⟨IsSemiterm.fvar (L := ℒₒᵣ) (V := V) (n := (1:V)) 0,
       IsSemiterm.fvar (L := ℒₒᵣ) (V := V) (n := (1:V)) 0⟩
  -- 向量桥：`subst ?[^&0] p = subst ?[^&0,^&0] p`（p 层 2，前 2 分量都是 `^&0`）
  have hbridge : ∀ {p : V}, IsSemiformula ℒₒᵣ (2:V) p →
      subst ℒₒᵣ (?[^&0] : V) p = subst ℒₒᵣ (?[^&0, ^&0] : V) p := by
    intro p hp
    have hw1 : IsSemitermVec ℒₒᵣ (1:V) (2:V) (?[^&0] : V) :=
      IsSemitermVec.singleton.mpr (IsSemiterm.fvar (L := ℒₒᵣ) (V := V) (n := (2:V)) 0)
    exact (subst_congr_prefix' (L := ℒₒᵣ) (n := (2:V)) (m := (2:V)) (k₁ := (1:V)) (k₂ := (2:V))
      (w := (?[^&0] : V)) (w' := (?[^&0, ^&0] : V)) p hp (by norm_num) (by norm_num)
      hw1 hw (fun j hj ↦ by
        have hj1 : j = 0 ∨ j = 1 := lt_two_cases hj
        rcases hj1 with rfl | rfl
        · rw [show (?[^&0] : V) = ((^&0 : V) ∷ (0:V)) from rfl,
            show (?[^&0, ^&0] : V) = (^&0 : V) ∷ ((^&0 : V) ∷ (0:V)) from rfl]
          rw [nth_adjoin_zero, nth_adjoin_zero]
        · rw [show (?[^&0, ^&0] : V) = (^&0 : V) ∷ ((^&0 : V) ∷ (0:V)) from rfl]
          rw [nth_adjoin_one, nth_adjoin_zero]
          rw [nth_lt_len (v := (?[^&0] : V)) (i := (1:V)) (by
            rw [show (?[^&0] : V) = ((^&0 : V) ∷ (0:V)) from rfl]
            simp only [len_adjoin, len_nil]; norm_num)])).symm
  rw [hbridge (isSemiformula_rel_iff.mpr ⟨hR, hv.isUTerm⟩)]
  rw [Bootstrapping.substs_rel (L := ℒₒᵣ) hR hv.isUTerm]
  trace_state
  sorry

end GodelQ.ProbeFL
