import GodelQ.ZFC.SeqTranslateFormula

/-! 探针 L9：conjunct 公式性所需的 IsSemitermVec 接口（临时文件，不进收据） -/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.Translate GodelQ.ZFCArith

namespace ProbeL9

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

#check @FFL.FirstOrder.Arithmetic.Bootstrapping.IsSemitermVec
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.IsSemitermVec.cons
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.IsSemitermVec.empty
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.IsSemitermVec.nth
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.IsSemiterm
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.IsSemiterm.bvar
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.IsSemitermVec.single
#check @GodelQ.Translate.shiftVec
#check @GodelQ.Translate.shiftVec_succ
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.termBShiftVec
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.IsSemitermVec.termBShiftVec

end ProbeL9
