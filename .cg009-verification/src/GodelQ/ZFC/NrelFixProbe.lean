-- CG-009: the nrel branch's layer-bookkeeping obstacle is NOT real.
-- 9276 concluded: from IsUTermVec alone, listMax (termBVVec k v) ≤ param fails.
-- True — but the induction hypothesis carries IsSemiformula ℒₒᵣ n (^nrel k R v),
-- whose bv_le gives exactly listMax (termBVVec k v) ≤ n, and the guard param = n
-- transports it. Foundation itself uses this at Formula/Basic.lean:1361.
import GodelQ.ZFC.GateBranches

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate

namespace GodelQ.NrelFixProbe

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- The bound 9276 said was unavailable: it follows from the formula-side hypothesis. -/
lemma listMax_le_of_semiformula {n k R v : V}
    (hp : IsSemiformula ℒₒᵣ n (^nrel k R v)) :
    listMax (termBVVec (L := ℒₒᵣ) k v) ≤ n := by
  -- bv (^nrel k R v) = listMax (termBVVec k v) definitionally, and hp.bv_le : bv .. ≤ n
  -- IsUFormula.nrel : IsUFormula (^nrel k R v) ↔ IsRel k R ∧ IsUTermVec k v
  have hU : (ℒₒᵣ).IsRel k R ∧ IsUTermVec ℒₒᵣ k v :=
    (IsUFormula.nrel (L := ℒₒᵣ)).mp hp.isUFormula
  have h := hp.bv_le
  rw [bv_nrel hU.1 hU.2] at h
  exact h

/-- Consequently IsUTermVec upgrades to IsUTermVec at the right layer, given the formula hyp. -/
lemma isUTermVec_of_nrel {n k R v : V}
    (hp : IsSemiformula ℒₒᵣ n (^nrel k R v)) :
    IsUTermVec ℒₒᵣ k v := by
  exact ((IsUFormula.nrel (L := ℒₒᵣ)).mp hp.isUFormula).2

/-- The upgrade the nrel branch needs: IsUTermVec + the formula-side bv_le give
    IsSemitermVec at layer n, hence isSemiformula_iTR applies. -/
lemma isSemiformula_iTR_of_nrel {n k R v : V}
    (hp : IsSemiformula ℒₒᵣ n (^nrel k R v)) :
    IsSemiformula ℒₛₑₜ n (iTR n k R v) := by
  have hU := (IsUFormula.nrel (L := ℒₒᵣ)).mp hp.isUFormula
  have hbv : listMax (termBVVec (L := ℒₒᵣ) k v) ≤ n := by
    have h := hp.bv_le
    rw [bv_nrel hU.1 hU.2] at h
    exact h
  have hstm : IsSemitermVec ℒₒᵣ k (listMax (termBVVec (L := ℒₒᵣ) k v)) v := hU.2.isSemitermVec
  have hstm' : IsSemitermVec ℒₒᵣ k n v := by
    rw [IsSemitermVec.iff] at hstm ⊢
    refine ⟨hstm.1, fun i hi ↦ ?_⟩
    have h1 : IsUTerm ℒₒᵣ v.[i] := (IsSemiterm.def.mp (hstm.2 i hi)).1
    have h2 : termBV ℒₒᵣ v.[i] ≤ listMax (termBVVec (L := ℒₒᵣ) k v) :=
      (IsSemiterm.def.mp (hstm.2 i hi)).2
    exact IsSemiterm.def.mpr ⟨h1, le_trans h2 hbv⟩
  exact isSemiformula_iTR hU.1 hstm' 

end GodelQ.NrelFixProbe
