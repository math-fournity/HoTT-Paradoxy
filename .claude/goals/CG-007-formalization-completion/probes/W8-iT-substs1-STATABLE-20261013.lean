import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## §12.9 复核：`iT_substs1` 能否被**陈述**？（2026-10-13）

交接 §12.9 断言：「`iT n p` 在 `p` 符号时根本无法在 Lean 里被提及（陈述层就超时）」。
若成立，则 `ExsBlockerQ` 的 `ex_m` 路线**在陈述层就不可写**——这是比证明更基础的事实。

本探针照 §12.9 的形状原样写，看是否复现超时。
**结论：exit 0，两个形状都 elaborate，§12.9 的超时未复现**
（`maxHeartbeats` 从 4000000 降到 200000 仍 exit 0）。
`sorry` 是**刻意的**：只测陈述能否 elaborate，不测证明。 -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 200000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

namespace GodelQ.ProbeStatable

-- 形状 A：一般 p，归纳式陈述（§12.9 说这条路线不能写）
example (n : V) : ∀ p, IsSemiformula ℒₒᵣ n p →
    iT (0:V) (subst ℒₒᵣ (?[^&0] : V) p) = subst ℒₛₑₜ (?[^&0] : V) (iT (1:V) p) := by
  sorry

-- 形状 B：§12.9 的具体反例（v 符号、R 特化）
example {v : V} (hv : IsSemitermVec ℒₒᵣ (2:V) (1:V) v) :
    iT (1:V) (subst ℒₒᵣ (?[^#0, ^&0] : V) (^rel 2 (↑cEqN) v))
      = subst ℒₛₑₜ (?[^&0] : V) (iT (1:V) (^rel 2 (↑cEqN) v)) := by
  sorry

end GodelQ.ProbeStatable