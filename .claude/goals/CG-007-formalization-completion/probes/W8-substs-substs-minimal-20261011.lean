import GodelQ.ZFC.ShCraigElimBranches

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate

namespace GodelQ.ProbeV
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 最小化：只用 substs_substs，看它到底要什么
example (hv1 : IsSemitermVec ℒₛₑₜ 1 1 (?[^#0] : V)) :
    subst ℒₛₑₜ (?[^&0] : V) (subst ℒₛₑₜ (?[^#0] : V) ((cDomN : ℕ) : V))
      = subst ℒₛₑₜ (termSubstVec ℒₛₑₜ 1 (?[^&0] : V) (?[^#0] : V)) ((cDomN : ℕ) : V) :=
  substs_substs (L := ℒₛₑₜ) (l := (1 : V)) (n := (1 : V)) (m := (1 : V))
    isSemiformula_cDomN hv1 hv1

end GodelQ.ProbeV
