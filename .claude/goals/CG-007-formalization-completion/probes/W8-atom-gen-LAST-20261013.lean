import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimSetupQ GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFL
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

lemma subst_two_to_one {p : V} (hp : IsSemiformula ℒₒᵣ (1:V) p) :
    subst ℒₒᵣ (?[^&0, ^&0] : V) p = subst ℒₒᵣ (?[^&0] : V) p := by
  have hw2 : IsSemitermVec ℒₒᵣ (2:V) (1:V) (?[^&0, ^&0] : V) :=
    IsSemitermVec.doubleton.mpr
      ⟨IsSemiterm.fvar (L := ℒₒᵣ) (V := V) (n := (1:V)) 0,
       IsSemiterm.fvar (L := ℒₒᵣ) (V := V) (n := (1:V)) 0⟩
  have hw1 : IsSemitermVec ℒₒᵣ (1:V) (1:V) (?[^&0] : V) :=
    IsSemitermVec.singleton.mpr (IsSemiterm.fvar (L := ℒₒᵣ) (V := V) (n := (1:V)) 0)
  exact subst_congr_prefix' (L := ℒₒᵣ) (n := (1:V)) (m := (1:V)) (k₁ := (2:V)) (k₂ := (1:V))
    (w := (?[^&0, ^&0] : V)) (w' := (?[^&0] : V)) p hp (by norm_num) (by norm_num)
    hw2 hw1 (fun j hj ↦ by
      have hj0 : j = 0 := lt_one_iff_eq_zero.mp hj
      subst hj0
      rw [show (?[^&0, ^&0] : V) = (^&0 : V) ∷ ((^&0 : V) ∷ (0:V)) from rfl,
        show (?[^&0] : V) = ((^&0 : V) ∷ (0:V)) from rfl]
      rw [nth_adjoin_zero, nth_adjoin_zero])

/-- **`rel` 支（`v` 一般）**：左端先用 `subst_two_to_one` 把向量缩到 `?[^&0]`。 -/
lemma iT_substs1_atom_gen {v : V} (hv : IsSemitermVec ℒₒᵣ (2:V) (1:V) v) :
    iT (0:V) (subst ℒₒᵣ (?[^&0] : V) (^rel 2 (↑cEqN) v))
      = subst ℒₛₑₜ (?[^&0] : V) (iT (1:V) (^rel 2 (↑cEqN) v)) := by
  have hR : (ℒₒᵣ).IsRel (2:V) (↑cEqN : V) := by rw [cEqN]; exact codeIn_rel_quote _
  have hrel : IsSemiformula ℒₒᵣ (1:V) (^rel 2 (↑cEqN) v) :=
    IsSemiformula.rel.mpr ⟨hR, hv.isUTerm⟩
  rw [← subst_two_to_one hrel]
  rw [Bootstrapping.substs_rel (L := ℒₒᵣ) hR hv.isUTerm]
  have hw : IsSemitermVec ℒₒᵣ (2:V) (1:V) (?[^&0, ^&0] : V) :=
    IsSemitermVec.doubleton.mpr
      ⟨IsSemiterm.fvar (L := ℒₒᵣ) (V := V) (n := (1:V)) 0,
       IsSemiterm.fvar (L := ℒₒᵣ) (V := V) (n := (1:V)) 0⟩
  rw [show iT (0:V) (^rel 2 (↑cEqN) (termSubstVec ℒₒᵣ (2:V) (?[^&0, ^&0] : V) v))
        = iTR (0:V) (2:V) (↑cEqN) (termSubstVec ℒₒᵣ (2:V) (?[^&0, ^&0] : V) v)
      from iT_rel (V := V) (n := (0:V)) (k := (2:V)) (R := (↑cEqN : V)) hR
        (IsUTermVec.of_isSemitermVec ?_)]
  trace_state
  sorry

end GodelQ.ProbeFL
