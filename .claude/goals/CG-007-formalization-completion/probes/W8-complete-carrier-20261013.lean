import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## `SetTheory.complete` 的载体核验（2026-10-13）

`Provable.sound` 被证实硬接线宇宙 0（`Provable.{0,0}`），不能用在任意 V 上。
现在核验语义路线的另一件：`SetTheory.complete` 本身能否在任意 V 上实例化。

它的签名（本机 #check）：
  SetTheory.complete : ∀ (T : SetTheory) [𝗘𝗤 ℒₛₑₜ ⪯ T] (φ : SetTheorySentence),
    (∀ (M : Type u_2) [SetStructure M] [Nonempty M] [M↓[ℒₛₑₜ] ⊧* T], M↓[ℒₛₑₜ] ⊧ φ) → T ⊢ φ

`M : Type u_2` —— **宇宙多态**，故模型侧可用。
关键问题：`T ⊢ φ` 里的 `⊢` 是否也宇宙多态（它是元层可导性，不经过 V 的码）。

本探针在任意 V 上核验。 -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
namespace ProbeCompleteCarrier
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 在任意 V 上引用（不证明）：看是否有宇宙冲突
#check @SetTheory.complete

-- 元层可导性 `⊢` 的形状
#check @Theory.Proof
#check @Provable.sound

end ProbeCompleteCarrier