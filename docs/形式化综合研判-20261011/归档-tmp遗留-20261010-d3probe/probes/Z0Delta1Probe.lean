import GodelQ.ZFC.Z0Bridge

/-! 决定性探测:能否为 Sh 构造 Theory.Δ₁ 实例。 -/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.Z0Bridge GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate

namespace GodelQ.Z0Delta1Probe

-- 探测:𝗭𝗙𝗖.Δ₁ 已存在(C-95),它的 ch 是什么?能否沿 iT 搬到 Sh?
-- 已知:zfcTr σ = trProv.val/[⌜σ⌝],而 trProv = "x. ∃y, !iTDef y 0 x ∧ !(provable 𝗭𝗙𝗖) y"
-- Sh 的成员判定就是 zfcTr,它本身是 Σ1 公式!
-- 所以 Sh.Δ₁.ch 的候选就是 trProv(或其 Σ1/Π1 对)。
noncomputable example : (trProv : ᵫaᵥᵄ₁.Semisentence 1) := trProv

end GodelQ.Z0Delta1Probe
