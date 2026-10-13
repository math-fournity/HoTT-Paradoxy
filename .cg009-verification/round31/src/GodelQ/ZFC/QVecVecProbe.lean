-- CG-009: `qVec² w` is a semiterm vector whenever `w` is.
import GodelQ.ZFC.SubstQqAlls

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate
open GodelQ.SubstQqAlls

example {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] {k n w : V}
    (hw : IsSemitermVec ℒₛₑₜ k n w) :
    IsSemitermVec ℒₛₑₜ (k + 1) (n + 1) (qVec ℒₛₑₜ w) :=
  hw.qVec

example {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] {k n w : V}
    (hw : IsSemitermVec ℒₛₑₜ k n w) :
    IsSemitermVec ℒₛₑₜ (k + 1 + 1) (n + 1 + 1) (qVec ℒₛₑₜ (qVec ℒₛₑₜ w)) :=
  hw.qVec.qVec
