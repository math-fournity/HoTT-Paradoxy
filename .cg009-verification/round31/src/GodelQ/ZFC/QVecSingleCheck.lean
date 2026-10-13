-- Master 核验：qVec ?[t'] 的长度-2 形状与越界补零（带 IsUTerm 假设）。
import GodelQ.ZFC.ITShiftFull

open FFL FFL.FirstOrder FFL FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.QVecSingleCheck
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

lemma qVec_single (t' : V) (ht : IsUTerm ℒₛₑₜ t') :
    qVec ℒₛₑₜ (?[t'] : V) = ((^#0 : V) ∷ (termBShift ℒₛₑₜ t' ∷ (0:V))) := by
  rw [Bootstrapping.qVec, show len (?[t'] : V) = (1:V) from by simp]
  rw [show (1:V) = 0 + 1 by norm_num,
    termBShiftVec_cons ht IsUTermVec.empty, termBShiftVec_nil]

end GodelQ.QVecSingleCheck

#print axioms GodelQ.QVecSingleCheck.qVec_single
