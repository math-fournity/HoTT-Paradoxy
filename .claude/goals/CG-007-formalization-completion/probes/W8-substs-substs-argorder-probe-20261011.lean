import GodelQ.ZFC.ShCraigElimBranches

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate

namespace GodelQ.ProbeU
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

set_option pp.all true in
example : IsSemiformula ℒₛₑₜ 1 ((cDomN : ℕ) : V) := isSemiformula_cDomN

example : IsSemiformula (V := V) ℒₛₑₜ (1 : V) ((cDomN : ℕ) : V) := by
  exact isSemiformula_cDomN

end GodelQ.ProbeU
