-- Master 核验：004-Flash 重做的四条 lang-indep 引理（逐字复制其证明体）。
import GodelQ.ZFC.ITShiftFull

open FFL FFL.FirstOrder FFL FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.LangIndepCheck
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

lemma termBShift_lang_indep_bvar (z : V) :
    termBShift ℒₒᵣ (^#z : V) = termBShift ℒₛₑₜ (^#z : V) := by
  rw [termBShift_bvar, termBShift_bvar]

lemma termBShift_lang_indep_fvar (x : V) :
    termBShift ℒₒᵣ (^&x : V) = termBShift ℒₛₑₜ (^&x : V) := by
  rw [termBShift_fvar, termBShift_fvar]

lemma termSubst_lang_indep_bvar (w z : V) :
    termSubst ℒₒᵣ w (^#z : V) = termSubst ℒₛₑₜ w (^#z : V) := by
  rw [termSubst_bvar, termSubst_bvar]

lemma termSubst_lang_indep_fvar (w x : V) :
    termSubst ℒₒᵣ w (^&x : V) = termSubst ℒₛₑₜ w (^&x : V) := by
  rw [termSubst_fvar, termSubst_fvar]

end GodelQ.LangIndepCheck

#print axioms GodelQ.LangIndepCheck.termBShift_lang_indep_bvar
#print axioms GodelQ.LangIndepCheck.termSubst_lang_indep_fvar
