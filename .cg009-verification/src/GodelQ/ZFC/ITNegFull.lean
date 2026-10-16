-- CG-009: complete iT_neg — guard + bv_le route + the imp-unfold trick for exs.
import GodelQ.ZFC.NrelFixProbe

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate

namespace GodelQ.ITNegFull

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

set_option maxHeartbeats 4000000

/-- The project's `isUFormula_iTR` is layer-free; reprove it here for self-containment. -/
lemma isUFormula_iTRV {n k R v : V} (hR : (ℒₒᵣ).IsRel k R) (hv : IsUTermVec ℒₒᵣ k v) :
    IsUFormula ℒₛₑₜ (iTR n k R v) :=
  (isSemiformula_iTR hR hv.isSemitermVec).isUFormula

/-- **The complete iT/neg compatibility law** (param = n guard; NrelFix for nrel). -/
theorem iT_neg_full {n : V} : ∀ p, IsSemiformula ℒₒᵣ n p →
    iT n (neg ℒₒᵣ p) = neg ℒₛₑₜ (iT n p) := by
  have key : ∀ {param n p : V}, IsSemiformula ℒₒᵣ n p →
      param = n → iT param (neg ℒₒᵣ p) = neg ℒₛₑₜ (iT param p) :=
    UformulaRec1.Construction.semiformula_result_induction
      (V := V) (c := iT.construction) (L := ℒₒᵣ)
      (P := fun param n p q => param = n → iT param (neg ℒₒᵣ p) = neg ℒₛₑₜ (iT param p))
      ?_ ?_ ?_ ?_ ?_ ?_ ?_ ?_ ?_
  · intro p hp
    simpa [iT] using (key hp rfl)
  · definability
  · -- rel
    intro n param k R v hR hv h
    show iT param (neg ℒₒᵣ (^rel k R v)) = neg ℒₛₑₜ (iT param (^rel k R v))
    rw [neg_rel (L := ℒₒᵣ) hR hv.isUTerm, iT_nrel hR hv.isUTerm, iT_rel hR hv.isUTerm]; rfl
  · -- nrel
    intro n param k R v hR hv h
    show iT param (neg ℒₒᵣ (^nrel k R v)) = neg ℒₛₑₜ (iT param (^nrel k R v))
    rw [neg_nrel (L := ℒₒᵣ) hR hv.isUTerm, iT_rel hR hv.isUTerm, iT_nrel hR hv.isUTerm]
    exact (IsUFormula.neg_neg (isUFormula_iTRV hR hv.isUTerm)).symm
  · -- verum
    intro n param
    show param = n → iT param (neg ℒₒᵣ (^⊤)) = neg ℒₛₑₜ (iT param (^⊤))
    intro; rw [neg_verum (L := ℒₒᵣ), iT_falsum, iT_verum]; rfl
  · -- falsum
    intro n param
    show param = n → iT param (neg ℒₒᵣ (^⊥)) = neg ℒₛₑₜ (iT param (^⊥))
    intro; rw [neg_falsum (L := ℒₒᵣ), iT_verum, iT_falsum]; rfl
  · -- and
    intro n param p q hp hq ihp ihq
    show param = n → iT param (neg ℒₒᵣ (p ^⋏ q)) = neg ℒₛₑₜ (iT param (p ^⋏ q))
    intro hn
    rw [neg_and (L := ℒₒᵣ) hp.isUFormula hq.isUFormula,
      iT_or (IsUFormula.neg hp.isUFormula) (IsUFormula.neg hq.isUFormula),
      ihp hn, ihq hn,
      neg_or (L := ℒₛₑₜ) (isSemiformula_iT (n := n) p hp).isUFormula
        (isSemiformula_iT (n := n) q hq).isUFormula,
      iT_and hp.isUFormula hq.isUFormula]
  · -- or
    intro n param p q hp hq ihp ihq
    show param = n → iT param (neg ℒₒᵣ (p ^⋎ q)) = neg ℒₛₑₜ (iT param (p ^⋎ q))
    intro hn
    rw [neg_or (L := ℒₒᵣ) hp.isUFormula hq.isUFormula,
      iT_and (IsUFormula.neg hp.isUFormula) (IsUFormula.neg hq.isUFormula),
      ihp hn, ihq hn,
      neg_and (L := ℒₛₑₜ) (isSemiformula_iT (n := n) p hp).isUFormula
        (isSemiformula_iT (n := n) q hq).isUFormula,
      iT_or hp.isUFormula hq.isUFormula]
  · -- all : LHS = ^∀ (imp domZero (iT(neg p))), RHS = ^∀ (neg (domZero ⋏ iT p))
    intro n param p hp ih
    show param = n → iT param (neg ℒₒᵣ (^∀ p)) = neg ℒₛₑₜ (iT param (^∀ p))
    intro hn
    have hres : IsUFormula ℒₛₑₜ (iT (param + 1) p) :=
      (isSemiformula_iT (n := param + 1) p (by simpa [← hn] using hp)).isUFormula
    rw [iT_all hp.isUFormula, neg_all (L := ℒₛₑₜ)
        (IsUFormula.imp.mpr ⟨(isSemiformula_domZero (n := param)).isUFormula, hres⟩),
      neg_ex (L := ℒₒᵣ) hp.isUFormula, iT_all (IsUFormula.neg hp.isUFormula)]
    -- LHS: ^∀ (imp domZero (iT (param+1) (neg p)))
    -- RHS: ^∀ (neg (imp domZero (iT (param+1) p)))
    rw [show neg ℒₛₑₜ (imp ℒₛₑₜ domZero (iT (param + 1) p)) =
        neg ℒₛₑₜ domZero ^⋎ neg ℒₛₑₜ (iT (param + 1) p) from rfl]
    rw [show imp ℒₛₑₜ domZero (iT (param + 1) (neg ℒₒᵣ p)) =
        neg ℒₛₑₜ domZero ^⋎ iT (param + 1) (neg ℒₒᵣ p) from rfl]
    exact congrArg (fun x => (^∀ (neg ℒₛₑₜ domZero ^⋎ x) : V))
      (ih 0 (by simp [iT.construction]) (by simp [iT.construction, hn]))
  · -- exs : LHS = ^∀ (imp domZero (iT(neg p))), RHS = ^∀ (neg (domZero ⋏ iT p))
    intro n param p hp ih
    show param = n → iT param (neg ℒₒᵣ (^∃ p)) = neg ℒₛₑₜ (iT param (^∃ p))
    intro hn
    have hres : IsUFormula ℒₛₑₜ (iT (param + 1) p) :=
      (isSemiformula_iT (n := param + 1) p (by simpa [← hn] using hp)).isUFormula
    rw [iT_exs hp.isUFormula, neg_ex (L := ℒₛₑₜ)
        (IsUFormula.and.mpr ⟨(isSemiformula_domZero (n := param)).isUFormula, hres⟩),
      neg_ex (L := ℒₒᵣ) hp.isUFormula, iT_all (IsUFormula.neg hp.isUFormula)]
    rw [show neg ℒₛₑₜ (domZero ^⋏ iT (param + 1) p) =
        neg ℒₛₑₜ domZero ^⋎ neg ℒₛₑₜ (iT (param + 1) p) from rfl]
    rw [show imp ℒₛₑₜ domZero (iT (param + 1) (neg ℒₒᵣ p)) =
        neg ℒₛₑₜ domZero ^⋎ iT (param + 1) (neg ℒₒᵣ p) from rfl]
    exact congrArg (fun x => (^∀ (neg ℒₛₑₜ domZero ^⋎ x) : V))
      (ih 0 (by simp [iT.construction]) (by simp [iT.construction, hn]))

end GodelQ.ITNegFull

#print axioms GodelQ.ITNegFull.iT_neg_full
