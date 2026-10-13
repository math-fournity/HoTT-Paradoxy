import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimSetupQ GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFL
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`iT_substs1_atom` 的一般化（`v` 一般、`R = cEqN`）**。

`iT_substs1_atom` 是 `v = ?[^#0,^#0]` 的特例。本引理放开 `v`。 -/
lemma iT_substs1_atom_gen {v : V} (hv : IsSemitermVec ℒₒᵣ (2:V) (1:V) v) :
    iT (0:V) (subst ℒₒᵣ (?[^&0] : V) (^rel 2 (↑cEqN) v))
      = subst ℒₛₑₜ (?[^&0] : V) (iT (1:V) (^rel 2 (↑cEqN) v)) := by
  have hR : (ℒₒᵣ).IsRel (2:V) (↑cEqN : V) := by rw [cEqN]; exact codeIn_rel_quote _
  have hR' : (ℒₛₑₜ).IsRel (2:V) (↑cEqN : V) := by rw [cEqN]; exact codeIn_rel_quote _
  have hw : IsSemitermVec ℒₒᵣ (2:V) (1:V) (?[^&0, ^&0] : V) :=
    IsSemitermVec.doubleton.mpr
      ⟨IsSemiterm.fvar (L := ℒₒᵣ) (V := V) (n := (1:V)) 0,
       IsSemiterm.fvar (L := ℒₒᵣ) (V := V) (n := (1:V)) 0⟩
  rw [show subst ℒₒᵣ (?[^&0] : V) (^rel 2 (↑cEqN) v)
        = (^rel 2 (↑cEqN) (termSubstVec ℒₒᵣ (2:V) (?[^&0, ^&0] : V) v) : V) from by
      rw [Bootstrapping.substs_rel (L := ℒₒᵣ) hR hv.isUTerm]
      congr 1
      rw [show (?[^&0] : V) = (?[^&0, ^&0] : V) from rfl]]
  rw [iT_rel (V := V) (n := (0:V)) (k := (2:V)) (R := (↑cEqN : V)) hR
      (IsSemitermVec.termSubstVec (L := ℒₒᵣ) (V := V) hv hw).isUTerm]
  rw [iT_rel (V := V) (n := (1:V)) (k := (2:V)) (R := (↑cEqN : V)) hR hv.isUTerm]
  rw [iTR, iTR]
  trace_state
  sorry

end GodelQ.ProbeFL
