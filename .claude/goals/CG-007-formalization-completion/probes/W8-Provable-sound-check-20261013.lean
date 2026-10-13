import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## Provable.sound 是语义路线的关键桥（2026-10-13）

Provable T ⌜φ⌝ → T ⊢ φ —— 这正是「V 里的可证码」到「元层可导性」的桥。

于是语义路线可以反向走：
1. 要 Provable 𝗭𝗙𝗖 (iT 0 (p[t] → ∃x p(x)))；
2. 若能说明该码 = ⌜arithTrln.translate (p[t] → ∃x p(x))⌝（用 iT_quote 反向）；
3. 则 Provable.sound 给出 𝗭𝗙𝗖 ⊢ translate (p[t] → ∃x p(x))；
4. 再用 translate_iff + 模型论证证 ⊢。

但方向 2 是难点：iT_quote 只对 ⌜φ⌝ 形（φ 是 Semisentence）给等式，
而 ExsBridge2 的 p 是 V 层符号、substs1 t p 更是 V 层运算的结果。

本探针核验 Provable.sound 的确切形状与可用性。 -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
namespace ProbeProvableSound

#check @Provable.sound
#check @Provable.sound2

end ProbeProvableSound