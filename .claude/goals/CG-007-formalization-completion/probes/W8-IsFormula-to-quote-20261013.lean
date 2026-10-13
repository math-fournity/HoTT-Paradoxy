import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## ★ `IsFormula p` → `p = ⌜σ⌝`？（2026-10-13）

`ExsBlockerQ` 里 `^∃ p ∈ s` 且 `s` 是 `IsFormulaSet`，
故 `IsFormula ℒₒᵣ (^∃ p)`，即 `IsSemiformula ℒₒᵣ 0 (^∃ p)`。

**关键问题**：`IsFormula p` 是否蕴含 `∃ σ : Sentence, p = ⌜σ⌝`？

若成立，语义路线的组装就通了——`p` 是码，码就是引号（`quote_*` 是 rfl），
于是 `iT_quote` 可用，`SetTheory.complete` 可用。

**本探针核验这条（这是整条路线的枢纽）**。 -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
namespace ProbeIsFormulaQuote

-- Foundation 里有没有 `IsFormula → ∃ σ, p = ⌜σ⌝`？
#check @Semiformula.quote_def
#check @Semiformula.quote_isSemiformula
#check @Semiformula.quote_inj_iff
#check @Semiformula.quote_ex
#check @Semiformula.quote_and
#check @Semiformula.quote_all

-- ★ 关键：找「IsSemiformula → 是引号」的反向引理（Foundation 无同名件）
#check @Semiformula.quote_isSemiformula   -- 正向：引号 ⇒ IsSemiformula（存在）
-- 反向不存在 ⇒ 但可以**自己造**：沿 IsSemiformula 的结构归纳
-- IsSemiformula 是 Fixpoint，用 `IsSemiformula.induction`（Basic.lean:468/501）

/-- **反向引理（本探针自造）**：任意层 n 的公式码都是某 Semiproposition 的引号。

`IsSemiformula L n p → ∃ φ : Semiproposition L n, p = ⌜φ⌝` -/
theorem isSemiformula_exists_quote (n : ℕ) : ∀ p : V, IsSemiformula ℒₒᵣ n p →
    ∃ φ : Semiproposition ℒₒᵣ n, p = (⌜φ⌝ : V) := by
  intro p hp
  induction hp using Semiformula.induction with
  | hrel k r v hk hv => exact ⟨.rel r (fun i ↦ Classical.choice (hv i (by simp))), by simp⟩
  | _ => sorry

end ProbeIsFormulaQuote