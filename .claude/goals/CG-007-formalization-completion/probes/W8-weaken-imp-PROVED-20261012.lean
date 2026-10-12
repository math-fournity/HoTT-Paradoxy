import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches
set_option maxHeartbeats 800000
namespace GodelQ.ProbeImp2
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## `weaken_imp`：从 `⊢ A, X` 得 `⊢ (D→A), X`

**更简单的路**：`(D→A)` 就是 `¬D ⋎ A`。而
`Derivable.or : Derivable (insert p (insert q s)) → Derivable (insert (p ⋎ q) s)`
——**取 `p = neg D`、`q = A`、`s = X`**，只需要
`Derivable (insert (neg D) (insert A X))`，那正是 `wk` 自 `insert A X` 加一项。

这比 `cut` 简单得多。 -/

lemma weaken_imp {A D X : V} (hA : IsFormula ℒₛₑₜ A) (hD : IsFormula ℒₛₑₜ D)
    (hX : IsFormulaSet (L := ℒₛₑₜ) X)
    (hd : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert A X)) :
    Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert (imp ℒₛₑₜ D A) X) := by
  show Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert (neg ℒₛₑₜ D ^⋎ A) X)
  refine Derivable.or (T := 𝗭𝗙𝗖) (s := X) (p := neg ℒₛₑₜ D) (q := A) ?_
  -- 需要 `Derivable (insert (neg D) (insert A X))` ← wk hd
  refine Derivable.wk (T := 𝗭𝗙𝗖) (s := insert (neg ℒₛₑₜ D) (insert A X))
    (s' := insert A X) ?_ ?_ hd
  · intro y hy
    rcases mem_bitInsert_iff.mp hy with rfl | hy
    · exact hD.neg
    · rcases mem_bitInsert_iff.mp hy with rfl | hy
      · exact hA
      · exact hX y hy
  · intro y hy
    rcases mem_bitInsert_iff.mp hy with rfl | hy
    · exact mem_bitInsert_iff.mpr (Or.inr (mem_bitInsert_iff.mpr (Or.inl rfl)))
    · exact mem_bitInsert_iff.mpr (Or.inr (mem_bitInsert_iff.mpr (Or.inr hy)))

end GodelQ.ProbeImp2
