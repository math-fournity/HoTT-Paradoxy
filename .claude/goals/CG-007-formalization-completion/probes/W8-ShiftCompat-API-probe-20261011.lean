import GodelQ.ZFC.TranslateShiftCompat

/-! 探针：确认 `iVE_shift` func 支与 `iT_shift` 所需的 API 形状。 -/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate

namespace GodelQ.ProbeShiftCompat

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- A. shift 的分布律
#check @Bootstrapping.shift_verum
#check @Bootstrapping.shift_falsum
#check @Bootstrapping.shift_and
#check @Bootstrapping.shift_or
#check @Bootstrapping.shift_all
#check @Bootstrapping.shift_exs
#check @Bootstrapping.shift_neg
#check @Bootstrapping.shift_rel
#check @Bootstrapping.shift_substs
#check @Bootstrapping.shift_not_uformula

-- B. IsUFormula / IsSemiformula 的构造子
#check @Bootstrapping.IsUFormula.neg
#check @Bootstrapping.IsUFormula.or
#check @Bootstrapping.IsUFormula.imp
#check @Bootstrapping.IsUFormula.qqAlls
#check @Bootstrapping.IsSemiformula.neg
#check @Bootstrapping.IsSemiformula.or
#check @Bootstrapping.IsSemiformula.imp

-- C. 项向量
#check @Bootstrapping.IsUTermVec.cons_iff
#check @Bootstrapping.IsUTermVec.nth
#check @Bootstrapping.IsUTermVec.adjoin
#check @Bootstrapping.IsUTermVec.termShiftVec

-- D. 带 V 的层数参数
#check @Bootstrapping.IsSemiformula.shift
#check @Bootstrapping.IsSemiformula.shift_iff

-- E. iVE 的化简
#check @GodelQ.Translate.iVE_bvar
#check @GodelQ.Translate.iVE_fvar
#check @GodelQ.Translate.iVE_func

-- F. 结构归纳
#check @Bootstrapping.IsSemiterm.sigma1_induction
#check @Bootstrapping.IsSemiformula.sigma1_structural_induction

-- G. quote 与 shift
#check @Bootstrapping.Sentence.shift_quote
#check @Bootstrapping.Sentence.quote_shift
#check @Bootstrapping.Sentence.quote_isUFormula
#check @Bootstrapping.Sentence.quote_isSemiformula

-- H. 具体项
#check @GodelQ.Translate.iT_rel
#check @GodelQ.Translate.iT_all
#check @GodelQ.Translate.iT_exs
#check @GodelQ.Translate.iTR

end GodelQ.ProbeShiftCompat
