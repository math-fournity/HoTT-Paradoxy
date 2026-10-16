import GodelQ.ZFC.SeqTranslateFormula

/-! 探针 L12：shiftVec 引理升级到 n : V（临时文件，不进收据） -/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.Translate GodelQ.ZFCArith

namespace ProbeL12

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺⁺₁]


#check @FFL.FirstOrder.Arithmetic.ISigma1.sigma1_succ_induction

set_option maxHeartbeats 4000000 in
lemma isSemitermVec_shiftVec (b : V) : ∀ n : V,
    IsSemitermVec ℒₛₑₜ n (b + n) (shiftVec b n) := by
  intro n
  induction n using ISigma1.sigma1_succ_induction
  · definability
  case zero => simp
  case succ n ih =>
    rw [shiftVec_succ, IsSemitermVec.cons_iff]
    refine ⟨?_, ?_⟩
    · rw [IsSemiterm.bvar]
      calc b < n + b + 1 := lt_add_self_add_one b n
        _ = b + (n + 1) := by ring
    · have h := IsSemitermVec.termBShiftVec (L := ℒₛₑₜ) ih
      simpa only [add_assoc] using h

end ProbeL12
