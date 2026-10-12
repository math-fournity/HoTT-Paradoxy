import GodelQ.ZFC.ShCraigElimSetupQ

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat

set_option maxHeartbeats 800000

namespace GodelQ.ProbeFreeK
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## 收束探针：`hAll` 走 `all_m` 的**确切**义务

`hAll` 里 `all_m` 要的 `q := imp ℒₛₑₜ domZero (iT 1 p)`。
关键：`free ℒₛₑₜ q` 由 `IsSemiformula.free`（Foundation，`Functions.lean:848`）给出，
**前提是 `IsSemiformula ℒₛₑₜ 1 q`**。有了它，`free q` 自动是公式——
**不需要**逐项验算向量长度（Foundation 已经保证了）。

所以 `hAll` 的真实义务只有两条：
1. `IsSemiformula ℒₛₑₜ 1 (imp domZero (iT 1 p))`（由 `isSemiformula_domZero'` + `isSemiformula_iT` 给）；
2. 把 `ih` 从 `insert (free ℒₒᵣ p) …` 搬到 `insert (free ℒₛₑₜ q) …`。

本探针确认第 1 条。 -/

-- `q` 的公式性：`IsSemiformula ℒₛₑₜ 1 (imp domZero (iT 1 p))`，`p` 层数 2
example {p : V} (hp : IsSemiformula ℒₒᵣ (1 + 1) p) :
    IsSemiformula ℒₛₑₜ 1 (imp ℒₛₑₜ (domZero (V := V)) (iT (1 : V) p)) := by
  have hq : IsSemiformula ℒₛₑₜ 1 (iT (1 : V) p) := by
    have := isSemiformula_iT (V := V) (n := (1 : V)) p hp
    simpa using this
  exact IsSemiformula.imp.mpr ⟨isSemiformula_domZero' (V := V), hq⟩

end GodelQ.ProbeFreeK
