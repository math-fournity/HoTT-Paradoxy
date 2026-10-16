import GodelQ.ZFC.SeqTranslateFormula

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate
open FFL.FirstOrder.Arithmetic.Bootstrapping.Syntax.Formula.Functions

namespace GodelQ.ProbeNeg

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

example (param k R v : V) (hR : ℒₒᵣ.IsRel k R) (hv : IsUTermVec ℒₒᵣ k v) :
    neg ℒₒᵣ (Negation.construction.rel param k R v) = (^rel k R v : V) := by
  dsimp only [Negation.construction.rel]
  exact neg_nrel (L := ℒₒᵣ) hR hv

example (param k R v : V) (hR : ℒₒᵣ.IsRel k R) (hv : IsUTermVec ℒₒᵣ k v) :
    neg ℒₒᵣ (Negation.construction.rel param k R v) = (^rel k R v : V) := by
  nth_rw 1 [Negation.construction.rel]
  exact neg_nrel (L := ℒₒᵣ) hR hv

example (param k R v : V) (hR : ℒₒᵣ.IsRel k R) (hv : IsUTermVec ℒₒᵣ k v) :
    neg ℒₒᵣ (Negation.construction.rel param k R v) = (^rel k R v : V) := by
  conv => lhs; simp only [Negation.construction.rel]
  exact neg_nrel (L := ℒₒᵣ) hR hv

end GodelQ.ProbeNeg
