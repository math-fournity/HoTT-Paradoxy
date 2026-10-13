import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimSetupQ GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFL
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **攻击 `ExsBlockerQ`：`Derivable.exs` + 弱化能否够？**

`exsIntro s p t dd` 支：`fstIdx dd = insert (substs1 ℒₒᵣ t p) s`，
`ih : Derivable (translateSeq (fstIdx dd))`，
即 `Derivable (insert (iT 0 (substs1 ℒₒᵣ t p)) (translateSeq s))`。

目标：`Derivable (translateSeq s)`。

**`translateSeq s` 里有 `^∃ (domZero ⋏ iT 1 p)`**（`iT_exs` + `hExs_mem`）。
**`Derivable.exs`** 要 `Derivable (insert (substs1 ℒₛₑₜ t' (domZero ⋏ iT 1 p)) S)`
配 `insert (^∃ (domZero ⋏ iT 1 p)) S`。

**关键问题**：能否从 `ih` 的 `insert (iT 0 (substs1 ℒₒᵣ t p)) S`
**弱化/推导**到 `insert (substs1 ℒₛₑₜ t' (domZero ⋏ iT 1 p)) S`？

**注意**：`Derivable.exs` 的**前提**是 sequent **可导**，
故若 `insert (iT 0 (substs1 ℒₒᵣ t p)) S ⊢`（可导），
且能**加上** `substs1 ℒₛₑₜ t' (domZero ⋏ iT 1 p)`（`wk`），
则 `Derivable.exs` 可用——**不需要两者相等**！ -/
lemma exs_blocker_route {S T : V}
    (hS : IsFormulaSet (L := ℒₛₑₜ) S)
    (ih : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert T S)) :
    Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert T (insert T S)) := by
  refine Derivable.wk (s := insert T (insert T S)) (s' := insert T S) ?_ ?_ ih
  · intro y hy
    rcases mem_bitInsert_iff.mp hy with rfl | hy
    · exact ih.isFormulaSet T (by simp)
    · rcases mem_bitInsert_iff.mp hy with rfl | hy
      · exact ih.isFormulaSet T (by simp)
      · exact hS y hy
  · intro y hy
    rcases mem_bitInsert_iff.mp hy with rfl | hy
    · exact mem_bitInsert_iff.mpr (Or.inl rfl)
    · exact mem_bitInsert_iff.mpr (Or.inr hy)

end GodelQ.ProbeFL
