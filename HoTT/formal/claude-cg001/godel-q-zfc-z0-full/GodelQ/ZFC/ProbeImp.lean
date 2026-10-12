import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches
set_option maxHeartbeats 800000
namespace GodelQ.ProbeImp
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## `hAll` 的关键缺口已找到解法

`hAll` 需要从 `ih : Derivable (insert B X)` 得到 `Derivable (insert (D→B) X)`。
（`B = iT 0 (free p)`，`D = subst ?[^&0] cDomN` = "&0 ∈ ω"，
因为 `free (imp domZero (iT 1 p)) = D → B`。）

**先前我误判为「不可证」**——其实可以：`cut B`。

* (i) `⊢ B, (D→B), X` ← `ih` 经 `wk`（加一项）✓
* (ii) `⊢ ¬B, (D→B), X` ← 这是**重言式**（`¬B ∨ (¬D∨B) ∨ ⋁¬X`）：
  由 `Derivable.or` 从 `⊢ ¬D, B, ¬B, X` 得（该 sequent 含 `B` 与 `¬B`，`axL` 直接给）✓

于是 `cut B` 给出 `Derivable (insert (D→B) X)` ✓。

**这条是 `hAll` 的最后一环**。下面把它写成一般引理。 -/

/-- **从 `⊢ A, X` 得 `⊢ (D→A), X`**（`D` 任意）。 -/
lemma weaken_imp {A D X : V} (hA : IsFormula ℒₛₑₜ A) (hD : IsFormula ℒₛₑₜ D)
    (hX : IsFormulaSet (L := ℒₛₑₜ) X)
    (hd : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert A X)) :
    Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert (imp ℒₛₑₜ D A) X) := by
  -- `imp D A = neg D ^⋎ A`
  show Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert (neg ℒₛₑₜ D ^⋎ A) X)
  refine Derivable.cut A ?_ ?_
  · -- (i) `insert A (insert (D→A) X)` ← wk hd
    refine Derivable.wk (s := insert A (insert (neg ℒₛₑₜ D ^⋎ A) X))
      (s' := insert A X) ?_ ?_ hd
    · intro y hy
      rcases mem_bitInsert_iff.mp hy with rfl | hy
      · exact hA
      · rcases mem_bitInsert_iff.mp hy with rfl | hy
        · exact IsSemiformula.or.mpr ⟨hD.neg, hA⟩
        · exact hX y hy
    · intro y hy
      rcases mem_bitInsert_iff.mp hy with rfl | hy
      · exact mem_bitInsert_iff.mpr (Or.inl rfl)
      · exact mem_bitInsert_iff.mpr (Or.inr (mem_bitInsert_iff.mpr (Or.inr hy)))
  · -- (ii) `insert (neg A) (insert (D→A) X)` ← or (axL)
    refine Derivable.or (s := insert (neg ℒₛₑₜ A) X) ?_
    show Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖
      (insert (neg ℒₛₑₜ D) (insert A (insert (neg ℒₛₑₜ A) X)))
    exact Derivable.axL (s := insert (neg ℒₛₑₜ D) (insert A (insert (neg ℒₛₑₜ A) X)))
      (by
        intro y hy
        rcases mem_bitInsert_iff.mp hy with rfl | hy
        · exact hD.neg
        · rcases mem_bitInsert_iff.mp hy with rfl | hy
          · exact hA
          · rcases mem_bitInsert_iff.mp hy with rfl | hy
            · exact hA.neg
            · exact hX y hy)
      (by simp [mem_bitInsert_iff])
      (by simp [mem_bitInsert_iff])

end GodelQ.ProbeImp
