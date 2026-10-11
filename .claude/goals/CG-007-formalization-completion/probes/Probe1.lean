import GodelQ.ZFC.Z0Full
import Foundation.FirstOrder.Incompleteness.StandardProvability

/-! 探针 1：摸清 Foundation 接口（临时文件，不进收据） -/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCZ0 GodelQ.Z0Full

namespace Probe1

-- A. provabilityPred 的类型
#check @FFL.FirstOrder.Arithmetic.provabilityPred
#check @FFL.FirstOrder.Arithmetic.Theory.standardProvability
#check @FFL.FirstOrder.Arithmetic.provable_D1
#check @FFL.FirstOrder.Arithmetic.provable_D2
#check @FFL.FirstOrder.Arithmetic.provable_D3
#check @FFL.FirstOrder.Arithmetic.provable_sigma_one_complete
#check @FFL.FirstOrder.Arithmetic.provable_sigma_one_complete_of_E
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.Arithmetic.sigma_one_complete
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.Arithmetic.provable_internalize

-- B. 𝗭𝗙𝗖 的 standardProvability：HBL2 应该有，HBL3 期望没有
example : (𝗭𝗙𝗖.standardProvability : Provability 𝗜𝚺₁ 𝗭𝗙𝗖).HBL2 := inferInstance

-- C. Theory.Δ₁ 𝗭𝗙𝗖 是否存在
example : (𝗭𝗙𝗖 : Theory ℒₛₑₜ).Δ₁ := inferInstance

-- D. Sh.craig 的 HBL3（本轮发现）
example : (Sh.craig.standardProvability : Provability 𝗜𝚺₁ Sh.craig).HBL3 := inferInstance

-- E. zfcTr 的定义与 Sh.craig 可证性谓词的形状
#check @GodelQ.Z0Full.zfcTr
#check @GodelQ.Z0Full.zfcTr_def
#check @GodelQ.Z0Full.models_zfcTr_iff
#check @GodelQ.Z0Full.trProv
#check @GodelQ.Z0Full.TrProvable

-- F. 试：能否把 zfcTr 写成 provabilityPred 𝗭𝗙𝗖 的代入
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.Arithmetic.sigma_one_complete

end Probe1
