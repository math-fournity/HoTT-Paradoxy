import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## D3 攻起：`qqVerums` 与 `iT` 的交换（2026-10-13）

`Theory.IsCraigAxiom (V := V) Sh p` 的 V 层展开是
`∃ s p', p = p' ^⋏ qqVerums s ∧ Evalb ![s,p'] ↑Sh.reWitness.val`。

`qqVerums k = ^⋀ repeatVec ^⊤ k`（`k` 个 `⊤` 的合取）——**纯构造**。
而 `iT` 对 `⋏` 与 `⊤` 都是同态（`iT_and`/`iT_verum`），
故 `iT n (qqVerums k)` 应当 = `qqVerums k`（每个 `⊤` 映射到 `⊤`）。

**这是 D3 的原子块**。本探针证出（exit 0）：

```
lemma isUFormula_qqVerums : ∀ (k : ℕ), IsUFormula ℒₒᵣ (qqVerums (k : V))
theorem iT_qqVerums (n : V) : ∀ (k : ℕ), iT n (qqVerums (k : V)) = qqVerums (k : V)
```

`#print axioms` = `[propext, Classical.choice, Quot.sound]`，**无 sorryAx**。

证法：对 `k : ℕ` 归纳（`qqVerums` 是 `V → V`，但由 `repeatVec` 的 `ℕ` 索引给出，
故 `ℕ` 归纳足够），每步用 `qqVerums_succ` + `iT_and` + `iT_verum`。

**意义**：`IsCraigAxiom` 展开式里的 `qqVerums s` 在 `iT` 下**不变**，
这是 D3 里最容易的一块（纯构造，无 `reWitness` 语义）。 -/
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

-- 辅助：`qqVerums k` 是合式公式
lemma isUFormula_qqVerums : ∀ (k : ℕ), IsUFormula ℒₒᵣ (qqVerums (k : V)) := by
  intro k
  induction k with
  | zero => simpa [qqVerums_zero] using IsUFormula.verum (L := ℒₒᵣ)
  | succ j ih =>
      rw [show ((j + 1 : ℕ) : V) = (j : V) + 1 by push_cast; ring, qqVerums_succ]
      exact IsUFormula.and.mpr ⟨IsUFormula.verum (L := ℒₒᵣ), ih⟩

-- 目标：`iT n (qqVerums k) = qqVerums k`
theorem iT_qqVerums (n : V) : ∀ (k : ℕ), iT n (qqVerums (k : V)) = qqVerums (k : V) := by
  intro k
  induction k with
  | zero => simp [qqVerums_zero, iT_verum]
  | succ j ih =>
      rw [show ((j + 1 : ℕ) : V) = (j : V) + 1 by push_cast; ring]
      rw [qqVerums_succ]
      rw [iT_and (V := V) (IsUFormula.verum (L := ℒₒᵣ)) (isUFormula_qqVerums j)]
      rw [iT_verum, ih]

end ProbeD3Verums

#print axioms ProbeD3Verums.iT_qqVerums