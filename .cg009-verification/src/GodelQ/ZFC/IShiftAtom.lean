-- CG-009: the atomic core of obligation ishift (v2, explicit intermediate equalities).
--   (a) shift (eqAtom t) = eqAtom (termShift t)      [needs IsUTerm t]
--   (b) iVE 0 (termShift t) = shift (iVE 0 t)        [for t = ^#z and t = ^&x]
-- Facts: termShift ^#z = ^#z; termShift ^&x = ^&(x+1);
--        iVE_bvar: iVE n ^#z = eqAtom ^#(z+1); iVE_fvar: iVE n ^&x = eqAtom ^&x.
import GodelQ.ZFC.GateBranches

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate

namespace GodelQ.IShiftAtom

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- (a) The set-language shift commutes with eqAtom (the atom of iVE's output). -/
lemma shift_eqAtom (t : V) (ht : IsUTerm ℒₛₑₜ t) :
    shift (L := ℒₛₑₜ) (eqAtom t) = eqAtom (termShift (L := ℒₛₑₜ) t) := by
  have hvec : IsUTermVec ℒₛₑₜ 2 (?[^#0, t] : V) :=
    IsUTermVec.two_iff.mpr ⟨^#0, t, IsUTerm.bvar (L := ℒₛₑₜ), ht, rfl⟩
  have hR : (ℒₛₑₜ).IsRel (V := V) 2 (cEqN : V) := by rw [cEqN]; exact codeIn_rel_quote _
  rw [eqAtom, shift_rel (L := ℒₛₑₜ) (k := 2) (R := (cEqN : V)) (v := ?[^#0, t]) hR hvec]
  rw [eqAtom]
  congr 1
  rw [termShiftVec_cons₂ (ht₁ := IsUTerm.bvar (L := ℒₛₑₜ)) (ht₂ := ht), termShift_bvar]

/-- (b1) iVE is compatible with term shift — bound-variable case. -/
lemma iVE_termShift_bvar (z : V) :
    iVE (0 : V) (termShift (L := ℒₒᵣ) (^#z)) = shift (L := ℒₛₑₜ) (iVE (0 : V) (^#z)) := by
  have h1 : iVE (0 : V) (termShift (L := ℒₒᵣ) (^#z)) = eqAtom (^#(z + 1)) := by
    rw [termShift_bvar, iVE_bvar]
  have h2 : shift (L := ℒₛₑₜ) (iVE (0 : V) (^#z)) = eqAtom (^#(z + 1)) := by
    rw [iVE_bvar]
    rw [shift_eqAtom (^#(z + 1)) (IsUTerm.bvar (L := ℒₛₑₜ))]
    rw [termShift_bvar]
  rw [h1, h2]

/-- (b2) iVE is compatible with term shift — free-variable case. -/
lemma iVE_termShift_fvar (x : V) :
    iVE (0 : V) (termShift (L := ℒₒᵣ) (^&x)) = shift (L := ℒₛₑₜ) (iVE (0 : V) (^&x)) := by
  have h1 : iVE (0 : V) (termShift (L := ℒₒᵣ) (^&x)) = eqAtom (^&(x + 1)) := by
    rw [termShift_fvar, iVE_fvar]
  have h2 : shift (L := ℒₛₑₜ) (iVE (0 : V) (^&x)) = eqAtom (^&(x + 1)) := by
    rw [iVE_fvar]
    rw [shift_eqAtom (^&x) (IsUTerm.fvar (L := ℒₛₑₜ) x)]
    rw [termShift_fvar]
  rw [h1, h2]

end GodelQ.IShiftAtom
