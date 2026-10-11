import GodelQ.ZFC.SeqTranslate

/-! 探针 L2：第二层所需的子引理清单（临时文件，不进收据） -/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.SeqTranslate

namespace ProbeL2

-- A. 归纳原理
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.Derivation.induction1
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.Derivation.axL
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.Derivation.verumIntro
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.Derivation.andIntro
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.Derivation.orIntro
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.Derivation.allIntro
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.Derivation.exsIntro
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.Derivation.wkRule
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.Derivation.shiftRule
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.Derivation.cutRule
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.Derivation.axm

-- B. fstIdx 与规则构造子的计算规则
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.fstIdx_axL
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.fstIdx_verumIntro
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.fstIdx_andIntro
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.fstIdx_allIntro
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.fstIdx_wkRule
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.fstIdx_shiftRule
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.fstIdx_cutRule
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.fstIdx_axm

-- C. iT 与 neg / 公式性的相容
#check @GodelQ.Translate.iT_neg
#check @GodelQ.Translate.iT_imp
#check @GodelQ.Translate.iT.construction.result_neg
#check @GodelQ.Translate.iT.construction.result_imp
#check @GodelQ.Translate.iT_defined

-- D. neg 的引理
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.neg
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.negGraph

-- E. Derivable 的构造
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.Derivable
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.derivable
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.Derivable.of_ss
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.Provable
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.provable

end ProbeL2
