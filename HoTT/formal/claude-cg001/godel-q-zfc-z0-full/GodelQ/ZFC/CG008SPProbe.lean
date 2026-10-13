import GodelQ.ZFC.CG008GapSharp

/-! # 探针：`standardProvability` 能实例化到哪里 -/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008SPProbe
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Z0Full GodelQ.Translate

-- 1. `standardProvability` 对任意 `Theory L`（语言通用）
noncomputable example : Provability 𝗜𝚺₁ 𝗭𝗙𝗖 := 𝗭𝗙𝗖.standardProvability

-- 2. 它的 HBL2 对任意理论
example : (𝗭𝗙𝗖.standardProvability).HBL2 := inferInstance

-- 3. HBL3 要 `𝗣𝗔⁻ ⪯ T` 且 `T` 是 **ArithmeticTheory**
--    而 𝗭𝗙𝗖 : SetTheory。所以 `T.standardProvability.HBL3` 不能对 𝗭𝗙𝗖 合成。
--    下面这行**应当失败**（本探针用它固定墙的位置）：
-- example : (𝗭𝗙𝗖.standardProvability).HBL3 := inferInstance

-- 4. `provable_D3` 的类型
#check @provable_D3

end GodelQ.CG008SPProbe
