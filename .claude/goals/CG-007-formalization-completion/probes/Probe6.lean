import GodelQ.ZFC.Z0Full
import Foundation.FirstOrder.Incompleteness.StandardProvability

/-! 探针 6：`Sh.reCh` 的 V 内部语义（临时文件，不进收据） -/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCZ0 GodelQ.Z0Full GodelQ.ZFCArith

namespace Probe6

-- 目标：Sh.reCh 的 V 内部语义就是「ZFC 证明 x 的翻译」
example {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] (x : V) :
    (Semiformula.Evalb ![x]) (Sh.reCh.val) ↔
      (Semiformula.Evalb ![x]) (GodelQ.Z0Full.trProv.val) := by
  simp only [GodelQ.Z0Full.trProv, Theory.reCh]

end Probe6
