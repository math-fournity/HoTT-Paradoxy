-- CG-009: hAll, unconditional — iT commutes with free/setShift at the sequent level.
import GodelQ.ZFC.TShiftBranches

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate
open GodelQ.GateBranches

namespace GodelQ.TAllBranches
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- The target: Derivable ZFC (translateSeq (insert (free p) (setShift s)))
--   ⟹ Derivable ZFC (translateSeq s)
-- Using all_m we need: (^∀ (iT 0 p)) ∈ translateSeq s and the antecedent at the
-- translated form insert (free (iT 0 p)) (setShift (translateSeq s)).
-- Plan: show translateSeq (insert (free p) (setShift s))
--         = insert (free ℒₛₑₜ (iT 0 p)) (setShift ℒₛₑₜ (translateSeq s))
-- (iT_free + tshift), then apply all_m.

/-- `iT` commutes with `free`: `iT 0 (free p) = free (iT 1 p)`-style.
    free p = substs1 ^&0 (shift p); so iT 0 (free p) = free ℒₛₑₜ (iT ...). -/
lemma iT_free {p : V} (hp : IsUFormula ℒₒᵣ p) :
    iT (0 : V) (free (L := ℒₒᵣ) p) = free (L := ℒₛₑₜ) (iT (1 : V) p) := by
  sorry

/-- The sequent-level commutation for `allIntro`'s premise. -/
lemma translateSeq_all_premise {s p : V} (hs : IsFormulaSet (L := ℒₒᵣ) s)
    (hp : IsUFormula ℒₒᵣ p) :
    translateSeq (V := V) (insert (free (L := ℒₒᵣ) p) (setShift (L := ℒₒᵣ) s)) =
      insert (free (L := ℒₛₑₜ) (iT (1 : V) p))
        (setShift (L := ℒₛₑₜ) (translateSeq (V := V) s)) := by
  rw [translateSeq_insert, iT_free hp,
    GodelQ.TShiftFull.tshift s hs]

/-- **`hAll`, unconditional**. -/
theorem hAll_uncond {s p d : V}
    (hs : IsFormulaSet (L := ℒₒᵣ) s)
    (hp : (^∀ p : V) ∈ s)
    (hd : DerivationOf (L := ℒₒᵣ) Sh.craig d (insert (free (L := ℒₒᵣ) p) (setShift (L := ℒₒᵣ) s)))
    (ih : Q d) : Q (allIntro s p d) := by
  simp only [Q, fstIdx_allIntro]
  have hpU : IsUFormula ℒₒᵣ p := (IsUFormula.all.mp ((hs (^∀ p) hp).isUFormula))
  have ih' : Derivable (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq (V := V)
      (insert (free (L := ℒₒᵣ) p) (setShift (L := ℒₒᵣ) s))) := by
    rw [← hd.1]; exact ih
  rw [translateSeq_all_premise hs hpU] at ih'
  refine Derivable.all_m (T := 𝗭𝗙𝗖) ?_ ih'
  rw [mem_translateSeq_iff]
  exact ⟨^∀ p, hp, (GodelQ.ITShiftFull.iT_shift (^∀ p) ⟨hpU, by simp⟩).symm⟩

end GodelQ.TAllBranches
