import GodelQ.ZFC.Z0Full
import Foundation.FirstOrder.Incompleteness.StandardProvability

/-! 探针 4：`Sh.reCh` 与 `trProv` 是否同一公式（临时文件，不进收据） -/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCZ0 GodelQ.Z0Full GodelQ.ZFCArith

namespace Probe4

-- A. 定义相等？
example : (Sh.reCh : {Γ := 𝚺, rank := 1}.Semisentence 1) = GodelQ.Z0Full.trProv := by
  with_unfolding_all rfl

end Probe4
