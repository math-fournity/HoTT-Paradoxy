
import GodelQ.ZFC.TranslateShiftCompat

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate

namespace GodelQ.ProbeAPI

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- shift distribution
#check @Bootstrapping.shift_and
#check @Bootstrapping.shift_or
#check @Bootstrapping.shift_imp
#check @Bootstrapping.shift_all
#check @Bootstrapping.shift_exs
#check @Bootstrapping.shift_verum
#check @Bootstrapping.shift_falsum
#check @Bootstrapping.shift_rel
#check @Bootstrapping.shift_nrel
#check @Bootstrapping.shift_substs
#check @Bootstrapping.shift_qqAlls
#check @Bootstrapping.shift_qqExs
#check @Bootstrapping.shift_vec
#check @Bootstrapping.shift_bvar
#check @Bootstrapping.shift_fvar
#check @Bootstrapping.shift_func

-- termShift
#check @Bootstrapping.termShift_bvar
#check @Bootstrapping.termShift_fvar
#check @Bootstrapping.termShift_func
#check @Bootstrapping.termShiftVec_nil
#check @Bootstrapping.termShiftVec_cons
#check @Bootstrapping.termShiftVec_cons₁
#check @Bootstrapping.termShiftVec_cons₂

-- IsUTermVec preservation
#check @IsUTermVec.termShiftVec
#check @IsUTermVec.termShift
#check @Bootstrapping.IsUTermVec.termShiftVec

-- FVar? / emb
#check @Semiformula.FVar?
#check @Rew.fvar?_emb
#check @Semiformula.fvar?_emb
#check @Rewriting.emb
#check @Rew.emb
#check @Semiformula.rew_eq_self_of
#check @Semiformula.quote_shift

-- iVE
#check @GodelQ.ZFCArith.iVE.construction.result_func'
#check @Language.TermRec.Construction.nth_resultVec
#check @Language.TermRec.Construction.resultVec_cons
#check @GodelQ.ZFCArith.iVE_func

-- IsFunc
#check @Arithmetic.isFunc_iff_LOR
#check @Arithmetic.IsFunc

-- sigma1_induction
#check @IsSemiterm.sigma1_induction

-- imp/neg unfold
#check @Bootstrapping.imp
#check @GodelQ.ZFCArith.neg

end GodelQ.ProbeAPI
