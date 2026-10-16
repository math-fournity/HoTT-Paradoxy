import GodelQ.ZFC.Z0Full
import Foundation.FirstOrder.Incompleteness.StandardProvability

/-! 探针 5：`Sh.reCh.val` 与 `trProv.val` 是否同一公式（临时文件，不进收据） -/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCZ0 GodelQ.Z0Full GodelQ.ZFCArith

namespace Probe5

-- A. 定义相等（公式级）
example : (Sh.reCh.val : Semiformula ℒₒᵣ ℕ 1) = GodelQ.Z0Full.trProv.val := by
  with_unfolding_all rfl

end Probe5
