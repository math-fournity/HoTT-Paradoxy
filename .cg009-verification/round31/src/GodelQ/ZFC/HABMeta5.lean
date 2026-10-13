-- CG-009: hAB path ① — testing the meta route with the right objects.
import GodelQ.ZFC.HAllProof

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.HABMeta5
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

#check @Semiformula.free
#check @Rewriting.free
#check @Semiformula.free_quote
#check @LawfulSyntacticRewriting.app_subst_fbar_zero_comp_shift_eq_free

end GodelQ.HABMeta5
