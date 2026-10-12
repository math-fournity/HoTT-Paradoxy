-- CG-009: the `cFunc` substitution piece of the func branch.
import GodelQ.ZFC.IVEOpenFunc8

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.IVEOpenFunc9
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc2 GodelQ.IVEOpenFunc3 GodelQ.IVEOpenFunc4
open GodelQ.IVEOpenFunc5 GodelQ.IVEOpenFunc6 GodelQ.IVEOpenFunc8

/-- The `ve2` body's vector `[^#2, ^#0, ^#1]` is a 3-term vector at layer `n` (`n ≥ 3`). -/
lemma isSemitermVec_two_zero_one (n : V) (hn : 3 ≤ n) :
    IsSemitermVec ℒₛₑₜ 3 n ((^#2 : V) ∷ ?[^#0, ^#1]) := by
  have h2 : (2 : V) < n := lt_of_lt_of_le (by norm_num) hn
  have h1 : (1 : V) < n := lt_of_lt_of_le (by norm_num) hn
  have h0 : (0 : V) < n := lt_of_lt_of_le (by norm_num) hn
  rw [show (3 : V) = 2 + 1 by norm_num, IsSemitermVec.cons_iff]
  refine ⟨IsSemiterm.bvar.mpr h2, ?_⟩
  rw [show (2 : V) = 1 + 1 by norm_num, IsSemitermVec.cons_iff]
  refine ⟨IsSemiterm.bvar.mpr h0, ?_⟩
  rw [show (1 : V) = 0 + 1 by norm_num, IsSemitermVec.cons_iff]
  exact ⟨IsSemiterm.bvar.mpr (by simpa using h1), IsSemitermVec.empty n⟩

end GodelQ.IVEOpenFunc9

#print axioms GodelQ.IVEOpenFunc9.isSemitermVec_two_zero_one
