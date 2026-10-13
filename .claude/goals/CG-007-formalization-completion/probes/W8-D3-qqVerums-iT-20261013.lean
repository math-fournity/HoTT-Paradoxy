import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## D3 攻起：`qqVerums` 与 `iT` 的交换（2026-10-13）

`Theory.IsCraigAxiom (V := V) Sh p` 的 V 层展开是
`∃ s p', p = p' ^⋏ qqVerums s ∧ Evalb ![s,p'] ↑Sh.reWitness.val`。

`qqVerums k = ^⋀ repeatVec ^⊤ k`（`k` 个 `⊤` 的合取）——**纯构造**。
而 `iT` 对 `⋏` 与 `⊤` 都是同态（`iT_and`/`iT_verum`），
故 `iT n (qqVerums k)` 应当 = `qqVerums k`（每个 `⊤` 映射到 `⊤`）。

**这是 D3 的原子块**。本探针核验。 -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
namespace ProbeD3Verums

-- `qqVerums` 的化简规则
#check @qqVerums_zero
#check @qqVerums_succ
#check @qqVerums

-- `iT` 对 `⊤` 与 `⋏` 的同态
#check @iT_verum
#check @iT_and

-- 目标：`iT n (qqVerums k) = qqVerums k`
-- 试直接对 k 归纳（用 `qqVerums_zero`/`qqVerums_succ`）
example (n : V) : ∀ (k : ℕ), iT n (qqVerums (k : V)) = qqVerums (k : V) := by
  intro k
  induction k with
  | zero => simp [qqVerums_zero, iT_verum]
  | succ j ih =>
      rw [show ((j + 1 : ℕ) : V) = (j : V) + 1 by push_cast; ring]
      rw [qqVerums_succ]
      rw [iT_and (V := V) (IsUFormula.verum (L := ℒₒᵣ)) (IsUFormula.qqVerums (L := ℒₒᵣ))]
      rw [iT_verum, ih]

end ProbeD3Verums