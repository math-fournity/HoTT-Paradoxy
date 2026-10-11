import GodelQ.ZFC.SeqTranslate
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.Translate
namespace ProbeL4
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.IsSemiformula.imp
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.IsSemiformula.neg
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.IsSemiformula.subst
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.IsSemiformula.substs
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.IsSemiformula.bShift
#check @GodelQ.Translate.iVE
#check @GodelQ.Translate.conjunct
#check @GodelQ.Translate.cRel
#check @GodelQ.Translate.qqAlls
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.IsSemiformula.isUFormula
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.IsSemiformula.isUTerm
end ProbeL4
