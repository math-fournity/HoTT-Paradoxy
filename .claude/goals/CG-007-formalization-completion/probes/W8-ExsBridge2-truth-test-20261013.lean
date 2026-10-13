import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## ExsBridge2 的真值测试（2026-10-13）

ExsBridge2 断言（对任意 p 层 1、t 项）：
  Provable 𝗭𝗙𝗖 (imp (iT 0 (substs1 ℒᵣ t p)) (^∃ (domZero ⋏ iT 1 p)))
即「p[t] → ∃x(x ∈ ω ∧ p(x))」。

关键性质：t 是任意的 ℒₒᵣ 项。若 t 含自由变量（如 ^&0），
则 iT 0 (substs1 t p) 也含自由变量 ^&0，而 ^∃ (domZero ⋏ iT 1 p) 是闭的
（p 层 1 ⇒ iT 1 p 层 1 ⇒ ^∃ 闭）。

于是 imp A B 带自由变量 ^&0，Provable 它即 ⊢ ∀x(A → B)——对任意 x 成立。

本探针只核验形状（自由变量出现位置），不判定真假——判定需要模型。 -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
namespace ProbeBridge2Truth

-- 形状核对：p = ⊤ 时桥退化为 ⊤ → ∃x(x ∈ ω ∧ ⊤)，即 ∃x(x ∈ ω)
example (t : V) : substs1 ℒₒᵣ t (^⊤ : V) = ^⊤ := by
  simp [substs1, Bootstrapping.substs_verum]

example : iT (0:V) (^⊤ : V) = ^⊤ := iT_verum (V := V) 0

-- ω 在 Foundation 里的名字（`domZero` 用的就是它）
#check @SetTheory.ω

end ProbeBridge2Truth