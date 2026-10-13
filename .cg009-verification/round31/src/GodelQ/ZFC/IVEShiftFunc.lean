import GodelQ.ZFC.TranslateShiftCompat
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate

namespace GodelQ.IVEShiftFunc
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

#check @isSemitermVec_single_bvar
#check @IsUTermVec.termShiftVec
#check @termShiftVec_cons₁
#check @qqAlls
#check @qqAlls_definable
