import GodelQ.ZFC.ShCraigElimBranches
import GodelQ.ZFC.TranslateShiftCompat

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.TranslateShiftCompat

set_option maxHeartbeats 800000

namespace GodelQ.ProbeP

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- ① 需要的代入相容律（项层地基）
example {σ : V} (hσ : IsSemiformula ℒₒᵣ 1 σ) :
    iT 0 (subst ℒₒᵣ ?[^&0] σ) = subst ℒₛₑₜ ?[^&0] (iT 1 σ) := by
  sorry

-- ② 由①得 `free` 的相容（`hAll` 需要的）
example {p : V} (hp : IsSemiformula ℒₒᵣ 1 p) :
    free ℒₛₑₜ (imp ℒₛₑₜ domZero (iT 1 p))
      = imp ℒₛₑₜ (subst ℒₛₑₜ ?[^&0] ((cDomN : ℕ) : V)) (iT 0 (free ℒₒᵣ p)) := by
  rw [free, free]
  rw [show shift ℒₛₑₜ (imp ℒₛₑₜ domZero (iT 1 p))
        = imp ℒₛₑₜ domZero (iT 1 (shift ℒₒᵣ p)) from by
      rw [shift_imp_domZero (isSemiformula_iT (n := 1) p hp).isUFormula,
        iT_shift (n := 1) p hp]]
  rw [show (imp ℒₛₑₜ domZero (iT 1 (shift ℒₒᵣ p)))
        = neg ℒₛₑₜ domZero ^⋎ iT 1 (shift ℒₒᵣ p) from rfl]
  sorry

-- ③ 加护罩一步：`Derivable (insert A S) → Derivable (insert (B → A) S)`
-- 走 or_m + wk。需要 A、B 都是公式（层数无所谓，只要 IsFormula）。
example {A B S : V} (hA : IsFormula ℒₛₑₜ A) (hB : IsFormula ℒₛₑₜ B)
    (hS : IsFormulaSet (L := ℒₛₑₜ) S)
    (hd : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert A S)) :
    Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert (imp ℒₛₑₜ B A) S) := by
  have hfs : IsFormulaSet (L := ℒₛₑₜ) (neg ℒₛₑₜ B ⫽ A ⫽ imp ℒₛₑₜ B A ⫽ S) := by
    intro p hp
    simp only [mem_bitInsert_iff] at hp
    rcases hp with rfl | rfl | rfl | hp
    · exact hB.neg
    · exact hA
    · exact IsSemiformula.or.mpr ⟨hB.neg, hA⟩
    · exact hS p hp
  refine Derivable.or_m (s := insert (imp ℒₛₑₜ B A) S)
    (p := neg ℒₛₑₜ B) (q := A) (by simp [imp]) ?_
  refine Derivable.wk hfs ?_ hd
  intro x hx
  simp only [mem_bitInsert_iff] at hx ⊢
  tauto

end GodelQ.ProbeP
